"""
小成图知识库
源自《易经》后天应用体系

小成图是一种简易占卜方法，以易经六十四卦为基础，
通过简单的起卦方式快速得出卦象进行占断分析。
"""

from .xiaocheng_tu import (
    XIAOCHENG_INTRO,
    XIAOCHENG_BAGUA,
    GUILAI_PRINCIPLES,
    QIGUA_METHODS,
    XIAOCHENG_INTERPRETATION_RULES,
    HEXAGRAM_POSITIONS,
)

__all__ = [
    'XIAOCHENG_INTRO',
    'XIAOCHENG_BAGUA',
    'GUILAI_PRINCIPLES',
    'QIGUA_METHODS',
    'XIAOCHENG_INTERPRETATION_RULES',
    'HEXAGRAM_POSITIONS',
]
