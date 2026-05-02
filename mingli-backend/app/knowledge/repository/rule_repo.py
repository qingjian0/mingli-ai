"""规则仓储层"""

from typing import Optional, List, Tuple
from uuid import UUID

from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.knowledge.models.rule import Rule
from app.knowledge.schemas.rule import RuleCreate, RuleUpdate


class RuleRepository:
    """规则仓储"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: RuleCreate) -> Rule:
        """创建规则"""
        rule = Rule(**data.model_dump())
        self.session.add(rule)
        await self.session.flush()
        await self.session.refresh(rule)
        return rule

    async def get_by_id(self, rule_id: UUID) -> Optional[Rule]:
        """根据ID获取规则"""
        result = await self.session.execute(
            select(Rule).where(Rule.id == rule_id)
        )
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 20,
        system: Optional[str] = None,
        rule_type: Optional[str] = None,
        school: Optional[str] = None,
        verification_status: Optional[str] = None,
    ) -> Tuple[List[Rule], int]:
        """获取规则列表"""
        query = select(Rule)

        if system:
            query = query.where(Rule.system == system)
        if rule_type:
            query = query.where(Rule.rule_type == rule_type)
        if school:
            query = query.where(Rule.school == school)
        if verification_status:
            query = query.where(Rule.verification_status == verification_status)

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.order_by(Rule.created_at.desc())
        query = query.offset(skip).limit(limit)

        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def update(
        self,
        rule_id: UUID,
        data: RuleUpdate
    ) -> Optional[Rule]:
        """更新规则"""
        rule = await self.get_by_id(rule_id)
        if not rule:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(rule, key, value)

        await self.session.flush()
        await self.session.refresh(rule)
        return rule

    async def delete(self, rule_id: UUID) -> bool:
        """删除规则"""
        rule = await self.get_by_id(rule_id)
        if not rule:
            return False

        await self.session.delete(rule)
        await self.session.flush()
        return True

    async def search(
        self,
        keyword: Optional[str] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> Tuple[List[Rule], int]:
        """搜索规则"""
        query = select(Rule)

        if keyword:
            query = query.where(
                Rule.rule_name.ilike(f"%{keyword}%")
                | Rule.condition.ilike(f"%{keyword}%")
                | Rule.explanation.ilike(f"%{keyword}%")
            )

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total

    async def get_by_source_book(
        self,
        book_id: UUID
    ) -> List[Rule]:
        """获取指定古籍来源的所有规则"""
        result = await self.session.execute(
            select(Rule)
            .where(Rule.source_book_id == book_id)
            .order_by(Rule.rule_name)
        )
        return list(result.scalars().all())

    async def get_by_school(
        self,
        school: str
    ) -> List[Rule]:
        """获取指定流派的所有规则"""
        result = await self.session.execute(
            select(Rule)
            .where(Rule.school == school)
            .order_by(Rule.rule_name)
        )
        return list(result.scalars().all())

    async def get_alternative_rules(
        self,
        rule_id: UUID
    ) -> List[Rule]:
        """获取替代规则"""
        rule = await self.get_by_id(rule_id)
        if not rule or not rule.alternative_rules:
            return []

        alternative_ids = rule.alternative_rules
        result = await self.session.execute(
            select(Rule)
            .where(Rule.id.in_(alternative_ids))
        )
        return list(result.scalars().all())

    async def add_verified_case(
        self,
        rule_id: UUID,
        case_id: UUID,
        case_summary: dict
    ) -> Optional[Rule]:
        """添加验证案例"""
        rule = await self.get_by_id(rule_id)
        if not rule:
            return None

        verified_cases = rule.verified_cases or []
        verified_cases.append({
            "case_id": str(case_id),
            "summary": case_summary
        })
        rule.verified_cases = verified_cases

        await self.session.flush()
        await self.session.refresh(rule)
        return rule

    async def add_dispute(
        self,
        rule_id: UUID,
        dispute: dict
    ) -> Optional[Rule]:
        """添加争议"""
        rule = await self.get_by_id(rule_id)
        if not rule:
            return None

        disputes = rule.disputes or []
        disputes.append(dispute)
        rule.disputes = disputes

        await self.session.flush()
        await self.session.refresh(rule)
        return rule

    async def get_disputed_rules(
        self,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[List[Rule], int]:
        """获取有争议的规则"""
        query = (
            select(Rule)
            .where(Rule.disputes.length() > 0)
        )

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        items = list(result.scalars().all())

        return items, total
