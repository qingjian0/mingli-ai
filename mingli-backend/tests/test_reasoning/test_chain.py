"""
推理链构建和序列化测试
"""

import pytest
import json
from datetime import datetime
from app.reasoning.chain import (
    ReasoningChain, ReasoningStep, ReasoningContext,
    StepStatus, AlternativePath
)


class TestReasoningStep:
    """推理步骤测试"""

    def test_step_creation(self):
        """测试步骤创建"""
        step = ReasoningStep(
            description="测试步骤",
            rule_id="rule_001",
            inputs={"key": "value"},
            outputs={"result": "success"},
            confidence=0.95
        )
        assert step.description == "测试步骤"
        assert step.rule_id == "rule_001"
        assert step.confidence == 0.95
        assert step.status == StepStatus.PENDING

    def test_step_status_transition(self):
        """测试步骤状态转换"""
        step = ReasoningStep(description="测试步骤")
        assert step.status == StepStatus.PENDING

        step.status = StepStatus.ACTIVE
        assert step.status == StepStatus.ACTIVE

        step.status = StepStatus.SUCCESS
        assert step.status == StepStatus.SUCCESS

    def test_step_serialization(self):
        """测试步骤序列化"""
        step = ReasoningStep(
            description="测试序列化",
            confidence=0.9,
            sources=["source1", "source2"]
        )
        step_dict = step.model_dump()
        assert isinstance(step_dict, dict)
        assert step_dict["description"] == "测试序列化"
        assert step_dict["confidence"] == 0.9

    def test_step_deserialization(self):
        """测试步骤反序列化"""
        data = {
            "step_id": "test-id-123",
            "description": "测试反序列化",
            "inputs": {"a": 1},
            "outputs": {"b": 2},
            "confidence": 0.85,
            "sources": [],
            "status": "success",
            "rule_id": None,
            "error_message": None,
            "metadata": {},
            "created_at": datetime.now().isoformat()
        }
        step = ReasoningStep(**data)
        assert step.step_id == "test-id-123"
        assert step.confidence == 0.85


class TestReasoningChain:
    """推理链测试"""

    @pytest.fixture
    def chain(self):
        return ReasoningChain()

    def test_chain_creation(self, chain):
        """测试推理链创建"""
        assert chain.chain_id is not None
        assert len(chain.steps) == 0
        assert chain.final_confidence == 0.0
        assert chain.conclusion == ""

    def test_add_step(self, chain):
        """测试添加步骤"""
        step = ReasoningStep(description="第一步")
        chain.add_step(step)
        assert len(chain.steps) == 1
        assert chain.steps[0].description == "第一步"

    def test_add_multiple_steps(self, chain):
        """测试添加多个步骤"""
        for i in range(5):
            step = ReasoningStep(description=f"步骤{i}")
            chain.add_step(step)
        assert len(chain.steps) == 5

    def test_get_step(self, chain):
        """测试获取步骤"""
        step1 = ReasoningStep(description="步骤1")
        step2 = ReasoningStep(description="步骤2")
        chain.add_step(step1)
        chain.add_step(step2)

        retrieved = chain.get_step(step1.step_id)
        assert retrieved is not None
        assert retrieved.description == "步骤1"

    def test_get_step_not_found(self, chain):
        """测试获取不存在的步骤"""
        result = chain.get_step("non-existent-id")
        assert result is None

    def test_get_successful_steps(self, chain):
        """测试获取成功的步骤"""
        step1 = ReasoningStep(description="成功步骤")
        step2 = ReasoningStep(description="失败步骤")
        step3 = ReasoningStep(description="另一个成功步骤")

        step1.status = StepStatus.SUCCESS
        step2.status = StepStatus.FAILED
        step3.status = StepStatus.SUCCESS

        chain.add_step(step1)
        chain.add_step(step2)
        chain.add_step(step3)

        successful = chain.get_successful_steps()
        assert len(successful) == 2

    def test_calculate_final_confidence(self, chain):
        """测试计算最终置信度"""
        step1 = ReasoningStep(description="步骤1", confidence=0.8)
        step2 = ReasoningStep(description="步骤2", confidence=0.9)
        step1.status = StepStatus.SUCCESS
        step2.status = StepStatus.SUCCESS

        chain.add_step(step1)
        chain.add_step(step2)

        confidence = chain.calculate_final_confidence()
        assert abs(confidence - 0.85) < 0.01

    def test_calculate_final_confidence_no_steps(self, chain):
        """测试无步骤时置信度"""
        confidence = chain.calculate_final_confidence()
        assert confidence == 0.0

    def test_calculate_final_confidence_no_successful(self, chain):
        """测试无成功步骤时置信度"""
        step1 = ReasoningStep(description="失败步骤")
        step1.status = StepStatus.FAILED
        chain.add_step(step1)

        confidence = chain.calculate_final_confidence()
        assert confidence == 0.0

    def test_update_conclusion(self, chain):
        """测试更新结论"""
        chain.update_conclusion("测试结论", 0.95)
        assert chain.conclusion == "测试结论"
        assert chain.final_confidence == 0.95

    def test_update_conclusion_auto_confidence(self, chain):
        """测试自动计算置信度"""
        step = ReasoningStep(description="步骤", confidence=0.8)
        step.status = StepStatus.SUCCESS
        chain.add_step(step)

        chain.update_conclusion("自动置信度结论")
        assert chain.conclusion == "自动置信度结论"
        assert chain.final_confidence == 0.8

    def test_to_summary(self, chain):
        """测试生成摘要"""
        step1 = ReasoningStep(description="步骤1")
        step2 = ReasoningStep(description="步骤2")
        step1.status = StepStatus.SUCCESS
        step2.status = StepStatus.SUCCESS
        chain.add_step(step1)
        chain.add_step(step2)
        chain.update_conclusion("测试摘要结论", 0.9)

        summary = chain.to_summary()
        assert summary["step_count"] == 2
        assert summary["successful_steps"] == 2
        assert summary["final_confidence"] == 0.9
        assert summary["conclusion"] == "测试摘要结论"


class TestAlternativePath:
    """备选推理路径测试"""

    def test_path_creation(self):
        """测试路径创建"""
        path = AlternativePath(
            path_type="branch",
            description="备选路径",
            confidence=0.75,
            reason="主路径不可行"
        )
        assert path.path_type == "branch"
        assert path.confidence == 0.75
        assert path.discarded is False

    def test_path_discard(self):
        """测试路径丢弃"""
        path = AlternativePath(
            path_type="rollback",
            description="回退路径",
            reason="需要回退"
        )
        path.discarded = True
        assert path.discarded is True


class TestReasoningContext:
    """推理上下文测试"""

    @pytest.fixture
    def context(self):
        return ReasoningContext()

    def test_context_creation(self, context):
        """测试上下文创建"""
        assert context.session_id is not None
        assert context.user_query == ""
        assert context.system_type == ""
        assert len(context.intermediate_results) == 0

    def test_set_and_get_variable(self, context):
        """测试变量存取"""
        context.set_variable("key1", "value1")
        context.set_variable("key2", {"nested": "data"})

        assert context.get_variable("key1") == "value1"
        assert context.get_variable("key2") == {"nested": "data"}

    def test_get_variable_default(self, context):
        """测试获取不存在的变量"""
        result = context.get_variable("nonexistent", "default_value")
        assert result == "default_value"

    def test_merge_chart_data(self, context):
        """测试合并命盘数据"""
        context.chart_data = {"existing": "data"}
        context.merge_chart_data({"new": "data", "existing": "updated"})

        assert context.chart_data["existing"] == "updated"
        assert context.chart_data["new"] == "data"


class TestChainSerialization:
    """推理链序列化测试"""

    @pytest.fixture
    def full_chain(self):
        chain = ReasoningChain(context={"test": "context"})
        step1 = ReasoningStep(
            description="步骤1",
            confidence=0.9,
            sources=["source1"]
        )
        step1.status = StepStatus.SUCCESS
        step1.outputs = {"result": "value1"}

        step2 = ReasoningStep(description="步骤2", confidence=0.85)
        step2.status = StepStatus.SUCCESS
        step2.outputs = {"result": "value2"}

        chain.add_step(step1)
        chain.add_step(step2)
        chain.update_conclusion("最终结论", 0.875)

        return chain

    def test_json_serialization(self, full_chain):
        """测试JSON序列化"""
        json_str = full_chain.model_dump_json()
        assert isinstance(json_str, str)
        assert "最终结论" in json_str

    def test_json_deserialization(self, full_chain):
        """测试JSON反序列化"""
        json_str = full_chain.model_dump_json()
        restored = ReasoningChain.model_validate_json(json_str)

        assert len(restored.steps) == 2
        assert restored.conclusion == "最终结论"
        assert restored.final_confidence == 0.875

    def test_dict_serialization(self, full_chain):
        """测试字典序列化"""
        data = full_chain.model_dump()
        assert isinstance(data, dict)
        assert "chain_id" in data
        assert "steps" in data
        assert "conclusion" in data

    def test_roundtrip_serialization(self, full_chain):
        """测试往返序列化"""
        data = full_chain.model_dump()
        restored_chain = ReasoningChain(**data)

        assert restored_chain.chain_id == full_chain.chain_id
        assert len(restored_chain.steps) == len(full_chain.steps)
        assert restored_chain.conclusion == full_chain.conclusion


class TestChainIntegration:
    """推理链集成测试"""

    def test_complete_reasoning_process(self):
        """测试完整的推理过程"""
        chain = ReasoningChain(user_query="分析我的命运")

        step1 = ReasoningStep(
            description="识别命盘类型",
            rule_id="rule_identify_chart",
            confidence=0.95
        )
        step1.inputs = {"birth_info": "provided"}
        step1.outputs = {"chart_type": "bazi"}
        step1.status = StepStatus.SUCCESS

        step2 = ReasoningStep(
            description="分析日主强弱",
            rule_id="rule_strength",
            confidence=0.88
        )
        step2.inputs = {"four_pillars": "extracted"}
        step2.outputs = {"strength": "中等"}
        step2.status = StepStatus.SUCCESS

        step3 = ReasoningStep(
            description="选取用神",
            rule_id="rule_usable_god",
            confidence=0.82
        )
        step3.inputs = {"strength_result": "analyzed"}
        step3.outputs = {"usable_god": "木"}
        step3.status = StepStatus.SUCCESS

        chain.add_step(step1)
        chain.add_step(step2)
        chain.add_step(step3)

        summary = chain.to_summary()
        assert summary["step_count"] == 3
        assert summary["successful_steps"] == 3
        assert chain.calculate_final_confidence() > 0.8

        chain.update_conclusion(
            "日主中等，用神为木，适合东方发展",
            confidence=chain.calculate_final_confidence()
        )
        assert "木" in chain.conclusion
