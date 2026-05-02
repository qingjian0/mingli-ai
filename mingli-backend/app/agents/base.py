"""
Agent基类模块

定义所有领域Agent的抽象基类和通用接口。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set
import hashlib
import json
import logging


class AnalysisType(str, Enum):
    """分析类型枚举"""
    PERSONALITY = "personality"
    CAREER = "career"
    LOVE = "love"
    WEALTH = "wealth"
    HEALTH = "health"
    RELATIONSHIP = "relationship"
    FATE_TREND = "fate_trend"
    LUCKY_PERIOD = "lucky_period"
    COMPATIBILITY = "compatibility"
    DIRECTION = "direction"
    TIMING = "timing"
    GENERAL = "general"


class ConfidenceLevel(str, Enum):
    """置信度等级"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class ReasoningStep:
    """推理步骤"""
    step_id: str
    description: str
    rule_id: Optional[str] = None
    inputs: Dict[str, Any] = field(default_factory=dict)
    outputs: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0
    sources: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "step_id": self.step_id,
            "description": self.description,
            "rule_id": self.rule_id,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "confidence": self.confidence,
            "sources": self.sources,
            "timestamp": self.timestamp.isoformat(),
        }


@dataclass
class AnalysisResult:
    """分析结果"""
    analysis_id: str
    analysis_type: AnalysisType
    agent_name: str
    content: Dict[str, Any]
    summary: str
    confidence: float
    confidence_level: ConfidenceLevel
    reasoning_chain: List[ReasoningStep] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "analysis_id": self.analysis_id,
            "analysis_type": self.analysis_type.value,
            "agent_name": self.agent_name,
            "content": self.content,
            "summary": self.summary,
            "confidence": self.confidence,
            "confidence_level": self.confidence_level.value,
            "reasoning_chain": [step.to_dict() for step in self.reasoning_chain],
            "recommendations": self.recommendations,
            "warnings": self.warnings,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AnalysisResult":
        data = data.copy()
        data["analysis_type"] = AnalysisType(data["analysis_type"])
        data["confidence_level"] = ConfidenceLevel(data["confidence_level"])
        data["created_at"] = datetime.fromisoformat(data["created_at"])
        data["reasoning_chain"] = [
            ReasoningStep(**step) for step in data.get("reasoning_chain", [])
        ]
        return cls(**data)


@dataclass
class TaskContext:
    """任务上下文"""
    user_id: int
    profile_id: int
    chart_id: int
    session_id: str
    chart_data: Dict[str, Any]
    profile_data: Dict[str, Any]
    user_query: str
    requested_types: Set[AnalysisType] = field(default_factory=set)
    options: Dict[str, Any] = field(default_factory=dict)
    memory_context: Optional[Dict[str, Any]] = None

    def get_chart_type(self) -> str:
        return self.chart_data.get("chart_type", "bazi")

    def get_birth_info(self) -> Dict[str, Any]:
        return self.chart_data.get("metadata", {}).get("birth_info", {})


class BaseAgent(ABC):
    """Agent抽象基类

    所有命理分析Agent的基类，定义统一的接口和通用功能。
    """

    def __init__(
        self,
        name: str,
        system_type: str,
        version: str = "1.0.0",
        enable_logging: bool = True
    ):
        self.name = name
        self.system_type = system_type
        self.version = version
        self.enable_logging = enable_logging
        self.logger = self._setup_logger() if enable_logging else None
        self._initialized = False

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(f"mingli.agent.{self.name}")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    @abstractmethod
    async def analyze(self, context: TaskContext) -> AnalysisResult:
        """执行分析并返回结果

        Args:
            context: 任务上下文

        Returns:
            分析结果
        """
        pass

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """返回Agent支持的能力列表

        Returns:
            能力列表
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> List[AnalysisType]:
        """返回Agent支持的分析类型

        Returns:
            分析类型列表
        """
        pass

    def initialize(self) -> bool:
        """初始化Agent资源

        子类可重写此方法来加载规则、初始化模型等资源。

        Returns:
            初始化是否成功
        """
        self._initialized = True
        return True

    def cleanup(self) -> None:
        """清理Agent资源"""
        self._initialized = False
        if self.logger:
            self.logger.info(f"Agent {self.name} cleaned up")

    def _create_reasoning_step(
        self,
        description: str,
        rule_id: Optional[str] = None,
        inputs: Optional[Dict[str, Any]] = None,
        outputs: Optional[Dict[str, Any]] = None,
        confidence: float = 1.0,
        sources: Optional[List[str]] = None
    ) -> ReasoningStep:
        step_id = hashlib.md5(
            f"{self.name}_{description}_{datetime.now().isoformat()}".encode()
        ).hexdigest()[:8]
        return ReasoningStep(
            step_id=step_id,
            description=description,
            rule_id=rule_id,
            inputs=inputs or {},
            outputs=outputs or {},
            confidence=confidence,
            sources=sources or [],
        )

    def _calculate_confidence_level(self, confidence: float) -> ConfidenceLevel:
        if confidence >= 0.8:
            return ConfidenceLevel.HIGH
        elif confidence >= 0.5:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    def _generate_analysis_id(self, context: TaskContext, analysis_type: AnalysisType) -> str:
        content = f"{context.chart_id}_{analysis_type.value}_{datetime.now().isoformat()}"
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def validate_input(self, context: TaskContext) -> tuple[bool, Optional[str]]:
        """验证输入数据

        Args:
            context: 任务上下文

        Returns:
            (是否有效, 错误信息)
        """
        if not context.chart_data:
            return False, "缺少命盘数据"
        if not context.chart_id:
            return False, "缺少命盘ID"
        return True, None

    def get_capabilities_info(self) -> Dict[str, Any]:
        """获取Agent能力详细信息

        Returns:
            包含Agent能力信息的字典
        """
        return {
            "name": self.name,
            "system_type": self.system_type,
            "version": self.version,
            "initialized": self._initialized,
            "capabilities": self.get_capabilities(),
            "supported_types": [t.value for t in self.get_supported_types()],
        }

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name}, type={self.system_type})>"
