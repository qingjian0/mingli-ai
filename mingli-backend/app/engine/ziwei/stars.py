"""
星曜定义模块
紫微斗数十四主星及辅星的定义
"""

from enum import Enum
from typing import Dict, List, Optional, Set


class StarCategory(str, Enum):
    """星曜类别"""
    MAIN = "main"           # 十四主星
    AUXILIARY = "auxiliary" # 辅星
    EVIL = "evil"           # 煞星
    MISC = "misc"           # 杂曜


class StarNature(str, Enum):
    """星曜性质"""
    YANG = "阳"
    YIN = "阴"
    NEUTRAL = "中"


MAIN_STARS = [
    "紫微", "天机", "太阳", "武曲", "天同", "廉贞",
    "天府", "太阴", "贪狼", "巨门", "天相", "天梁",
    "七杀", "破军"
]

STAR_ATTRS = {
    "紫微": {"nature": "阴", "element": "土", "category": "main",
             "desc": "帝王星，众星枢纽，掌生杀之权"},
    "天机": {"nature": "阴", "element": "木", "category": "main",
             "desc": "智慧星，机动善变，司谋略"},
    "太阳": {"nature": "阳", "element": "火", "category": "main",
             "desc": "光明星，日出有功，司贵显"},
    "武曲": {"nature": "阳", "element": "金", "category": "main",
             "desc": "财星，刚毅果断，司财权"},
    "天同": {"nature": "阳", "element": "水", "category": "main",
             "desc": "福星，温顺平和，司福禄"},
    "廉贞": {"nature": "阴", "element": "火", "category": "main",
             "desc": "囚星，情感复杂，司是非"},
    "天府": {"nature": "阳", "element": "土", "category": "main",
             "desc": "南斗主星，保守稳重，司财库"},
    "太阴": {"nature": "阴", "element": "水", "category": "main",
             "desc": "月亮，温柔细腻，司财福"},
    "贪狼": {"nature": "阳", "element": "木", "category": "main",
             "desc": "欲望星，多才多艺，司桃花"},
    "巨门": {"nature": "阴", "element": "土", "category": "main",
             "desc": "暗星，口才出众，司是非"},
    "天相": {"nature": "阳", "element": "水", "category": "main",
             "desc": "印星，辅佐之星，司权柄"},
    "天梁": {"nature": "阳", "element": "土", "category": "main",
             "desc": "蔭星，逢凶化吉，司寿"},
    "七杀": {"nature": "阳", "element": "金", "category": "main",
             "desc": "将星，威猛刚烈，司杀伐"},
    "破军": {"nature": "阳", "element": "水", "category": "main",
             "desc": "耗星，破坏建设，司成败"}
}

AUXILIARY_STARS = [
    "左辅", "右弼", "文昌", "文曲", "天魁", "天钺",
    "科甲权", "青龙", "白虎", "朱雀", "玄武"
]

EVIL_STARS = [
    "擎羊", "陀罗", "火星", "铃星", "地空", "地劫"
]

MISC_STARS = [
    "天姚", "红鸾", "天喜", "天刑", "天德", "月德",
    "三台", "八座", "恩光", "天贵", "天官", "天福",
    "天伤", "天使", "龙池", "凤阁", "天马", "解神"
]

STAR_POSITIONS_BASIS = {
    "紫微": "午宫",
    "天机": "丑宫",
    "太阳": "未宫",
    "武曲": "辰宫",
    "天同": "戌宫",
    "廉贞": "寅宫",
    "天府": "卯宫",
    "太阴": "酉宫",
    "贪狼": "子宫",
    "巨门": "丑宫",
    "天相": "丑宫",
    "天梁": "卯宫",
    "七杀": "午宫",
    "破军": "子宫"
}


def get_star_attrs(star: str) -> Dict:
    """获取星曜属性"""
    if star in STAR_ATTRS:
        return STAR_ATTRS[star]
    return {"desc": star, "category": "unknown"}


def is_main_star(star: str) -> bool:
    """判断是否十四主星"""
    return star in MAIN_STARS


def is_evil_star(star: str) -> bool:
    """判断是否煞星"""
    return star in EVIL_STARS


def get_star_category(star: str) -> StarCategory:
    """获取星曜类别"""
    if star in MAIN_STARS:
        return StarCategory.MAIN
    elif star in AUXILIARY_STARS:
        return StarCategory.AUXILIARY
    elif star in EVIL_STARS:
        return StarCategory.EVIL
    elif star in MISC_STARS:
        return StarCategory.MISC
    return StarCategory.MISC


def get_star_element(star: str) -> str:
    """获取星曜五行"""
    attrs = get_star_attrs(star)
    return attrs.get("element", "土")


def get_star_nature(star: str) -> str:
    """获取星曜阴阳"""
    attrs = get_star_attrs(star)
    return attrs.get("nature", "中")
