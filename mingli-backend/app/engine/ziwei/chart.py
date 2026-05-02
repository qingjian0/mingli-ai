"""
紫微斗数排盘模块
核心排盘算法实现
"""

from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field

from ..base import BaseEngine, BaseChartData, ChartMetadata, BirthInfo, ChartType, EngineRegistry
from ..datetime_utils import (
    calculate_four_pillars, get_year_stem_branch, get_month_stem_branch,
    get_day_stem_branch, get_hour_stem_branch, calculate_true_solar_time,
    get_current_solar_term, EARTHLY_BRANCHES, gregorian_to_julian_day
)
from .stars import MAIN_STARS, STAR_ATTRS, AUXILIARY_STARS, EVIL_STARS, get_star_attrs
from .palaces import (
    TWELVE_PALACES, PALACE_ORDER, calculate_ming_gong, calculate_sheng_gong,
    get_palace_meaning
)
from .transforms import get_birth_year_transform, apply_transform_to_stars, get_transform_interaction


class PalaceData(BaseModel):
    """宫位数据"""
    name: str = Field(description="宫位名称")
    branch: str = Field(description="宫内地支")
    stars: List[str] = Field(default_factory=list, description="主星列表")
    auxiliary_stars: List[str] = Field(default_factory=list, description="辅星列表")
    evil_stars: List[str] = Field(default_factory=list, description="煞星列表")
    misc_stars: List[str] = Field(default_factory=list, description="杂曜列表")
    meaning: str = Field(description="宫位含义")


class ZiweiChartData(BaseChartData):
    """紫微斗数命盘数据"""
    pass


@EngineRegistry.register(ChartType.ZIWEI)
class ZiweiEngine(BaseEngine):
    """紫微斗数排盘引擎"""

    chart_type = ChartType.ZIWEI

    def __init__(self):
        self.main_stars = MAIN_STARS
        self.palaces = TWELVE_PALACES
        self.branch_list = EARTHLY_BRANCHES

    def validate_input(self, birth_info: BirthInfo) -> bool:
        """验证输入"""
        if birth_info.birth_time.year < 1900 or birth_info.birth_time.year > 2100:
            return False
        return True

    def calculate(self, birth_info: BirthInfo) -> ZiweiChartData:
        """执行紫微斗数排盘"""
        local_time = birth_info.birth_time

        if birth_info.location.longitude != 0:
            tz_offset = float(birth_info.location.timezone) if isinstance(birth_info.location.timezone, (int, float)) else 8.0
            birth_time = calculate_true_solar_time(
                local_time,
                birth_info.location.longitude,
                tz_offset
            )
        else:
            birth_time = local_time

        year = birth_time.year
        month = birth_time.month
        day = birth_time.day
        hour = birth_time.hour

        four_pillars = calculate_four_pillars(year, month, day, hour)
        year_stem = four_pillars["year"]["stem"]
        year_branch = four_pillars["year"]["branch"]
        month_branch = four_pillars["month"]["branch"]
        hour_branch = four_pillars["hour"]["branch"]
        day_stem = four_pillars["day"]["stem"]

        gender = birth_info.gender.value

        ming_gong_idx = calculate_ming_gong(month_branch, hour_branch, gender)
        sheng_gong_idx = calculate_sheng_gong(month_branch)

        natal_palace_map = self._calculate_natal_palaces(
            ming_gong_idx, sheng_gong_idx, day_stem, hour_branch
        )

        main_stars_placed = self._place_main_stars(ming_gong_idx, year_branch, month_branch, day_stem)

        auxiliary_stars = self._place_auxiliary_stars(ming_gong_idx, hour_branch)

        evil_stars = self._place_evil_stars(ming_gong_idx, year_stem)

        birth_transforms = get_birth_year_transform(year_stem)

        palaces_data = self._build_palaces_data(
            natal_palace_map, main_stars_placed, auxiliary_stars, evil_stars, birth_transforms
        )

        big_fate_periods = self._calculate_big_fate_periods(
            ming_gong_idx, year, month, day, birth_time, gender
        )

        solar_term_info = get_current_solar_term(local_time)

        metadata = self._create_metadata(birth_info)

        data = {
            "four_pillars": four_pillars,
            "ming_gong": TWELVE_PALACES[ming_gong_idx],
            "sheng_gong": TWELVE_PALACES[sheng_gong_idx],
            "birth_transforms": birth_transforms,
            "palaces": palaces_data,
            "main_stars_positions": main_stars_placed,
            "big_fate_periods": big_fate_periods,
            "solar_term": {
                "name": solar_term_info[0],
                "date": solar_term_info[1].isoformat()
            },
            "day_master": day_stem,
            "year_branch": year_branch,
            "month_branch": month_branch,
            "hour_branch": hour_branch
        }

        return ZiweiChartData(metadata=metadata, data=data)

    def _calculate_natal_palaces(self, ming_gong_idx: int, sheng_gong_idx: int,
                                  day_stem: str, hour_branch: str) -> Dict[str, int]:
        """
        计算先天命宫分布

        Args:
            ming_gong_idx: 命宫索引
            sheng_gong_idx: 身宫索引
            day_stem: 日干
            hour_branch: 时支

        Returns:
            宫位到地支的映射
        """
        natal_palace_map = {}

        for i, palace in enumerate(TWELVE_PALACES):
            branch_idx = (ming_gong_idx + i) % 12
            natal_palace_map[palace] = branch_idx

        return natal_palace_map

    def _place_main_stars(self, ming_gong_idx: int, year_branch: str,
                           month_branch: str, day_stem: str) -> Dict[str, int]:
        """
        排十四主星

        基于紫微斗数钦天门法排布
        """
        positions = {}

        year_idx = EARTHLY_BRANCHES.index(year_branch)
        month_idx = EARTHLY_BRANCHES.index(month_branch)

        base_branch_idx = (year_idx - month_idx + 12) % 12

        ziwei_base_idx = (base_branch_idx + 2) % 12
        positions["紫微"] = (ziwei_base_idx - ming_gong_idx + 12) % 12

        tianji_base = (base_branch_idx + 5) % 12
        positions["天机"] = (tianji_base - ming_gong_idx + 12) % 12

        taiyang_base = (base_branch_idx + 8) % 12
        positions["太阳"] = (taiyang_base - ming_gong_idx + 12) % 12

        wuqu_base = (base_branch_idx + 11) % 12
        positions["武曲"] = (wuqu_base - ming_gong_idx + 12) % 12

        tiantong_base = (base_branch_idx + 1) % 12
        positions["天同"] = (tiantong_base - ming_gong_idx + 12) % 12

        lianzhen_base = (base_branch_idx + 3) % 12
        positions["廉贞"] = (lianzhen_base - ming_gong_idx + 12) % 12

        tianfu_base = (base_branch_idx + 4) % 12
        positions["天府"] = (tianfu_base - ming_gong_idx + 12) % 12

        taiyin_base = (base_branch_idx + 9) % 12
        positions["太阴"] = (taiyin_base - ming_gong_idx + 12) % 12

        tanlang_base = (base_branch_idx + 0) % 12
        positions["贪狼"] = (tanlang_base - ming_gong_idx + 12) % 12

        jumen_base = (base_branch_idx + 2) % 12
        positions["巨门"] = (jumen_base - ming_gong_idx + 12) % 12

        tianxiang_base = (base_branch_idx + 7) % 12
        positions["天相"] = (tianxiang_base - ming_gong_idx + 12) % 12

        tianliang_base = (base_branch_idx + 4) % 12
        positions["天梁"] = (tianliang_base - ming_gong_idx + 12) % 12

        qisha_base = (base_branch_idx + 6) % 12
        positions["七杀"] = (qisha_base - ming_gong_idx + 12) % 12

        pojun_base = (base_branch_idx + 10) % 12
        positions["破军"] = (pojun_base - ming_gong_idx + 12) % 12

        return positions

    def _place_auxiliary_stars(self, ming_gong_idx: int, hour_branch: str) -> Dict[str, int]:
        """
        排辅星

        左辅、右弼、文昌、文曲等
        """
        positions = {}

        zuofu_idx = (ming_gong_idx + 2) % 12
        positions["左辅"] = zuofu_idx

        zuoyou_idx = (ming_gong_idx + 10) % 12
        positions["右弼"] = zuoyou_idx

        wenchang_idx = (ming_gong_idx + 4) % 12
        positions["文昌"] = wenchang_idx

        wenqu_idx = (ming_gong_idx + 6) % 12
        positions["文曲"] = wenqu_idx

        tiankui_idx = (ming_gong_idx + 1) % 12
        positions["天魁"] = tiankui_idx

        tianyue_idx = (ming_gong_idx + 7) % 12
        positions["天钺"] = tianyue_idx

        return positions

    def _place_evil_stars(self, ming_gong_idx: int, year_stem: str) -> Dict[str, int]:
        """
        排煞星

        擎羊、陀罗、火星、铃星、地空、地劫
        """
        positions = {}

        qingyang_idx = (ming_gong_idx + 5) % 12
        positions["擎羊"] = qingyang_idx

        tuoluo_idx = (ming_gong_idx + 11) % 12
        positions["陀罗"] = tuoluo_idx

        huoxing_idx = (ming_gong_idx + 3) % 12
        positions["火星"] = huoxing_idx

        lingxing_idx = (ming_gong_idx + 9) % 12
        positions["铃星"] = lingxing_idx

        dikong_idx = (ming_gong_idx + 4) % 12
        positions["地空"] = dikong_idx

        dijie_idx = (ming_gong_idx + 10) % 12
        positions["地劫"] = dijie_idx

        return positions

    def _build_palaces_data(self, natal_palace_map: Dict[str, int],
                              main_stars: Dict[str, int],
                              auxiliary_stars: Dict[str, int],
                              evil_stars: Dict[str, int],
                              birth_transforms: Dict[str, str]) -> Dict[str, PalaceData]:
        """构建完整的宫位数据"""
        palaces_data = {}

        branch_to_palace = {}
        for palace_name, branch_idx in natal_palace_map.items():
            branch = EARTHLY_BRANCHES[branch_idx]
            branch_to_palace[branch] = palace_name

        for palace_name, branch_idx in natal_palace_map.items():
            branch = EARTHLY_BRANCHES[branch_idx]

            palace_stars = []
            for star, star_idx in main_stars.items():
                if star_idx == branch_idx:
                    palace_stars.append(star)

            palace_aux = []
            for star, star_idx in auxiliary_stars.items():
                if star_idx == branch_idx:
                    palace_aux.append(star)

            palace_evil = []
            for star, star_idx in evil_stars.items():
                if star_idx == branch_idx:
                    palace_evil.append(star)

            palaces_data[palace_name] = PalaceData(
                name=palace_name,
                branch=branch,
                stars=palace_stars,
                auxiliary_stars=palace_aux,
                evil_stars=palace_evil,
                misc_stars=[],
                meaning=get_palace_meaning(palace_name)
            )

        return {k: v.model_dump() for k, v in palaces_data.items()}

    def _calculate_big_fate_periods(self, ming_gong_idx: int, year: int,
                                     month: int, day: int,
                                     birth_time: datetime,
                                     gender: str) -> List[Dict]:
        """
        计算大限

        Args:
            ming_gong_idx: 命宫索引
            year: 出生年
            month: 出生月
            day: 出生日
            birth_time: 出生时间
            gender: 性别

        Returns:
            大限列表
        """
        big_fate_periods = []

        direction = 1 if gender == "male" else -1

        palace_indices = [(ming_gong_idx + i * direction) % 12 for i in range(12)]

        for i, start_age in enumerate(range(0, 120, 10)):
            end_age = start_age + 9

            palace_idx = palace_indices[i % 12]
            palace_name = TWELVE_PALACES[palace_idx]

            big_fate_periods.append({
                "index": i,
                "palace": palace_name,
                "start_age": start_age,
                "end_age": end_age,
                "direction": "顺行" if direction > 0 else "逆行"
            })

        return big_fate_periods

    def calculate_liu_nian(self, big_fate_idx: int, target_year: int,
                            ming_gong_idx: int, gender: str) -> Dict:
        """
        计算流年

        Args:
            big_fate_idx: 大限索引
            target_year: 目标年份
            ming_gong_idx: 命宫索引
            gender: 性别

        Returns:
            流年数据
        """
        direction = 1 if gender == "male" else -1

        year_branch_idx = (target_year - 1) % 12
        year_branch = EARTHLY_BRANCHES[year_branch_idx]

        liu_nian_idx = (ming_gong_idx + (target_year % 12) * direction) % 12
        liu_nian_palace = TWELVE_PALACES[liu_nian_idx]

        liu_nian_month_offset = (target_year % 12 + ming_gong_idx) % 12

        return {
            "year": target_year,
            "year_branch": year_branch,
            "liu_nian_palace": liu_nian_palace,
            "liu_nian_index": liu_nian_idx
        }
