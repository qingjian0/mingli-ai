"""
紫微斗数全书
收录《紫微斗数全书》核心章节原文及注释
"""

from .ziwei_star_meanings import ZIWEI_STARS, ASSISTANT_STARS
from .palace_meanings import ZIWEI_PALACES
from .transform_meanings import ZIWEI_TRANSFORMS
from .pattern_collection import ZIWEI_PATTERNS
from .ziwei_doushu_quanshu import ZIWEI_QUANSHU_EXCERPTS, ZIWEI_RULES
from .auxiliary_stars import AUXILIARY_STARS, SINFUL_STARS, MISC_STARS

__all__ = [
    'ZIWEI_STARS',
    'ASSISTANT_STARS',
    'ZIWEI_PALACES',
    'ZIWEI_TRANSFORMS',
    'ZIWEI_PATTERNS',
    'ZIWEI_QUANSHU_EXCERPTS',
    'ZIWEI_RULES',
    'AUXILIARY_STARS',
    'SINFUL_STARS',
    'MISC_STARS'
]
