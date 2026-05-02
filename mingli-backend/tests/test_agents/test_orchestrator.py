"""
编排器单元测试
"""

import pytest
from app.agents.orchestrator import (
    Orchestrator, IntentClassifier, TaskDecomposer, AgentScheduler,
    ResultIntegrator, IntentType, TaskType, SubTask, OrchestrationContext
)


class TestIntentClassifier:
    """意图分类器测试"""

    @pytest.fixture
    def classifier(self):
        return IntentClassifier()

    def test_classify_personality(self, classifier):
        """测试性格分析意图"""
        query = "分析我的性格特点"
        intent = classifier.classify(query)
        assert intent == IntentType.PERSONALITY_ANALYSIS

    def test_classify_career(self, classifier):
        """测试事业分析意图"""
        query = "我的事业发展如何"
        intent = classifier.classify(query)
        assert intent == IntentType.CAREER_ANALYSIS

    def test_classify_love(self, classifier):
        """测试感情分析意图"""
        query = "我的姻缘什么时候来"
        intent = classifier.classify(query)
        assert intent == IntentType.LOVE_ANALYSIS

    def test_classify_wealth(self, classifier):
        """测试财富分析意图"""
        query = "我最近的财运怎么样"
        intent = classifier.classify(query)
        assert intent == IntentType.WEALTH_ANALYSIS

    def test_classify_health(self, classifier):
        """测试健康分析意图"""
        query = "我的健康需要注意什么"
        intent = classifier.classify(query)
        assert intent == IntentType.HEALTH_ANALYSIS

    def test_classify_fate_trend(self, classifier):
        """测试命运走势意图"""
        query = "我未来十年的命运走势"
        intent = classifier.classify(query)
        assert intent == IntentType.FATE_TREND

    def test_classify_unknown(self, classifier):
        """测试未知意图"""
        query = "今天天气真好"
        intent = classifier.classify(query)
        assert intent == IntentType.UNKNOWN

    def test_classify_with_confidence(self, classifier):
        """测试带置信度的分类"""
        query = "我的性格和事业分析"
        intent, confidence = classifier.classify_with_confidence(query)
        assert intent in IntentType
        assert 0.0 <= confidence <= 1.0

    def test_classify_multiple_intents(self, classifier):
        """测试多意图识别"""
        query = "分析我的性格和财运"
        intent, confidence = classifier.classify_with_confidence(query)
        assert intent in [IntentType.PERSONALITY_ANALYSIS, IntentType.WEALTH_ANALYSIS]


class TestTaskDecomposer:
    """任务分解器测试"""

    @pytest.fixture
    def decomposer(self):
        return TaskDecomposer()

    def test_decompose_personality(self, decomposer):
        """测试性格分析任务分解"""
        subtasks = decomposer.decompose(IntentType.PERSONALITY_ANALYSIS, "bazi")
        assert len(subtasks) > 0
        for task in subtasks:
            assert task.intent_type == IntentType.PERSONALITY_ANALYSIS
            assert task.agent_name in ["BaziAgent", "ZiweiAgent", "GeneralAgent"]

    def test_decompose_career(self, decomposer):
        """测试事业分析任务分解"""
        subtasks = decomposer.decompose(IntentType.CAREER_ANALYSIS, "bazi")
        assert len(subtasks) > 0

    def test_decompose_love(self, decomposer):
        """测试感情分析任务分解"""
        subtasks = decomposer.decompose(IntentType.LOVE_ANALYSIS, "ziwei")
        assert len(subtasks) > 0

    def test_decompose_unknown(self, decomposer):
        """测试未知意图分解"""
        subtasks = decomposer.decompose(IntentType.UNKNOWN, "bazi")
        assert len(subtasks) > 0
        assert all(t.agent_name == "GeneralAgent" for t in subtasks)

    def test_subtask_priorities(self, decomposer):
        """测试子任务优先级"""
        subtasks = decomposer.decompose(IntentType.CAREER_ANALYSIS, "bazi")
        if len(subtasks) > 1:
            assert subtasks[0].priority <= subtasks[1].priority


class TestAgentScheduler:
    """Agent调度器测试"""

    @pytest.fixture
    def scheduler(self):
        return AgentScheduler()

    def test_register_agent(self, scheduler):
        """测试Agent注册"""
        class MockAgent:
            pass

        scheduler.register_agent("MockAgent", MockAgent())
        agent = scheduler.get_agent("MockAgent")
        assert agent is not None

    def test_get_nonexistent_agent(self, scheduler):
        """测试获取不存在的Agent"""
        agent = scheduler.get_agent("NonExistentAgent")
        assert agent is None


class TestResultIntegrator:
    """结果整合器测试"""

    @pytest.fixture
    def integrator(self):
        return ResultIntegrator()

    def test_integrate_single_result(self, integrator):
        """测试单结果整合"""
        from app.agents.orchestrator import TaskResult

        results = [
            TaskResult(
                task_id="task1",
                intent_type=IntentType.PERSONALITY_ANALYSIS,
                success=True,
                results=[{"summary": "性格分析完成", "confidence": 0.85}]
            )
        ]

        integrated = integrator.integrate(results, IntentType.PERSONALITY_ANALYSIS)
        assert integrated["success"] is True
        assert integrated["successful_tasks"] == 1

    def test_integrate_multiple_results(self, integrator):
        """测试多结果整合"""
        from app.agents.orchestrator import TaskResult

        results = [
            TaskResult(
                task_id="task1",
                intent_type=IntentType.PERSONALITY_ANALYSIS,
                success=True,
                results=[{"summary": "八字分析"}],
                execution_time=0.5
            ),
            TaskResult(
                task_id="task2",
                intent_type=IntentType.PERSONALITY_ANALYSIS,
                success=True,
                results=[{"summary": "紫微分析"}],
                execution_time=0.6
            )
        ]

        integrated = integrator.integrate(results, IntentType.PERSONALITY_ANALYSIS)
        assert integrated["successful_tasks"] == 2
        assert len(integrated["results"]) == 2

    def test_integrate_all_failed(self, integrator):
        """测试全部失败"""
        from app.agents.orchestrator import TaskResult

        results = [
            TaskResult(
                task_id="task1",
                intent_type=IntentType.CAREER_ANALYSIS,
                success=False,
                error="Agent not found"
            )
        ]

        integrated = integrator.integrate(results, IntentType.CAREER_ANALYSIS)
        assert integrated["success"] is False
        assert len(integrated["failed_tasks"]) == 1

    def test_calculate_overall_confidence(self, integrator):
        """测试总体置信度计算"""
        from app.agents.orchestrator import TaskResult

        results = [
            TaskResult(
                task_id="task1",
                intent_type=IntentType.PERSONALITY_ANALYSIS,
                success=True,
                results=[{"confidence": 0.85}]
            ),
            TaskResult(
                task_id="task2",
                intent_type=IntentType.PERSONALITY_ANALYSIS,
                success=True,
                results=[{"confidence": 0.90}]
            )
        ]

        integrated = integrator.integrate(results, IntentType.PERSONALITY_ANALYSIS)
        assert 0.8 <= integrated["confidence"] <= 0.95


class TestOrchestrator:
    """编排器测试"""

    @pytest.fixture
    def orchestrator(self):
        return Orchestrator()

    def test_orchestrator_initialization(self, orchestrator):
        """测试编排器初始化"""
        assert orchestrator.logger is not None
        assert orchestrator.intent_classifier is not None
        assert orchestrator.task_decomposer is not None
        assert orchestrator.agent_scheduler is not None
        assert orchestrator.result_integrator is not None

    def test_get_supported_intents(self, orchestrator):
        """测试获取支持的意图"""
        intents = orchestrator.get_supported_intents()
        assert len(intents) > 0
        assert "personality_analysis" in intents
        assert "career_analysis" in intents

    def test_get_agent_info(self, orchestrator):
        """测试获取Agent信息"""
        info = orchestrator.get_agent_info()
        assert "initialized" in info
        assert "registered_agents" in info

    def test_process_without_initialization(self, orchestrator):
        """测试未初始化时的处理"""
        result = orchestrator.process(
            user_id=1,
            profile_id=1,
            chart_id=1,
            session_id="test_session",
            chart_data={"chart_type": "bazi"},
            profile_data={},
            user_query="分析我的性格"
        )
        assert result["success"] is False
        assert "not initialized" in result["error"]


class TestOrchestrationContext:
    """编排上下文测试"""

    def test_context_creation(self):
        """测试上下文创建"""
        context = OrchestrationContext(
            user_id=1,
            session_id="session123",
            profile_id=1,
            chart_id=1,
            chart_data={"test": "data"},
            profile_data={"name": "测试用户"},
            user_query="测试查询"
        )

        assert context.user_id == 1
        assert context.session_id == "session123"
        assert context.intent == IntentType.UNKNOWN
        assert len(context.subtasks) == 0
        assert len(context.results) == 0

    def test_context_with_intent(self):
        """测试带意图的上下文"""
        context = OrchestrationContext(
            user_id=1,
            session_id="session123",
            profile_id=1,
            chart_id=1,
            chart_data={},
            profile_data={},
            user_query="分析性格",
            intent=IntentType.PERSONALITY_ANALYSIS
        )

        assert context.intent == IntentType.PERSONALITY_ANALYSIS


class TestSubTask:
    """子任务测试"""

    def test_subtask_creation(self):
        """测试子任务创建"""
        task = SubTask(
            task_id="task001",
            intent_type=IntentType.CAREER_ANALYSIS,
            agent_name="BaziAgent",
            analysis_types={"career"}
        )

        assert task.task_id == "task001"
        assert task.intent_type == IntentType.CAREER_ANALYSIS
        assert "career" in task.analysis_types

    def test_subtask_with_dependencies(self):
        """测试带依赖的子任务"""
        task = SubTask(
            task_id="task002",
            intent_type=IntentType.CAREER_ANALYSIS,
            agent_name="BaziAgent",
            analysis_types={"career"},
            dependencies=["task001"]
        )

        assert "task001" in task.dependencies
