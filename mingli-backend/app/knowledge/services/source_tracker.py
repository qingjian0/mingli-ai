"""来源追溯服务"""

import hashlib
import json
from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.knowledge.models.ancient_book import AncientBook, BookSection
from app.knowledge.models.knowledge_entry import KnowledgeEntry
from app.knowledge.models.rule import Rule
from app.knowledge.models.case import Case


class SourceTrace:
    """来源追溯记录"""

    def __init__(
        self,
        entity_type: str,
        entity_id: UUID,
        source_type: str,
        source_info: Dict[str, Any],
        verification_level: str = "pending",
        verified_at: Optional[datetime] = None,
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.source_type = source_type
        self.source_info = source_info
        self.verification_level = verification_level
        self.verified_at = verified_at

    def to_dict(self) -> dict:
        return {
            "entity_type": self.entity_type,
            "entity_id": str(self.entity_id),
            "source_type": self.source_type,
            "source_info": self.source_info,
            "verification_level": self.verification_level,
            "verified_at": self.verified_at.isoformat() if self.verified_at else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SourceTrace":
        return cls(
            entity_type=data["entity_type"],
            entity_id=UUID(data["entity_id"]),
            source_type=data["source_type"],
            source_info=data["source_info"],
            verification_level=data.get("verification_level", "pending"),
            verified_at=datetime.fromisoformat(data["verified_at"])
            if data.get("verified_at")
            else None,
        )


class SourceTrackerService:
    """来源追溯服务"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def track_knowledge_source(
        self,
        entry_id: UUID
    ) -> Optional[SourceTrace]:
        """追踪知识条目的来源"""
        result = await self.session.execute(
            select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
        )
        entry = result.scalar_one_or_none()

        if not entry:
            return None

        source_info = {
            "term": entry.term,
            "source_type": entry.source_type,
            "original_content": entry.original_content[:500] if entry.original_content else None,
        }

        if entry.source_type == "ancient_book" and entry.source_book_id:
            source_info.update({
                "book_id": str(entry.source_book_id),
                "chapter": entry.source_chapter,
                "page": entry.source_page,
            })
            book = await self._get_book(entry.source_book_id)
            if book:
                source_info["book_title"] = book.title
                source_info["book_dynasty"] = book.dynasty

        elif entry.source_type == "expert":
            source_info["author"] = entry.source_author

        elif entry.source_type == "url":
            source_info["url"] = entry.source_url

        verification_level = self._determine_verification_level(
            entry.source_type,
            entry.verification_status,
            entry.source_book_id is not None if entry.source_type == "ancient_book" else True
        )

        return SourceTrace(
            entity_type="knowledge_entry",
            entity_id=entry_id,
            source_type=entry.source_type,
            source_info=source_info,
            verification_level=verification_level,
            verified_at=datetime.utcnow() if verification_level in ["high", "medium"] else None,
        )

    async def track_rule_source(
        self,
        rule_id: UUID
    ) -> Optional[SourceTrace]:
        """追踪规则来源"""
        result = await self.session.execute(
            select(Rule).where(Rule.id == rule_id)
        )
        rule = result.scalar_one_or_none()

        if not rule:
            return None

        source_info = {
            "rule_name": rule.rule_name,
            "rule_type": rule.rule_type,
            "system": rule.system,
        }

        if rule.source_book_id:
            source_info.update({
                "book_id": str(rule.source_book_id),
                "chapter": rule.source_chapter,
                "page": rule.source_page,
            })
            book = await self._get_book(rule.source_book_id)
            if book:
                source_info["book_title"] = book.title

        verification_level = self._determine_verification_level(
            "ancient_book" if rule.source_book_id else "unknown",
            rule.verification_status,
            rule.source_book_id is not None
        )

        return SourceTrace(
            entity_type="rule",
            entity_id=rule_id,
            source_type="ancient_book" if rule.source_book_id else "unknown",
            source_info=source_info,
            verification_level=verification_level,
        )

    async def build_citation_graph(
        self,
        book_id: UUID
    ) -> Dict[str, Any]:
        """构建引用关系图"""
        book = await self._get_book(book_id)
        if not book:
            return {}

        citations = book.citations or []

        book_refs = await self.session.execute(
            select(AncientBook)
            .where(AncientBook.citations.contains([{"book_id": str(book_id)}]))
        )
        referenced_by = [
            {"id": str(b.id), "title": b.title, "dynasty": b.dynasty}
            for b in book_refs.scalars().all()
        ]

        book_cites = []
        for citation in citations:
            if citation.get("type") == "book" and citation.get("book_id"):
                cited_book = await self._get_book(UUID(citation["book_id"]))
                if cited_book:
                    book_cites.append({
                        "id": str(cited_book.id),
                        "title": cited_book.title,
                        "dynasty": cited_book.dynasty,
                    })

        return {
            "book_id": str(book_id),
            "book_title": book.title,
            "cited_by": referenced_by,
            "cites": book_cites,
            "total_citations": len(citations),
        }

    async def trace_lineage(
        self,
        entry_id: UUID,
        entity_type: str = "knowledge_entry"
    ) -> List[SourceTrace]:
        """追溯知识条目或规则的传承脉络"""
        lineage = []

        if entity_type == "knowledge_entry":
            current = await self.track_knowledge_source(entry_id)
            if current:
                lineage.append(current)

                entries = await self.session.execute(
                    select(KnowledgeEntry)
                    .where(KnowledgeEntry.related_entries.contains([str(entry_id)]))
                )
                for related in entries.scalars().all():
                    trace = SourceTrace(
                        entity_type="knowledge_entry",
                        entity_id=related.id,
                        source_type=related.source_type,
                        source_info={
                            "term": related.term,
                            "source_type": related.source_type,
                        },
                        verification_level="pending",
                    )
                    lineage.append(trace)

        return lineage

    async def generate_source_hash(
        self,
        entry_id: UUID,
        entity_type: str = "knowledge_entry"
    ) -> str:
        """生成来源内容哈希"""
        if entity_type == "knowledge_entry":
            result = await self.session.execute(
                select(KnowledgeEntry).where(KnowledgeEntry.id == entry_id)
            )
            entry = result.scalar_one_or_none()
            if entry:
                content = f"{entry.original_content}:{entry.source_chapter}:{entry.source_page}"
                return hashlib.sha256(content.encode()).hexdigest()[:16]

        elif entity_type == "rule":
            result = await self.session.execute(
                select(Rule).where(Rule.id == entry_id)
            )
            rule = result.scalar_one_or_none()
            if rule:
                content = f"{rule.condition}:{rule.result}:{rule.source_chapter}:{rule.source_page}"
                return hashlib.sha256(content.encode()).hexdigest()[:16]

        return ""

    async def verify_source_integrity(
        self,
        entry_id: UUID,
        entity_type: str = "knowledge_entry"
    ) -> Dict[str, Any]:
        """验证来源完整性"""
        trace = None
        if entity_type == "knowledge_entry":
            trace = await self.track_knowledge_source(entry_id)
        elif entity_type == "rule":
            trace = await self.track_rule_source(entry_id)

        if not trace:
            return {"valid": False, "reason": "Entity not found"}

        issues = []

        if trace.source_type == "ancient_book":
            if not trace.source_info.get("book_id"):
                issues.append("Missing book reference")

        if trace.verification_level == "pending":
            issues.append("Source not verified")

        if not trace.source_info.get("original_content"):
            issues.append("Missing original content")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "verification_level": trace.verification_level,
            "source_trace": trace.to_dict(),
        }

    def _determine_verification_level(
        self,
        source_type: str,
        verification_status: str,
        has_book_reference: bool
    ) -> str:
        """确定验证级别"""
        if verification_status == "verified":
            if source_type == "ancient_book" and has_book_reference:
                return "high"
            return "medium"
        elif verification_status == "disputed":
            return "low"
        return "pending"

    async def _get_book(
        self,
        book_id: UUID
    ) -> Optional[AncientBook]:
        """获取古籍"""
        result = await self.session.execute(
            select(AncientBook).where(AncientBook.id == book_id)
        )
        return result.scalar_one_or_none()
