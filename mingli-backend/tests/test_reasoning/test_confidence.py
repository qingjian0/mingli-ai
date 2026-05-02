"""
置信度计算测试
"""

import pytest
from app.reasoning.chain import ReasoningChain, ReasoningStep, StepStatus


class TestConfidenceCalculation:
    """置信度计算测试"""

    def test_average_confidence(self):
        """测试平均置信度"""
        chain = ReasoningChain()

        for i, conf in enumerate([0.9, 0.8, 0.85, 0.95]):
            step = ReasoningStep(description=f"步骤{i}", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain.add_step(step)

        avg_confidence = chain.calculate_final_confidence()
        expected = (0.9 + 0.8 + 0.85 + 0.95) / 4
        assert abs(avg_confidence - expected) < 0.01

    def test_weighted_confidence(self):
        """测试加权置信度"""
        steps = []
        for i, (conf, weight) in enumerate([(0.9, 3), (0.6, 1)]):
            step = ReasoningStep(description=f"步骤{i}", confidence=conf)
            step.status = StepStatus.SUCCESS
            step.metadata["weight"] = weight
            steps.append(step)

        total_weight = sum(s.metadata["weight"] for s in steps)
        weighted_sum = sum(
            s.confidence * s.metadata["weight"] for s in steps
        )
        weighted_confidence = weighted_sum / total_weight

        assert abs(weighted_confidence - 0.825) < 0.01

    def test_confidence_with_failed_steps(self):
        """测试包含失败步骤的置信度"""
        chain = ReasoningChain()

        step1 = ReasoningStep(description="成功步骤", confidence=0.9)
        step1.status = StepStatus.SUCCESS

        step2 = ReasoningStep(description="失败步骤", confidence=0.5)
        step2.status = StepStatus.FAILED

        step3 = ReasoningStep(description="另一个成功", confidence=0.85)
        step3.status = StepStatus.SUCCESS

        chain.add_step(step1)
        chain.add_step(step2)
        chain.add_step(step3)

        avg_confidence = chain.calculate_final_confidence()
        expected = (0.9 + 0.85) / 2
        assert abs(avg_confidence - expected) < 0.01

    def test_confidence_edge_case_zero(self):
        """测试零置信度边界情况"""
        chain = ReasoningChain()

        step = ReasoningStep(description="零置信度步骤", confidence=0.0)
        step.status = StepStatus.SUCCESS
        chain.add_step(step)

        assert chain.calculate_final_confidence() == 0.0

    def test_confidence_edge_case_one(self):
        """测试完美置信度边界情况"""
        chain = ReasoningChain()

        step = ReasoningStep(description="完美置信度步骤", confidence=1.0)
        step.status = StepStatus.SUCCESS
        chain.add_step(step)

        assert chain.calculate_final_confidence() == 1.0

    def test_confidence_empty_chain(self):
        """测试空推理链"""
        chain = ReasoningChain()
        assert chain.calculate_final_confidence() == 0.0


class TestConfidencePropagation:
    """置信度传播测试"""

    def test_step_confidence_propagation(self):
        """测试步骤置信度传播"""
        chain = ReasoningChain()

        step1 = ReasoningStep(
            description="步骤1",
            confidence=0.9,
            sources=["source_a"]
        )
        step1.status = StepStatus.SUCCESS
        chain.add_step(step1)

        step2 = ReasoningStep(
            description="步骤2",
            confidence=0.85
        )
        step2.status = StepStatus.SUCCESS
        chain.add_step(step2)

        step3 = ReasoningStep(
            description="步骤3",
            confidence=0.8
        )
        step3.status = StepStatus.SUCCESS
        chain.add_step(step3)

        final_confidence = chain.calculate_final_confidence()
        assert 0.8 <= final_confidence <= 0.9

    def test_low_confidence_step_impact(self):
        """测试低置信度步骤的影响"""
        chain1 = ReasoningChain()
        for conf in [0.9, 0.9, 0.9]:
            step = ReasoningStep(description="步骤", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain1.add_step(step)
        avg1 = chain1.calculate_final_confidence()

        chain2 = ReasoningChain()
        for conf in [0.9, 0.3, 0.9]:
            step = ReasoningStep(description="步骤", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain2.add_step(step)
        avg2 = chain2.calculate_final_confidence()

        assert avg2 < avg1


class TestConfidenceThreshold:
    """置信度阈值测试"""

    def test_confidence_below_threshold(self):
        """测试低于阈值的置信度"""
        threshold = 0.7
        chain = ReasoningChain()

        for conf in [0.6, 0.65, 0.7]:
            step = ReasoningStep(description="步骤", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain.add_step(step)

        avg_confidence = chain.calculate_final_confidence()
        assert avg_confidence < threshold

    def test_confidence_above_threshold(self):
        """测试高于阈值的置信度"""
        threshold = 0.8
        chain = ReasoningChain()

        for conf in [0.85, 0.9, 0.8]:
            step = ReasoningStep(description="步骤", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain.add_step(step)

        avg_confidence = chain.calculate_final_confidence()
        assert avg_confidence >= threshold

    def test_confidence_marginal(self):
        """测试临界置信度"""
        threshold = 0.8
        chain = ReasoningChain()

        for conf in [0.8, 0.8, 0.8]:
            step = ReasoningStep(description="步骤", confidence=conf)
            step.status = StepStatus.SUCCESS
            chain.add_step(step)

        avg_confidence = chain.calculate_final_confidence()
        assert abs(avg_confidence - threshold) < 0.01


class TestSourceBasedConfidence:
    """基于源的置信度测试"""

    def test_single_source_confidence(self):
        """测试单一来源置信度"""
        step = ReasoningStep(
            description="单源步骤",
            confidence=0.8,
            sources=["source_a"]
        )
        step.status = StepStatus.SUCCESS

        source_factor = len(step.sources) / 3
        adjusted_confidence = step.confidence * (0.7 + 0.3 * min(source_factor, 1.0))

        assert 0.7 <= adjusted_confidence <= 0.9

    def test_multiple_sources_confidence(self):
        """测试多来源置信度"""
        step = ReasoningStep(
            description="多源步骤",
            confidence=0.8,
            sources=["source_a", "source_b", "source_c"]
        )
        step.status = StepStatus.SUCCESS

        source_factor = len(step.sources) / 3
        adjusted_confidence = step.confidence * (0.7 + 0.3 * min(source_factor, 1.0))

        assert adjusted_confidence > 0.8


class TestRuleBasedConfidence:
    """基于规则的置信度测试"""

    def test_known_rule_confidence(self):
        """测试已知规则的置信度"""
        step = ReasoningStep(
            description="经典规则步骤",
            rule_id="classical_rule_001",
            confidence=0.95
        )
        step.status = StepStatus.SUCCESS
        step.metadata["rule_type"] = "classical"

        assert step.confidence >= 0.9

    def test_derived_rule_confidence(self):
        """测试推导规则的置信度"""
        step = ReasoningStep(
            description="推导规则步骤",
            rule_id="derived_rule_001",
            confidence=0.75
        )
        step.status = StepStatus.SUCCESS
        step.metadata["rule_type"] = "derived"

        assert 0.6 <= step.confidence < 0.9

    def test_heuristic_confidence(self):
        """测试启发式规则置信度"""
        step = ReasoningStep(
            description="启发式步骤",
            confidence=0.55
        )
        step.status = StepStatus.SUCCESS
        step.metadata["rule_type"] = "heuristic"

        assert step.confidence < 0.7


class TestConfidenceAggregation:
    """置信度聚合测试"""

    def test_multi_method_aggregation(self):
        """测试多方法聚合"""
        chain = ReasoningChain()

        step1 = ReasoningStep(description="八字分析", confidence=0.85)
        step1.status = StepStatus.SUCCESS
        step1.metadata["method"] = "bazi"

        step2 = ReasoningStep(description="紫微分析", confidence=0.82)
        step2.status = StepStatus.SUCCESS
        step2.metadata["method"] = "ziwei"

        step3 = ReasoningStep(description="奇门分析", confidence=0.78)
        step3.status = StepStatus.SUCCESS
        step3.metadata["method"] = "qimen"

        chain.add_step(step1)
        chain.add_step(step2)
        chain.add_step(step3)

        avg_confidence = chain.calculate_final_confidence()
        assert 0.7 <= avg_confidence <= 0.9

    def test_cross_validation_confidence(self):
        """测试交叉验证置信度"""
        chain = ReasoningChain()

        step1 = ReasoningStep(description="方法A结果", confidence=0.8)
        step1.status = StepStatus.SUCCESS
        step2 = ReasoningStep(description="方法B结果", confidence=0.85)
        step2.status = StepStatus.SUCCESS
        step3 = ReasoningStep(description="方法C结果", confidence=0.75)
        step3.status = StepStatus.SUCCESS

        chain.add_step(step1)
        chain.add_step(step2)
        chain.add_step(step3)

        base_confidence = chain.calculate_final_confidence()
        consensus_bonus = 0.05
        final_confidence = min(base_confidence + consensus_bonus, 1.0)

        assert final_confidence > base_confidence
        assert final_confidence <= 1.0
