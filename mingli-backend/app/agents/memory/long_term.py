"""
长期记忆模块

管理Profile数据、历史分析摘要等信息。
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.profile import Profile
    from app.models.analysis import Analysis

import json


@dataclass
class ProfileSummary:
    """Profile摘要"""
    profile_id: int
    user_id: int
    name: str
    chart_types: List[str] = field(default_factory=list)
    last_analysis_date: Optional[datetime] = None
    analysis_count: int = 0
    key_insights: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "profile_id": self.profile_id,
            "user_id": self.user_id,
            "name": self.name,
            "chart_types": self.chart_types,
            "last_analysis_date": self.last_analysis_date.isoformat() if self.last_analysis_date else None,
            "analysis_count": self.analysis_count,
            "key_insights": self.key_insights,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProfileSummary":
        data = data.copy()
        if data.get("last_analysis_date"):
            data["last_analysis_date"] = datetime.fromisoformat(data["last_analysis_date"])
        return cls(**data)


@dataclass
class HistoricalAnalysis:
    """历史分析记录"""
    analysis_id: int
    chart_id: int
    analysis_type: str
    summary: str
    created_at: datetime
    confidence: float = 0.8
    content_hash: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "analysis_id": self.analysis_id,
            "chart_id": self.chart_id,
            "analysis_type": self.analysis_type,
            "summary": self.summary,
            "created_at": self.created_at.isoformat(),
            "confidence": self.confidence,
            "content_hash": self.content_hash,
            "tags": self.tags,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "HistoricalAnalysis":
        data = data.copy()
        data["created_at"] = datetime.fromisoformat(data["created_at"])
        return cls(**data)


class LongTermMemory:
    """长期记忆管理器

    管理Profile摘要、历史分析记录等长期信息。
    """

    def __init__(self, max_insights: int = 10):
        self._profiles: Dict[int, ProfileSummary] = {}
        self._analyses: Dict[int, List[HistoricalAnalysis]] = {}
        self._profile_analyses_index: Dict[int, List[int]] = {}
        self._max_insights = max_insights

    def create_profile_summary(
        self,
        profile_id: int,
        user_id: int,
        name: str,
        chart_types: Optional[List[str]] = None
    ) -> ProfileSummary:
        summary = ProfileSummary(
            profile_id=profile_id,
            user_id=user_id,
            name=name,
            chart_types=chart_types or []
        )
        self._profiles[profile_id] = summary
        self._analyses[profile_id] = []
        self._profile_analyses_index[profile_id] = []
        return summary

    def get_profile_summary(self, profile_id: int) -> Optional[ProfileSummary]:
        return self._profiles.get(profile_id)

    def update_profile_summary(
        self,
        profile_id: int,
        **kwargs
    ) -> bool:
        summary = self._profiles.get(profile_id)
        if not summary:
            return False

        for key, value in kwargs.items():
            if hasattr(summary, key):
                setattr(summary, key, value)

        return True

    def add_analysis_record(
        self,
        profile_id: int,
        analysis_id: int,
        chart_id: int,
        analysis_type: str,
        summary: str,
        confidence: float = 0.8,
        content_hash: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[HistoricalAnalysis]:
        if profile_id not in self._profiles:
            return None

        record = HistoricalAnalysis(
            analysis_id=analysis_id,
            chart_id=chart_id,
            analysis_type=analysis_type,
            summary=summary,
            created_at=datetime.now(),
            confidence=confidence,
            content_hash=content_hash,
            tags=tags or [],
            metadata=metadata or {}
        )

        self._analyses[profile_id].append(record)
        self._profile_analyses_index[profile_id].append(analysis_id)

        self._profiles[profile_id].analysis_count += 1
        self._profiles[profile_id].last_analysis_date = datetime.now()

        self._update_profile_insights(profile_id, record)

        return record

    def _update_profile_insights(self, profile_id: int, analysis: HistoricalAnalysis) -> None:
        summary = self._profiles.get(profile_id)
        if not summary:
            return

        if len(summary.key_insights) >= self._max_insights:
            summary.key_insights.pop(0)

        insight_text = f"[{analysis.analysis_type}] {analysis.summary[:50]}"
        if insight_text not in summary.key_insights:
            summary.key_insights.append(insight_text)

    def get_analyses(
        self,
        profile_id: int,
        analysis_type: Optional[str] = None,
        limit: Optional[int] = None
    ) -> List[HistoricalAnalysis]:
        if profile_id not in self._analyses:
            return []

        analyses = self._analyses[profile_id]

        if analysis_type:
            analyses = [a for a in analyses if a.analysis_type == analysis_type]

        analyses = sorted(analyses, key=lambda x: x.created_at, reverse=True)

        if limit:
            analyses = analyses[:limit]

        return analyses

    def get_analysis_by_id(
        self,
        profile_id: int,
        analysis_id: int
    ) -> Optional[HistoricalAnalysis]:
        analyses = self._analyses.get(profile_id, [])
        for analysis in analyses:
            if analysis.analysis_id == analysis_id:
                return analysis
        return None

    def search_analyses(
        self,
        profile_id: int,
        query: str,
        limit: int = 10
    ) -> List[HistoricalAnalysis]:
        analyses = self._analyses.get(profile_id, [])
        query_lower = query.lower()

        matched = [
            a for a in analyses
            if query_lower in a.summary.lower()
            or query_lower in a.analysis_type.lower()
            or any(query_lower in tag.lower() for tag in a.tags)
        ]

        matched.sort(key=lambda x: x.created_at, reverse=True)
        return matched[:limit]

    def get_analysis_by_tags(
        self,
        profile_id: int,
        tags: List[str],
        match_all: bool = False
    ) -> List[HistoricalAnalysis]:
        analyses = self._analyses.get(profile_id, [])
        matched = []

        for analysis in analyses:
            if match_all:
                if all(tag in analysis.tags for tag in tags):
                    matched.append(analysis)
            else:
                if any(tag in analysis.tags for tag in tags):
                    matched.append(analysis)

        return sorted(matched, key=lambda x: x.created_at, reverse=True)

    def delete_analysis(self, profile_id: int, analysis_id: int) -> bool:
        if profile_id not in self._analyses:
            return False

        analyses = self._analyses[profile_id]
        for i, analysis in enumerate(analyses):
            if analysis.analysis_id == analysis_id:
                analyses.pop(i)
                if analysis_id in self._profile_analyses_index[profile_id]:
                    self._profile_analyses_index[profile_id].remove(analysis_id)

                if self._profiles.get(profile_id):
                    self._profiles[profile_id].analysis_count = max(
                        0, self._profiles[profile_id].analysis_count - 1
                    )
                return True

        return False

    def get_profile_stats(self, profile_id: int) -> Dict[str, Any]:
        analyses = self._analyses.get(profile_id, [])

        type_counts: Dict[str, int] = {}
        for analysis in analyses:
            type_counts[analysis.analysis_type] = type_counts.get(analysis.analysis_type, 0) + 1

        avg_confidence = sum(a.confidence for a in analyses) / len(analyses) if analyses else 0

        return {
            "total_analyses": len(analyses),
            "analysis_types": type_counts,
            "average_confidence": round(avg_confidence, 2),
            "first_analysis_date": analyses[-1].created_at.isoformat() if analyses else None,
            "last_analysis_date": analyses[0].created_at.isoformat() if analyses else None
        }

    def get_user_profiles(self, user_id: int) -> List[ProfileSummary]:
        return [
            summary for summary in self._profiles.values()
            if summary.user_id == user_id
        ]

    def serialize(self) -> str:
        data = {
            "profiles": {
                pid: summary.to_dict()
                for pid, summary in self._profiles.items()
            },
            "analyses": {
                pid: [a.to_dict() for a in analyses]
                for pid, analyses in self._analyses.items()
            }
        }
        return json.dumps(data)

    def deserialize(self, data: str) -> bool:
        try:
            loaded = json.loads(data)
            self._profiles = {
                int(pid): ProfileSummary.from_dict(s)
                for pid, s in loaded.get("profiles", {}).items()
            }
            self._analyses = {
                int(pid): [HistoricalAnalysis.from_dict(a) for a in analyses]
                for pid, analyses in loaded.get("analyses", {}).items()
            }
            self._profile_analyses_index = {
                pid: [a.analysis_id for a in analyses]
                for pid, analyses in self._analyses.items()
            }
            return True
        except Exception:
            return False

    def clear_profile(self, profile_id: int) -> bool:
        if profile_id in self._profiles:
            del self._profiles[profile_id]
        if profile_id in self._analyses:
            del self._analyses[profile_id]
        if profile_id in self._profile_analyses_index:
            del self._profile_analyses_index[profile_id]
        return True
