"""
"明理"AI命理平台 Agent系统模块

提供智能命理分析的Agent框架，包括：
- BaseAgent: Agent基类
- Orchestrator: 任务编排器
- ZiweiAgent: 紫微斗数Agent
- BaziAgent: 八字Agent
- QimenAgent: 奇门遁甲Agent
- GeneralAgent: 综合分析Agent
"""

from .base import BaseAgent, AnalysisResult, TaskContext
from .orchestrator import Orchestrator, TaskType, TaskResult, IntentType
from .ziwei_agent import ZiweiAgent
from .bazi_agent import BaziAgent
from .qimen_agent import QimenAgent
from .general_agent import GeneralAgent

__all__ = [
    "BaseAgent",
    "AnalysisResult",
    "TaskContext",
    "Orchestrator",
    "TaskType",
    "TaskResult",
    "IntentType",
    "ZiweiAgent",
    "BaziAgent",
    "QimenAgent",
    "GeneralAgent",
]
