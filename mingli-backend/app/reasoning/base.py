"""
推理引擎基类模块

定义推理引擎的抽象基类和通用功能接口。
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Type
from datetime import datetime
import logging

from .chain import ReasoningChain, ReasoningStep, ReasoningContext, StepStatus


class BaseReasoningEngine(ABC):
    """推理引擎抽象基类

    所有命理推理引擎的基类，定义统一的接口和通用功能。
    子类需要实现具体的推理逻辑。
    """

    def __init__(
        self,
        system_name: str,
        version: str = "1.0.0",
        enable_logging: bool = True
    ):
        """初始化推理引擎

        Args:
            system_name: 命理体系名称（如"八字"、"紫微斗数"）
            version: 引擎版本号
            enable_logging: 是否启用日志记录
        """
        self.system_name = system_name
        self.version = version
        self.enable_logging = enable_logging
        self.logger = self._setup_logger() if enable_logging else None
        self._initialized = False

    def _setup_logger(self) -> logging.Logger:
        """配置日志记录器"""
        logger = logging.getLogger(f"mingli.{self.system_name}")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    @abstractmethod
    def initialize(self) -> bool:
        """初始化引擎资源

        子类需要实现此方法来加载规则、初始化模型等资源。

        Returns:
            初始化是否成功
        """
        pass

    @abstractmethod
    def reason(
        self,
        context: ReasoningContext,
        chain: ReasoningChain
    ) -> ReasoningChain:
        """执行推理

        核心推理方法，子类需要实现具体的推理逻辑。

        Args:
            context: 推理上下文，包含输入数据和中间状态
            chain: 推理链，用于记录推理步骤

        Returns:
            更新后的推理链
        """
        pass

    @abstractmethod
    def validate_input(self, context: ReasoningContext) -> tuple[bool, Optional[str]]:
        """验证输入数据

        检查上下文中的输入数据是否满足推理要求。

        Args:
            context: 推理上下文

        Returns:
            (是否有效, 错误信息)
        """
        pass

    @abstractmethod
    def extract_features(self, context: ReasoningContext) -> Dict[str, Any]:
        """从上下文中提取特征

        将原始输入数据转换为推理引擎可用的特征表示。

        Args:
            context: 推理上下文

        Returns:
            特征字典
        """
        pass

    def _create_step(
        self,
        description: str,
        rule_id: Optional[str] = None,
        inputs: Optional[Dict[str, Any]] = None,
        outputs: Optional[Dict[str, Any]] = None,
        confidence: float = 1.0,
        sources: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> ReasoningStep:
        """创建推理步骤的辅助方法

        Args:
            description: 步骤描述
            rule_id: 关联的规则ID
            inputs: 输入参数
            outputs: 输出结果
            confidence: 置信度
            sources: 引用来源
            metadata: 元数据

        Returns:
            推理步骤对象
        """
        return ReasoningStep(
            description=description,
            rule_id=rule_id,
            inputs=inputs or {},
            outputs=outputs or {},
            confidence=confidence,
            sources=sources or [],
            metadata=metadata or {},
            status=StepStatus.PENDING
        )

    def _log_step(self, step: ReasoningStep, chain: ReasoningChain) -> None:
        """记录推理步骤到日志和链中

        Args:
            step: 推理步骤
            chain: 推理链
        """
        if self.logger and step.status == StepStatus.SUCCESS:
            self.logger.info(f"Step {step.step_id}: {step.description}")
            self.logger.debug(f"  Inputs: {step.inputs}")
            self.logger.debug(f"  Outputs: {step.outputs}")

        chain.add_step(step)

    def _mark_step_success(
        self,
        step: ReasoningStep,
        outputs: Dict[str, Any],
        confidence: float = 1.0
    ) -> ReasoningStep:
        """标记步骤成功并更新输出

        Args:
            step: 推理步骤
            outputs: 输出结果
            confidence: 置信度

        Returns:
            更新后的步骤
        """
        step.status = StepStatus.SUCCESS
        step.outputs = outputs
        step.confidence = confidence
        return step

    def _mark_step_failed(
        self,
        step: ReasoningStep,
        error_message: str
    ) -> ReasoningStep:
        """标记步骤失败

        Args:
            step: 推理步骤
            error_message: 错误信息

        Returns:
            更新后的步骤
        """
        step.status = StepStatus.FAILED
        step.error_message = error_message
        if self.logger:
            self.logger.error(f"Step {step.step_id} failed: {error_message}")
        return step

    def get_capabilities(self) -> Dict[str, Any]:
        """获取引擎能力描述

        Returns:
            包含引擎能力信息的字典
        """
        return {
            "system_name": self.system_name,
            "version": self.version,
            "initialized": self._initialized,
            "features": self._get_feature_list()
        }

    @abstractmethod
    def _get_feature_list(self) -> List[str]:
        """获取支持的特性列表

        子类需要实现此方法，返回支持的特性名称列表。

        Returns:
            特性名称列表
        """
        pass

    def cleanup(self) -> None:
        """清理引擎资源

        子类可以重写此方法来释放占用的资源。
        """
        self._initialized = False
        if self.logger:
            self.logger.info(f"Engine {self.system_name} cleaned up")


class CompositeReasoningEngine(BaseReasoningEngine):
    """组合推理引擎

    支持多个子引擎协同工作的组合推理引擎。
    可用于多体系融合推理。
    """

    def __init__(
        self,
        system_name: str = "composite",
        version: str = "1.0.0"
    ):
        super().__init__(system_name, version)
        self.engines: Dict[str, BaseReasoningEngine] = {}
        self.primary_engine: Optional[str] = None

    def add_engine(self, name: str, engine: BaseReasoningEngine) -> None:
        """添加子引擎

        Args:
            name: 引擎名称
            engine: 推理引擎实例
        """
        self.engines[name] = engine
        if self.primary_engine is None:
            self.primary_engine = name

    def set_primary_engine(self, name: str) -> None:
        """设置主引擎

        Args:
            name: 引擎名称
        """
        if name not in self.engines:
            raise ValueError(f"Engine '{name}' not found")
        self.primary_engine = name

    def initialize(self) -> bool:
        """初始化所有子引擎"""
        success = True
        for name, engine in self.engines.items():
            if not engine.initialize():
                if self.logger:
                    self.logger.error(f"Failed to initialize engine: {name}")
                success = False
        self._initialized = success
        return success

    def reason(
        self,
        context: ReasoningContext,
        chain: ReasoningChain
    ) -> ReasoningChain:
        """协调多个子引擎进行推理"""
        if not self._initialized:
            raise RuntimeError("Engine not initialized")

        for name, engine in self.engines.items():
            if self.logger:
                self.logger.info(f"Running engine: {name}")
            context.system_type = engine.system_name
            chain = engine.reason(context, chain)

        return chain

    def validate_input(self, context: ReasoningContext) -> tuple[bool, Optional[str]]:
        """验证输入是否满足至少一个子引擎的要求"""
        for engine in self.engines.values():
            valid, error = engine.validate_input(context)
            if valid:
                return True, None
        return False, "Input not valid for any registered engine"

    def extract_features(self, context: ReasoningContext) -> Dict[str, Any]:
        """提取所有子引擎的特征"""
        features = {}
        for name, engine in self.engines.items():
            features[name] = engine.extract_features(context)
        return features

    def _get_feature_list(self) -> List[str]:
        """获取所有子引擎的特性"""
        features = []
        for name, engine in self.engines.items():
            features.extend([
                f"{name}.{f}" for f in engine._get_feature_list()
            ])
        return features
