"""
八字Agent模块

提供八字命理专项分析的Agent实现。
分析维度包括：用神、大运、流年吉凶等。
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


class BaziAgent(BaseAgent):
    """八字分析Agent

    专注于八字命盘的分析，提供用神、大运、流年等分析服务。
    """

    def __init__(self):
        super().__init__(
            name="BaziAgent",
            system_type="bazi",
            version="1.0.0"
        )
        self._stem_meanings = self._load_stem_meanings()
        self._branch_meanings = self._load_branch_meanings()
        self._element_strength = self._load_element_strength()

    def _load_stem_meanings(self) -> Dict[str, Dict[str, Any]]:
        return {
            "甲": {"element": "木", "nature": "阳木", "keywords": ["仁慈", "正直", "上进"]},
            "乙": {"element": "木", "nature": "阴木", "keywords": ["柔韧", "婉转", "敏感"]},
            "丙": {"element": "火", "nature": "阳火", "keywords": ["热情", "开朗", "冲动"]},
            "丁": {"element": "火", "nature": "阴火", "keywords": ["细腻", "内敛", "执着"]},
            "戊": {"element": "土", "nature": "阳土", "keywords": ["稳重", "诚信", "固执"]},
            "己": {"element": "土", "nature": "阴土", "keywords": ["包容", "务实", "多疑"]},
            "庚": {"element": "金", "nature": "阳金", "keywords": ["刚毅", "果断", "冷酷"]},
            "辛": {"element": "金", "nature": "阴金", "keywords": ["细腻", "敏感", "清高"]},
            "壬": {"element": "水", "nature": "阳水", "keywords": ["聪明", "灵活", "放任"]},
            "癸": {"element": "水", "nature": "阴水", "keywords": ["柔和", "内秀", "城府"]}
        }

    def _load_branch_meanings(self) -> Dict[str, Dict[str, Any]]:
        return {
            "子": {"animal": "鼠", "element": "水", "keywords": ["智慧", "机敏", "桃花"]},
            "丑": {"animal": "牛", "element": "土", "keywords": ["勤劳", "固执", "积蓄"]},
            "寅": {"animal": "虎", "element": "木", "keywords": ["勇敢", "自信", "冲动"]},
            "卯": {"animal": "兔", "element": "木", "keywords": ["温和", "善良", "敏感"]},
            "辰": {"animal": "龙", "element": "土", "keywords": ["包容", "变动", "包容"]},
            "巳": {"animal": "蛇", "element": "火", "keywords": ["智慧", "神秘", "灵活"]},
            "午": {"animal": "马", "element": "火", "keywords": ["热情", "奔放", "急躁"]},
            "未": {"animal": "羊", "element": "土", "keywords": ["温和", "忍耐", "依赖"]},
            "申": {"animal": "猴", "element": "金", "keywords": ["机灵", "善变", "交际"]},
            "酉": {"animal": "鸡", "element": "金", "keywords": ["精细", "认真", "挑剔"]},
            "戌": {"animal": "狗", "element": "土", "keywords": ["忠诚", "正直", "保守"]},
            "亥": {"animal": "猪", "element": "水", "keywords": ["善良", "宽容", "懒散"]}
        }

    def _load_element_strength(self) -> Dict[str, float]:
        return {
            "木": 0.0, "火": 0.0, "土": 0.0, "金": 0.0, "水": 0.0
        }

    def get_capabilities(self) -> List[str]:
        return [
            "yongshen_analysis",
            "dayun_analysis",
            "liunian_analysis",
            "personality_analysis",
            "career_analysis",
            "wealth_analysis",
            "health_analysis",
            "compatibility_analysis"
        ]

    def get_supported_types(self) -> List[AnalysisType]:
        return [
            AnalysisType.PERSONALITY,
            AnalysisType.CAREER,
            AnalysisType.WEALTH,
            AnalysisType.HEALTH,
            AnalysisType.FATE_TREND,
            AnalysisType.LUCKY_PERIOD,
            AnalysisType.COMPATIBILITY
        ]

    async def analyze(self, context: TaskContext) -> AnalysisResult:
        valid, error = self.validate_input(context)
        if not valid:
            raise ValueError(f"输入验证失败: {error}")

        chart_data = context.chart_data
        reasoning_chain: List[ReasoningStep] = []

        step1 = self._create_reasoning_step(
            description="提取八字四柱天干地支信息",
            rule_id="bazi_core_extract",
            inputs={"chart_data": chart_data},
            outputs={"four_pillars": self._extract_four_pillars(chart_data)}
        )
        reasoning_chain.append(step1)

        step2 = self._create_reasoning_step(
            description="分析五行生克关系确定用神",
            rule_id="bazi_wuxing_analysis",
            inputs={"四柱信息": self._extract_four_pillars(chart_data)},
            outputs={"wuxing_balance": self._analyze_wuxing_balance(chart_data)}
        )
        reasoning_chain.append(step2)

        step3 = self._create_reasoning_step(
            description="判断日主强弱定用神喜忌",
            rule_id="bazi_yongshen",
            inputs={"五行平衡": self._analyze_wuxing_balance(chart_data)},
            outputs={"yongshen": self._determine_yongshen(chart_data)}
        )
        reasoning_chain.append(step3)

        analysis_type = self._determine_primary_analysis(context.requested_types)
        content = await self._generate_analysis_content(chart_data, analysis_type, context)

        result = AnalysisResult(
            analysis_id=self._generate_analysis_id(context, analysis_type),
            analysis_type=analysis_type,
            agent_name=self.name,
            content=content,
            summary=content.get("summary", ""),
            confidence=0.88,
            confidence_level=self._calculate_confidence_level(0.88),
            reasoning_chain=reasoning_chain,
            recommendations=content.get("recommendations", []),
            warnings=content.get("warnings", []),
            metadata={
                "system": "子平八字",
                "version": self.version,
                "chart_id": context.chart_id,
                "yongshen": self._determine_yongshen(chart_data)
            }
        )

        return result

    def _extract_four_pillars(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return chart_data.get("data", {}).get("four_pillars", {
            "year": {"stem": "甲", "branch": "子"},
            "month": {"stem": "乙", "branch": "丑"},
            "day": {"stem": "丙", "branch": "寅"},
            "hour": {"stem": "丁", "branch": "卯"}
        })

    def _extract_day_master(self, chart_data: Dict[str, Any]) -> str:
        pillars = self._extract_four_pillars(chart_data)
        return pillars.get("day", {}).get("stem", "甲")

    def _analyze_wuxing_balance(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        pillars = self._extract_four_pillars(chart_data)
        element_counts = {"木": 0, "火": 0, "土": 0, "金": 0, "水": 0}

        for position in ["year", "month", "day", "hour"]:
            pillar = pillars.get(position, {})
            stem = pillar.get("stem", "")
            branch = pillar.get("branch", "")

            if stem in self._stem_meanings:
                element = self._stem_meanings[stem]["element"]
                element_counts[element] += 1
            if branch in self._branch_meanings:
                element = self._branch_meanings[branch]["element"]
                element_counts[element] += 1

        total = sum(element_counts.values()) or 1
        percentages = {k: round(v / total * 100, 1) for k, v in element_counts.items()}

        return {
            "counts": element_counts,
            "percentages": percentages,
            "strongest": max(element_counts, key=element_counts.get),
            "weakest": min(element_counts, key=element_counts.get)
        }

    def _determine_yongshen(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        balance = self._analyze_wuxing_balance(chart_data)
        day_master = self._extract_day_master(chart_data)
        day_element = self._stem_meanings.get(day_master, {}).get("element", "木")

        strongest = balance["strongest"]
        weakest = balance["weakest"]

        if day_element == strongest:
            yongshen = self._get_counter_element(weakest)
            avoid = strongest
        else:
            yongshen = self._get_counter_element(strongest)
            avoid = weakest

        return {
            "day_master": day_master,
            "day_element": day_element,
            "yongshen": yongshen,
            "avoid": avoid,
            "yongshen_nature": self._get_element_nature(yongshen)
        }

    def _get_counter_element(self, element: str) -> str:
        counter_map = {"木": "金", "金": "木", "水": "火", "火": "水", "土": "木"}
        return counter_map.get(element, "土")

    def _get_element_nature(self, element: str) -> str:
        natures = {
            "木": "生发条达",
            "火": "炎上炽烈",
            "土": "厚德载物",
            "金": "肃杀收敛",
            "水": "流动变化"
        }
        return natures.get(element, "")

    def _determine_primary_analysis(self, requested_types: set) -> AnalysisType:
        if AnalysisType.FATE_TREND in requested_types:
            return AnalysisType.FATE_TREND
        if AnalysisType.LUCKY_PERIOD in requested_types:
            return AnalysisType.LUCKY_PERIOD
        if AnalysisType.PERSONALITY in requested_types:
            return AnalysisType.PERSONALITY
        return AnalysisType.FATE_TREND

    async def _generate_analysis_content(
        self,
        chart_data: Dict[str, Any],
        analysis_type: AnalysisType,
        context: TaskContext
    ) -> Dict[str, Any]:
        yongshen = self._determine_yongshen(chart_data)

        if analysis_type == AnalysisType.FATE_TREND:
            return await self._analyze_fate_trend(chart_data, yongshen)
        elif analysis_type == AnalysisType.LUCKY_PERIOD:
            return await self._analyze_lucky_period(chart_data, yongshen)
        elif analysis_type == AnalysisType.PERSONALITY:
            return await self._analyze_personality(chart_data)
        elif analysis_type == AnalysisType.CAREER:
            return await self._analyze_career(chart_data, yongshen)
        elif analysis_type == AnalysisType.WEALTH:
            return await self._analyze_wealth(chart_data, yongshen)
        elif analysis_type == AnalysisType.HEALTH:
            return await self._analyze_health(chart_data, yongshen)
        else:
            return await self._analyze_general(chart_data, yongshen)

    async def _analyze_fate_trend(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": f"命主用神为{yongshen['yongshen']}，喜{self._get_element_nature(yongshen['yongshen'])}之物",
            "yongshen_analysis": yongshen,
            "life_phases": [
                {"age_range": "0-20岁", "description": "根基培养期", "favorable": True},
                {"age_range": "20-40岁", "description": "事业发展期", "favorable": True},
                {"age_range": "40-60岁", "description": "收获稳定期", "favorable": True}
            ],
            "recommendations": [
                f"多接触{yongshen['yongshen']}属性的事物",
                "注意把握人生关键转折期"
            ],
            "warnings": [f"规避{yongshen['avoid']}属性过强的环境"]
        }

    async def _analyze_lucky_period(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "大运流年分析",
            "current_dayun": {
                "age_range": "30-35岁",
                "element": yongshen['yongshen'],
                "quality": "中等"
            },
            "upcoming_liunian": [
                {"year": "2024", "quality": "平运"},
                {"year": "2025", "quality": "好运"},
                {"year": "2026", "quality": "旺运"}
            ],
            "recommendations": [
                "把握好运势积极行动",
                "逆运时宜静不宜动"
            ],
            "warnings": ["流年冲克时需谨慎决策"]
        }

    async def _analyze_personality(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        pillars = self._extract_four_pillars(chart_data)
        day_stem = pillars.get("day", {}).get("stem", "甲")
        day_info = self._stem_meanings.get(day_stem, {})

        return {
            "summary": f"日主{day_info.get('nature', '')}，{day_info.get('keywords', [])[0] if day_info.get('keywords') else ''}",
            "day_master": day_stem,
            "day_nature": day_info,
            "personality_traits": day_info.get("keywords", []),
            "recommendations": ["发挥日主优势"],
            "warnings": ["注意性格短板"]
        }

    async def _analyze_career(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "事业运势分析",
            "suitable_fields": self._infer_career_fields(yongshen),
            "career_advice": "宜稳定发展，忌盲目变动",
            "recommendations": [
                "选择与用神相合的行业",
                "注意事业合作伙伴的选择"
            ],
            "warnings": []
        }

    async def _analyze_wealth(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "财富运势分析",
            "wealth_type": "正财稳健型",
            "money_tips": [f"多用{yongshen['yongshen']}属性的理财方式"],
            "recommendations": [
                "注重储蓄积累",
                "避免高风险投资"
            ],
            "warnings": ["注意破财年份"]
        }

    async def _analyze_health(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "健康状况分析",
            "weak_organs": [yongshen["avoid"]],
            "health_advice": "注意调理",
            "recommendations": [],
            "warnings": ["关注相关脏腑健康"]
        }

    async def _analyze_general(self, chart_data: Dict[str, Any], yongshen: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "综合命理分析",
            "yongshen": yongshen,
            "recommendations": ["建议针对性分析具体方面"],
            "warnings": []
        }

    def _infer_career_fields(self, yongshen: Dict[str, Any]) -> List[str]:
        element = yongshen.get("yongshen", "土")
        fields_map = {
            "木": ["文化教育", "农林园艺", "木材家具"],
            "火": ["能源化工", "餐饮娱乐", "光电通讯"],
            "土": ["房地产", "农业畜牧", "矿产开采"],
            "金": ["金融投资", "金属加工", "法律军事"],
            "水": ["运输物流", "贸易商业", "水利工程"]
        }
        return fields_map.get(element, ["一般行业"])
