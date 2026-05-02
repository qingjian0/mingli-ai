"""质量控制服务"""

from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any, Tuple
from uuid import UUID

from sqlalchemy import select, func, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.knowledge.models.knowledge_entry import KnowledgeEntry
from app.knowledge.models.rule import Rule
from app.knowledge.models.case import Case
from app.knowledge.models.review import ReviewTask


class QualityMetrics:
    """质量指标"""

    def __init__(
        self,
        total_entries: int,
        verified_entries: int,
        disputed_entries: int,
        avg_accuracy: float,
        avg_reference_count: float,
    ):
        self.total_entries = total_entries
        self.verified_entries = verified_entries
        self.disputed_entries = disputed_entries
        self.avg_accuracy = avg_accuracy
        self.avg_reference_count = avg_reference_count
        self.verification_rate = (
            verified_entries / total_entries if total_entries > 0 else 0
        )

    def to_dict(self) -> dict:
        return {
            "total_entries": self.total_entries,
            "verified_entries": self.verified_entries,
            "disputed_entries": self.disputed_entries,
            "verification_rate": round(self.verification_rate, 4),
            "avg_accuracy": round(self.avg_accuracy, 2),
            "avg_reference_count": round(self.avg_reference_count, 2),
        }


class QualityIssue:
    """质量问题"""

    def __init__(
        self,
        issue_type: str,
        severity: str,
        entity_type: str,
        entity_id: UUID,
        description: str,
        recommendation: str,
    ):
        self.issue_type = issue_type
        self.severity = severity
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.description = description
        self.recommendation = recommendation

    def to_dict(self) -> dict:
        return {
            "issue_type": self.issue_type,
            "severity": self.severity,
            "entity_type": self.entity_type,
            "entity_id": str(self.entity_id),
            "description": self.description,
            "recommendation": self.recommendation,
        }


class QualityControlService:
    """质量控制服务"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_knowledge_metrics(
        self,
        system: Optional[str] = None
    ) -> QualityMetrics:
        """获取知识库质量指标"""
        query = select(KnowledgeEntry)
        if system:
            query = query.where(KnowledgeEntry.system == system)

        result = await self.session.execute(query)
        entries = result.scalars().all()

        total = len(entries)
        verified = sum(1 for e in entries if e.verification_status == "verified")
        disputed = sum(1 for e in entries if e.verification_status == "disputed")

        accuracies = [e.accuracy_rating for e in entries if e.accuracy_rating > 0]
        avg_accuracy = sum(accuracies) / len(accuracies) if accuracies else 0

        reference_counts = [e.reference_count for e in entries]
        avg_ref_count = sum(reference_counts) / len(reference_counts) if reference_counts else 0

        return QualityMetrics(
            total_entries=total,
            verified_entries=verified,
            disputed_entries=disputed,
            avg_accuracy=avg_accuracy,
            avg_reference_count=avg_ref_count,
        )

    async def get_rule_metrics(
        self,
        system: Optional[str] = None
    ) -> Dict[str, Any]:
        """获取规则质量指标"""
        query = select(Rule)
        if system:
            query = query.where(Rule.system == system)

        result = await self.session.execute(query)
        rules = result.scalars().all()

        total = len(rules)
        verified = sum(1 for r in rules if r.verification_status == "verified")
        with_disputes = sum(
            1 for r in rules
            if r.disputes and len(r.disputes) > 0
        )

        schools = {}
        for rule in rules:
            school = rule.school or "unknown"
            schools[school] = schools.get(school, 0) + 1

        return {
            "total_rules": total,
            "verified_rules": verified,
            "disputed_rules": with_disputes,
            "verification_rate": round(verified / total, 4) if total > 0 else 0,
            "rules_by_school": schools,
        }

    async def identify_quality_issues(
        self,
        days_threshold: int = 30
    ) -> List[QualityIssue]:
        """识别质量问题"""
        issues = []

        cutoff_date = datetime.utcnow() - timedelta(days=days_threshold)

        result = await self.session.execute(
            select(KnowledgeEntry)
            .where(
                and_(
                    KnowledgeEntry.review_status == "pending",
                    KnowledgeEntry.created_at < cutoff_date
                )
            )
        )
        for entry in result.scalars().all():
            issues.append(QualityIssue(
                issue_type="pending_review",
                severity="high",
                entity_type="knowledge_entry",
                entity_id=entry.id,
                description=f"知识条目 '{entry.term}' 超过 {days_threshold} 天未审核",
                recommendation="立即安排审核",
            ))

        result = await self.session.execute(
            select(KnowledgeEntry)
            .where(KnowledgeEntry.verification_status == "disputed")
        )
        for entry in result.scalars().all():
            issues.append(QualityIssue(
                issue_type="disputed_content",
                severity="medium",
                entity_type="knowledge_entry",
                entity_id=entry.id,
                description=f"知识条目 '{entry.term}' 存在争议",
                recommendation="组织专家评审解决争议",
            ))

        result = await self.session.execute(
            select(Rule)
            .where(
                and_(
                    Rule.verification_status == "pending",
                    or_(
                        Rule.source_book_id.is_(None),
                        Rule.source_chapter.is_(None)
                    )
                )
            )
        )
        for rule in result.scalars().all():
            issues.append(QualityIssue(
                issue_type="unverified_rule",
                severity="medium",
                entity_type="rule",
                entity_id=rule.id,
                description=f"规则 '{rule.rule_name}' 缺少古籍来源",
                recommendation="补充原典出处",
            ))

        result = await self.session.execute(
            select(KnowledgeEntry)
            .where(KnowledgeEntry.accuracy_rating < 3.0)
            .where(KnowledgeEntry.reference_count >= 10)
        )
        for entry in result.scalars().all():
            issues.append(QualityIssue(
                issue_type="low_accuracy",
                severity="high",
                entity_type="knowledge_entry",
                entity_id=entry.id,
                description=f"知识条目 '{entry.term}' 被引用 {entry.reference_count} 次但准确性评分较低",
                recommendation="复核并更新条目内容",
            ))

        return issues

    async def create_review_task(
        self,
        entry_type: str,
        entry_id: UUID,
        priority: str = "medium",
        review_level: int = 1,
    ) -> ReviewTask:
        """创建审核任务"""
        task = ReviewTask(
            entry_type=entry_type,
            entry_id=entry_id,
            review_level=review_level,
            priority=priority,
            status="pending",
        )
        self.session.add(task)
        await self.session.flush()
        await self.session.refresh(task)
        return task

    async def get_pending_review_tasks(
        self,
        skip: int = 0,
        limit: int = 20,
        priority: Optional[str] = None,
    ) -> Tuple[List[ReviewTask], int]:
        """获取待审核任务"""
        query = select(ReviewTask).where(ReviewTask.status == "pending")

        if priority:
            query = query.where(ReviewTask.priority == priority)

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = (
            query.order_by(
                ReviewTask.priority.desc(),
                ReviewTask.created_at.asc()
            )
            .offset(skip)
            .limit(limit)
        )

        result = await self.session.execute(query)
        return list(result.scalars().all()), total

    async def approve_entry(
        self,
        entry_id: UUID,
        entry_type: str,
        reviewer_id: UUID,
        notes: str = "",
    ) -> bool:
        """批准条目"""
        if entry_type == "knowledge_entry":
            result = await self.session.execute(
                select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
            )
            entry = result.scalar_one_or_none()
            if entry:
                entry.review_status = "approved"
                entry.reviewed_by = reviewer_id
                entry.reviewed_at = datetime.utcnow()
                await self.session.flush()
                return True

        elif entry_type == "rule":
            result = await self.session.execute(
                select(Rule).where(Rule.id == entry_id)
            )
            rule = result.scalar_one_or_none()
            if rule:
                rule.review_status = "approved"
                await self.session.flush()
                return True

        return False

    async def reject_entry(
        self,
        entry_id: UUID,
        entry_type: str,
        reviewer_id: UUID,
        reason: str,
    ) -> bool:
        """拒绝条目"""
        task_result = await self.session.execute(
            select(ReviewTask)
            .where(
                and_(
                    ReviewTask.entry_id == entry_id,
                    ReviewTask.entry_type == entry_type
                )
            )
        )
        task = task_result.scalar_one_or_none()

        if task:
            task.status = "rejected"
            task.reviewer_id = reviewer_id
            task.review_result = "rejected"
            task.review_notes = reason
            task.completed_at = datetime.utcnow()
            await self.session.flush()
            return True

        return False

    async def resolve_dispute(
        self,
        entry_id: UUID,
        entry_type: str,
        resolution: str,
    ) -> bool:
        """解决争议"""
        if entry_type == "knowledge_entry":
            result = await self.session.execute(
                select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
            )
            entry = result.scalar_one_or_none()
            if entry:
                entry.verification_status = "verified"
                await self.session.flush()
                return True

        elif entry_type == "rule":
            result = await self.session.execute(
                select(Rule).where(Rule.id == entry_id)
            )
            rule = result.scalar_one_or_none()
            if rule:
                rule.verification_status = "verified"
                await self.session.flush()
                return True

        return False

    async def get_system_statistics(
        self,
        system: str
    ) -> Dict[str, Any]:
        """获取系统统计信息"""
        entry_metrics = await self.get_knowledge_metrics(system=system)
        rule_metrics = await self.get_rule_metrics(system=system)

        result = await self.session.execute(
            select(func.count())
            .select_from(Case)
            .where(Case.system == system)
        )
        total_cases = result.scalar() or 0

        result = await self.session.execute(
            select(func.count())
            .select_from(Case)
            .where(
                and_(
                    Case.system == system,
                    Case.accuracy_rating.isnot(None)
                )
            )
        )
        cases_with_rating = result.scalar() or 0

        return {
            "system": system,
            "knowledge_metrics": entry_metrics.to_dict(),
            "rule_metrics": rule_metrics,
            "total_cases": total_cases,
            "cases_with_rating": cases_with_rating,
            "report_generated_at": datetime.utcnow().isoformat(),
        }
