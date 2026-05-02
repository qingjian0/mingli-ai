"""
地支模块
定义十二地支的属性、地支藏干和相互关系
"""

from enum import Enum
from typing import Dict, List, Set, Tuple
from .stems import Element, STEM_INDICES


BRANCH_INDICES: Dict[str, int] = {
    "子": 0, "丑": 1, "寅": 2, "卯": 3, "辰": 4, "巳": 5,
    "午": 6, "未": 7, "申": 8, "酉": 9, "戌": 10, "亥": 11
}

BRANCH_ORDER = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

BRANCH_ELEMENTS: Dict[str, Element] = {
    "子": Element.WATER, "丑": Element.EARTH, "寅": Element.WOOD, "卯": Element.WOOD,
    "辰": Element.EARTH, "巳": Element.FIRE, "午": Element.FIRE, "未": Element.EARTH,
    "申": Element.METAL, "酉": Element.METAL, "戌": Element.EARTH, "亥": Element.WATER
}

BRANCH_YINYANG: Dict[str, str] = {
    "子": "阳", "丑": "阴", "寅": "阳", "卯": "阴",
    "辰": "阳", "巳": "阴", "午": "阳", "未": "阴",
    "申": "阳", "酉": "阴", "戌": "阳", "亥": "阴"
}

BRANCH_HIDDEN_STEMS: Dict[str, List[Tuple[str, float]]] = {
    "子": [("癸", 1.0)],
    "丑": [("己", 0.6), ("癸", 0.3), ("辛", 0.1)],
    "寅": [("甲", 0.7), ("丙", 0.2), ("戊", 0.1)],
    "卯": [("乙", 1.0)],
    "辰": [("戊", 0.6), ("乙", 0.3), ("癸", 0.1)],
    "巳": [("丙", 0.7), ("庚", 0.2), ("戊", 0.1)],
    "午": [("丁", 0.7), ("己", 0.3)],
    "未": [("己", 0.6), ("丁", 0.3), ("乙", 0.1)],
    "申": [("庚", 0.7), ("壬", 0.2), ("戊", 0.1)],
    "酉": [("辛", 1.0)],
    "戌": [("戊", 0.6), ("辛", 0.3), ("丁", 0.1)],
    "亥": [("壬", 0.7), ("甲", 0.3)]
}

BRANCH_SEASON: Dict[str, str] = {
    "寅": "春", "卯": "春", "辰": "春",
    "巳": "夏", "午": "夏", "未": "夏",
    "申": "秋", "酉": "秋", "戌": "秋",
    "亥": "冬", "子": "冬", "丑": "冬"
}

BRANCH_ANIMALS: Dict[str, str] = {
    "子": "鼠", "丑": "牛", "寅": "虎", "卯": "兔",
    "辰": "龙", "巳": "蛇", "午": "马", "未": "羊",
    "申": "猴", "酉": "鸡", "戌": "狗", "亥": "猪"
}

BRANCH_HOUR_MAP: Dict[str, str] = {
    "子": "23:00-01:00", "丑": "01:00-03:00", "寅": "03:00-05:00",
    "卯": "05:00-07:00", "辰": "07:00-09:00", "巳": "09:00-11:00",
    "午": "11:00-13:00", "未": "13:00-15:00", "申": "15:00-17:00",
    "酉": "17:00-19:00", "戌": "19:00-21:00", "亥": "21:00-23:00"
}


def get_branch_index(branch: str) -> int:
    """获取地支索引"""
    return BRANCH_INDICES[branch]

def get_branch_element(branch: str) -> Element:
    """获取地支五行"""
    return BRANCH_ELEMENTS[branch]

def get_branch_hidden_stems(branch: str) -> List[Tuple[str, float]]:
    """获取地支藏干及权重"""
    return BRANCH_HIDDEN_STEMS[branch]

def get_branch_yinyang(branch: str) -> str:
    """获取地支阴阳"""
    return BRANCH_YINYANG[branch]

def branches_generate(cycle_start: str = "子", count: int = 12) -> List[str]:
    """生成地支序列"""
    start_idx = BRANCH_INDICES[cycle_start]
    return [BRANCH_ORDER[(start_idx + i) % 12] for i in range(count)]

def get_next_branch(branch: str, step: int = 1) -> str:
    """获取下一个地支（顺时针）"""
    current_idx = BRANCH_INDICES[branch]
    next_idx = (current_idx + step) % 12
    return BRANCH_ORDER[next_idx]

def get_prev_branch(branch: str, step: int = 1) -> str:
    """获取上一个地支（逆时针）"""
    current_idx = BRANCH_INDICES[branch]
    prev_idx = (current_idx - step) % 12
    return BRANCH_ORDER[prev_idx]
