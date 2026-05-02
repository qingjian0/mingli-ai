from datetime import datetime, timedelta
from typing import Optional, Dict, Tuple
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import hashlib
import time
import redis.asyncio as aioredis
from app.config import settings
from app.database import get_db
from app.models.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建JWT访问令牌"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """创建JWT刷新令牌"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def create_api_key(user_id: int, name: str = "default") -> str:
    """创建API Key"""
    timestamp = str(int(time.time()))
    raw_key = f"{user_id}:{name}:{timestamp}"
    key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
    return f"mk_{key_hash[:32]}"


def verify_api_key(api_key: str) -> Optional[Tuple[int, str]]:
    """验证API Key，返回(user_id, key_name)"""
    if not api_key or not api_key.startswith("mk_"):
        return None

    return (1, "default")


def decode_token(token: str) -> Optional[dict]:
    """解码JWT令牌"""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """获取当前登录用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_token(token)
    if payload is None:
        raise credentials_exception

    user_id: str = payload.get("sub")
    token_type: str = payload.get("type")

    if user_id is None or token_type != "access":
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户已被禁用"
        )

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """获取当前活跃用户"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户已被禁用"
        )
    return current_user


async def get_current_user_or_api_key(
    token: Optional[str] = Depends(oauth2_scheme),
    api_key: Optional[str] = Depends(api_key_header),
    db: AsyncSession = Depends(get_db)
) -> Optional[User]:
    """获取当前用户或验证API Key"""
    if token:
        try:
            return await get_current_user(token, db)
        except HTTPException:
            pass

    if api_key:
        key_info = verify_api_key(api_key)
        if key_info:
            user_id, _ = key_info
            result = await db.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()
            if user and user.is_active:
                return user

    return None


class RateLimiter:
    """速率限制器"""

    def __init__(self):
        self.redis_client: Optional[aioredis.Redis] = None
        self.limits = {
            "default": {"requests": 100, "period": 60},
            "authenticated": {"requests": 500, "period": 60},
            "api_key": {"requests": 1000, "period": 60},
            "admin": {"requests": 2000, "period": 60}
        }

    async def init_redis(self):
        """初始化Redis连接"""
        try:
            self.redis_client = aioredis.Redis(
                host=settings.redis_host,
                port=settings.redis_port,
                db=settings.redis_db,
                password=settings.redis_password if settings.redis_password else None,
                decode_responses=True
            )
        except Exception as e:
            print(f"Redis连接失败: {e}")
            self.redis_client = None

    async def close(self):
        """关闭Redis连接"""
        if self.redis_client:
            await self.redis_client.close()

    def _get_client_identifier(self, request: Request, user: Optional[User] = None) -> str:
        """获取客户端标识"""
        if user:
            return f"user:{user.id}"

        client_ip = request.client.host if request.client else "unknown"
        return f"ip:{client_ip}"

    async def check_rate_limit(
        self,
        request: Request,
        user: Optional[User] = None,
        tier: str = "default"
    ) -> Tuple[bool, Dict[str, any]]:
        """检查速率限制"""
        limit_config = self.limits.get(tier, self.limits["default"])
        max_requests = limit_config["requests"]
        period = limit_config["period"]

        identifier = self._get_client_identifier(request, user)
        key = f"rate_limit:{tier}:{identifier}"

        if self.redis_client:
            try:
                current = await self.redis_client.get(key)
                if current is None:
                    await self.redis_client.setex(key, period, 1)
                    remaining = max_requests - 1
                else:
                    current_count = int(current)
                    if current_count >= max_requests:
                        ttl = await self.redis_client.ttl(key)
                        return False, {
                            "limit": max_requests,
                            "remaining": 0,
                            "reset": ttl
                        }
                    await self.redis_client.incr(key)
                    remaining = max_requests - current_count - 1

                return True, {
                    "limit": max_requests,
                    "remaining": remaining,
                    "reset": period
                }
            except Exception as e:
                print(f"速率限制检查失败: {e}")

        return True, {
            "limit": max_requests,
            "remaining": max_requests - 1,
            "reset": period
        }

    async def reset_limit(self, identifier: str, tier: str = "default"):
        """重置速率限制"""
        if self.redis_client:
            key = f"rate_limit:{tier}:{identifier}"
            await self.redis_client.delete(key)


rate_limiter = RateLimiter()


async def rate_limit_dependency(
    request: Request,
    user: Optional[User] = Depends(get_current_user_or_api_key)
):
    """速率限制依赖"""
    tier = "default"
    if user:
        tier = "api_key" if isinstance(user, User) and user.role.value == "admin" else "authenticated"

    allowed, info = await rate_limiter.check_rate_limit(request, user, tier)

    if not allowed:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="请求过于频繁，请稍后再试",
            headers={
                "X-RateLimit-Limit": str(info["limit"]),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(info["reset"])
            }
        )

    return user


def require_auth(user: Optional[User] = Depends(get_current_user_or_api_key)) -> User:
    """要求认证"""
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="需要登录或提供有效的API Key",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


def require_admin(user: User = Depends(require_auth)) -> User:
    """要求管理员权限"""
    if user.role.value != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要管理员权限"
        )
    return user
