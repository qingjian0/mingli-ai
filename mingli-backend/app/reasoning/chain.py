"""
推理链数据结构模块

定义推理步骤和推理链的核心数据结构，用于记录完整的推理过程。
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from enum import Enum
import uuid
from datetime import datetime


class StepStatus(str, Enum):
    """推理步骤状态枚举"""
    PENDING = "pending"       # 待执行
    ACTIVE = "active"        # 执行中
    SUCCESS = "success"       # 成功
    FAILED = "failed"         # 失败
    SKIPPED = "skipped"       # 跳过


class ReasoningStep(BaseModel):
    """推理步骤数据模型

    记录推理过程中的单个步骤，包括输入、输出、使用的规则等信息。
    """
    step_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str = Field(description="步骤描述")
    rule_id: Optional[str] = Field(default=None, description="关联的规则ID")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="输入参数")
    outputs: Dict[str, Any] = Field(default_factory=dict, description="输出结果")
    confidence: float = Field(default=1.0, ge=0.0, le=1.0, description="步骤置信度")
    sources: List[str] = Field(default_factory=list, description="引用来源列表")
    status: StepStatus = Field(default=StepStatus.PENDING, description="步骤状态")
    error_message: Optional[str] = Field(default=None, description="错误信息")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        use_enum_values = True


class AlternativePath(BaseModel):
    """备选推理路径

    当主路径不可行时，记录其他可能的推理路径。
    """
    path_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    path_type: str = Field(description="路径类型：branch/rollback/parallel")
    description: str = Field(description="路径描述")
    steps: List[ReasoningStep] = Field(default_factory=list)
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    reason: str = Field(description="选择此路径的原因")
    discarded: bool = Field(default=False, description="是否已丢弃")


class ReasoningChain(BaseModel):
    """推理链数据模型

    完整的推理过程记录，包含所有推理步骤、备选路径和最终结论。
    """
    chain_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    steps: List[ReasoningStep] = Field(default_factory=list)
    alternative_paths: List[AlternativePath] = Field(default_factory=list)
    final_confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    conclusion: str = Field(default="", description="最终结论")
    context: Dict[str, Any] = Field(default_factory=dict, description="推理上下文")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def add_step(self, step: ReasoningStep) -> None:
        """添加推理步骤"""
        step.created_at = datetime.now()
        self.steps.append(step)
        self.updated_at = datetime.now()

    def add_alternative_path(self, path: AlternativePath) -> None:
        """添加备选推理路径"""
        self.alternative_paths.append(path)
        self.updated_at = datetime.now()

    def get_step(self, step_id: str) -> Optional[ReasoningStep]:
        """根据ID获取推理步骤"""
        for step in self.steps:
            if step.step_id == step_id:
                return step
        return None

    def get_successful_steps(self) -> List[ReasoningStep]:
        """获取所有成功的推理步骤"""
        return [s for s in self.steps if s.status == StepStatus.SUCCESS]

    def calculate_final_confidence(self) -> float:
        """根据所有步骤的置信度计算最终置信度"""
        successful_steps = self.get_successful_steps()
        if not successful_steps:
            return 0.0

        confidences = [s.confidence for s in successful_steps]
        return sum(confidences) / len(confidences)

    def update_conclusion(self, conclusion: str, confidence: Optional[float] = None) -> None:
        """更新最终结论"""
        self.conclusion = conclusion
        if confidence is not None:
            self.final_confidence = confidence
        else:
            self.final_confidence = self.calculate_final_confidence()
        self.updated_at = datetime.now()

    def to_summary(self) -> Dict[str, Any]:
        """生成推理链摘要"""
        return {
            "chain_id": self.chain_id,
            "step_count": len(self.steps),
            "successful_steps": len(self.get_successful_steps()),
            "alternative_paths_count": len(self.alternative_paths),
            "final_confidence": self.final_confidence,
            "conclusion": self.conclusion,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ReasoningContext(BaseModel):
    """推理上下文

    在推理过程中维护和传递的上下文信息。
    """
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_query: str = Field(default="", description="用户查询")
    system_type: str = Field(default="", description="命理体系：八字/紫微斗数/铁板神数等")
    birth_info: Dict[str, Any] = Field(default_factory=dict, description="出生信息")
    chart_data: Dict[str, Any] = Field(default_factory=dict, description="命盘数据")
    intermediate_results: Dict[str, Any] = Field(default_factory=dict)
    variables: Dict[str, Any] = Field(default_factory=dict, description="变量存储")
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def set_variable(self, key: str, value: Any) -> None:
        """设置变量"""
        self.variables[key] = value

    def get_variable(self, key: str, default: Any = None) -> Any:
        """获取变量"""
        return self.variables.get(key, default)

    def merge_chart_data(self, data: Dict[str, Any]) -> None:
        """合并命盘数据"""
        self.chart_data.update(data)
