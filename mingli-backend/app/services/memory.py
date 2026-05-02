from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import hashlib
from redis.asyncio import Redis
from app.config import settings
import logging

logger = logging.getLogger("mingli.memory")


class MemoryService:
    """记忆系统服务"""

    def __init__(self, redis: Redis):
        self.redis = redis
        self.prefix = "mingli:memory:"
        self.default_ttl = settings.cache_ttl

    def _make_key(self, user_id: int, key: str) -> str:
        """生成缓存键"""
        return f"{self.prefix}{user_id}:{key}"

    def _make_hash(self, content: str) -> str:
        """生成内容哈希"""
        return hashlib.md5(content.encode()).hexdigest()

    async def store(
        self,
        user_id: int,
        key: str,
        content: Any,
        ttl: Optional[int] = None
    ) -> bool:
        """存储记忆"""
        try:
            cache_key = self._make_key(user_id, key)
            ttl = ttl or self.default_ttl

            serialized = json.dumps(content, ensure_ascii=False, default=str)
            await self.redis.setex(cache_key, ttl, serialized)

            logger.debug(f"存储记忆: {cache_key}, TTL: {ttl}s")
            return True
        except Exception as e:
            logger.error(f"存储记忆失败: {str(e)}")
            return False

    async def retrieve(
        self,
        user_id: int,
        key: str,
        default: Any = None
    ) -> Any:
        """获取记忆"""
        try:
            cache_key = self._make_key(user_id, key)
            content = await self.redis.get(cache_key)

            if content is None:
                return default

            return json.loads(content)
        except Exception as e:
            logger.error(f"获取记忆失败: {str(e)}")
            return default

    async def delete(
        self,
        user_id: int,
        key: str
    ) -> bool:
        """删除记忆"""
        try:
            cache_key = self._make_key(user_id, key)
            result = await self.redis.delete(cache_key)
            return result > 0
        except Exception as e:
            logger.error(f"删除记忆失败: {str(e)}")
            return False

    async def exists(
        self,
        user_id: int,
        key: str
    ) -> bool:
        """检查记忆是否存在"""
        try:
            cache_key = self._make_key(user_id, key)
            return await self.redis.exists(cache_key) > 0
        except Exception as e:
            logger.error(f"检查记忆存在失败: {str(e)}")
            return False

    async def store_analysis_context(
        self,
        user_id: int,
        chart_id: int,
        analysis_type: str,
        context: Dict[str, Any]
    ) -> bool:
        """存储分析上下文"""
        key = f"chart:{chart_id}:{analysis_type}:context"
        return await self.store(user_id, key, context, ttl=3600)

    async def get_analysis_context(
        self,
        user_id: int,
        chart_id: int,
        analysis_type: str
    ) -> Optional[Dict[str, Any]]:
        """获取分析上下文"""
        key = f"chart:{chart_id}:{analysis_type}:context"
        return await self.retrieve(user_id, key)

    async def store_conversation(
        self,
        user_id: int,
        conversation_id: str,
        messages: List[Dict[str, Any]],
        ttl: Optional[int] = None
    ) -> bool:
        """存储对话历史"""
        key = f"conversation:{conversation_id}"
        return await self.store(user_id, key, messages, ttl=ttl or 1800)

    async def get_conversation(
        self,
        user_id: int,
        conversation_id: str
    ) -> List[Dict[str, Any]]:
        """获取对话历史"""
        messages = await self.retrieve(user_id, f"conversation:{conversation_id}")
        return messages or []

    async def clear_user_memory(
        self,
        user_id: int
    ) -> int:
        """清除用户所有记忆"""
        try:
            pattern = f"{self.prefix}{user_id}:*"
            cursor = 0
            deleted_count = 0

            while True:
                cursor, keys = await self.redis.scan(cursor, match=pattern, count=100)
                if keys:
                    deleted_count += await self.redis.delete(*keys)
                if cursor == 0:
                    break

            logger.info(f"清除用户 {user_id} 的 {deleted_count} 条记忆")
            return deleted_count
        except Exception as e:
            logger.error(f"清除用户记忆失败: {str(e)}")
            return 0
