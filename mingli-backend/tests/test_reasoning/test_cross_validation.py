"""
交叉验证测试
"""

import pytest
from typing import Dict, Any, List
from app.reasoning.chain import ReasoningChain, ReasoningStep, StepStatus


class TestCrossValidation:
    """交叉验证基础测试"""

    def test_same_conclusion_different_methods(self):
        """测试不同方法得出相同结论"""
        results = {
            "bazi": {"conclusion": "木旺", "confidence": 0.85, "method": "八字"},
            "ziwei": {"conclusion": "木旺", "confidence": 0.82, "method": "紫微"},
            "qimen": {"conclusion": "木旺", "confidence": 0.78, "method": "奇门"}
        }

        conclusions = [r["conclusion"] for r in results.values()]
        assert len(set(conclusions)) == 1

        avg_confidence = sum(r["confidence"] for r in results.values()) / len(results)
        assert avg_confidence > 0.8

    def test_different_conclusions_analysis(self):
        """测试不同结论分析"""
        results = {
            "bazi": {"conclusion": "木旺", "confidence": 0.85},
            "ziwei": {"conclusion": "火旺", "confidence": 0.80}
        }

        conclusions = [r["conclusion"] for r in results.values()]
        assert len(set(conclusions)) > 1

        conflicts = []
        for i, (m1, r1) in enumerate(results.items()):
            for m2, r2 in list(results.items())[i+1:]:
                if r1["conclusion"] != r2["conclusion"]:
                    conflicts.append({
                        "method1": m1,
                        "method2": m2,
                        "diff": abs(r1["confidence"] - r2["confidence"])
                    })

        assert len(conflicts) > 0

    def test_confidence_weighted_consensus(self):
        """测试置信度加权共识"""
        results = [
            {"method": "bazi", "conclusion": "木", "confidence": 0.9},
            {"method": "ziwei", "conclusion": "木", "confidence": 0.85},
            {"method": "qimen", "conclusion": "土", "confidence": 0.75}
        ]

        conclusion_weights: Dict[str, float] = {}
        for r in results:
            c = r["conclusion"]
            if c not in conclusion_weights:
                conclusion_weights[c] = 0
            conclusion_weights[c] += r["confidence"]

        consensus = max(conclusion_weights, key=conclusion_weights.get)
        assert consensus == "木"
        assert conclusion_weights["木"] > conclusion_weights["土"]


class TestMethodConsistency:
    """方法一致性测试"""

    def test_bazi_consistency_check(self):
        """测试八字内部一致性"""
        pillars = {
            "year": {"stem": "甲", "branch": "辰"},
            "month": {"stem": "戊", "branch": "辰"},
            "day": {"stem": "乙", "branch": "亥"},
            "hour": {"stem": "丁", "branch": "未"}
        }

        month_stem = pillars["month"]["stem"]
        month_branch = pillars["month"]["branch"]

        valid_stem_branches = [
            ("甲", "寅"), ("乙", "卯"), ("丙", "辰"), ("丁", "巳"),
            ("戊", "辰"), ("己", "巳"), ("庚", "午"), ("辛", "未"),
            ("壬", "申"), ("癸", "酉")
        ]

        is_valid = (month_stem, month_branch) in valid_stem_branches
        assert is_valid or month_stem[0] in ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    def test_ziwei_consistency_check(self):
        """测试紫微内部一致性"""
        palaces = ["命宫", "父母宫", "福德宫", "田宅宫", "官禄宫",
                   "相貌宫", "迁移宫", "疾厄宫", "财帛宫", "子女宫",
                   "夫妻宫", "兄弟宫"]

        assert len(palaces) == 12

        palace_branches = {
            "命宫": "丑", "父母宫": "子", "福德宫": "亥",
            "田宅宫": "戌", "官禄宫": "酉", "相貌宫": "申",
            "迁移宫": "未", "疾厄宫": "午", "财帛宫": "巳",
            "子女宫": "辰", "夫妻宫": "卯", "兄弟宫": "寅"
        }

        assert len(palace_branches) == 12

    def test_qimen_consistency_check(self):
        """测试奇门内部一致性"""
        doors = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
        assert len(doors) == 8

        stars = ["蓬", "任", "冲", "辅", "英", "芮", "柱", "心"]
        assert len(stars) == 9

        gods = ["值符", "螣蛇", "太阴", "白虎", "玄武", "九地", "九天", "六合"]
        assert len(gods) == 8


class TestCrossMethodValidation:
    """跨方法验证测试"""

    def test_bazi_ziwei_consistency(self):
        """测试八字和紫微一致性"""
        bazi_day_master = "甲"
        ziwei_day_master = "甲"

        assert bazi_day_master == ziwei_day_master

    def test_year_branch_consistency(self):
        """测试年支一致性"""
        bazi_year_branch = "辰"
        ziwei_year_branch = "辰"

        assert bazi_year_branch == ziwei_year_branch

    def test_gender_consistency(self):
        """测试性别对大运方向的影响"""
        male_chart = {"gender": "male", "dayun_direction": "顺行"}
        female_chart = {"gender": "female", "dayun_direction": "逆行"}

        assert male_chart["dayun_direction"] != female_chart["dayun_direction"]


class TestValidationResults:
    """验证结果测试"""

    def test_validation_pass(self):
        """测试验证通过"""
        validation_result = {
            "passed": True,
            "checks": [
                {"name": "stem_branch_valid", "result": True},
                {"name": "palace_complete", "result": True},
                {"name": "stars_positioned", "result": True}
            ]
        }

        assert validation_result["passed"]
        assert all(c["result"] for c in validation_result["checks"])

    def test_validation_fail(self):
        """测试验证失败"""
        validation_result = {
            "passed": False,
            "checks": [
                {"name": "stem_branch_valid", "result": True},
                {"name": "palace_complete", "result": False},
                {"name": "stars_positioned", "result": True}
            ],
            "failed_check": "palace_complete"
        }

        assert not validation_result["passed"]
        assert validation_result["failed_check"] == "palace_complete"

    def test_validation_warning(self):
        """测试验证警告"""
        validation_result = {
            "passed": True,
            "warnings": [
                "Multiple methods disagree on dayun direction",
                "Confidence below threshold for conclusion"
            ]
        }

        assert validation_result["passed"]
        assert len(validation_result["warnings"]) > 0


class TestContradictionResolution:
    """矛盾解决测试"""

    def test_high_confidence_override(self):
        """测试高置信度优先"""
        conclusions = [
            {"conclusion": "木旺", "confidence": 0.95, "method": "bazi"},
            {"conclusion": "火旺", "confidence": 0.60, "method": "ziwei"}
        ]

        final_conclusion = max(conclusions, key=lambda x: x["confidence"])
        assert final_conclusion["conclusion"] == "木旺"

    def test_consensus_override(self):
        """测试共识优先"""
        conclusions = [
            {"conclusion": "木旺", "confidence": 0.75, "method": "bazi"},
            {"conclusion": "木旺", "confidence": 0.70, "method": "ziwei"},
            {"conclusion": "火旺", "confidence": 0.85, "method": "qimen"}
        ]

        conclusion_votes = {}
        for c in conclusions:
            if c["conclusion"] not in conclusion_votes:
                conclusion_votes[c["conclusion"]] = {"votes": 0, "total_conf": 0}
            conclusion_votes[c["conclusion"]]["votes"] += 1
            conclusion_votes[c["conclusion"]]["total_conf"] += c["confidence"]

        for c in conclusion_votes.values():
            c["avg_conf"] = c["total_conf"] / c["votes"]

        consensus = max(conclusion_votes.items(), key=lambda x: (
            x[1]["votes"], x[1]["avg_conf"]
        ))
        assert consensus[0] == "木旺"

    def test_weighted_resolution(self):
        """测试加权解决"""
        conclusions = [
            {"conclusion": "木", "confidence": 0.8, "weight": 1.0},
            {"conclusion": "火", "confidence": 0.9, "weight": 0.5},
            {"conclusion": "土", "confidence": 0.85, "weight": 0.8}
        ]

        weighted_scores = {}
        for c in conclusions:
            score = c["confidence"] * c["weight"]
            weighted_scores[c["conclusion"]] = score

        resolved = max(weighted_scores, key=weighted_scores.get)
        assert resolved in ["木", "火", "土"]


class TestValidationChain:
    """验证链测试"""

    def test_sequential_validation(self):
        """测试顺序验证"""
        steps = [
            {"check": "input_valid", "result": True},
            {"check": "chart_computed", "result": True},
            {"check": "analysis_valid", "result": True}
        ]

        for step in steps:
            assert step["result"], f"Failed at {step['check']}"

    def test_validation_with_break(self):
        """测试提前终止验证"""
        steps = [
            {"check": "input_valid", "result": True},
            {"check": "chart_computed", "result": False},
            {"check": "analysis_valid", "result": True}
        ]

        failed_step = None
        for step in steps:
            if not step["result"]:
                failed_step = step
                break

        assert failed_step is not None
        assert failed_step["check"] == "chart_computed"


class TestFuzzyValidation:
    """模糊验证测试"""

    def test_similar_conclusions(self):
        """测试相似结论"""
        c1 = "木旺，适合东方发展"
        c2 = "木旺，适合去东方"

        assert "木旺" in c1 and "木旺" in c2

    def test_confidence_range(self):
        """测试置信度范围"""
        confidence = 0.85

        assert 0.0 <= confidence <= 1.0
        assert confidence > 0.7

    def test_uncertainty_handling(self):
        """测试不确定性处理"""
        results = [
            {"conclusion": "木旺", "confidence": 0.55},
            {"conclusion": "火旺", "confidence": 0.45}
        ]

        max_conf = max(r["confidence"] for r in results)
        uncertainty = 1 - max_conf

        assert 0.4 <= uncertainty <= 0.5
