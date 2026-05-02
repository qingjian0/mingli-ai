"""知识条目仓储层"""

from typing import Optional, List, Tuple
from uuid import UUID

from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.knowledge.models.knowledge_entry import KnowledgeEntry
from app.knowledge.schemas.knowledge_entry import (
    KnowledgeEntryCreate,
    KnowledgeEntryUpdate,
)


class KnowledgeRepository:
    """知识条目仓储"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: KnowledgeEntryCreate) -> KnowledgeEntry:
        """创建知识条目"""
        entry = KnowledgeEntry(**data.model_dump())
        self.session.add(entry)
        await self.session.flush()
        await self.session.refresh(entry)
        return entry

    async def get_by_id(self, entry_id: UUID) -> Optional[KnowledgeEntry]:
        """根据ID获取知识条目"""
        result = await self.session.execute(
            select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
        )
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 20,
        category: Optional[str] = None,
        system: Optional[str] = None,
        verification_status: Optional[str] = None,
        review_status: Optional[str] = None,
    ) -> Tuple[List[KnowledgeEntry], int]:
        """获取知识条目列表"""
        query = select(KnowledgeEntry)

        if category:
            query = query.where(KnowledgeEntry.category == category)
        if system:
            query = query.where(KnowledgeEntry.system == system)
        if verification_status:
            query = query.where(
                KnowledgeEntry.verification_status == verification_status
            )
        if review_status:
            query = query.where(KnowledgeEntry.review_status == review_status)

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.order_by(KnowledgeEntry.created_at.desc())
        query = query.offset(skip).limit(limit)

        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def update(
        self,
        entry_id: UUID,
        data: KnowledgeEntryUpdate
    ) -> Optional[KnowledgeEntry]:
        """更新知识条目"""
        entry = await self.get_by_id(entry_id)
        if not entry:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(entry, key, value)

        await self.session.flush()
        await self.session.refresh(entry)
        return entry

    async def delete(self, entry_id: UUID) -> bool:
        """删除知识条目"""
        entry = await self.get_by_id(entry_id)
        if not entry:
            return False

        await self.session.delete(entry)
        await self.session.flush()
        return True

    async def search(
        self,
        keyword: Optional[str] = None,
        tags: Optional[List[str]] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> Tuple[List[KnowledgeEntry], int]:
        """搜索知识条目"""
        query = select(KnowledgeEntry)

        if keyword:
            query = query.where(
                KnowledgeEntry.term.ilike(f"%{keyword}%")
                | KnowledgeEntry.pinyin.ilike(f"%{keyword}%")
                | KnowledgeEntry.interpretation.ilike(f"%{keyword}%")
            )

        if tags:
            query = query.where(KnowledgeEntry.tags.contains(tags))

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def increment_view_count(self, entry_id: UUID) -> None:
        """增加浏览次数"""
        await self.session.execute(
            update(KnowledgeEntry)
            .where(KnowledgeEntry.id == entry_id)
            .values(view_count=KnowledgeEntry.view_count + 1)
        )
        await self.session.flush()

    async def increment_reference_count(self, entry_id: UUID) -> None:
        """增加引用次数"""
        await self.session.execute(
            update(KnowledgeEntry)
            .where(KnowledgeEntry.id == entry_id)
            .values(reference_count=KnowledgeEntry.reference_count + 1)
        )
        await self.session.flush()

    async def update_accuracy_rating(
        self,
        entry_id: UUID,
        rating: float
    ) -> Optional[KnowledgeEntry]:
        """更新准确性评分"""
        entry = await self.get_by_id(entry_id)
        if not entry:
            return None

        total_count = entry.reference_count
        if total_count > 0:
            current_total = entry.accuracy_rating * (total_count - 1)
            new_rating = (current_total + rating) / total_count
        else:
            new_rating = rating

        entry.accuracy_rating = new_rating
        await self.session.flush()
        await self.session.refresh(entry)
        return entry

    async def get_by_source_book(
        self,
        book_id: UUID
    ) -> List[KnowledgeEntry]:
        """获取指定古籍来源的所有知识条目"""
        result = await self.session.execute(
            select(KnowledgeEntry)
            .where(KnowledgeEntry.source_book_id == book_id)
            .order_by(KnowledgeEntry.term)
        )
        return list(result.scalars().all())

    async def get_related_entries(
        self,
        entry_id: UUID
    ) -> List[KnowledgeEntry]:
        """获取关联的知识条目"""
        entry = await self.get_by_id(entry_id)
        if not entry or not entry.related_entries:
            return []

        related_ids = entry.related_entries
        result = await self.session.execute(
            select(KnowledgeEntry)
            .where(KnowledgeEntry.id.in_(related_ids))
        )
        return list(result.scalars().all())
