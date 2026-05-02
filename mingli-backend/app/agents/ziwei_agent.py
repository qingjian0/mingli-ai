"""
紫微斗数Agent模块

提供紫微斗数专项分析的Agent实现。
分析维度包括：性格、事业、财运、婚恋、健康等。
"""

from typing import Any, Dict, List, Optional
from .base import (
    BaseAgent,
    AnalysisResult,
    AnalysisType,
    TaskContext,
    ReasoningStep,
)


class ZiweiAgent(BaseAgent):
    """紫微斗数分析Agent

    专注于紫微斗数命盘的分析，提供全面的命理分析服务。
    """

    def __init__(self):
        super().__init__(
            name="ZiweiAgent",
            system_type="ziwei",
            version="1.0.0"
        )
        self._star_meanings = self._load_star_meanings()
        self._palace_attributes = self._load_palace_attributes()

    def _load_star_meanings(self) -> Dict[str, Dict[str, Any]]:
        return {
            "紫微星": {
                "nature": "帝王之星",
                "keywords": ["尊贵", "领导", "孤独"],
                "aspects": ["事业", "地位", "领导力"]
            },
            "天机星": {
                "nature": "智慧之星",
                "keywords": ["聪明", "机变", "谋略"],
                "aspects": ["智慧", "学业", "策划"]
            },
            "太阳星": {
                "nature": "光明之星",
                "keywords": ["热情", "正直", "付出"],
                "aspects": ["名望", "贵人", "公益"]
            },
            "武曲星": {
                "nature": "财帛之星",
                "keywords": ["刚毅", "果决", "固执"],
                "aspects": ["财运", "事业", "武职"]
            },
            "天同星": {
                "nature": "福禄之星",
                "keywords": ["温和", "享乐", "依赖"],
                "aspects": ["福气", "享受", "人际关系"]
            },
            "廉贞星": {
                "nature": "次桃花",
                "keywords": ["感情", "叛逆", "执着"],
                "aspects": ["感情", "艺术", "自律"]
            },
            "天府星": {
                "nature": "南斗帝王",
                "keywords": ["稳重", "保守", "福泽"],
                "aspects": ["财库", "稳定", "领导"]
            },
            "太阴星": {
                "nature": "财库之星",
                "keywords": ["细腻", "敏感", "内敛"],
                "aspects": ["财运", "房产", "女性缘"]
            },
            "贪狼星": {
                "nature": "多欲之星",
                "keywords": ["欲望", "桃花", "交际"],
                "aspects": ["桃花", "社交", "野心"]
            },
            "巨门星": {
                "nature": "暗昧之星",
                "keywords": ["口才", "是非", "疑惑"],
                "aspects": ["口才", "是非", "学术"]
            },
            "天相星": {
                "nature": "印星",
                "keywords": ["服务", "调和", "稳重"],
                "aspects": ["事业", "名声", "辅佐"]
            },
            "天梁星": {
                "nature": "荫星",
                "keywords": ["庇护", "寿星", "固执"],
                "aspects": ["健康", "长寿", "祖业"]
            },
            "七杀星": {
                "nature": "战斗之星",
                "keywords": ["刚猛", "冒险", "冲动"],
                "aspects": ["事业", "挑战", "变动"]
            },
            "破军星": {
                "nature": "耗星",
                "keywords": ["破坏", "开创", "消耗"],
                "aspects": ["开创", "变动", "消耗"]
            }
        }

    def _load_palace_attributes(self) -> Dict[str, Dict[str, Any]]:
        return {
            "命宫": {"domain": "自我", "keywords": ["性格", "命运"]},
            "兄弟宫": {"domain": "兄弟姐妹", "keywords": ["人际关系", "财务"]},
            "夫妻宫": {"domain": "婚姻", "keywords": ["感情", "配偶"]},
            "子女宫": {"domain": "子女", "keywords": ["后代", "桃花"]},
            "财帛宫": {"domain": "财富", "keywords": ["财运", "理财"]},
            "疾厄宫": {"domain": "健康", "keywords": ["身体", "疾病"]},
            "迁移宫": {"domain": "迁移", "keywords": ["外出", "人缘"]},
            "奴仆宫": {"domain": "交友", "keywords": ["下属", "社交"]},
            "官禄宫": {"domain": "事业", "keywords": ["工作", "地位"]},
            "田宅宫": {"domain": "家宅", "keywords": ["房产", "祖业"]},
            "福德宫": {"domain": "福气", "keywords": ["享受", "品德"]},
            "父母宫": {"domain": "父母", "keywords": ["遗传", "文书"]}
        }

    def get_capabilities(self) -> List[str]:
        return [
            "personality_analysis",
            "career_analysis",
            "love_analysis",
            "wealth_analysis",
            "health_analysis",
            "lucky_direction",
            "lucky_timing",
            "compatibility_analysis"
        ]

    def get_supported_types(self) -> List[AnalysisType]:
        return [
            AnalysisType.PERSONALITY,
            AnalysisType.CAREER,
            AnalysisType.LOVE,
            AnalysisType.WEALTH,
            AnalysisType.HEALTH,
            AnalysisType.DIRECTION,
            AnalysisType.TIMING,
            AnalysisType.COMPATIBILITY
        ]

    async def analyze(self, context: TaskContext) -> AnalysisResult:
        valid, error = self.validate_input(context)
        if not valid:
            raise ValueError(f"输入验证失败: {error}")

        chart_data = context.chart_data
        reasoning_chain: List[ReasoningStep] = []

        step1 = self._create_reasoning_step(
            description="提取紫微斗数命盘核心星曜信息",
            rule_id="ziwei_core_extract",
            inputs={"chart_data": chart_data},
            outputs={"main_stars": self._extract_main_stars(chart_data)}
        )
        reasoning_chain.append(step1)

        step2 = self._create_reasoning_step(
            description="分析命宫星曜组合判断性格特质",
            rule_id="ziwei_personality",
            inputs={"命宫星曜": self._get_palace_stars(chart_data, "命宫")},
            outputs={"personality_traits": self._analyze_personality(chart_data)}
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
            confidence=0.85,
            confidence_level=self._calculate_confidence_level(0.85),
            reasoning_chain=reasoning_chain,
            recommendations=content.get("recommendations", []),
            warnings=content.get("warnings", []),
            metadata={
                "system": "紫微斗数",
                "version": self.version,
                "chart_id": context.chart_id
            }
        )

        return result

    def _extract_main_stars(self, chart_data: Dict[str, Any]) -> List[str]:
        stars = chart_data.get("data", {}).get("stars", [])
        main_stars = [s for s in stars if s in self._star_meanings]
        return main_stars[:6]

    def _get_palace_stars(self, chart_data: Dict[str, Any], palace: str) -> List[str]:
        palaces_data = chart_data.get("data", {}).get("palaces", {})
        return palaces_data.get(palace, {}).get("stars", [])

    def _analyze_personality(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        main_stars = self._extract_main_stars(chart_data)
        traits = []
        keywords = []

        for star in main_stars:
            if star in self._star_meanings:
                traits.append(self._star_meanings[star]["nature"])
                keywords.extend(self._star_meanings[star]["keywords"])

        return {
            "core_traits": traits,
            "keywords": list(set(keywords))[:5],
            "description": self._generate_personality_description(traits)
        }

    def _generate_personality_description(self, traits: List[str]) -> str:
        if not traits:
            return "命格特质需要进一步分析"
        return "、".join(traits[:3])

    def _determine_primary_analysis(
        self,
        requested_types: set
    ) -> AnalysisType:
        priority_order = [
            AnalysisType.CAREER,
            AnalysisType.LOVE,
            AnalysisType.WEALTH,
            AnalysisType.HEALTH,
            AnalysisType.PERSONALITY
        ]
        for at in priority_order:
            if at in requested_types:
                return at
        return AnalysisType.PERSONALITY

    async def _generate_analysis_content(
        self,
        chart_data: Dict[str, Any],
        analysis_type: AnalysisType,
        context: TaskContext
    ) -> Dict[str, Any]:
        if analysis_type == AnalysisType.PERSONALITY:
            return await self._analyze_personality_full(chart_data)
        elif analysis_type == AnalysisType.CAREER:
            return await self._analyze_career(chart_data)
        elif analysis_type == AnalysisType.LOVE:
            return await self._analyze_love(chart_data)
        elif analysis_type == AnalysisType.WEALTH:
            return await self._analyze_wealth(chart_data)
        elif analysis_type == AnalysisType.HEALTH:
            return await self._analyze_health(chart_data)
        else:
            return await self._analyze_general(chart_data)

    async def _analyze_personality_full(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        personality = self._analyze_personality(chart_data)
        return {
            "summary": f"命主具有{personality['description']}的特质",
            "traits": personality,
            "strengths": self._extract_strengths(chart_data),
            "weaknesses": self._extract_weaknesses(chart_data),
            "recommendations": [
                "注意发挥自身优势，避免性格短板",
                "多参与社交活动，拓展人脉资源",
                "培养专注力，提升执行力"
            ],
            "warnings": []
        }

    async def _analyze_career(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        career_palace = self._get_palace_stars(chart_data, "官禄宫")
        suitable_industries = self._infer_industries(career_palace)
        return {
            "summary": "事业运势分析",
            "career_direction": suitable_industries,
            "lucky_periods": self._get_career_lucky_periods(chart_data),
            "recommendations": [
                "宜选择稳定的职业发展方向",
                "注意把握事业机遇，勇于挑战"
            ],
            "warnings": ["避免盲目投资或跳槽"]
        }

    async def _analyze_love(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        relationship_palace = self._get_palace_stars(chart_data, "夫妻宫")
        return {
            "summary": "婚恋感情分析",
            "love_traits": self._analyze_love_traits(relationship_palace),
            "ideal_partner": self._infer_partner_traits(relationship_palace),
            "timing": {"best_age_range": "25-35岁", "challenges": "需注意沟通方式"},
            "recommendations": [
                "注重感情经营，保持坦诚沟通",
                "提升自我价值，增强吸引力"
            ],
            "warnings": []
        }

    async def _analyze_wealth(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        wealth_palace = self._get_palace_stars(chart_data, "财帛宫")
        return {
            "summary": "财富运势分析",
            "wealth_type": self._infer_wealth_type(wealth_palace),
            "money_attitude": "理财观念分析",
            "recommendations": [
                "宜稳扎稳打，不宜投机",
                "注重长期投资规划"
            ],
            "warnings": ["注意财务风险"]
        }

    async def _analyze_health(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        health_palace = self._get_palace_stars(chart_data, "疾厄宫")
        return {
            "summary": "健康状况分析",
            "health_weak_points": self._infer_health_weak_points(health_palace),
            "health_tips": ["保持规律作息", "注意饮食调理"],
            "recommendations": [],
            "warnings": ["需定期体检关注身体健康"]
        }

    async def _analyze_general(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "summary": "综合命盘分析",
            "main_stars": self._extract_main_stars(chart_data),
            "life_aspects": {
                "personality": self._analyze_personality(chart_data)["keywords"],
                "career_direction": "事业需进一步分析",
                "love_outlook": "感情需进一步分析"
            },
            "recommendations": ["建议针对具体方面进行深入分析"],
            "warnings": []
        }

    def _extract_strengths(self, chart_data: Dict[str, Any]) -> List[str]:
        return ["聪慧", "适应力强", "人缘佳"]

    def _extract_weaknesses(self, chart_data: Dict[str, Any]) -> List[str]:
        return ["有时过于理想化", "需注意执行力"]

    def _infer_industries(self, stars: List[str]) -> List[str]:
        return ["服务业", "文化教育", "商业贸易"]

    def _get_career_lucky_periods(self, chart_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            {"age_range": "25-30岁", "description": "事业起步期"},
            {"age_range": "35-45岁", "description": "事业高峰期"}
        ]

    def _analyze_love_traits(self, stars: List[str]) -> Dict[str, Any]:
        return {
            "love_style": "真诚型",
            "emotional_needs": "需要被理解和尊重"
        }

    def _infer_partner_traits(self, stars: List[str]) -> Dict[str, Any]:
        return {
            "personality": "稳重可靠",
            "values": "重视家庭"
        }

    def _infer_wealth_type(self, stars: List[str]) -> str:
        return "正财为主，偏财为辅"

    def _infer_health_weak_points(self, stars: List[str]) -> List[str]:
        return ["需注意消化系统", "保持情绪稳定"]
