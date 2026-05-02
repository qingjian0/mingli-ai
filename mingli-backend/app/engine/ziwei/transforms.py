"""
四化计算模块
生年四化、大限四化、流年四化的计算
"""

from typing import Dict, List, Tuple
from enum import Enum


class TransformType(str, Enum):
    """四化类型"""
    LU = "禄"   # 化禄
    QUAN = "权" # 化权
    KE = "科"   # 化科
    HAI = "忌"  # 化忌


STAR_TRANSFORMS = {
    "紫微": {"禄": "权", "权": "科", "科": "禄", "忌": "忌"},
    "天机": {"禄": "忌", "权": "禄", "科": "权", "忌": "科"},
    "太阳": {"禄": "权", "权": "科", "科": "忌", "忌": "禄"},
    "武曲": {"禄": "权", "权": "忌", "科": "禄", "忌": "科"},
    "天同": {"禄": "权", "权": "科", "科": "忌", "忌": "禄"},
    "廉贞": {"禄": "忌", "权": "禄", "科": "权", "忌": "科"},
    "天府": {"禄": "科", "权": "禄", "科": "权", "忌": "忌"},
    "太阴": {"禄": "忌", "权": "科", "科": "权", "忌": "禄"},
    "贪狼": {"禄": "忌", "权": "禄", "科": "科", "忌": "权"},
    "巨门": {"禄": "权", "权": "忌", "科": "禄", "忌": "科"},
    "天相": {"禄": "科", "权": "权", "科": "忌", "忌": "禄"},
    "天梁": {"禄": "科", "权": "权", "科": "禄", "忌": "忌"},
    "七杀": {"禄": "权", "权": "忌", "科": "科", "忌": "禄"},
    "破军": {"禄": "权", "权": "科", "科": "忌", "忌": "禄"}
}

TRANSFORM_MEANINGS = {
    "禄": "财禄、缘分、福气、享受",
    "权": "权力、欲望、争执、变化",
    "科": "科名、声誉、文采、智慧",
    "忌": "执念、阻碍、伤害、消耗"
}

YEAR_STEM_TRANSFORM = {
    "甲": "廉贞化禄、破军化权、武曲化科、太阳化忌",
    "乙": "天机化禄、天梁化权、紫微化科、太阴化忌",
    "丙": "天同化禄、天机化权、文昌化科、廉贞化忌",
    "丁": "太阳化禄、天机化权、天同化科、巨门化忌",
    "戊": "贪狼化禄、太阴化权、天府化科、武曲化忌",
    "己": "武曲化禄、贪狼化权、天梁化科、巨门化忌",
    "庚": "太阳化禄、天同化权、文曲化科、廉贞化忌",
    "辛": "巨门化禄、太阳化权、天机化科、贪狼化忌",
    "壬": "天梁化禄、紫微化权、文曲化科、贪狼化忌",
    "癸": "破军化禄、巨门化权、天机化科、贪狼化忌"
}


def get_birth_year_transform(year_stem: str) -> Dict[str, str]:
    """
    获取生年四化

    Args:
        year_stem: 年干

    Returns:
        {星曜: 化什么}
    """
    transform_str = YEAR_STEM_TRANSFORM.get(year_stem, "")

    if not transform_str:
        return {}

    result = {}
    parts = transform_str.split("、")
    for part in parts:
        if "化" in part:
            star, transform = part.split("化")
            result[star] = transform

    return result


def get_star_transform(star: str, original_transform: str) -> str:
    """
    获取星曜在某四化作用下的变化

    Args:
        star: 星曜
        original_transform: 原始四化（禄/权/科/忌）

    Returns:
        化后的结果
    """
    star_transforms = STAR_TRANSFORMS.get(star, {})
    return star_transforms.get(original_transform, "")


def calculate_transform_effect(transform: str, star: str) -> Dict[str, any]:
    """
    计算四化效果

    Args:
        transform: 四化类型
        star: 星曜

    Returns:
        效果描述
    """
    meaning = TRANSFORM_MEANINGS.get(transform, "")

    effect_map = {
        "禄": {
            "性质": "吉利",
            "描述": f"化禄代表财运、桃花、福气，与{star}结合增强其吉利性质"
        },
        "权": {
            "性质": "变动",
            "描述": f"化权代表权力、欲望、争执，与{star}结合增加其强势和变化"
        },
        "科": {
            "性质": "文雅",
            "描述": f"化科代表名声、才华、科名，与{star}结合增强其文雅性质"
        },
        "忌": {
            "性质": "凶险",
            "描述": f"化忌代表阻碍、执念、消耗，与{star}结合需要特别注意"
        }
    }

    return effect_map.get(transform, {"性质": "未知", "描述": ""})


def apply_transform_to_stars(stars: List[str], transforms: Dict[str, str]) -> Dict[str, str]:
    """
    将四化应用到星曜列表

    Args:
        stars: 星曜列表
        transforms: 四化字典 {星曜: 四化类型}

    Returns:
        转换后的结果 {星曜: 化后结果}
    """
    result = {}

    for star in stars:
        if star in transforms:
            original = transforms[star]
            transformed = get_star_transform(star, original)
            if transformed:
                result[f"{star}化{transformed}"] = original
            result[star] = original
        else:
            result[star] = ""

    return result


def parse_transform_string(transform_str: str) -> List[Tuple[str, str]]:
    """
    解析四化字符串

    Args:
        transform_str: "廉贞化禄、破军化权..."

    Returns:
        [(星曜, 四化类型), ...]
    """
    result = []

    if not transform_str:
        return result

    parts = transform_str.split("、")
    for part in parts:
        if "化" in part:
            star, transform = part.split("化")
            result.append((star, transform))

    return result


def get_transform_interaction(transform1: str, transform2: str) -> str:
    """
    判断两个四化的相互作用

    Args:
        transform1: 四化1
        transform2: 四化2

    Returns:
        相互作用描述
    """
    if transform1 == transform2:
        return "同气相求，增强力量"

    interactions = {
        ("禄", "权"): "禄权相会，财权双收",
        ("禄", "科"): "禄科同度，名利双全",
        ("禄", "忌"): "禄忌相冲，吉凶参半",
        ("权", "科"): "权科相会，权威与学识并重",
        ("权", "忌"): "权忌相冲，变动较大",
        ("科", "忌"): "科忌相会，文墨之事需注意"
    }

    key = tuple(sorted([transform1, transform2]))
    return interactions.get(key, "")
