from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime


class DisputeType(Enum):
    """争议类型"""
    FACTUAL = "factual"
    INTERPRETATION = "interpretation"
    SOURCE = "source"
    METHODOLOGY = "methodology"


class DisputeStatus(Enum):
    """争议状态"""
    PENDING = "pending"
    UNDER_REVIEW = "under_review"
    RESOLVED = "resolved"
    ESCALATED = "escalated"


class Dispute:
    """争议"""

    def __init__(
        self,
        dispute_id: str,
        entry1_id: str,
        entry2_id: str,
        dispute_type: DisputeType,
        description: str
    ):
        self.dispute_id = dispute_id
        self.entry1_id = entry1_id
        self.entry2_id = entry2_id
        self.dispute_type = dispute_type
        self.description = description
        self.status = DisputeStatus.PENDING
        self.positions: List[Dict] = []
        self.resolution: Optional[Dict] = None
        self.created_at = datetime.now().isoformat()


class DisputeResolver:
    """争议解决器"""

    def __init__(self):
        self.disputes: Dict[str, Dispute] = {}
        self.resolution_templates: Dict[DisputeType, str] = {
            DisputeType.FACTUAL: "经核实，{fact}，结论：{conclusion}",
            DisputeType.INTERPRETATION: "综合考量，采纳{position}的观点",
            DisputeType.SOURCE: "经查证，{source_info}更可靠",
            DisputeType.METHODOLOGY: "按{method}方法论统一处理"
        }

    def create_dispute(
        self,
        entry1_id: str,
        entry2_id: str,
        dispute_type: str,
        description: str
    ) -> Dict:
        """创建争议"""
        import uuid

        try:
            dtype = DisputeType(dispute_type)
        except ValueError:
            dtype = DisputeType.FACTUAL

        dispute = Dispute(
            dispute_id=str(uuid.uuid4()),
            entry1_id=entry1_id,
            entry2_id=entry2_id,
            dispute_type=dtype,
            description=description
        )

        self.disputes[dispute.dispute_id] = dispute

        return {
            "dispute_id": dispute.dispute_id,
            "status": dispute.status.value,
            "created_at": dispute.created_at
        }

    def add_position(
        self,
        dispute_id: str,
        expert_id: str,
        expert_name: str,
        position: str,
        evidence: str = ""
    ) -> Dict:
        """添加立场"""
        dispute = self.disputes.get(dispute_id)
        if not dispute:
            return {"error": "争议不存在"}

        position_data = {
            "expert_id": expert_id,
            "expert_name": expert_name,
            "position": position,
            "evidence": evidence,
            "timestamp": datetime.now().isoformat()
        }

        dispute.positions.append(position_data)

        return {
            "dispute_id": dispute_id,
            "position_added": True,
            "total_positions": len(dispute.positions)
        }

    def resolve_dispute(
        self,
        dispute_id: str,
        resolution: str,
        conclusion: str,
        winner: Optional[str] = None
    ) -> Dict:
        """解决争议"""
        dispute = self.disputes.get(dispute_id)
        if not dispute:
            return {"error": "争议不存在"}

        template = self.resolution_templates.get(
            dispute.dispute_type,
            "综合各方意见，做出如下裁决：{conclusion}"
        )

        dispute.resolution = {
            "resolution": resolution,
            "conclusion": conclusion,
            "winner": winner,
            "template_applied": template,
            "resolved_at": datetime.now().isoformat(),
            "resolved_by": "system"
        }

        dispute.status = DisputeStatus.RESOLVED

        return {
            "dispute_id": dispute_id,
            "status": "resolved",
            "resolution": dispute.resolution
        }

    def escalate_dispute(self, dispute_id: str, reason: str) -> Dict:
        """升级争议"""
        dispute = self.disputes.get(dispute_id)
        if not dispute:
            return {"error": "争议不存在"}

        dispute.status = DisputeStatus.ESCALATED

        return {
            "dispute_id": dispute_id,
            "status": "escalated",
            "reason": reason,
            "escalated_at": datetime.now().isoformat()
        }

    def get_dispute_summary(self, dispute_id: str) -> Optional[Dict]:
        """获取争议摘要"""
        dispute = self.disputes.get(dispute_id)
        if not dispute:
            return None

        return {
            "dispute_id": dispute.dispute_id,
            "entry1_id": dispute.entry1_id,
            "entry2_id": dispute.entry2_id,
            "dispute_type": dispute.dispute_type.value,
            "description": dispute.description,
            "status": dispute.status.value,
            "position_count": len(dispute.positions),
            "resolution": dispute.resolution,
            "created_at": dispute.created_at
        }

    def get_pending_disputes(self) -> List[Dict]:
        """获取待处理争议"""
        pending = [
            d for d in self.disputes.values()
            if d.status in [DisputeStatus.PENDING, DisputeStatus.UNDER_REVIEW]
        ]

        return [self.get_dispute_summary(d.dispute_id) for d in pending]

    def get_disputes_by_entry(self, entry_id: str) -> List[Dict]:
        """获取与条目相关的争议"""
        related = [
            d for d in self.disputes.values()
            if d.entry1_id == entry_id or d.entry2_id == entry_id
        ]

        return [self.get_dispute_summary(d.dispute_id) for d in related]

    def analyze_dispute_patterns(self) -> Dict:
        """分析争议模式"""
        dispute_types: Dict[str, int] = {}
        resolution_count = 0
        escalation_count = 0

        for dispute in self.disputes.values():
            dtype = dispute.dispute_type.value
            dispute_types[dtype] = dispute_types.get(dtype, 0) + 1

            if dispute.status == DisputeStatus.RESOLVED:
                resolution_count += 1
            elif dispute.status == DisputeStatus.ESCALATED:
                escalation_count += 1

        total = len(self.disputes)

        return {
            "total_disputes": total,
            "by_type": dispute_types,
            "resolved_count": resolution_count,
            "escalated_count": escalation_count,
            "resolution_rate": resolution_count / total if total > 0 else 0,
            "escalation_rate": escalation_count / total if total > 0 else 0
        }
