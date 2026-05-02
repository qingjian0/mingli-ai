"""
十二宫位模块
紫微斗数十二宫的名称和含义
"""

from typing import Dict, List
from enum import Enum


class PalaceType(str, Enum):
    """宫位类型"""
    PERSONAL = "personal"      # 本宫
    COMBINED = "combined"     # 组合宫
    TRANSIT = "transit"        # 流年宫


TWELVE_PALACES = [
    "命宫", "兄弟宫", "夫妻宫", "子女宫",
    "财帛宫", "疾厄宫", "迁移宫", "奴仆宫",
    "官禄宫", "田宅宫", "福德宫", "父母宫"
]

PALACE_ORDER = {name: idx for idx, name in enumerate(TWELVE_PALACES)}

PALACE_MEANINGS = {
    "命宫": "先天运势、性格特点、生命本源",
    "兄弟宫": "兄弟姐妹、同辈朋友、合伙关系",
    "夫妻宫": "婚姻感情、配偶情况、恋爱经历",
    "子女宫": "子女缘分、桃花运势、创造力",
    "财帛宫": "财运收入、理财能力、物质生活",
    "疾厄宫": "健康状况、意外灾厄、疾病类型",
    "迁移宫": "外出发展、旅行运势、人际关系",
    "奴仆宫": "下属员工、朋友关系、晚辈子女",
    "官禄宫": "事业运势、学历功名、领导能力",
    "田宅宫": "房产物业、家庭环境、祖业积累",
    "福德宫": "精神修养、福气因果、兴趣爱好",
    "父母宫": "父母缘分、学历背景、头顶疾病"
}

PALACE_RELATIONS = {
    "命宫": {"对立": "迁移宫", "相邻": ["兄弟宫", "夫妻宫"]},
    "兄弟宫": {"对立": "奴仆宫", "相邻": ["命宫", "子女宫"]},
    "夫妻宫": {"对立": "官禄宫", "相邻": ["命宫", "子女宫"]},
    "子女宫": {"对立": "田宅宫", "相邻": ["兄弟宫", "财帛宫"]},
    "财帛宫": {"对立": "疾厄宫", "相邻": ["子女宫", "疾厄宫"]},
    "疾厄宫": {"对立": "财帛宫", "相邻": ["财帛宫", "迁移宫"]},
    "迁移宫": {"对立": "命宫", "相邻": ["疾厄宫", "奴仆宫"]},
    "奴仆宫": {"对立": "兄弟宫", "相邻": ["迁移宫", "官禄宫"]},
    "官禄宫": {"对立": "夫妻宫", "相邻": ["奴仆宫", "田宅宫"]},
    "田宅宫": {"对立": "子女宫", "相邻": ["官禄宫", "福德宫"]},
    "福德宫": {"对立": "父母宫", "相邻": ["田宅宫", "父母宫"]},
    "父母宫": {"对立": "福德宫", "相邻": ["福德宫", "命宫"]}
}

BRANCH_TO_PALACE_OFFSET = {
    "子": 0,   # 命宫在子
    "丑": 0,   # 命宫在丑
    "寅": 0,   # 命宫在寅
    "卯": 0,   # 命宫在卯
    "辰": 0,   # 命宫在辰
    "巳": 0,   # 命宫在巳
    "午": 0,   # 命宫在午
    "未": 0,   # 命宫在未
    "申": 0,   # 命宫在申
    "酉": 0,   # 命宫在酉
    "戌": 0,   # 命宫在戌
    "亥": 0    # 命宫在亥
}

YINYANG_PALACE = {
    "阳男阴女": ["命宫", "财帛宫", "迁移宫", "官禄宫"],
    "阴男阳女": ["命宫", "财帛宫", "迁移宫", "官禄宫"]
}


def get_palace_index(palace: str) -> int:
    """获取宫位索引"""
    return PALACE_ORDER[palace]


def get_palace_meaning(palace: str) -> str:
    """获取宫位含义"""
    return PALACE_MEANINGS.get(palace, "")


def get_palace_relation(palace: str) -> Dict:
    """获取宫位关系"""
    return PALACE_RELATIONS.get(palace, {})


def calculate_ming_gong(month_branch: str, hour_branch: str, gender: str) -> int:
    """
    计算命宫索引（基于钦天门法）

    Args:
        month_branch: 月支
        hour_branch: 时支
        gender: 性别

    Returns:
        命宫索引
    """
    month_map = {
        "寅": 0, "卯": 1, "辰": 2, "巳": 3,
        "午": 4, "未": 5, "申": 6, "酉": 7,
        "戌": 8, "亥": 9, "子": 10, "丑": 11
    }

    month_idx = month_map.get(month_branch, 0)
    hour_idx = month_map.get(hour_branch, 0)

    ming_gong_idx = (month_idx + hour_idx) % 12

    if gender == "male":
        ming_gong_idx = (ming_gong_idx + 6) % 12
    else:
        ming_gong_idx = (12 - ming_gong_idx) % 12

    return ming_gong_idx


def calculate_sheng_gong(month_branch: str) -> int:
    """
    计算身宫索引

    Args:
        month_branch: 月支

    Returns:
        身宫索引
    """
    month_map = {
        "寅": 2, "卯": 3, "辰": 4, "巳": 5,
        "午": 6, "未": 7, "申": 8, "酉": 9,
        "戌": 10, "亥": 11, "子": 0, "丑": 1
    }
    return month_map.get(month_branch, 0)


def get_all_palaces() -> List[str]:
    """获取所有宫位名称"""
    return TWELVE_PALACES.copy()


def get_opposite_palace(palace: str) -> str:
    """获取对宫"""
    idx = get_palace_index(palace)
    opposite_idx = (idx + 6) % 12
    return TWELVE_PALACES[opposite_idx]
