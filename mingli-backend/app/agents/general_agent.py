"""
综合分析Agent模块

提供多体系融合的综合分析服务，整合八字、紫微斗数、奇门遁甲等体系的分析结果。
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING
from .base import (
    BaseAgent,
    AnalysisResult,
    AnalysisType,
    TaskContext,
    ReasoningStep,
)

if TYPE_CHECKING:
    from .ziwei_agent import ZiweiAgent
    from .bazi_agent import BaziAgent
    from .qimen_agent import QimenAgent


class GeneralAgent(BaseAgent):
    """综合分析Agent

    整合多个命理体系的分析结果，提供全面的综合分析和建议。
    """

    def __init__(self):
        super().__init__(
            name="GeneralAgent",
            system_type="general",
            version="1.0.0"
        )
        self._sub_agents: Dict[str, BaseAgent] = {}
        self._integration_rules = self._load_integration_rules()

    def _load_integration_rules(self) -> Dict[str, Any]:
        return {
            "priority_order": ["bazi", "ziwei", "qimen"],
            "consensus_weight": {
                "high": 0.9,
                "medium": 0.7,
                "low": 0.5
            },
            "conflict_resolution": "prefer_higher_confidence"
        }

    def register_sub_agent(self, agent: BaseAgent) -> None:
        self._sub_agents[agent.system_type] = agent

    def get_capabilities(self) -> List[str]:
        return [
            "integrated_analysis",
            "multi_system_comparison",
            "comprehensive_recommendations",
            "life_guidance",
            "cross_system_validation"
        ]

    def get_supported_types(self) -> List[AnalysisType]:
        return [
            AnalysisType.GENERAL,
            AnalysisType.PERSONALITY,
            AnalysisType.CAREER,
            AnalysisType.LOVE,
            AnalysisType.WEALTH,
            AnalysisType.HEALTH,
            AnalysisType.FATE_TREND,
            AnalysisType.LUCKY_PERIOD
        ]

    async def analyze(self, context: TaskContext) -> AnalysisResult:
        valid, error = self.validate_input(context)
        if not valid:
            raise ValueError(f"输入验证失败: {error}")

        chart_type = context.get_chart_type()
        reasoning_chain: List[ReasoningStep] = []

        step1 = self._create_reasoning_step(
            description="收集各体系分析结果",
            rule_id="general_collect",
            inputs={"chart_type": chart_type},
            outputs={"sub_results": {}}
        )
        reasoning_chain.append(step1)

        sub_results = await self._collect_sub_results(context)
        step1.outputs = {"sub_results": list(sub_results.keys())}

        step2 = self._create_reasoning_step(
            description="整合分析结果，识别共识与差异",
            rule_id="general_integrate",
            inputs={"sub_results": sub_results},
            outputs={"integrated_view": self._integrate_results(sub_results)}
        )
        reasoning_chain.append(step2)

        step3 = self._create_reasoning_step(
            description="生成综合建议和行动计划",
            rule_id="general_recommend",
            inputs={"integrated_view": self._integrate_results(sub_results)},
            outputs={"recommendations": []}
        )
        reasoning_chain.append(step3)

        content = await self._generate_integrated_content(context, sub_results)
        step3.outputs = {"recommendations": content.get("recommendations", [])}

        integrated_view = self._integrate_results(sub_results)
        confidence = self._calculate_integrated_confidence(sub_results)

        result = AnalysisResult(
            analysis_id=self._generate_analysis_id(context, AnalysisType.GENERAL),
            analysis_type=AnalysisType.GENERAL,
            agent_name=self.name,
            content=content,
            summary=content.get("summary", ""),
            confidence=confidence,
            confidence_level=self._calculate_confidence_level(confidence),
            reasoning_chain=reasoning_chain,
            recommendations=content.get("recommendations", []),
            warnings=content.get("warnings", []),
            metadata={
                "system": "综合分析",
                "version": self.version,
                "chart_id": context.chart_id,
                "sub_systems": list(sub_results.keys()),
                "integration_quality": integrated_view.get("consensus_level", "unknown")
            }
        )

        return result

    async def _collect_sub_results(self, context: TaskContext) -> Dict[str, Dict[str, Any]]:
        results = {}

        if "bazi" in self._sub_agents and context.get_chart_type() in ["bazi", "bazi_ziwei"]:
            agent: "BaziAgent" = self._sub_agents["bazi"]
            try:
                result = await agent.analyze(context)
                results["bazi"] = result.content
            except Exception as e:
                if self.logger:
                    self.logger.warning(f"BaziAgent分析失败: {e}")

        if "ziwei" in self._sub_agents and context.get_chart_type() in ["ziwei", "bazi_ziwei"]:
            agent: "ZiweiAgent" = self._sub_agents["ziwei"]
            try:
                result = await agent.analyze(context)
                results["ziwei"] = result.content
            except Exception as e:
                if self.logger:
                    self.logger.warning(f"ZiweiAgent分析失败: {e}")

        if "qimen" in self._sub_agents and context.get_chart_type() in ["qimen", "bazi_ziwei"]:
            agent: "QimenAgent" = self._sub_agents["qimen"]
            try:
                result = await agent.analyze(context)
                results["qimen"] = result.content
            except Exception as e:
                if self.logger:
                    self.logger.warning(f"QimenAgent分析失败: {e}")

        return results

    def _integrate_results(self, sub_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        if not sub_results:
            return {"consensus_level": "unknown", "points": []}

        consensus_points = []
        conflict_points = []

        personality_from_bazi = sub_results.get("bazi", {}).get("personality_traits", [])
        personality_from_ziwei = sub_results.get("ziwei", {}).get("traits", {}).get("keywords", [])

        if personality_from_bazi and personality_from_ziwei:
            overlap = set(personality_from_bazi) & set(personality_from_ziwei)
            if len(overlap) >= 2:
                consensus_points.append({
                    "aspect": "性格特质",
                    "consensus": list(overlap),
                    "confidence": "high"
                })
            else:
                conflict_points.append({
                    "aspect": "性格特质",
                    "different_views": {
                        "八字": personality_from_bazi,
                        "紫微": personality_from_ziwei
                    }
                })

        career_consensus = self._find_career_consensus(sub_results)
        if career_consensus:
            consensus_points.append(career_consensus)

        luck_consensus = self._find_luck_consensus(sub_results)
        if luck_consensus:
            consensus_points.append(luck_consensus)

        consensus_level = "high" if len(consensus_points) >= 3 else "medium" if consensus_points else "low"

        return {
            "consensus_level": consensus_level,
            "consensus_points": consensus_points,
            "conflict_points": conflict_points,
            "summary": self._generate_integration_summary(consensus_points, conflict_points)
        }

    def _find_career_consensus(self, sub_results: Dict[str, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        career_fields = []

        if "bazi" in sub_results:
            bazi_career = sub_results["bazi"].get("suitable_fields", [])
            career_fields.extend(bazi_career)

        if "ziwei" in sub_results:
            ziwei_career = sub_results["ziwei"].get("career_direction", [])
            career_fields.extend(ziwei_career)

        if not career_fields:
            return None

        field_counts: Dict[str, int] = {}
        for field in career_fields:
            field_counts[field] = field_counts.get(field, 0) + 1

        top_fields = sorted(field_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        return {
            "aspect": "事业方向",
            "consensus": [f[0] for f in top_fields],
            "confidence": "medium" if len(top_fields) > 1 else "low"
        }

    def _find_luck_consensus(self, sub_results: Dict[str, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        lucky_periods = []

        if "bazi" in sub_results:
            bazi_luck = sub_results["bazi"].get("life_phases", [])
            lucky_periods.extend([p.get("description", "") for p in bazi_luck if p.get("favorable")])

        if "qimen" in sub_results:
            qimen_luck = sub_results["qimen"].get("favorable_periods", [])
            lucky_periods.extend([p.get("time", "") for p in qimen_luck if p.get("quality") == "吉"])

        if not lucky_periods:
            return None

        return {
            "aspect": "吉运时期",
            "consensus": list(set(lucky_periods))[:5],
            "confidence": "medium"
        }

    def _generate_integration_summary(
        self,
        consensus_points: List[Dict[str, Any]],
        conflict_points: List[Dict[str, Any]]
    ) -> str:
        if not consensus_points and not conflict_points:
            return "各体系分析结果待补充"

        parts = []
        if consensus_points:
            aspects = [p["aspect"] for p in consensus_points]
            parts.append(f"各体系在{', '.join(aspects)}方面达成共识")

        if conflict_points:
            aspects = [p["aspect"] for p in conflict_points]
            parts.append(f"以下方面存在差异：{', '.join(aspects)}，建议综合考量")

        return "；".join(parts) if parts else "分析完成"

    def _calculate_integrated_confidence(self, sub_results: Dict[str, Dict[str, Any]]) -> float:
        if not sub_results:
            return 0.5

        weights = {"bazi": 0.4, "ziwei": 0.35, "qimen": 0.25}
        total_weight = 0.0
        weighted_confidence = 0.0

        for system, result in sub_results.items():
            weight = weights.get(system, 0.3)
            confidence = result.get("confidence", 0.8)
            weighted_confidence += weight * confidence
            total_weight += weight

        return weighted_confidence / total_weight if total_weight > 0 else 0.5

    async def _generate_integrated_content(
        self,
        context: TaskContext,
        sub_results: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        integrated_view = self._integrate_results(sub_results)

        summary = self._generate_summary_text(sub_results, integrated_view)
        recommendations = self._generate_recommendations(sub_results, integrated_view)
        warnings = self._generate_warnings(sub_results)

        life_guidance = self._generate_life_guidance(sub_results, integrated_view)

        return {
            "summary": summary,
            "integrated_view": integrated_view,
            "personality_analysis": self._integrate_personality(sub_results),
            "career_advice": self._integrate_career(sub_results),
            "wealth_outlook": self._integrate_wealth(sub_results),
            "relationship_guidance": self._integrate_relationship(sub_results),
            "life_guidance": life_guidance,
            "recommendations": recommendations,
            "warnings": warnings,
            "sub_system_results": {
                system: {
                    "summary": result.get("summary", ""),
                    "key_points": self._extract_key_points(result)
                }
                for system, result in sub_results.items()
            }
        }

    def _generate_summary_text(
        self,
        sub_results: Dict[str, Dict[str, Any]],
        integrated_view: Dict[str, Any]
    ) -> str:
        systems = list(sub_results.keys())
        system_names = {
            "bazi": "八字",
            "ziwei": "紫微斗数",
            "qimen": "奇门遁甲"
        }
        system_text = "、".join([system_names.get(s, s) for s in systems])

        consensus_text = ""
        if integrated_view.get("consensus_level") == "high":
            consensus_text = "各体系分析高度一致"
        elif integrated_view.get("consensus_level") == "medium":
            consensus_text = "各体系分析基本一致，存在部分差异"
        else:
            consensus_text = "建议进一步综合分析"

        return f"综合{system_text}分析：{consensus_text}。{integrated_view.get('summary', '')}"

    def _integrate_personality(self, sub_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        traits = []
        sources = []

        if "bazi" in sub_results:
            bazi_traits = sub_results["bazi"].get("personality_traits", [])
            traits.extend(bazi_traits)
            sources.append("八字")

        if "ziwei" in sub_results:
            ziwei_traits = sub_results["ziwei"].get("traits", {}).get("keywords", [])
            traits.extend(ziwei_traits)
            sources.append("紫微")

        unique_traits = list(set(traits))[:5]

        return {
            "summary": f"综合{sources}分析，性格特质为：{', '.join(unique_traits)}",
            "traits": unique_traits,
            "sources": sources
        }

    def _integrate_career(self, sub_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        fields = []
        if "bazi" in sub_results:
            fields.extend(sub_results["bazi"].get("suitable_fields", []))
        if "ziwei" in sub_results:
            fields.extend(sub_results["ziwei"].get("career_direction", []))

        field_counts: Dict[str, int] = {}
        for field in fields:
            field_counts[field] = field_counts.get(field, 0) + 1

        top_fields = sorted(field_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        return {
            "recommended_fields": [f[0] for f in top_fields],
            "advice": "多体系一致推荐的事业方向"
        }

    def _integrate_wealth(self, sub_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        wealth_types = []
        if "bazi" in sub_results:
            wealth_types.append(sub_results["bazi"].get("wealth_type", "稳健型"))
        if "ziwei" in sub_results:
            wealth_types.append(sub_results["ziwei"].get("wealth_type", "正财为主"))

        return {
            "wealth_type": wealth_types[0] if wealth_types else "综合分析",
            "advice": "宜稳扎稳打，注重长期积累"
        }

    def _integrate_relationship(self, sub_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        love_advice = []
        if "ziwei" in sub_results:
            love_advice.append(sub_results["ziwei"].get("love_traits", {}))

        return {
            "summary": "感情分析综合建议",
            "advice": love_advice[0] if love_advice else {}
        }

    def _generate_life_guidance(
        self,
        sub_results: Dict[str, Dict[str, Any]],
        integrated_view: Dict[str, Any]
    ) -> Dict[str, Any]:
        guidance = {
            "short_term": [],
            "medium_term": [],
            "long_term": []
        }

        if "bazi" in sub_results:
            phases = sub_results["bazi"].get("life_phases", [])
            for phase in phases:
                age = phase.get("age_range", "")
                if "20" in age or "30" in age:
                    guidance["short_term"].append(phase.get("description", ""))
                elif "40" in age or "50" in age:
                    guidance["medium_term"].append(phase.get("description", ""))
                else:
                    guidance["long_term"].append(phase.get("description", ""))

        if "qimen" in sub_results:
            periods = sub_results["qimen"].get("favorable_periods", [])
            guidance["short_term"].extend([p.get("suitable", "") for p in periods[:2]])

        return guidance

    def _generate_recommendations(
        self,
        sub_results: Dict[str, Dict[str, Any]],
        integrated_view: Dict[str, Any]
    ) -> List[str]:
        recommendations = []

        consensus_points = integrated_view.get("consensus_points", [])
        for point in consensus_points:
            aspect = point.get("aspect", "")
            consensus = point.get("consensus", [])
            if aspect == "事业方向":
                recommendations.append(f"事业：{', '.join(consensus[:2])}方向发展有利")
            elif aspect == "性格特质":
                recommendations.append(f"性格：注意发挥{', '.join(consensus[:2])}的优势")

        recommendations.append("各体系综合分析结果一致，建议据此规划人生")

        return recommendations[:5]

    def _generate_warnings(self, sub_results: Dict[str, Dict[str, Any]]) -> List[str]:
        warnings = []

        conflict_points = []
        if "bazi" in sub_results:
            warnings.extend(sub_results["bazi"].get("warnings", []))
        if "ziwei" in sub_results:
            warnings.extend(sub_results["ziwei"].get("warnings", []))
        if "qimen" in sub_results:
            warnings.extend(sub_results["qimen"].get("warnings", []))

        unique_warnings = list(set(warnings))
        return unique_warnings[:3]

    def _extract_key_points(self, result: Dict[str, Any]) -> List[str]:
        key_points = []
        if result.get("summary"):
            key_points.append(result["summary"])
        if result.get("yongshen"):
            key_points.append(f"用神：{result['yongshen'].get('yongshen', '')}")
        if result.get("traits"):
            traits = result["traits"].get("keywords", [])
            key_points.append(f"特质：{', '.join(traits[:3])}")
        return key_points[:3]
