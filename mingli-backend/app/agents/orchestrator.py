"""
任务编排器模块

负责任务理解、子任务分解、Agent调度与协调、结果整合与质量控制。
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Callable
import asyncio
import hashlib
import json
import logging


class IntentType(str, Enum):
    """意图类型枚举"""
    PERSONALITY_ANALYSIS = "personality_analysis"
    CAREER_ANALYSIS = "career_analysis"
    LOVE_ANALYSIS = "love_analysis"
    WEALTH_ANALYSIS = "wealth_analysis"
    HEALTH_ANALYSIS = "health_analysis"
    FATE_TREND = "fate_trend"
    LUCKY_PERIOD = "lucky_period"
    LUCKY_DIRECTION = "lucky_direction"
    LUCKY_TIMING = "lucky_timing"
    COMPATIBILITY = "compatibility"
    COMPREHENSIVE = "comprehensive"
    UNKNOWN = "unknown"


class TaskType(str, Enum):
    """任务类型枚举"""
    SINGLE_ANALYSIS = "single_analysis"
    MULTI_ANALYSIS = "multi_analysis"
    INTEGRATED_ANALYSIS = "integrated_analysis"
    CONSULTATION = "consultation"


@dataclass
class SubTask:
    """子任务"""
    task_id: str
    intent_type: IntentType
    agent_name: str
    analysis_types: Set[str]
    priority: int = 1
    dependencies: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskResult:
    """任务结果"""
    task_id: str
    intent_type: IntentType
    success: bool
    results: List[Dict[str, Any]] = field(default_factory=list)
    error: Optional[str] = None
    execution_time: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestrationContext:
    """编排上下文"""
    user_id: int
    session_id: str
    profile_id: int
    chart_id: int
    chart_data: Dict[str, Any]
    profile_data: Dict[str, Any]
    user_query: str
    intent: IntentType = IntentType.UNKNOWN
    subtasks: List[SubTask] = field(default_factory=list)
    results: List[TaskResult] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


class IntentClassifier:
    """意图分类器

    分析用户查询，识别用户意图并映射到相应的分析类型。
    """

    def __init__(self):
        self._intent_patterns = self._load_intent_patterns()

    def _load_intent_patterns(self) -> Dict[str, List[str]]:
        return {
            IntentType.PERSONALITY_ANALYSIS: [
                "性格", "个性", "为人", "脾气", "人品", "是什么样的人",
                "character", "personality", "性格分析"
            ],
            IntentType.CAREER_ANALYSIS: [
                "事业", "工作", "职业", "财运", "升职", "创业", "前途",
                "career", "job", "事业运势"
            ],
            IntentType.LOVE_ANALYSIS: [
                "感情", "婚姻", "恋爱", "桃花", "配偶", "姻缘", "婚恋",
                "love", "marriage", "感情运势"
            ],
            IntentType.WEALTH_ANALYSIS: [
                "财富", "金钱", "财运", "投资", "理财", "收入", "赚钱",
                "wealth", "money", "财富运势"
            ],
            IntentType.HEALTH_ANALYSIS: [
                "健康", "身体", "疾病", "养生", "体质",
                "health", "身体状况"
            ],
            IntentType.FATE_TREND: [
                "命运", "走势", "趋势", "运势", "大运", "流年",
                "fate", "fortune", "命运走势"
            ],
            IntentType.LUCKY_PERIOD: [
                "吉年", "好运", "旺运", "高峰期", "好运年",
                "lucky period", "好运时期"
            ],
            IntentType.LUCKY_DIRECTION: [
                "方位", "方向", "吉方", "朝向", "风水方位",
                "direction", "方位选择"
            ],
            IntentType.LUCKY_TIMING: [
                "时机", "吉时", "时间", "择日", "何时",
                "timing", "时间选择"
            ],
            IntentType.COMPATIBILITY: [
                "合盘", "配对", "合婚", "匹配", "相配",
                "compatibility", "配对分析"
            ],
            IntentType.COMPREHENSIVE: [
                "全面", "综合", "整体", "整体分析", "全面分析",
                "comprehensive", "full analysis", "综合分析"
            ]
        }

    def classify(self, query: str) -> IntentType:
        query_lower = query.lower()

        scores: Dict[IntentType, int] = {}
        for intent, patterns in self._intent_patterns.items():
            score = sum(1 for pattern in patterns if pattern in query_lower)
            if score > 0:
                scores[intent] = score

        if not scores:
            return IntentType.UNKNOWN

        return max(scores, key=scores.get)

    def classify_with_confidence(self, query: str) -> tuple[IntentType, float]:
        intent = self.classify(query)
        query_lower = query.lower()

        total_matches = sum(
            sum(1 for pattern in patterns if pattern in query_lower)
            for patterns in self._intent_patterns.values()
        )

        if total_matches == 0:
            return IntentType.UNKNOWN, 0.0

        matches = sum(
            1 for pattern in self._intent_patterns.get(intent, []) if pattern in query_lower
        )

        confidence = min(matches / 2.0, 1.0) if matches > 0 else 0.0
        return intent, confidence


class TaskDecomposer:
    """任务分解器

    将用户意图分解为可执行的子任务。
    """

    def __init__(self):
        self._intent_to_subtasks = self._load_subtask_mapping()

    def _load_subtask_mapping(self) -> Dict[IntentType, List[Dict[str, Any]]]:
        return {
            IntentType.PERSONALITY_ANALYSIS: [
                {"intent": IntentType.PERSONALITY_ANALYSIS, "agent": "ZiweiAgent", "types": ["personality"]},
                {"intent": IntentType.PERSONALITY_ANALYSIS, "agent": "BaziAgent", "types": ["personality"]}
            ],
            IntentType.CAREER_ANALYSIS: [
                {"intent": IntentType.CAREER_ANALYSIS, "agent": "ZiweiAgent", "types": ["career"]},
                {"intent": IntentType.CAREER_ANALYSIS, "agent": "BaziAgent", "types": ["career"]}
            ],
            IntentType.LOVE_ANALYSIS: [
                {"intent": IntentType.LOVE_ANALYSIS, "agent": "ZiweiAgent", "types": ["love"]},
                {"intent": IntentType.LOVE_ANALYSIS, "agent": "BaziAgent", "types": ["relationship"]}
            ],
            IntentType.WEALTH_ANALYSIS: [
                {"intent": IntentType.WEALTH_ANALYSIS, "agent": "ZiweiAgent", "types": ["wealth"]},
                {"intent": IntentType.WEALTH_ANALYSIS, "agent": "BaziAgent", "types": ["wealth"]}
            ],
            IntentType.HEALTH_ANALYSIS: [
                {"intent": IntentType.HEALTH_ANALYSIS, "agent": "ZiweiAgent", "types": ["health"]},
                {"intent": IntentType.HEALTH_ANALYSIS, "agent": "BaziAgent", "types": ["health"]}
            ],
            IntentType.FATE_TREND: [
                {"intent": IntentType.FATE_TREND, "agent": "BaziAgent", "types": ["fate_trend"]},
                {"intent": IntentType.FATE_TREND, "agent": "ZiweiAgent", "types": ["fate_trend"]}
            ],
            IntentType.LUCKY_PERIOD: [
                {"intent": IntentType.LUCKY_PERIOD, "agent": "BaziAgent", "types": ["lucky_period"]},
                {"intent": IntentType.LUCKY_PERIOD, "agent": "ZiweiAgent", "types": ["lucky_period"]}
            ],
            IntentType.LUCKY_DIRECTION: [
                {"intent": IntentType.LUCKY_DIRECTION, "agent": "ZiweiAgent", "types": ["direction"]},
                {"intent": IntentType.LUCKY_DIRECTION, "agent": "QimenAgent", "types": ["direction"]}
            ],
            IntentType.LUCKY_TIMING: [
                {"intent": IntentType.LUCKY_TIMING, "agent": "QimenAgent", "types": ["timing"]},
                {"intent": IntentType.LUCKY_TIMING, "agent": "BaziAgent", "types": ["fate_trend"]}
            ],
            IntentType.COMPREHENSIVE: [
                {"intent": IntentType.PERSONALITY_ANALYSIS, "agent": "GeneralAgent", "types": ["general"]}
            ],
            IntentType.UNKNOWN: [
                {"intent": IntentType.PERSONALITY_ANALYSIS, "agent": "GeneralAgent", "types": ["general"]}
            ]
        }

    def decompose(self, intent: IntentType, chart_type: str) -> List[SubTask]:
        subtask_configs = self._intent_to_subtasks.get(intent, self._intent_to_subtasks[IntentType.UNKNOWN])

        subtasks = []
        for i, config in enumerate(subtask_configs):
            task_id = hashlib.md5(f"{intent.value}_{i}_{datetime.now().isoformat()}".encode()).hexdigest()[:8]

            subtask = SubTask(
                task_id=task_id,
                intent_type=config["intent"],
                agent_name=config["agent"],
                analysis_types=set(config["types"]),
                priority=1 if i == 0 else 2
            )
            subtasks.append(subtask)

        return subtasks


class AgentScheduler:
    """Agent调度器

    负责Agent的并行/串行调度执行。
    """

    def __init__(self):
        self._agent_registry: Dict[str, Any] = {}

    def register_agent(self, name: str, agent: Any) -> None:
        self._agent_registry[name] = agent

    def get_agent(self, name: str) -> Optional[Any]:
        return self._agent_registry.get(name)

    async def execute_single(self, subtask: SubTask, context: OrchestrationContext) -> TaskResult:
        agent = self.get_agent(subtask.agent_name)
        if not agent:
            return TaskResult(
                task_id=subtask.task_id,
                intent_type=subtask.intent_type,
                success=False,
                error=f"Agent {subtask.agent_name} not found"
            )

        try:
            from .base import TaskContext as BaseTaskContext, AnalysisType

            analysis_types = [AnalysisType(at) for at in subtask.analysis_types]

            base_context = BaseTaskContext(
                user_id=context.user_id,
                profile_id=context.profile_id,
                chart_id=context.chart_id,
                session_id=context.session_id,
                chart_data=context.chart_data,
                profile_data=context.profile_data,
                user_query=context.user_query,
                requested_types=set(analysis_types)
            )

            start_time = datetime.now()
            result = await agent.analyze(base_context)
            execution_time = (datetime.now() - start_time).total_seconds()

            return TaskResult(
                task_id=subtask.task_id,
                intent_type=subtask.intent_type,
                success=True,
                results=[result.to_dict()],
                execution_time=execution_time,
                metadata={
                    "agent": subtask.agent_name,
                    "analysis_types": list(subtask.analysis_types)
                }
            )
        except Exception as e:
            return TaskResult(
                task_id=subtask.task_id,
                intent_type=subtask.intent_type,
                success=False,
                error=str(e)
            )

    async def execute_parallel(
        self,
        subtasks: List[SubTask],
        context: OrchestrationContext
    ) -> List[TaskResult]:
        tasks = [self.execute_single(st, context) for st in subtasks]
        return await asyncio.gather(*tasks)

    async def execute_sequential(
        self,
        subtasks: List[SubTask],
        context: OrchestrationContext
    ) -> List[TaskResult]:
        results = []
        for subtask in subtasks:
            result = await self.execute_single(subtask, context)
            results.append(result)
            if not result.success:
                break
        return results


class ResultIntegrator:
    """结果整合器

    整合多个Agent的分析结果，生成统一输出。
    """

    def __init__(self):
        self._integration_strategies = self._load_strategies()

    def _load_strategies(self) -> Dict[str, Any]:
        return {
            "high_confidence_priority": True,
            "cross_validation": True,
            "consensus_threshold": 0.6
        }

    def integrate(
        self,
        results: List[TaskResult],
        intent: IntentType
    ) -> Dict[str, Any]:
        successful_results = [r for r in results if r.success]
        failed_results = [r for r in results if not r.success]

        if not successful_results:
            return {
                "success": False,
                "error": "All subtasks failed",
                "failed_tasks": [r.task_id for r in failed_results]
            }

        integrated = {
            "success": True,
            "intent": intent.value,
            "total_tasks": len(results),
            "successful_tasks": len(successful_results),
            "failed_tasks": [r.task_id for r in failed_results],
            "execution_time": sum(r.execution_time for r in results),
            "results": self._merge_results(successful_results),
            "summary": self._generate_summary(successful_results, intent),
            "recommendations": self._aggregate_recommendations(successful_results),
            "warnings": self._aggregate_warnings(successful_results),
            "confidence": self._calculate_overall_confidence(successful_results)
        }

        return integrated

    def _merge_results(self, results: List[TaskResult]) -> List[Dict[str, Any]]:
        merged = []
        for result in results:
            for res in result.results:
                merged.append({
                    "task_id": result.task_id,
                    "intent": result.intent_type.value,
                    "content": res,
                    "execution_time": result.execution_time
                })
        return merged

    def _generate_summary(self, results: List[TaskResult], intent: IntentType) -> str:
        summaries = []
        for result in results:
            for res in result.results:
                summary = res.get("summary", "")
                if summary:
                    summaries.append(summary)

        if summaries:
            return f"综合分析：{' '.join(summaries[:2])}"
        return f"{intent.value}分析完成"

    def _aggregate_recommendations(self, results: List[TaskResult]) -> List[str]:
        recommendations = []
        seen = set()

        for result in results:
            for res in result.results:
                for rec in res.get("recommendations", []):
                    if rec not in seen:
                        recommendations.append(rec)
                        seen.add(rec)

        return recommendations[:5]

    def _aggregate_warnings(self, results: List[TaskResult]) -> List[str]:
        warnings = []
        seen = set()

        for result in results:
            for res in result.results:
                for warning in res.get("warnings", []):
                    if warning not in seen:
                        warnings.append(warning)
                        seen.add(warning)

        return warnings[:3]

    def _calculate_overall_confidence(self, results: List[TaskResult]) -> float:
        confidences = []
        for result in results:
            for res in result.results:
                confidence = res.get("confidence", 0.8)
                confidences.append(confidence)

        return sum(confidences) / len(confidences) if confidences else 0.5


class Orchestrator:
    """任务编排器

    协调意图识别、任务分解、Agent调度和结果整合的完整流程。
    """

    def __init__(self):
        self.logger = logging.getLogger("mingli.orchestrator")
        self.intent_classifier = IntentClassifier()
        self.task_decomposer = TaskDecomposer()
        self.agent_scheduler = AgentScheduler()
        self.result_integrator = ResultIntegrator()
        self._initialized = False

    def initialize(self) -> bool:
        try:
            from .ziwei_agent import ZiweiAgent
            from .bazi_agent import BaziAgent
            from .qimen_agent import QimenAgent
            from .general_agent import GeneralAgent

            self.agent_scheduler.register_agent("ZiweiAgent", ZiweiAgent())
            self.agent_scheduler.register_agent("BaziAgent", BaziAgent())
            self.agent_scheduler.register_agent("QimenAgent", QimenAgent())

            general_agent = GeneralAgent()
            general_agent.register_sub_agent(self.agent_scheduler.get_agent("BaziAgent"))
            general_agent.register_sub_agent(self.agent_scheduler.get_agent("ZiweiAgent"))
            general_agent.register_sub_agent(self.agent_scheduler.get_agent("QimenAgent"))
            self.agent_scheduler.register_agent("GeneralAgent", general_agent)

            self._initialized = True
            self.logger.info("Orchestrator initialized successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize orchestrator: {e}")
            return False

    async def process(
        self,
        user_id: int,
        profile_id: int,
        chart_id: int,
        session_id: str,
        chart_data: Dict[str, Any],
        profile_data: Dict[str, Any],
        user_query: str,
        parallel: bool = True
    ) -> Dict[str, Any]:
        if not self._initialized:
            return {"success": False, "error": "Orchestrator not initialized"}

        intent, confidence = self.intent_classifier.classify_with_confidence(user_query)

        chart_type = chart_data.get("chart_type", "bazi")
        subtasks = self.task_decomposer.decompose(intent, chart_type)

        context = OrchestrationContext(
            user_id=user_id,
            session_id=session_id,
            profile_id=profile_id,
            chart_id=chart_id,
            chart_data=chart_data,
            profile_data=profile_data,
            user_query=user_query,
            intent=intent,
            subtasks=subtasks
        )

        if parallel:
            results = await self.agent_scheduler.execute_parallel(subtasks, context)
        else:
            results = await self.agent_scheduler.execute_sequential(subtasks, context)

        integrated = self.result_integrator.integrate(results, intent)

        integrated["intent_analysis"] = {
            "detected_intent": intent.value,
            "confidence": confidence
        }
        integrated["subtasks"] = [
            {
                "task_id": st.task_id,
                "agent": st.agent_name,
                "intent": st.intent_type.value
            }
            for st in subtasks
        ]

        return integrated

    def get_supported_intents(self) -> List[str]:
        return [intent.value for intent in IntentType]

    def get_agent_info(self) -> Dict[str, Any]:
        return {
            "initialized": self._initialized,
            "registered_agents": list(self.agent_scheduler._agent_registry.keys())
        }
