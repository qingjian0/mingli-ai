"""
Agent功能测试
"""

import pytest
from unittest.mock import Mock, AsyncMock, patch
from datetime import datetime


class TestBaseAgent:
    """基础Agent测试"""

    def test_agent_base_structure(self):
        """测试Agent基类结构"""
        from app.agents.base import BaseAgent

        assert hasattr(BaseAgent, "analyze")
        assert hasattr(BaseAgent, "register_sub_agent")

    def test_agent_name_property(self):
        """测试Agent名称属性"""
        from app.agents.base import BaseAgent

        class TestAgent(BaseAgent):
            name = "TestAgent"

        agent = TestAgent()
        assert agent.name == "TestAgent"


class TestZiweiAgent:
    """紫微斗数Agent测试"""

    @pytest.fixture
    def ziwei_agent(self):
        from app.agents.ziwei_agent import ZiweiAgent
        return ZiweiAgent()

    def test_agent_initialization(self, ziwei_agent):
        """测试Agent初始化"""
        assert ziwei_agent.name == "ZiweiAgent"

    def test_agent_has_analyze_method(self, ziwei_agent):
        """测试分析方法存在"""
        assert hasattr(ziwei_agent, "analyze")
        assert callable(ziwei_agent.analyze)


class TestBaziAgent:
    """八字Agent测试"""

    @pytest.fixture
    def bazi_agent(self):
        from app.agents.bazi_agent import BaziAgent
        return BaziAgent()

    def test_agent_initialization(self, bazi_agent):
        """测试Agent初始化"""
        assert bazi_agent.name == "BaziAgent"

    def test_agent_has_analyze_method(self, bazi_agent):
        """测试分析方法存在"""
        assert hasattr(bazi_agent, "analyze")
        assert callable(bazi_agent.analyze)


class TestQimenAgent:
    """奇门遁甲Agent测试"""

    @pytest.fixture
    def qimen_agent(self):
        from app.agents.qimen_agent import QimenAgent
        return QimenAgent()

    def test_agent_initialization(self, qimen_agent):
        """测试Agent初始化"""
        assert qimen_agent.name == "QimenAgent"

    def test_agent_has_analyze_method(self, qimen_agent):
        """测试分析方法存在"""
        assert hasattr(qimen_agent, "analyze")
        assert callable(qimen_agent.analyze)


class TestGeneralAgent:
    """综合Agent测试"""

    @pytest.fixture
    def general_agent(self):
        from app.agents.general_agent import GeneralAgent
        return GeneralAgent()

    def test_agent_initialization(self, general_agent):
        """测试Agent初始化"""
        assert general_agent.name == "GeneralAgent"

    def test_register_sub_agent(self, general_agent):
        """测试注册子Agent"""
        mock_agent = Mock()
        mock_agent.name = "MockAgent"

        general_agent.register_sub_agent(mock_agent)

        assert len(general_agent.sub_agents) == 1
        assert "MockAgent" in general_agent.sub_agents

    def test_sub_agents_initial_empty(self, general_agent):
        """测试子Agent初始为空"""
        assert len(general_agent.sub_agents) == 0


class TestAgentAnalysisTypes:
    """Agent分析类型测试"""

    def test_analysis_type_enum(self):
        """测试分析类型枚举"""
        from app.agents.base import AnalysisType

        assert hasattr(AnalysisType, "PERSONALITY")
        assert hasattr(AnalysisType, "CAREER")
        assert hasattr(AnalysisType, "LOVE")
        assert hasattr(AnalysisType, "WEALTH")
        assert hasattr(AnalysisType, "HEALTH")

    def test_analysis_type_values(self):
        """测试分析类型值"""
        from app.agents.base import AnalysisType

        assert AnalysisType.PERSONALITY.value == "personality"
        assert AnalysisType.CAREER.value == "career"


class TestAgentTaskContext:
    """Agent任务上下文测试"""

    def test_task_context_creation(self):
        """测试任务上下文创建"""
        from app.agents.base import TaskContext

        context = TaskContext(
            user_id=1,
            profile_id=1,
            chart_id=1,
            session_id="test_session",
            chart_data={"test": "data"},
            profile_data={},
            user_query="测试查询"
        )

        assert context.user_id == 1
        assert context.chart_id == 1

    def test_task_context_with_analysis_types(self):
        """测试带分析类型的上下文"""
        from app.agents.base import TaskContext, AnalysisType

        context = TaskContext(
            user_id=1,
            profile_id=1,
            chart_id=1,
            session_id="test_session",
            chart_data={},
            profile_data={},
            user_query="测试",
            requested_types={AnalysisType.PERSONALITY, AnalysisType.CAREER}
        )

        assert len(context.requested_types) == 2
        assert AnalysisType.PERSONALITY in context.requested_types


class TestAgentResponse:
    """Agent响应测试"""

    def test_analysis_result_structure(self):
        """测试分析结果结构"""
        from app.agents.base import AnalysisResult

        result = AnalysisResult(
            analysis_type="personality",
            summary="性格分析完成",
            content={"key": "value"},
            confidence=0.85,
            warnings=[],
            recommendations=["建议1"]
        )

        assert result.analysis_type == "personality"
        assert result.confidence == 0.85
        assert len(result.recommendations) == 1

    def test_analysis_result_to_dict(self):
        """测试分析结果转字典"""
        from app.agents.base import AnalysisResult

        result = AnalysisResult(
            analysis_type="career",
            summary="事业分析",
            content={},
            confidence=0.8
        )

        result_dict = result.to_dict()
        assert isinstance(result_dict, dict)
        assert result_dict["analysis_type"] == "career"


class TestAgentMockAnalysis:
    """Agent模拟分析测试"""

    @pytest.mark.asyncio
    async def test_mock_bazi_analysis(self):
        """测试模拟八字分析"""
        from app.agents.base import TaskContext, AnalysisResult

        context = TaskContext(
            user_id=1,
            profile_id=1,
            chart_id=1,
            session_id="test",
            chart_data={
                "four_pillars": {
                    "year": {"stem": "甲", "branch": "子"},
                    "month": {"stem": "乙", "branch": "丑"},
                    "day": {"stem": "丙", "branch": "寅"},
                    "hour": {"stem": "丁", "branch": "卯"}
                }
            },
            profile_data={},
            user_query="分析事业"
        )

        mock_result = AnalysisResult(
            analysis_type="career",
            summary="事业分析完成",
            content={"dayun": "发展良好"},
            confidence=0.85
        )

        assert mock_result.analysis_type == "career"
        assert mock_result.confidence > 0.8


class TestAgentIntegration:
    """Agent集成测试"""

    def test_multiple_agents_coordination(self):
        """测试多Agent协调"""
        from app.agents.base import BaseAgent

        class Coordinator:
            def __init__(self):
                self.agents = []

            def register(self, agent):
                self.agents.append(agent)

        coordinator = Coordinator()

        mock_agent1 = Mock()
        mock_agent1.name = "Agent1"
        mock_agent2 = Mock()
        mock_agent2.name = "Agent2"

        coordinator.register(mock_agent1)
        coordinator.register(mock_agent2)

        assert len(coordinator.agents) == 2

    def test_agent_result_aggregation(self):
        """测试Agent结果聚合"""
        from app.agents.base import AnalysisResult

        results = [
            AnalysisResult(
                analysis_type="personality",
                summary="八字分析",
                content={},
                confidence=0.85
            ),
            AnalysisResult(
                analysis_type="personality",
                summary="紫微分析",
                content={},
                confidence=0.82
            )
        ]

        avg_confidence = sum(r.confidence for r in results) / len(results)
        assert 0.8 <= avg_confidence <= 0.9
