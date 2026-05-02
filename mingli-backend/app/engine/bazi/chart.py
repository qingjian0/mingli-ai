"""
八字排盘模块
核心八字命盘计算逻辑
"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from pydantic import BaseModel, Field

from ..base import BaseEngine, BaseChartData, ChartMetadata, BirthInfo, ChartType, EngineRegistry
from ..datetime_utils import (
    calculate_four_pillars, get_year_stem_branch, get_month_stem_branch,
    get_day_stem_branch, get_hour_stem_branch, calculate_true_solar_time,
    get_current_solar_term, HEAVENLY_STEMS, EARTHLY_BRANCHES
)
from .stems import STEM_ELEMENTS, STEM_INDICES, Element
from .branches import BRANCH_ELEMENTS, BRANCH_INDICES, get_branch_hidden_stems
from .combinations import analyze_pillar_relations, check_branch_xing


class BaziPillar(BaseModel):
    """单柱模型"""
    stem: str = Field(description="天干")
    branch: str = Field(description="地支")
    stem_element: str = Field(description="天干五行")
    branch_element: str = Field(description="地支五行")
    hidden_stems: List[Dict[str, Any]] = Field(default_factory=list, description="地支藏干")


class BaziChartData(BaseChartData):
    """八字命盘数据"""
    pass


class BaziStrengthResult(BaseModel):
    """日主强弱分析结果"""
    day_master_strength: float = Field(description="日主得分(0-100)")
    level: str = Field(description="强弱等级: 极强/强/中和/弱/极弱")
    factors: List[Dict[str, str]] = Field(default_factory=list, description="影响因素")


@EngineRegistry.register(ChartType.BAZI)
class BaziEngine(BaseEngine):
    """八字排盘引擎"""

    chart_type = ChartType.BAZI

    def __init__(self):
        self.stems = HEAVENLY_STEMS
        self.branches = EARTHLY_BRANCHES

    def validate_input(self, birth_info: BirthInfo) -> bool:
        """验证输入参数"""
        if birth_info.birth_time.year < 1900 or birth_info.birth_time.year > 2100:
            return False
        if birth_info.birth_time.hour < 0 or birth_info.birth_time.hour > 23:
            return False
        return True

    def calculate(self, birth_info: BirthInfo) -> BaziChartData:
        """执行八字排盘"""
        local_time = birth_info.birth_time

        if birth_info.location.longitude != 0:
            tz_offset = float(birth_info.location.timezone) if isinstance(birth_info.location.timezone, (int, float)) else 8.0
            true_solar_time = calculate_true_solar_time(
                local_time,
                birth_info.location.longitude,
                tz_offset
            )
        else:
            true_solar_time = local_time

        year = true_solar_time.year
        month = true_solar_time.month
        day = true_solar_time.day
        hour = true_solar_time.hour

        year_stem, year_branch = get_year_stem_branch(year)
        month_stem, month_branch = get_month_stem_branch(year_stem, month)
        day_stem, day_branch = get_day_stem_branch(year, month, day)
        hour_stem, hour_branch = get_hour_stem_branch(day_stem, hour)

        pillars = {
            "year": {"stem": year_stem, "branch": year_branch},
            "month": {"stem": month_stem, "branch": month_branch},
            "day": {"stem": day_stem, "branch": day_branch},
            "hour": {"stem": hour_stem, "branch": hour_branch}
        }

        natal_pillars = self._build_pillars(pillars)

        relations = analyze_pillar_relations(pillars)

        strength = self._calculate_day_master_strength(pillars)

        dayun = self._calculate_dayun(year, month, day, hour, birth_info.gender.value)

        solar_term_info = get_current_solar_term(local_time)

        metadata = self._create_metadata(birth_info)

        data = {
            "four_pillars": natal_pillars,
            "relations": relations,
            "strength_analysis": strength.model_dump(),
            "dayun": dayun,
            "solar_term": {
                "name": solar_term_info[0],
                "date": solar_term_info[1].isoformat()
            },
            "true_solar_time": true_solar_time.isoformat(),
            "day_master": day_stem
        }

        return BaziChartData(metadata=metadata, data=data)

    def _build_pillars(self, pillars: Dict[str, Dict[str, str]]) -> Dict[str, BaziPillar]:
        """构建四柱模型"""
        result = {}
        for key, pillar in pillars.items():
            stem = pillar["stem"]
            branch = pillar["branch"]
            hidden = get_branch_hidden_stems(branch)

            result[key] = BaziPillar(
                stem=stem,
                branch=branch,
                stem_element=STEM_ELEMENTS[stem].value,
                branch_element=BRANCH_ELEMENTS[branch].value,
                hidden_stems=[{"stem": h[0], "ratio": h[1]} for h in hidden]
            )
        return {k: v.model_dump() for k, v in {k: BaziPillar(**{**pillars[k],
            "stem_element": STEM_ELEMENTS[pillars[k]["stem"]].value,
            "branch_element": BRANCH_ELEMENTS[pillars[k]["branch"]].value,
            "hidden_stems": [{"stem": h[0], "ratio": h[1]} for h in get_branch_hidden_stems(pillars[k]["branch"])]
        }) for k in pillars}.items()}

    def _calculate_day_master_strength(self, pillars: Dict[str, Dict[str, str]]) -> BaziStrengthResult:
        """计算日主强弱"""
        day_stem = pillars["day"]["stem"]
        day_element = STEM_ELEMENTS[day_stem]

        element_counts = {Element.WATER: 0, Element.FIRE: 0, Element.WOOD: 0, Element.EARTH: 0, Element.METAL: 0}

        for pillar in pillars.values():
            stem = pillar["stem"]
            branch = pillar["branch"]

            element_counts[STEM_ELEMENTS[stem]] += 1

            hidden_stems = get_branch_hidden_stems(branch)
            for hidden_stem, ratio in hidden_stems:
                element_counts[STEM_ELEMENTS[hidden_stem]] += ratio

        score = 50

        element_map = {
            Element.WATER: "水",
            Element.FIRE: "火",
            Element.WOOD: "木",
            Element.EARTH: "土",
            Element.METAL: "金"
        }

        factors = []

        if day_element == Element.WOOD:
            score += (element_counts[Element.WATER] - element_counts[Element.METAL]) * 8
            if element_counts[Element.FIRE] > 0:
                factors.append({"type": "泄", "desc": "火泄木气"})
            if element_counts[Element.METAL] > 0:
                factors.append({"type": "克", "desc": "金克木"})
        elif day_element == Element.FIRE:
            score += (element_counts[Element.WOOD] - element_counts[Element.WATER]) * 8
            if element_counts[Element.EARTH] > 0:
                factors.append({"type": "生", "desc": "土助火势"})
        elif day_element == Element.EARTH:
            score += (element_counts[Element.FIRE] - element_counts[Element.WOOD]) * 8
            if element_counts[Element.METAL] > 0:
                factors.append({"type": "生", "desc": "金泄土气"})
        elif day_element == Element.METAL:
            score += (element_counts[Element.EARTH] - element_counts[Element.FIRE]) * 8
            if element_counts[Element.WATER] > 0:
                factors.append({"type": "生", "desc": "水助金势"})
        elif day_element == Element.WATER:
            score += (element_counts[Element.METAL] - element_counts[Element.EARTH]) * 8
            if element_counts[Element.WOOD] > 0:
                factors.append({"type": "生", "desc": "木泄水气"})

        month_branch = pillars["month"]["branch"]
        month_element = BRANCH_ELEMENTS[month_branch]
        if month_element == day_element:
            score += 10
            factors.append({"type": "得令", "desc": f"月令{element_map[month_element]}与日主同气"})

        score = max(0, min(100, score))

        if score >= 80:
            level = "极强"
        elif score >= 65:
            level = "强"
        elif score >= 45:
            level = "中和"
        elif score >= 30:
            level = "弱"
        else:
            level = "极弱"

        return BaziStrengthResult(
            day_master_strength=score,
            level=level,
            factors=factors
        )

    def _calculate_dayun(self, year: int, month: int, day: int,
                         hour: int, gender: str) -> List[Dict]:
        """计算大运"""
        dayun_start_age = 0

        month_stem, month_branch = get_month_stem_branch(
            get_year_stem_branch(year)[0], month
        )

        dayun_direction = 1 if gender == "male" else -1

        dayun_stems = []
        dayun_branches = []

        month_idx = BRANCH_INDICES[month_branch]
        month_stem_idx = STEM_INDICES[month_stem]

        for i in range(10):
            stem_idx = (month_stem_idx + dayun_direction * (i + 1)) % 10
            branch_idx = (month_idx + dayun_direction * (i + 1)) % 12
            dayun_stems.append(HEAVENLY_STEMS[stem_idx])
            dayun_branches.append(EARTHLY_BRANCHES[branch_idx])

        dayun = []
        for i in range(10):
            dayun.append({
                "stem": dayun_stems[i],
                "branch": dayun_branches[i],
                "element": STEM_ELEMENTS[dayun_stems[i]].value,
                "start_year": 0,
                "end_year": 10
            })

        return dayun

    def select_usable_god(self, strength_result: BaziStrengthResult,
                          pillars: Dict[str, Dict[str, str]]) -> Dict[str, str]:
        """选取用神"""
        day_stem = pillars["day"]["stem"]
        day_element = STEM_ELEMENTS[day_stem]

        usable_gods = {"main": "", "auxiliary": []}

        if strength_result.level in ["极强", "强"]:
            if day_element == Element.WOOD:
                usable_gods["main"] = "庚辛金"
                usable_gods["auxiliary"] = ["壬癸水", "戊己土"]
            elif day_element == Element.FIRE:
                usable_gods["main"] = "壬癸水"
                usable_gods["auxiliary"] = ["甲乙木", "庚辛金"]
            elif day_element == Element.EARTH:
                usable_gods["main"] = "甲乙木"
                usable_gods["auxiliary"] = ["丙丁火", "壬癸水"]
            elif day_element == Element.METAL:
                usable_gods["main"] = "丁丙火"
                usable_gods["auxiliary"] = ["戊己土", "甲乙木"]
            elif day_element == Element.WATER:
                usable_gods["main"] = "戊己土"
                usable_gods["auxiliary"] = ["庚辛金", "丙丁火"]
        else:
            if day_element == Element.WOOD:
                usable_gods["main"] = "甲乙木"
                usable_gods["auxiliary"] = ["壬癸水", "丙丁火"]
            elif day_element == Element.FIRE:
                usable_gods["main"] = "丙丁火"
                usable_gods["auxiliary"] = ["甲乙木", "戊己土"]
            elif day_element == Element.EARTH:
                usable_gods["main"] = "戊己土"
                usable_gods["auxiliary"] = ["丙丁火", "庚辛金"]
            elif day_element == Element.METAL:
                usable_gods["main"] = "庚辛金"
                usable_gods["auxiliary"] = ["戊己土", "壬癸水"]
            elif day_element == Element.WATER:
                usable_gods["main"] = "壬癸水"
                usable_gods["auxiliary"] = ["庚辛金", "甲乙木"]

        return usable_gods
