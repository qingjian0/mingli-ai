"""
排盘引擎模块
明理AI命理平台核心排盘引擎
"""

from .base import (
    BaseEngine,
    BaseChartData,
    ChartMetadata,
    BirthInfo,
    ChartType,
    Gender,
    Location,
    EngineRegistry,
    export_chart
)

from .datetime_utils import (
    calculate_four_pillars,
    get_year_stem_branch,
    get_month_stem_branch,
    get_day_stem_branch,
    get_hour_stem_branch,
    calculate_true_solar_time,
    get_current_solar_term,
    gregorian_to_julian_day,
    calculate_solar_term,
    SOLAR_TERMS,
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES
)

from .rating_system import (
    RatingDimension,
    RatingLevel,
    SystemRating,
    RatingSystem
)

from .new_systems import *

__version__ = "2.0.0"
__all__ = [
    "BaseEngine",
    "BaseChartData",
    "ChartMetadata",
    "BirthInfo",
    "ChartType",
    "Gender",
    "Location",
    "EngineRegistry",
    "export_chart",
    "calculate_four_pillars",
    "get_year_stem_branch",
    "get_month_stem_branch",
    "get_day_stem_branch",
    "get_hour_stem_branch",
    "calculate_true_solar_time",
    "get_current_solar_term",
    "gregorian_to_julian_day",
    "calculate_solar_term",
    "SOLAR_TERMS",
    "HEAVENLY_STEMS",
    "EARTHLY_BRANCHES",
    "RatingDimension",
    "RatingLevel",
    "SystemRating",
    "RatingSystem"
]
