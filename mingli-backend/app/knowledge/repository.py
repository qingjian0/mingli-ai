from typing import List, Optional, Tuple, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_, update, delete
from sqlalchemy.orm import selectinload
from app.models.knowledge import (
    KnowledgeEntry, KnowledgeRelation, KnowledgeCategoryModel,
    ClassicText, ClassicSection, CaseRecord, CaseFeedback
)
from app.schemas.knowledge import (
    KnowledgeEntryCreate, KnowledgeEntryUpdate,
    KnowledgeRelationCreate,
    KnowledgeCategoryCreate, KnowledgeCategoryUpdate,
    ClassicTextCreate, ClassicTextUpdate,
    ClassicSectionCreate,
    CaseRecordCreate, CaseRecordUpdate,
    CaseFeedbackCreate, CaseFeedbackUpdate,
    KnowledgeCategoryEnum, KnowledgeTypeEnum
)


class KnowledgeRepository:
    """知识库仓储层"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_entry(self, entry_data: KnowledgeEntryCreate, user_id: Optional[int] = None) -> KnowledgeEntry:
        """创建知识条目"""
        entry = KnowledgeEntry(
            title=entry_data.title,
            content=entry_data.content,
            summary=entry_data.summary,
            category=entry_data.category.value,
            knowledge_type=entry_data.knowledge_type.value,
            source_type=entry_data.source_type.value,
            source=entry_data.source,
            source_author=entry_data.source_author,
            page_reference=entry_data.page_reference,
            tags=entry_data.tags,
            metadata=entry_data.metadata,
            verification_level=entry_data.verification_level.value,
            created_by=user_id
        )
        self.db.add(entry)
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def get_entry(self, entry_id: int) -> Optional[KnowledgeEntry]:
        """获取知识条目"""
        result = await self.db.execute(
            select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
        )
        return result.scalar_one_or_none()

    async def get_entry_with_relations(self, entry_id: int) -> Optional[KnowledgeEntry]:
        """获取知识条目及其关联"""
        result = await self.db.execute(
            select(KnowledgeEntry)
            .options(selectinload(KnowledgeEntry.related_to))
            .where(KnowledgeEntry.id == entry_id)
        )
        return result.scalar_one_or_none()

    async def update_entry(
        self,
        entry_id: int,
        entry_data: KnowledgeEntryUpdate,
        user_id: Optional[int] = None
    ) -> Optional[KnowledgeEntry]:
        """更新知识条目"""
        entry = await self.get_entry(entry_id)
        if not entry:
            return None

        update_data = entry_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if field in ['category', 'knowledge_type', 'source_type']:
                setattr(entry, field, value.value if hasattr(value, 'value') else value)
            else:
                setattr(entry, field, value)

        entry.updated_by = user_id
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def delete_entry(self, entry_id: int) -> bool:
        """删除知识条目"""
        result = await self.db.execute(
            delete(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def list_entries(
        self,
        category: Optional[KnowledgeCategoryEnum] = None,
        knowledge_type: Optional[KnowledgeTypeEnum] = None,
        tags: Optional[List[str]] = None,
        verification_level: Optional[str] = None,
        is_published: Optional[bool] = None,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[KnowledgeEntry], int]:
        """列出知识条目"""
        query = select(KnowledgeEntry)
        conditions = []

        if category:
            conditions.append(KnowledgeEntry.category == category.value)
        if knowledge_type:
            conditions.append(KnowledgeEntry.knowledge_type == knowledge_type.value)
        if verification_level:
            conditions.append(KnowledgeEntry.verification_level == verification_level)
        if is_published is not None:
            conditions.append(KnowledgeEntry.is_published == is_published)
        if tags:
            for tag in tags:
                conditions.append(KnowledgeEntry.tags.contains([tag]))

        if conditions:
            query = query.where(and_(*conditions))

        count_query = select(func.count()).select_from(query.subquery())
        count_result = await self.db.execute(count_query)
        total = count_result.scalar()

        result = await self.db.execute(
            query
            .offset(skip)
            .limit(limit)
            .order_by(KnowledgeEntry.created_at.desc())
        )
        entries = result.scalars().all()

        return list(entries), total

    async def increment_view_count(self, entry_id: int) -> None:
        """增加浏览次数"""
        await self.db.execute(
            update(KnowledgeEntry)
            .where(KnowledgeEntry.id == entry_id)
            .values(view_count=KnowledgeEntry.view_count + 1)
        )
        await self.db.commit()

    async def create_relation(self, from_entry_id: int, relation_data: KnowledgeRelationCreate) -> Optional[KnowledgeRelation]:
        """创建知识关联"""
        if from_entry_id == relation_data.to_entry_id:
            return None

        relation = KnowledgeRelation(
            from_entry_id=from_entry_id,
            to_entry_id=relation_data.to_entry_id,
            relation_type=relation_data.relation_type,
            weight=relation_data.weight
        )
        self.db.add(relation)
        await self.db.commit()
        await self.db.refresh(relation)
        return relation

    async def delete_relation(self, relation_id: int) -> bool:
        """删除知识关联"""
        result = await self.db.execute(
            delete(KnowledgeRelation).where(KnowledgeRelation.id == relation_id)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def get_related_entries(
        self,
        entry_id: int,
        relation_type: Optional[str] = None,
        limit: int = 10
    ) -> List[KnowledgeEntry]:
        """获取关联的知识条目"""
        query = (
            select(KnowledgeEntry)
            .join(KnowledgeRelation, KnowledgeRelation.to_entry_id == KnowledgeEntry.id)
            .where(KnowledgeRelation.from_entry_id == entry_id)
        )

        if relation_type:
            query = query.where(KnowledgeRelation.relation_type == relation_type)

        result = await self.db.execute(
            query.limit(limit)
        )
        return list(result.scalars().all())


class CategoryRepository:
    """分类仓储层"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_category(self, category_data: KnowledgeCategoryCreate) -> KnowledgeCategoryModel:
        """创建分类"""
        category = KnowledgeCategoryModel(
            name=category_data.name,
            code=category_data.code,
            description=category_data.description,
            icon=category_data.icon,
            parent_id=category_data.parent_id,
            sort_order=category_data.sort_order
        )
        self.db.add(category)
        await self.db.commit()
        await self.db.refresh(category)
        return category

    async def get_category(self, category_id: int) -> Optional[KnowledgeCategoryModel]:
        """获取分类"""
        result = await self.db.execute(
            select(KnowledgeCategoryModel).where(KnowledgeCategoryModel.id == category_id)
        )
        return result.scalar_one_or_none()

    async def get_category_by_code(self, code: str) -> Optional[KnowledgeCategoryModel]:
        """根据编码获取分类"""
        result = await self.db.execute(
            select(KnowledgeCategoryModel).where(KnowledgeCategoryModel.code == code)
        )
        return result.scalar_one_or_none()

    async def update_category(
        self,
        category_id: int,
        category_data: KnowledgeCategoryUpdate
    ) -> Optional[KnowledgeCategoryModel]:
        """更新分类"""
        category = await self.get_category(category_id)
        if not category:
            return None

        update_data = category_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(category, field, value)

        await self.db.commit()
        await self.db.refresh(category)
        return category

    async def delete_category(self, category_id: int) -> bool:
        """删除分类"""
        result = await self.db.execute(
            delete(KnowledgeCategoryModel).where(KnowledgeCategoryModel.id == category_id)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def list_categories(
        self,
        parent_id: Optional[int] = None,
        include_children: bool = False
    ) -> List[KnowledgeCategoryModel]:
        """列出分类"""
        query = select(KnowledgeCategoryModel)

        if parent_id is not None:
            query = query.where(KnowledgeCategoryModel.parent_id == parent_id)
        else:
            query = query.where(KnowledgeCategoryModel.parent_id.is_(None))

        query = query.order_by(KnowledgeCategoryModel.sort_order)

        result = await self.db.execute(query)
        categories = list(result.scalars().all())

        if include_children:
            for category in categories:
                category.children = await self.list_categories(category.id, include_children=True)

        return categories


class ClassicRepository:
    """古籍仓储层"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_text(self, text_data: ClassicTextCreate) -> ClassicText:
        """创建古籍"""
        text = ClassicText(
            title=text_data.title,
            author=text_data.author,
            dynasty=text_data.dynasty,
            category=text_data.category,
            description=text_data.description,
            full_text=text_data.full_text,
            chapters=text_data.chapters,
            source_url=text_data.source_url
        )
        self.db.add(text)
        await self.db.commit()
        await self.db.refresh(text)
        return text

    async def get_text(self, text_id: int) -> Optional[ClassicText]:
        """获取古籍"""
        result = await self.db.execute(
            select(ClassicText).where(ClassicText.id == text_id)
        )
        return result.scalar_one_or_none()

    async def get_text_with_sections(self, text_id: int) -> Optional[ClassicText]:
        """获取古籍及其章节"""
        result = await self.db.execute(
            select(ClassicText)
            .options(selectinload(ClassicText.sections))
            .where(ClassicText.id == text_id)
        )
        return result.scalar_one_or_none()

    async def update_text(
        self,
        text_id: int,
        text_data: ClassicTextUpdate
    ) -> Optional[ClassicText]:
        """更新古籍"""
        text = await self.get_text(text_id)
        if not text:
            return None

        update_data = text_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(text, field, value)

        await self.db.commit()
        await self.db.refresh(text)
        return text

    async def delete_text(self, text_id: int) -> bool:
        """删除古籍"""
        result = await self.db.execute(
            delete(ClassicText).where(ClassicText.id == text_id)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def list_texts(
        self,
        category: Optional[str] = None,
        dynasty: Optional[str] = None,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[ClassicText], int]:
        """列出古籍"""
        query = select(ClassicText)
        conditions = []

        if category:
            conditions.append(ClassicText.category == category)
        if dynasty:
            conditions.append(ClassicText.dynasty == dynasty)

        if conditions:
            query = query.where(and_(*conditions))

        count_query = select(func.count()).select_from(query.subquery())
        count_result = await self.db.execute(count_query)
        total = count_result.scalar()

        result = await self.db.execute(
            query
            .offset(skip)
            .limit(limit)
            .order_by(ClassicText.created_at.desc())
        )
        texts = result.scalars().all()

        return list(texts), total

    async def create_section(self, section_data: ClassicSectionCreate) -> ClassicSection:
        """创建章节"""
        section = ClassicSection(
            text_id=section_data.text_id,
            chapter=section_data.chapter,
            section=section_data.section,
            content=section_data.content,
            page_number=section_data.page_number,
            line_start=section_data.line_start,
            line_end=section_data.line_end
        )
        self.db.add(section)
        await self.db.commit()
        await self.db.refresh(section)
        return section

    async def get_section(self, section_id: int) -> Optional[ClassicSection]:
        """获取章节"""
        result = await self.db.execute(
            select(ClassicSection).where(ClassicSection.id == section_id)
        )
        return result.scalar_one_or_none()

    async def search_sections(
        self,
        text_id: Optional[int] = None,
        keyword: Optional[str] = None,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[ClassicSection], int]:
        """搜索章节"""
        query = select(ClassicSection)
        conditions = []

        if text_id:
            conditions.append(ClassicSection.text_id == text_id)
        if keyword:
            conditions.append(ClassicSection.content.contains(keyword))

        if conditions:
            query = query.where(and_(*conditions))

        count_query = select(func.count()).select_from(query.subquery())
        count_result = await self.db.execute(count_query)
        total = count_result.scalar()

        result = await self.db.execute(
            query
            .offset(skip)
            .limit(limit)
            .order_by(ClassicSection.id)
        )
        sections = result.scalars().all()

        return list(sections), total


class CaseRepository:
    """案例仓储层"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_case(
        self,
        case_data: CaseRecordCreate,
        user_id: Optional[int] = None
    ) -> CaseRecord:
        """创建案例"""
        case = CaseRecord(
            title=case_data.title,
            case_type=case_data.case_type,
            system=case_data.system,
            birth_info=case_data.birth_info,
            chart_data=case_data.chart_data,
            analysis_process=case_data.analysis_process,
            conclusion=case_data.conclusion,
            result_feedback=case_data.result_feedback,
            tags=case_data.tags,
            metadata=case_data.metadata,
            created_by=user_id
        )
        self.db.add(case)
        await self.db.commit()
        await self.db.refresh(case)
        return case

    async def get_case(self, case_id: int) -> Optional[CaseRecord]:
        """获取案例"""
        result = await self.db.execute(
            select(CaseRecord).where(CaseRecord.id == case_id)
        )
        return result.scalar_one_or_none()

    async def update_case(
        self,
        case_id: int,
        case_data: CaseRecordUpdate
    ) -> Optional[CaseRecord]:
        """更新案例"""
        case = await self.get_case(case_id)
        if not case:
            return None

        update_data = case_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(case, field, value)

        await self.db.commit()
        await self.db.refresh(case)
        return case

    async def delete_case(self, case_id: int) -> bool:
        """删除案例"""
        result = await self.db.execute(
            delete(CaseRecord).where(CaseRecord.id == case_id)
        )
        await self.db.commit()
        return result.rowcount > 0

    async def list_cases(
        self,
        case_type: Optional[str] = None,
        system: Optional[str] = None,
        tags: Optional[List[str]] = None,
        is_public: Optional[bool] = None,
        created_by: Optional[int] = None,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[CaseRecord], int]:
        """列出案例"""
        query = select(CaseRecord)
        conditions = []

        if case_type:
            conditions.append(CaseRecord.case_type == case_type)
        if system:
            conditions.append(CaseRecord.system == system)
        if is_public is not None:
            conditions.append(CaseRecord.is_public == is_public)
        if created_by:
            conditions.append(CaseRecord.created_by == created_by)
        if tags:
            for tag in tags:
                conditions.append(CaseRecord.tags.contains([tag]))

        if conditions:
            query = query.where(and_(*conditions))

        count_query = select(func.count()).select_from(query.subquery())
        count_result = await self.db.execute(count_query)
        total = count_result.scalar()

        result = await self.db.execute(
            query
            .offset(skip)
            .limit(limit)
            .order_by(CaseRecord.created_at.desc())
        )
        cases = result.scalars().all()

        return list(cases), total

    async def create_feedback(
        self,
        feedback_data: CaseFeedbackCreate,
        user_id: Optional[int] = None
    ) -> CaseFeedback:
        """创建反馈"""
        feedback = CaseFeedback(
            case_id=feedback_data.case_id,
            user_id=user_id,
            feedback_type=feedback_data.feedback_type,
            content=feedback_data.content,
            rating=feedback_data.rating
        )
        self.db.add(feedback)
        await self.db.commit()
        await self.db.refresh(feedback)
        return feedback

    async def update_feedback(
        self,
        feedback_id: int,
        feedback_data: CaseFeedbackUpdate
    ) -> Optional[CaseFeedback]:
        """更新反馈"""
        result = await self.db.execute(
            select(CaseFeedback).where(CaseFeedback.id == feedback_id)
        )
        feedback = result.scalar_one_or_none()

        if not feedback:
            return None

        update_data = feedback_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(feedback, field, value)

        await self.db.commit()
        await self.db.refresh(feedback)
        return feedback

    async def get_case_feedbacks(
        self,
        case_id: int,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[CaseFeedback], int]:
        """获取案例反馈"""
        query = select(CaseFeedback).where(CaseFeedback.case_id == case_id)

        count_query = select(func.count()).select_from(query.subquery())
        count_result = await self.db.execute(count_query)
        total = count_result.scalar()

        result = await self.db.execute(
            query
            .offset(skip)
            .limit(limit)
            .order_by(CaseFeedback.created_at.desc())
        )
        feedbacks = result.scalars().all()

        return list(feedbacks), total
