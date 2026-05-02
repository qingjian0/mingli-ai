from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from redis.asyncio import Redis
import redis.asyncio as aioredis
from app.config import settings
from app.database import get_db
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)


async def get_redis() -> Redis:
    """获取Redis连接"""
    redis = aioredis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=settings.redis_db,
        password=settings.redis_password if settings.redis_password else None,
        decode_responses=settings.redis_decode_responses,
        max_connections=settings.redis_max_connections
    )
    try:
        yield redis
    finally:
        await redis.close()


async def get_current_user_optional(
    token: Optional[str] = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> Optional[User]:
    """获取当前用户（可选，未登录时返回None）"""
    if not token:
        return None

    try:
        from app.core.security import decode_token
        payload = decode_token(token)
        if payload is None:
            return None

        user_id = payload.get("sub")
        token_type = payload.get("type")
        if user_id is None or token_type != "access":
            return None

        result = await db.execute(select(User).where(User.id == int(user_id)))
        user = result.scalar_one_or_none()
        return user
    except Exception:
        return None


async def get_pagination_params(
    page: int = 1,
    page_size: int = 20
) -> dict:
    """分页参数"""
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 20
    if page_size > 100:
        page_size = 100

    return {
        "skip": (page - 1) * page_size,
        "limit": page_size,
        "page": page,
        "page_size": page_size
    }
