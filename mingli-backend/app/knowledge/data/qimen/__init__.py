"""
奇门遁甲模块
收录奇门遁甲全书、八门、九星、八神等核心数据
"""

from .qimen_quanshu import QIMEN_QUANSHU_EXCERPTS
from .eight_doors import QIMEN_DOORS
from .nine_stars_qimen import QIMEN_STARS
from .eight_gods_qimen import QIMEN_SPIRITS

__all__ = [
    'QIMEN_QUANSHU_EXCERPTS',
    'QIMEN_DOORS',
    'QIMEN_STARS',
    'QIMEN_SPIRITS'
]
