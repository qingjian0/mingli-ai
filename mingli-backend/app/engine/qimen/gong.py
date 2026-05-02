"""
九宫八卦模块
奇门遁甲九宫格的定义
"""

from enum import Enum
from typing import Dict, List, Tuple


class Element(str, Enum):
    """五行"""
    WOOD = "木"
    FIRE = "火"
    EARTH = "土"
    METAL = "金"
    WATER = "水"


TRIGRAMS = {
    "坎一宫": {"trigram": "坎", "number": 1, "element": Element.WATER, "direction": "北",
               "binary": "中男", "nature": "陷"},
    "坤二宫": {"trigram": "坤", "number": 2, "element": Element.EARTH, "direction": "西南",
               "binary": "老母", "nature": "顺"},
    "震三宫": {"trigram": "震", "number": 3, "element": Element.WOOD, "direction": "东",
               "binary": "长男", "nature": "动"},
    "巽四宫": {"trigram": "巽", "number": 4, "element": Element.WOOD, "direction": "东南",
               "binary": "长女", "nature": "入"},
    "中五宫": {"trigram": "中", "number": 5, "element": Element.EARTH, "direction": "中",
               "binary": "寄坤", "nature": "平"},
    "乾六宫": {"trigram": "乾", "number": 6, "element": Element.METAL, "direction": "西北",
               "binary": "老父", "nature": "健"},
    "兑七宫": {"trigram": "兑", "number": 7, "element": Element.METAL, "direction": "西",
               "binary": "少女", "nature": "悦"},
    "艮八宫": {"trigram": "艮", "number": 8, "element": Element.EARTH, "direction": "东北",
               "binary": "少男", "nature": "止"},
    "离九宫": {"trigram": "离", "number": 9, "element": Element.FIRE, "direction": "南",
               "binary": "中女", "nature": "丽"}
}

TRIGRAMS_REVERSED = {
    "坎": "坎一宫", "坤": "坤二宫", "震": "震三宫",
    "巽": "巽四宫", "乾": "乾六宫", "兑": "兑七宫",
    "艮": "艮八宫", "离": "离九宫"
}

TRIGRAMS_NUMERIC = {
    1: "坎一宫", 2: "坤二宫", 3: "震三宫",
    4: "巽四宫", 6: "乾六宫", 7: "兑七宫",
    8: "艮八宫", 9: "离九宫"
}

TRIGRAMS_POSITIONS = {
    "一宫": "北方", "二宫": "西南方", "三宫": "东方",
    "四宫": "东南方", "五宫": "中央", "六宫": "西北方",
    "七宫": "西方", "八宫": "东北方", "九宫": "南方"
}

GUA_TRIGRAMS = {
    "乾": {"属性": "金", "阴阳": "阳", "方位": "西北", "五行数": 4},
    "坤": {"属性": "土", "阴阳": "阴", "方位": "西南", "五行数": 5},
    "震": {"属性": "木", "阴阳": "阳", "方位": "东", "五行数": 3},
    "巽": {"属性": "木", "阴阳": "阴", "方位": "东南", "五行数": 3},
    "坎": {"属性": "水", "阴阳": "阳", "方位": "北", "五行数": 1},
    "离": {"属性": "火", "阴阳": "阴", "方位": "南", "五行数": 2},
    "艮": {"属性": "土", "阴阳": "阳", "方位": "东北", "五行数": 5},
    "兑": {"属性": "金", "阴阳": "阴", "方位": "西", "五行数": 4}
}


def get_gong_info(gong_name: str) -> Dict:
    """获取宫位信息"""
    return TRIGRAMS.get(gong_name, {})


def get_gong_by_number(num: int) -> str:
    """根据数字获取宫位"""
    if num == 5:
        return "中五宫"
    if num in TRIGRAMS_NUMERIC:
        return TRIGRAMS_NUMERIC[num]
    return ""


def get_gong_by_trigram(trigram: str) -> str:
    """根据卦名获取宫位"""
    return TRIGRAMS_REVERSED.get(trigram, "")


def get_gong_element(gong_name: str) -> Element:
    """获取宫位五行"""
    info = get_gong_info(gong_name)
    return info.get("element", Element.EARTH)


def get_gong_direction(gong_name: str) -> str:
    """获取宫位方向"""
    info = get_gong_info(gong_name)
    return info.get("direction", "")


def get_trigram_info(trigram: str) -> Dict:
    """获取卦象信息"""
    return GUA_TRIGRAMS.get(trigram, {})


def calculate_wu_xing_number(element: Element) -> int:
    """计算五行数"""
    if element == Element.WATER:
        return 1
    elif element == Element.FIRE:
        return 2
    elif element == Element.WOOD:
        return 3
    elif element == Element.METAL:
        return 4
    elif element == Element.EARTH:
        return 5
    return 5


def get_sheng_gong(current_gong: str, element: Element) -> List[str]:
    """获取生我的宫位"""
    if element == Element.WOOD:
        return ["坎一宫", "离九宫"]
    elif element == Element.FIRE:
        return ["巽四宫", "震三宫"]
    elif element == Element.EARTH:
        return ["坤二宫", "艮八宫"]
    elif element == Element.METAL:
        return ["乾六宫", "兑七宫"]
    elif element == Element.WATER:
        return ["坤二宫", "艮八宫"]
    return []


def get_ke_gong(current_gong: str, element: Element) -> List[str]:
    """获取我克的宫位"""
    if element == Element.WOOD:
        return ["坤二宫", "艮八宫"]
    elif element == Element.FIRE:
        return ["乾六宫", "兑七宫"]
    elif element == Element.EARTH:
        return ["坎一宫", "离九宫"]
    elif element == Element.METAL:
        return ["震三宫", "巽四宫"]
    elif element == Element.WATER:
        return ["离九宫"]
    return []
