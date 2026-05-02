from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal
from datetime import datetime


class BirthInfo(BaseModel):
    """出生信息"""
    year: int = Field(..., description="出生年")
    month: int = Field(..., ge=1, le=12, description="出生月")
    day: int = Field(..., ge=1, le=31, description="出生日")
    hour: int = Field(..., ge=0, le=23, description="出生时")
    minute: int = Field(0, ge=0, le=59, description="出生分")
    timezone: str = Field("Asia/Shanghai", description="时区")
    gender: Literal["male", "female"] = Field(..., description="性别")
    birth_place: Optional[str] = Field(None, description="出生地")


class ChartData(BaseModel):
    """命盘数据"""
    system: str = Field(..., description="命理体系")
    chart_type: str = Field(..., description="命盘类型")
    data: Dict[str, Any] = Field(default_factory=dict, description="命盘原始数据")
    interpretation: Optional[str] = Field(None, description="命盘解读")


class AnalysisStep(BaseModel):
    """分析步骤"""
    step_number: int = Field(..., description="步骤编号")
    step_name: str = Field(..., description="步骤名称")
    input_data: Dict[str, Any] = Field(default_factory=dict, description="输入数据")
    analysis_method: str = Field(..., description="分析方法")
    reasoning: str = Field(..., description="推理过程")
    conclusion: str = Field(..., description="得出结论")
    references: List[str] = Field(default_factory=list, description="参考知识")
    confidence: float = Field(1.0, ge=0.0, le=1.0, description="置信度")


class AnalysisProcess(BaseModel):
    """分析过程"""
    steps: List[AnalysisStep] = Field(default_factory=list, description="分析步骤")
    overall_confidence: float = Field(1.0, ge=0.0, le=1.0, description="整体置信度")
    key_insights: List[str] = Field(default_factory=list, description="关键发现")
    warnings: List[str] = Field(default_factory=list, description="警告信息")


class CaseConclusion(BaseModel):
    """案例结论"""
    summary: str = Field(..., description="结论摘要")
    details: Dict[str, Any] = Field(default_factory=dict, description="详细结论")
    predictions: List[Dict[str, Any]] = Field(default_factory=list, description="预测内容")
    recommendations: List[str] = Field(default_factory=list, description="建议内容")


class FeedbackRecord(BaseModel):
    """反馈记录"""
    feedback_id: str = Field(..., description="反馈ID")
    feedback_type: str = Field(..., description="反馈类型")
    content: str = Field(..., description="反馈内容")
    rating: Optional[int] = Field(None, ge=1, le=5, description="评分")
    evidence: Optional[Dict[str, Any]] = Field(None, description="证据材料")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    status: Literal["pending", "reviewed", "accepted", "rejected"] = Field("pending", description="处理状态")


class CaseValidation(BaseModel):
    """案例验证"""
    is_validated: bool = Field(False, description="是否已验证")
    validation_method: Optional[str] = Field(None, description="验证方法")
    validation_result: Optional[Literal["accurate", "partial", "inaccurate"]] = Field(None, description="验证结果")
    validator_id: Optional[int] = Field(None, description="验证者ID")
    validated_at: Optional[datetime] = Field(None, description="验证时间")
    validation_notes: Optional[str] = Field(None, description="验证备注")


class CaseRecord:
    """案例记录类"""

    def __init__(
        self,
        id: Optional[int] = None,
        title: str = "",
        case_type: str = "",
        system: str = "",
        birth_info: Optional[BirthInfo] = None,
        chart_data: Optional[ChartData] = None,
        analysis_process: Optional[AnalysisProcess] = None,
        conclusion: Optional[CaseConclusion] = None,
        result_feedback: Optional[FeedbackRecord] = None,
        validation: Optional[CaseValidation] = None,
        tags: List[str] = None,
        metadata: Dict[str, Any] = None,
        created_by: Optional[int] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.title = title
        self.case_type = case_type
        self.system = system
        self.birth_info = birth_info
        self.chart_data = chart_data
        self.analysis_process = analysis_process
        self.conclusion = conclusion
        self.result_feedback = result_feedback
        self.validation = validation
        self.tags = tags or []
        self.metadata = metadata or {}
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "id": self.id,
            "title": self.title,
            "case_type": self.case_type,
            "system": self.system,
            "birth_info": self.birth_info.model_dump() if self.birth_info else None,
            "chart_data": self.chart_data.model_dump() if self.chart_data else None,
            "analysis_process": self.analysis_process.model_dump() if self.analysis_process else None,
            "conclusion": self.conclusion.model_dump() if self.conclusion else None,
            "result_feedback": self.result_feedback.model_dump() if self.result_feedback else None,
            "validation": self.validation.model_dump() if self.validation else None,
            "tags": self.tags,
            "metadata": self.metadata,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CaseRecord":
        """从字典创建"""
        birth_info = BirthInfo(**data["birth_info"]) if data.get("birth_info") else None
        chart_data = ChartData(**data["chart_data"]) if data.get("chart_data") else None
        analysis_process = AnalysisProcess(**data["analysis_process"]) if data.get("analysis_process") else None
        conclusion = CaseConclusion(**data["conclusion"]) if data.get("conclusion") else None
        result_feedback = FeedbackRecord(**data["result_feedback"]) if data.get("result_feedback") else None
        validation = CaseValidation(**data["validation"]) if data.get("validation") else None

        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            case_type=data.get("case_type", ""),
            system=data.get("system", ""),
            birth_info=birth_info,
            chart_data=chart_data,
            analysis_process=analysis_process,
            conclusion=conclusion,
            result_feedback=result_feedback,
            validation=validation,
            tags=data.get("tags", []),
            metadata=data.get("metadata", {}),
            created_by=data.get("created_by"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )

    def add_feedback(self, feedback: FeedbackRecord) -> None:
        """添加反馈"""
        self.result_feedback = feedback

    def validate(self, result: str, notes: str = "") -> None:
        """验证案例"""
        self.validation = CaseValidation(
            is_validated=True,
            validation_method="manual",
            validation_result=result,
            validated_at=datetime.now(),
            validation_notes=notes
        )

    def get_summary(self) -> str:
        """获取摘要"""
        parts = [self.title]
        parts.append(f"体系: {self.system}")
        parts.append(f"类型: {self.case_type}")
        if self.conclusion:
            parts.append(f"结论: {self.conclusion.summary[:100]}...")
        return " | ".join(parts)
