"""古籍仓储层"""

from typing import Optional, List, Tuple
from uuid import UUID

from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.knowledge.models.ancient_book import AncientBook, BookSection
from app.knowledge.schemas.ancient_book import (
    AncientBookCreate,
    AncientBookUpdate,
    BookSectionCreate,
    BookSectionUpdate,
)


class AncientBookRepository:
    """古籍仓储"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: AncientBookCreate) -> AncientBook:
        """创建古籍"""
        book = AncientBook(**data.model_dump())
        self.session.add(book)
        await self.session.flush()
        await self.session.refresh(book)
        return book

    async def get_by_id(self, book_id: UUID) -> Optional[AncientBook]:
        """根据ID获取古籍"""
        result = await self.session.execute(
            select(AncientBook)
            .where(AncientBook.id == book_id)
        )
        return result.scalar_one_or_none()

    async def get_by_id_with_sections(self, book_id: UUID) -> Optional[AncientBook]:
        """根据ID获取古籍（含章节）"""
        result = await self.session.execute(
            select(AncientBook)
            .options(selectinload(AncientBook.sections))
            .where(AncientBook.id == book_id)
        )
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 20,
        category: Optional[str] = None,
        dynasty: Optional[str] = None,
        keyword: Optional[str] = None,
    ) -> Tuple[List[AncientBook], int]:
        """获取古籍列表"""
        query = select(AncientBook)

        if category:
            query = query.where(AncientBook.category == category)
        if dynasty:
            query = query.where(AncientBook.dynasty == dynasty)
        if keyword:
            query = query.where(
                or_(
                    AncientBook.title.ilike(f"%{keyword}%"),
                    AncientBook.author.ilike(f"%{keyword}%")
                )
            )

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.order_by(AncientBook.created_at.desc())
        query = query.offset(skip).limit(limit)

        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def update(
        self,
        book_id: UUID,
        data: AncientBookUpdate
    ) -> Optional[AncientBook]:
        """更新古籍"""
        book = await self.get_by_id(book_id)
        if not book:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(book, key, value)

        await self.session.flush()
        await self.session.refresh(book)
        return book

    async def delete(self, book_id: UUID) -> bool:
        """删除古籍"""
        book = await self.get_by_id(book_id)
        if not book:
            return False

        await self.session.delete(book)
        await self.session.flush()
        return True

    async def create_section(
        self,
        data: BookSectionCreate
    ) -> BookSection:
        """创建章节"""
        section = BookSection(**data.model_dump())
        self.session.add(section)
        await self.session.flush()
        await self.session.refresh(section)
        return section

    async def get_section_by_id(
        self,
        section_id: UUID
    ) -> Optional[BookSection]:
        """获取章节"""
        result = await self.session.execute(
            select(BookSection).where(BookSection.id == section_id)
        )
        return result.scalar_one_or_none()

    async def get_sections_by_book(
        self,
        book_id: UUID
    ) -> List[BookSection]:
        """获取古籍的所有章节"""
        result = await self.session.execute(
            select(BookSection)
            .where(BookSection.book_id == book_id)
            .order_by(BookSection.page_start)
        )
        return list(result.scalars().all())

    async def update_section(
        self,
        section_id: UUID,
        data: BookSectionUpdate
    ) -> Optional[BookSection]:
        """更新章节"""
        section = await self.get_section_by_id(section_id)
        if not section:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(section, key, value)

        await self.session.flush()
        await self.session.refresh(section)
        return section

    async def delete_section(self, section_id: UUID) -> bool:
        """删除章节"""
        section = await self.get_section_by_id(section_id)
        if not section:
            return False

        await self.session.delete(section)
        await self.session.flush()
        return True

    async def search_by_content(
        self,
        keyword: str,
        skip: int = 0,
        limit: int = 20
    ) -> List[Tuple[AncientBook, BookSection]]:
        """搜索古籍内容"""
        query = (
            select(BookSection)
            .join(AncientBook)
            .where(BookSection.content.ilike(f"%{keyword}%"))
        )

        count_query = select(func.count()).select_from(query.subquery())
        result = await self.session.execute(query.offset(skip).limit(limit))
        sections = list(result.scalars().all())

        return sections
