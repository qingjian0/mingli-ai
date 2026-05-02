"""
奇门遁甲排盘模块
奇门遁甲核心算法
"""

from .gong import (
    TRIGRAMS,
    TRIGRAMS_REVERSED,
    TRIGRAMS_NUMERIC,
    TRIGRAMS_POSITIONS,
    GUA_TRIGRAMS,
    get_gong_info,
    get_gong_by_number,
    get_gong_by_trigram,
    get_gong_element,
    get_gong_direction,
    get_trigram_info,
    calculate_wu_xing_number,
    get_sheng_gong,
    get_ke_gong,
    Element as GongElement
)

from .pan import (
    YinDun,
    EIGHT_DOORS,
    EIGHT_GODS,
    NINE_STARS_QIMEN,
    GONG_KAI_FANG,
    START_DOOR_BY_DUN,
    START_STAR_BY_YUAN,
    START_GOD_BY_DUN,
    get_dun_type,
    get_door_info,
    get_god_info,
    get_star_info,
    calculate_yuan,
    calculate_start_gong,
    calculate_door_position
)

from .chart import (
    QimenEngine,
    QimenChartData,
    GongData
)

__all__ = [
    "TRIGRAMS",
    "TRIGRAMS_REVERSED",
    "TRIGRAMS_NUMERIC",
    "TRIGRAMS_POSITIONS",
    "GUA_TRIGRAMS",
    "get_gong_info",
    "get_gong_by_number",
    "get_gong_by_trigram",
    "get_gong_element",
    "get_gong_direction",
    "get_trigram_info",
    "calculate_wu_xing_number",
    "get_sheng_gong",
    "get_ke_gong",
    "GongElement",
    "YinDun",
    "EIGHT_DOORS",
    "EIGHT_GODS",
    "NINE_STARS_QIMEN",
    "GONG_KAI_FANG",
    "START_DOOR_BY_DUN",
    "START_STAR_BY_YUAN",
    "START_GOD_BY_DUN",
    "get_dun_type",
    "get_door_info",
    "get_god_info",
    "get_star_info",
    "calculate_yuan",
    "calculate_start_gong",
    "calculate_door_position",
    "QimenEngine",
    "QimenChartData",
    "GongData"
]
