"""
奇门遁甲Agent模块

提供奇门遁甲专项分析的Agent实现。
分析维度包括：时局分析、方位选择、吉凶判断等。
"""

from typing import Any, Dict, List, Optional
from datetime import datetime
from .base import (
    BaseAgent,
    AnalysisResult,
    AnalysisType,
    TaskContext,
    ReasoningStep,
)


class QimenAgent(BaseAgent):
    """奇门遁甲分析Agent

    专注于奇门遁甲时局分析，提供方位选择、吉凶判断等服务。
    """

    def __init__(self):
        super().__init__(
            name="QimenAgent",
            system_type="qimen",
            version="1.0.0"
        )
        self._eight_doors = self._load_eight_doors()
        self._nine_stars = self._load_nine_stars()
        self._eight_trigrams = self._load_eight_trigrams()

    def _load_eight_doors(self) -> Dict[str, Dict[str, Any]]:
        return {
            "开门": {"nature": "吉门", "keywords": ["事业", "开店", "出差"], "auspicious": True},
            "休门": {"nature": "吉门", "keywords": ["休养", "水行业"], "auspicious": True},
            "生门": {"nature": "吉门", "keywords": ["生财", "产业", "买卖"], "auspicious": True},
            "伤门": {"nature": "凶门", "keywords": ["伤灾", "竞争", "狩猎"], "auspicious": False},
            "杜门": {"nature": "平门", "keywords": ["保密", "技术", "阻塞"], "auspicious": True},
            "景门": {"nature": "平门", "keywords": ["文化", "表达", "虚惊"], "auspicious": True},
            "死门": {"nature": "凶门", "keywords": ["丧事", "不动", "不动"], "auspicious": False},
            "惊门": {"nature": "凶门", "keywords": ["惊恐", "口舌", "诉讼"], "auspicious": False}
        }

    def _load_nine_stars(self) -> Dict[str, Dict[str, Any]]:
        return {
            "天蓬星": {"nature": "凶星", "keywords": ["破财", "盗贼", "大浪"], "element": "水"},
            "天任星": {"nature": "吉星", "keywords": ["求财", "农作", "稳重"], "element": "土"},
            "天冲星": {"nature": "凶星", "keywords": ["行动", "冲撞", "武事"], "element": "木"},
            "天辅星": {"nature": "吉星", "keywords": ["学业", "文化", "助人"], "element": "木"},
            "天禽星": {"nature": "吉星", "keywords": ["求财", "领导", "中正"], "element": "土"},
            "天心星": {"nature": "吉星", "keywords": ["医疗", "策划", "善良"], "element": "金"},
            "天柱星": {"nature": "凶星", "keywords": ["破财", "讼争", "修造"], "element": "金"},
            "天任星": {"nature": "吉星", "keywords": ["求财", "农作", "稳重"], "element": "土"},
            "天英星": {"nature": "凶星", "keywords": ["血光", "性燥", "虚花"], "element": "火"},
            "天芮星": {"nature": "凶星", "keywords": ["学业", "结交", "疾病"], "element": "土"}
        }

    def _load_eight_trigrams(self) -> Dict[str, Dict[str, Any]]:
        return {
            "乾": {"nature": "刚健", "direction": "西北", "element": "金"},
            "坎": {"nature": "陷险", "direction": "北", "element": "水"},
            "艮": {"nature": "静止", "direction": "东北", "element": "土"},
            "震": {"nature": "震动", "direction": "东", "element": "木"},
            "巽": {"nature": "入随", "direction": "东南", "element": "木"},
            "离": {"nature": "分离", "direction": "南", "element": "火"},
            "坤": {"nature": "柔顺", "direction": "西南", "element": "土"},
            "兑": {"nature": "喜悦", "direction": "西", "element": "金"}
        }

    def get_capabilities(self) -> List[str]:
        return [
            "timing_analysis",
            "direction_selection",
            "auspicious_analysis",
            "business_consultation",
            "travel_planning",
            "career_advice"
        ]

    def get_supported_types(self) -> List[AnalysisType]:
        return [
            AnalysisType.TIMING,
            AnalysisType.DIRECTION,
            AnalysisType.CAREER,
            AnalysisType.GENERAL
        ]

    async def analyze(self, context: TaskContext) -> AnalysisResult:
        valid, error = self.validate_input(context)
        if not valid:
            raise ValueError(f"输入验证失败: {error}")

        chart_data = context.chart_data
        reasoning_chain: List[ReasoningStep] = []

        step1 = self._create_reasoning_step(
            description="提取奇门遁甲局盘信息",
            rule_id="qimen_core_extract",
            inputs={"chart_data": chart_data},
            outputs={"gong_data": self._extract_gongs(chart_data)}
        )
        reasoning_chain.append(step1)

        step2 = self._create_reasoning_step(
            description="分析九宫格局与星门配合",
            rule_id="qimen_pattern_analysis",
            inputs={"宫位": self._extract_gongs(chart_data)},
            outputs={"pattern_quality": self._analyze_pattern_quality(chart_data)}
        )
        reasoning_chain.append(step2)

        analysis_type = self._determine_primary_analysis(context.requested_types)
        content = await self._generate_analysis_content(chart_data, analysis_type, context)

        result = AnalysisResult(
            analysis_id=self._generate_analysis_id(context, analysis_type),
            analysis_type=analysis_type,
            agent_name=self.name,
            content=content,
            summary=content.get("summary", ""),
            confidence=0.82,
            confidence_level=self._calculate_confidence_level(0.82),
            reasoning_chain=reasoning_chain,
            recommendations=content.get("recommendations", []),
            warnings=content.get("warnings", []),
            metadata={
                "system": "奇门遁甲",
                "version": self.version,
                "chart_id": context.chart_id,
                "pattern": self._analyze_pattern_quality(chart_data)
            }
        )

        return result

    def _extract_gongs(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return chart_data.get("data", {}).get("gongs", {
            str(i): {"door": "休门", "star": "天任星", "trigram": "乾"} for i in range(1, 10)
        })

    def _analyze_pattern_quality(self, chart_data: Dict[str, Any]) -> str:
        gongs = self._extract_gongs(chart_data)
        sheng_men_count = 0
        xiong_count = 0

        for gong in gongs.values():
            door = gong.get("door", "")
            if door in ["开门", "休门", "生门"]:
                sheng_men_count += 1
            if door in ["死门", "惊门", "伤门"]:
                xiong_count += 1

        if sheng_men_count >= 4:
            return "上吉"
        elif sheng_men_count >= 2:
            return "吉"
        elif xiong_count >= 4:
            return "凶"
        elif xiong_count >= 2:
            return "平"
        return "中平"

    def _determine_primary_analysis(self, requested_types: set) -> AnalysisType:
        if AnalysisType.TIMING in requested_types:
            return AnalysisType.TIMING
        if AnalysisType.DIRECTION in requested_types:
            return AnalysisType.DIRECTION
        return AnalysisType.TIMING

    async def _generate_analysis_content(
        self,
        chart_data: Dict[str, Any],
        analysis_type: AnalysisType,
        context: TaskContext
    ) -> Dict[str, Any]:
        if analysis_type == AnalysisType.TIMING:
            return await self._analyze_timing(chart_data)
        elif analysis_type == AnalysisType.DIRECTION:
            return await self._analyze_direction(chart_data)
        elif analysis_type == AnalysisType.CAREER:
            return await self._analyze_career_direction(chart_data)
        else:
            return await self._analyze_general(chart_data)

    async def _analyze_timing(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        pattern = self._analyze_pattern_quality(chart_data)
        favorable_times = self._get_favorable_times(chart_data)
        unfavorable_times = self._get_unfavorable_times(chart_data)

        return {
            "summary": f"当前格局{pattern}，宜择时行动",
            "pattern_quality": pattern,
            "favorable_periods": favorable_times,
            "unfavorable_periods": unfavorable_times,
            "best_timing": self._get_best_timing(chart_data),
            "recommendations": [
                "吉时宜进取，凶时宜守静",
                "重要决策避开凶时凶方"
            ],
            "warnings": ["凶时不可妄动"]
        }

    async def _analyze_direction(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        favorable_directions = self._get_favorable_directions(chart_data)
        unfavorable_directions = self._get_unfavorable_directions(chart_data)

        return {
            "summary": "方位选择分析",
            "best_directions": favorable_directions,
            "avoid_directions": unfavorable_directions,
            "daily_direction": favorable_directions[0] if favorable_directions else None,
            "recommendations": [
                "吉方宜坐卧，凶方忌面向",
                "出行办事选吉方出发"
            ],
            "warnings": ["忌面朝凶方久坐"]
        }

    async def _analyze_career_direction(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "事业方位分析",
            "best_work_direction": self._get_favorable_directions(chart_data)[0] if self._get_favorable_directions(chart_data) else "东",
            "office_arrangement": self._get_office_arrangement(chart_data),
            "recommendations": [
                "办公桌宜面向吉方",
                "重要会议选吉时进行"
            ],
            "warnings": []
        }

    async def _analyze_general(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "奇门遁甲综合分析",
            "pattern": self._analyze_pattern_quality(chart_data),
            "overview": "时局分析已完成",
            "recommendations": [
                "建议针对具体事项进行定向分析"
            ],
            "warnings": []
        }

    def _get_favorable_times(self, chart_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            {"time": "子时", "quality": "吉", "suitable": "静心养性"},
            {"time": "丑时", "quality": "吉", "suitable": "积蓄准备"},
            {"time": "寅时", "quality": "吉", "suitable": "贵人相助"}
        ]

    def _get_unfavorable_times(self, chart_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            {"time": "午时", "quality": "凶", "avoid": "重大决策"},
            {"time": "未时", "quality": "凶", "avoid": "投资理财"}
        ]

    def _get_best_timing(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "period": "卯时至午时",
            "reason": "吉门得位，事半功倍"
        }

    def _get_favorable_directions(self, chart_data: Dict[str, Any]) -> List[str]:
        return ["东", "东南", "北"]

    def _get_unfavorable_directions(self, chart_data: Dict[str, Any]) -> List[str]:
        return ["西", "西南", "东北"]

    def _get_office_arrangement(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "desk_direction": "坐北朝南",
            "avoid_direction": "忌朝西",
            "tips": "背后有靠山，面向吉方"
        }
