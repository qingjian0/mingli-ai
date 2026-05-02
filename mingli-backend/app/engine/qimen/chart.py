"""
奇门遁甲排盘模块
核心排盘算法实现
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field

from ..base import BaseEngine, BaseChartData, ChartMetadata, BirthInfo, ChartType, EngineRegistry
from ..datetime_utils import (
    calculate_four_pillars, get_year_stem_branch, get_day_stem_branch,
    calculate_true_solar_time, get_current_solar_term,
    gregorian_to_julian_day, calculate_solar_term, SOLAR_TERMS, SOLAR_TERM_DEGREES
)
from .gong import TRIGRAMS, TRIGRAMS_NUMERIC, get_gong_by_number, get_gong_info
from .pan import (
    YinDun, EIGHT_DOORS, EIGHT_GODS, NINE_STARS_QIMEN,
    get_dun_type, get_door_info, get_god_info, get_star_info,
    calculate_yuan, calculate_start_gong, START_DOOR_BY_DUN, START_STAR_BY_YUAN, START_GOD_BY_DUN
)


class GongData(BaseModel):
    """宫位数据"""
    position: int = Field(description="宫位数字")
    name: str = Field(description="宫位名称")
    trigram: str = Field(description="卦象")
    element: str = Field(description="五行")
    direction: str = Field(description="方位")
    door: Optional[str] = Field(default=None, description="八门")
    star: Optional[str] = Field(default=None, description="九星")
    god: Optional[str] = Field(default=None, description="八神")
    stem: Optional[str] = Field(default=None, description="天干")
    branch: Optional[str] = Field(default=None, description="地支")
    rest_location: Optional[int] = Field(default=None, description="伏吟/反吟位置")


class QimenChartData(BaseChartData):
    """奇门遁甲命盘数据"""
    pass


@EngineRegistry.register(ChartType.QIMEN)
class QimenEngine(BaseEngine):
    """奇门遁甲排盘引擎"""

    chart_type = ChartType.QIMEN

    YIN_DUN_WINTER_SOLSTICE = 11
    YANG_DUN_SUMMER_SOLSTICE = 5

    def validate_input(self, birth_info: BirthInfo) -> bool:
        """验证输入"""
        if birth_info.birth_time.year < 1900 or birth_info.birth_time.year > 2100:
            return False
        return True

    def calculate(self, birth_info: BirthInfo) -> QimenChartData:
        """执行奇门遁甲排盘"""
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
        day_stem = four_pillars["day"]["stem"]
        day_branch = four_pillars["day"]["branch"]
        hour_stem = four_pillars["hour"]["stem"]

        solar_term_info = get_current_solar_term(birth_time)
        current_term = solar_term_info[0]

        dun_type = get_dun_type(current_term)

        term_date = solar_term_info[1]
        term_jd = gregorian_to_julian_day(term_date.year, term_date.month, term_date.day)
        birth_jd = gregorian_to_julian_day(year, month, day)

        yuan = self._calculate_yuan(birth_jd, term_jd, dun_type)

        start_gong = self._calculate_start_gong(yuan, dun_type)

        hour_ke = self._calculate_hour_ke(hour)

        palace_data = self._build_palace(
            start_gong, yuan, dun_type, hour_ke,
            day_stem, day_branch, hour_stem
        )

        metadata = self._create_metadata(birth_info)

        data = {
            "four_pillars": four_pillars,
            "dun_type": dun_type.value,
            "yuan": yuan,
            "start_gong": start_gong,
            "solar_term": {
                "name": solar_term_info[0],
                "date": solar_term_info[1].isoformat()
            },
            "palaces": palace_data,
            "men_pa": self._get_men_pa(yuan, dun_type),
            "xun_shou": self._get_xun_shou(yuan)
        }

        return QimenChartData(metadata=metadata, data=data)

    def _calculate_yuan(self, birth_jd: float, term_jd: float, dun_type: YinDun) -> int:
        """计算上中下元"""
        days_diff = int(birth_jd - term_jd)

        if dun_type == YinDun.YANG:
            yuans = {0: 1, 5: 2, 10: 3}
            for offset, yuan in yuans.items():
                if days_diff >= offset:
                    current_yuan = yuan
            current_yuan = ((days_diff // 5) % 3) + 1
        else:
            yuans = {0: 1, 5: 2, 10: 3}
            current_yuan = ((days_diff // 5) % 3) + 1

        return current_yuan

    def _calculate_start_gong(self, yuan: int, dun_type: YinDun) -> int:
        """计算起宫"""
        if dun_type == YinDun.YANG:
            base_gongs = {1: 1, 2: 4, 3: 7}
        else:
            base_gongs = {1: 9, 2: 6, 3: 3}
        return base_gongs.get(yuan, 1)

    def _calculate_hour_ke(self, hour: int) -> int:
        """计算时干入宫"""
        hour_ke_map = {
            23: 1, 0: 1, 1: 2, 2: 2, 3: 3, 4: 3,
            5: 4, 6: 4, 7: 5, 8: 5, 9: 6, 10: 6,
            11: 7, 12: 7, 13: 8, 14: 8, 15: 9, 16: 9,
            17: 1, 18: 1, 19: 2, 20: 2, 21: 3, 22: 3
        }
        return hour_ke_map.get(hour, 1)

    def _get_men_pa(self, yuan: int, dun_type: YinDun) -> str:
        """获取门迫"""
        if yuan == 1:
            return "伤门迫宫"
        elif yuan == 2:
            return "杜门迫宫"
        else:
            return "景门迫宫"

    def _get_xun_shou(self, yuan: int) -> str:
        """获取旬首"""
        xun_shou_map = {
            1: "甲子", 2: "甲寅", 3: "甲辰",
            4: "甲午", 5: "甲申", 6: "甲戌"
        }
        return xun_shou_map.get(((yuan - 1) % 6) + 1, "甲子")

    def _build_palace(self, start_gong: int, yuan: int, dun_type: YinDun,
                       hour_ke: int, day_stem: str, day_branch: str,
                       hour_stem: str) -> Dict[str, GongData]:
        """构建九宫数据"""
        palaces = {}

        if dun_type == YinDun.YANG:
            door_sequence = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
            star_sequence = ["蓬", "任", "冲", "辅", "英", "芮", "柱", "心"]
            gong_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            door_sequence = ["休", "惊", "开", "生", "伤", "杜", "景", "死"]
            star_sequence = ["蓬", "心", "柱", "任", "英", "芮", "冲", "辅"]
            gong_order = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        for i, pos in enumerate(gong_order):
            if pos == 5:
                continue

            door_idx = (i + start_gong - 1) % 8
            star_idx = (i + start_gong - 1) % 8

            gong_name = get_gong_by_number(pos)
            gong_info = get_gong_info(gong_name)

            palaces[pos] = GongData(
                position=pos,
                name=gong_name,
                trigram=gong_info.get("trigram", ""),
                element=gong_info.get("element", "").value if gong_info.get("element") else "",
                direction=gong_info.get("direction", ""),
                door=f"{door_sequence[door_idx]}门",
                star=f"天{star_sequence[star_idx]}星",
                god=""
            )

        palaces[5] = GongData(
            position=5,
            name="中五宫",
            trigram="寄坤",
            element="土",
            direction="中",
            door="死门" if dun_type == YinDun.YANG else "景门",
            star="天禽星",
            god=""
        )

        gods = ["值符", "螣蛇", "太阴", "白虎", "玄武", "九地", "九天", "六合"]
        god_start = 1 if dun_type == YinDun.YANG else 8

        for i, pos in enumerate([1, 8, 3, 4, 6, 2, 9, 7]):
            if pos == 5:
                continue
            if pos in palaces:
                god_idx = (god_start - 1 + i) % 8
                palaces[pos].god = gods[god_idx]

        self._place_stems_and_branches(palaces, day_stem, hour_stem, dun_type)

        return {k: v.model_dump() for k, v in palaces.items()}

    def _place_stems_and_branches(self, palaces: Dict[str, GongData],
                                    day_stem: str, hour_stem: str,
                                    dun_type: YinDun) -> None:
        """排布天干地支"""
        stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

        day_stem_idx = stems.index(day_stem) if day_stem in stems else 0
        hour_stem_idx = stems.index(hour_stem) if hour_stem in stems else 0

        start_stem_idx = day_stem_idx

        gong_order = [1, 8, 3, 4, 6, 2, 9, 7]
        for i, pos in enumerate(gong_order):
            if pos in palaces:
                stem_idx = (start_stem_idx + i) % 10
                palaces[pos].stem = stems[stem_idx]

        palaces[5].stem = "己"

    def calculate_zi_jia(self, target_jd: float, start_jd: float) -> int:
        """
        计算符首（甲子旬）

        Args:
            target_jd: 目标儒略日
            start_jd: 起局儒略日

        Returns:
            符首数（1-6）
        """
        days_diff = int(target_jd - start_jd)
        return (days_diff % 60) // 10 + 1
