"""
紫微斗数排盘模块
紫微斗数核心算法
"""

from .stars import (
    MAIN_STARS,
    AUXILIARY_STARS,
    EVIL_STARS,
    MISC_STARS,
    STAR_ATTRS,
    STAR_POSITIONS_BASIS,
    get_star_attrs,
    is_main_star,
    is_evil_star,
    get_star_category,
    get_star_element,
    get_star_nature,
    StarCategory,
    StarNature
)

from .palaces import (
    TWELVE_PALACES,
    PALACE_ORDER,
    PALACE_MEANINGS,
    PALACE_RELATIONS,
    get_palace_index,
    get_palace_meaning,
    get_palace_relation,
    calculate_ming_gong,
    calculate_sheng_gong,
    get_all_palaces,
    get_opposite_palace
)

from .transforms import (
    STAR_TRANSFORMS,
    TRANSFORM_MEANINGS,
    YEAR_STEM_TRANSFORM,
    get_birth_year_transform,
    get_star_transform,
    calculate_transform_effect,
    apply_transform_to_stars,
    parse_transform_string,
    get_transform_interaction,
    TransformType
)

from .chart import (
    ZiweiEngine,
    ZiweiChartData,
    PalaceData
)

__all__ = [
    "MAIN_STARS",
    "AUXILIARY_STARS",
    "EVIL_STARS",
    "MISC_STARS",
    "STAR_ATTRS",
    "STAR_POSITIONS_BASIS",
    "get_star_attrs",
    "is_main_star",
    "is_evil_star",
    "get_star_category",
    "get_star_element",
    "get_star_nature",
    "StarCategory",
    "StarNature",
    "TWELVE_PALACES",
    "PALACE_ORDER",
    "PALACE_MEANINGS",
    "PALACE_RELATIONS",
    "get_palace_index",
    "get_palace_meaning",
    "get_palace_relation",
    "calculate_ming_gong",
    "calculate_sheng_gong",
    "get_all_palaces",
    "get_opposite_palace",
    "STAR_TRANSFORMS",
    "TRANSFORM_MEANINGS",
    "YEAR_STEM_TRANSFORM",
    "get_birth_year_transform",
    "get_star_transform",
    "calculate_transform_effect",
    "apply_transform_to_stars",
    "parse_transform_string",
    "get_transform_interaction",
    "TransformType",
    "ZiweiEngine",
    "ZiweiChartData",
    "PalaceData"
]
