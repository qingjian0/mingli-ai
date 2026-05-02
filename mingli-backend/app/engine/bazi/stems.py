"""
天干模块
定义十天干的属性和相互关系
"""

from enum import Enum
from typing import Dict, List, Set


class Element(str, Enum):
    """五行元素"""
    WOOD = "木"
    FIRE = "火"
    EARTH = "土"
    METAL = "金"
    WATER = "水"


class Yinyang(str, Enum):
    """阴阳"""
    YANG = "阳"
    YIN = "阴"


STEM_ELEMENTS: Dict[str, Element] = {
    "甲": Element.WOOD, "乙": Element.WOOD,
    "丙": Element.FIRE, "丁": Element.FIRE,
    "戊": Element.EARTH, "己": Element.EARTH,
    "庚": Element.METAL, "辛": Element.METAL,
    "壬": Element.WATER, "癸": Element.WATER
}

STEM_YINYANG: Dict[str, Yinyang] = {
    "甲": Yinyang.YANG, "乙": Yinyang.YIN,
    "丙": Yinyang.YANG, "丁": Yinyang.YIN,
    "戊": Yinyang.YANG, "己": Yinyang.YIN,
    "庚": Yinyang.YANG, "辛": Yinyang.YIN,
    "壬": Yinyang.YANG, "癸": Yinyang.YIN
}

STEM_INDICES: Dict[str, int] = {
    "甲": 0, "乙": 1, "丙": 2, "丁": 3, "戊": 4,
    "己": 5, "庚": 6, "辛": 7, "壬": 8, "癸": 9
}

STEM_ORDER = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]


STEM_RELATIONS: Dict[str, List[str]] = {
    "甲": ["己", "丁"],
    "乙": ["戊", "丙"],
    "丙": ["辛", "癸"],
    "丁": ["庚", "壬"],
    "戊": ["癸", "乙"],
    "己": ["甲", "丁"],
    "庚": ["乙", "丁"],
    "辛": ["丙", "戊"],
    "壬": ["丁", "甲"],
    "癸": ["戊", "丙"]
}

def get_stem_element(stem: str) -> Element:
    """获取天干五行"""
    return STEM_ELEMENTS[stem]

def get_stem_yinyang(stem: str) -> Yinyang:
    """获取天干阴阳"""
    return STEM_YINYANG[stem]

def get_stem_index(stem: str) -> int:
    """获取天干索引"""
    return STEM_INDICES[stem]

def stems_generate(cycle_start: str = "甲", count: int = 10) -> List[str]:
    """生成天干序列"""
    start_idx = STEM_INDICES[cycle_start]
    return [STEM_ORDER[(start_idx + i) % 10] for i in range(count)]

def stems_combination(stem1: str, stem2: str) -> str:
    """天干五合"""
    combinations = {
        ("甲", "己"): "甲己合土",
        ("乙", "庚"): "乙庚合金",
        ("丙", "辛"): "丙辛合水",
        ("丁", "壬"): "丁壬合木",
        ("戊", "癸"): "戊癸合火"
    }
    return combinations.get((stem1, stem2), combinations.get((stem2, stem1), ""))

def stems_clash(stem1: str, stem2: str) -> bool:
    """天干相冲"""
    clashes = {
        ("甲", "庚"): True, ("乙", "辛"): True,
        ("丙", "壬"): True, ("丁", "癸"): True
    }
    return clashes.get((stem1, stem2), False)
