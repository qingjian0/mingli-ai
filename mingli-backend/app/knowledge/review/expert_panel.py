from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime


class ExpertSpecialty(Enum):
    """专家专长"""
    BAZI = "八字"
    ZIWEI = "紫微斗数"
    LIUYAO = "六爻"
    FENGSHUI = "风水"
    YIJING = "易经"
    QIMEN = "奇门"
    GENERAL = "综合"


class ExpertLevel(Enum):
    """专家级别"""
    JUNIOR = "junior"
    SENIOR = "senior"
    MASTER = "master"


class Expert:
    """专家"""

    def __init__(
        self,
        expert_id: str,
        name: str,
        specialties: List[ExpertSpecialty],
        level: ExpertLevel = ExpertLevel.JUNIOR
    ):
        self.expert_id = expert_id
        self.name = name
        self.specialties = specialties
        self.level = level
        self.review_history: List[Dict] = []
        self.approval_rate = 0.0
        self.accuracy_rate = 0.0

    def to_dict(self) -> Dict:
        return {
            "expert_id": self.expert_id,
            "name": self.name,
            "specialties": [s.value for s in self.specialties],
            "level": self.level.value,
            "review_count": len(self.review_history),
            "approval_rate": self.approval_rate,
            "accuracy_rate": self.accuracy_rate
        }


class ExpertPanel:
    """专家审核组"""

    def __init__(self):
        self.experts: Dict[str, Expert] = {}
        self.review_assignments: Dict[str, List[str]] = {}

    def register_expert(
        self,
        expert_id: str,
        name: str,
        specialties: List[str],
        level: str = "junior"
    ) -> Expert:
        """注册专家"""
        specialty_enums = []
        for s in specialties:
            try:
                specialty_enums.append(ExpertSpecialty(s))
            except ValueError:
                specialty_enums.append(ExpertSpecialty.GENERAL)

        level_enum = ExpertLevel(level)

        expert = Expert(expert_id, name, specialty_enums, level_enum)
        self.experts[expert_id] = expert
        return expert

    def assign_reviewer(
        self,
        task_id: str,
        system: str,
        required_count: int = 1
    ) -> List[str]:
        """指派审核专家"""
        qualified_experts = self._find_qualified_experts(system)

        if len(qualified_experts) < required_count:
            qualified_experts = list(self.experts.values())

        assigned = qualified_experts[:required_count]
        assigned_ids = [e.expert_id for e in assigned]

        self.review_assignments[task_id] = assigned_ids
        return assigned_ids

    def _find_qualified_experts(self, system: str) -> List[Expert]:
        """查找符合条件的专家"""
        qualified = []

        try:
            system_specialty = ExpertSpecialty(system)
        except ValueError:
            system_specialty = ExpertSpecialty.GENERAL

        for expert in self.experts.values():
            if system_specialty in expert.specialties or ExpertSpecialty.GENERAL in expert.specialties:
                if expert.level in [ExpertLevel.SENIOR, ExpertLevel.MASTER]:
                    qualified.append(expert)

        qualified.sort(key=lambda e: e.accuracy_rate, reverse=True)
        return qualified

    def submit_review(
        self,
        task_id: str,
        expert_id: str,
        decision: str,
        comments: str = ""
    ) -> Dict:
        """提交审核意见"""
        expert = self.experts.get(expert_id)
        if not expert:
            return {"error": "专家不存在"}

        review = {
            "task_id": task_id,
            "expert_id": expert_id,
            "decision": decision,
            "comments": comments,
            "timestamp": datetime.now().isoformat()
        }

        expert.review_history.append(review)
        self._update_expert_stats(expert_id)

        return review

    def _update_expert_stats(self, expert_id: str) -> None:
        """更新专家统计"""
        expert = self.experts.get(expert_id)
        if not expert:
            return

        history = expert.review_history
        if not history:
            return

        approved = sum(1 for r in history if r.get("decision") == "approved")
        expert.approval_rate = approved / len(history)

    def get_expert_workload(self, expert_id: str) -> Dict:
        """获取专家工作量"""
        expert = self.experts.get(expert_id)
        if not expert:
            return {"error": "专家不存在"}

        recent_reviews = [
            r for r in expert.review_history
            if datetime.fromisoformat(r["timestamp"]) > datetime.now() - timedelta(days=30)
        ]

        return {
            "expert_id": expert_id,
            "total_reviews": len(expert.review_history),
            "recent_reviews_30d": len(recent_reviews),
            "approval_rate": expert.approval_rate,
            "accuracy_rate": expert.accuracy_rate
        }

    def get_panel_summary(self) -> Dict:
        """获取专家组概览"""
        total_experts = len(self.experts)
        by_specialty = {}

        for expert in self.experts.values():
            for specialty in expert.specialties:
                if specialty.value not in by_specialty:
                    by_specialty[specialty.value] = 0
                by_specialty[specialty.value] += 1

        by_level = {}
        for expert in self.experts.values():
            level = expert.level.value
            by_level[level] = by_level.get(level, 0) + 1

        return {
            "total_experts": total_experts,
            "by_specialty": by_specialty,
            "by_level": by_level
        }

    def recommend_experts(self, system: str, count: int = 3) -> List[Dict]:
        """推荐专家"""
        qualified = self._find_qualified_experts(system)
        recommended = qualified[:count]

        return [e.to_dict() for e in recommended]


from datetime import timedelta
