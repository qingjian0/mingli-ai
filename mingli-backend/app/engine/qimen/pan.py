"""
奇门遁甲盘模块
九宫八门八神的定义和排布逻辑
"""

from typing import Dict, List, Optional
from enum import Enum


class YinDun(str, Enum):
    """遁甲类型"""
    YANG = "阳遁"   # 阳遁（冬至到夏至）
    YIN = "阴遁"    # 阴遁（夏至到冬至）


EIGHT_DOORS = {
    "休门": {"性质": "吉", "五行": "水", "含义": "休养、生息、休息"},
    "生门": {"性质": "大吉", "五行": "土", "含义": "生长、生存、财运"},
    "伤门": {"性质": "凶", "五行": "木", "含义": "伤害、损伤、竞争"},
    "杜门": {"性质": "小凶", "五行": "木", "含义": "隐藏、阻隔、保密"},
    "景门": {"性质": "小吉", "五行": "火", "含义": "风景、显眼、表现"},
    "死门": {"性质": "大凶", "五行": "土", "含义": "死亡、结束、破财"},
    "惊门": {"性质": "凶", "五行": "金", "含义": "惊吓、口舌、诉讼"},
    "开门": {"性质": "大吉", "五行": "金", "含义": "开始、公开、事业"}
}

EIGHT_GODS = {
    "值符": {"性质": "大吉", "含义": "核心、领导、保护"},
    "螣蛇": {"性质": "小凶", "含义": "虚假、变化、惊恐"},
    "太阴": {"性质": "吉", "含义": "隐秘、阴柔、协助"},
    "白虎": {"性质": "凶", "含义": "凶险、疾病、意外"},
    "玄武": {"性质": "小凶", "含义": "暗昧、狡猾、盗贼"},
    "九地": {"性质": "吉", "含义": "稳定、保守、长久"},
    "九天": {"性质": "大吉", "含义": "高远、行动、发挥"},
    "六合": {"性质": "吉", "含义": "合作、和谐、婚姻"}
}

NINE_STARS_QIMEN = {
    "天蓬星": {"性质": "凶", "五行": "水", "含义": "破财、大盗"},
    "天芮星": {"性质": "凶", "五行": "土", "含义": "疾病、问题"},
    "天冲星": {"性质": "吉", "五行": "木", "含义": "行动、冲突"},
    "天辅星": {"性质": "大吉", "五行": "木", "含义": "教育、文化"},
    "天禽星": {"性质": "吉", "五行": "土", "含义": "中正、领导"},
    "天心星": {"性质": "吉", "五行": "金", "含义": "智慧、医疗"},
    "天柱星": {"性质": "凶", "五行": "金", "含义": "破坏、口舌"},
    "天任星": {"性质": "吉", "五行": "土", "含义": "任重、固执"},
    "天英星": {"性质": "小凶", "五行": "火", "含义": "文章、热情"}
}

GONG_KAI_FANG = {
    1: ["生", "伤", "杜", "景", "死", "惊", "开", "休"],
    2: ["死", "惊", "开", "休", "生", "伤", "杜", "景"],
    3: ["伤", "杜", "景", "死", "惊", "开", "休", "生"],
    4: ["杜", "景", "死", "惊", "开", "休", "生", "伤"],
    6: ["开", "休", "生", "伤", "杜", "景", "死", "惊"],
    7: ["休", "生", "伤", "杜", "景", "死", "惊", "开"],
    8: ["惊", "开", "休", "生", "伤", "杜", "景", "死"],
    9: ["景", "死", "惊", "开", "休", "生", "伤", "杜"]
}

START_DOOR_BY_DUN = {
    YinDun.YANG: {
        1: "休门", 2: "生门", 3: "伤门", 4: "杜门",
        6: "开门", 7: "惊门", 8: "死门", 9: "景门"
    },
    YinDun.YIN: {
        1: "休门", 2: "惊门", 3: "伤门", 4: "死门",
        6: "开门", 7: "杜门", 8: "生门", 9: "景门"
    }
}

START_STAR_BY_YUAN = {
    1: "天蓬星", 2: "天芮星", 3: "天冲星", 4: "天辅星",
    5: "天禽星", 6: "天心星", 7: "天柱星", 8: "天任星", 9: "天英星"
}

START_GOD_BY_DUN = {
    YinDun.YANG: "值符",
    YinDun.YIN: "螣蛇"
}


def get_dun_type(solar_term: str) -> YinDun:
    """根据节气判断遁甲类型"""
    winter_terms = ["立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]
    return YinDun.YIN if solar_term in winter_terms else YinDun.YANG


def get_door_info(door: str) -> Dict:
    """获取门的信息"""
    return EIGHT_DOORS.get(door, {})


def get_god_info(god: str) -> Dict:
    """获取神的信息"""
    return EIGHT_GODS.get(god, {})


def get_star_info(star: str) -> Dict:
    """获取星的信息"""
    return NINE_STARS_QIMEN.get(star, {})


def calculate_yuan(start_date_jd: int, target_date_jd: int) -> int:
    """
    计算上中下元

    Args:
        start_date_jd: 起始日期的儒略日（节气开始日）
        target_date_jd: 目标日期的儒略日

    Returns:
        元数（1=上元, 2=中元, 3=下元）
    """
    days_diff = target_date_jd - start_date_jd
    return (days_diff % 15) // 5 + 1


def calculate_start_gong(yuan: int, dun_type: YinDun) -> int:
    """
    计算起宫

    Args:
        yuan: 元（1-3）
        dun_type: 遁甲类型

    Returns:
        起始宫位数字
    """
    if dun_type == YinDun.YANG:
        base_gongs = {1: 1, 2: 4, 3: 7}
    else:
        base_gongs = {1: 9, 2: 6, 3: 3}
    return base_gongs.get(yuan, 1)


def calculate_door_position(start_gong: int, dun_type: YinDun, step: int = 0) -> int:
    """
    计算门的宫位

    Args:
        start_gong: 起始宫位
        dun_type: 遁甲类型
        step: 步数

    Returns:
        宫位数字
    """
    if dun_type == YinDun.YANG:
        return (start_gong - 1 + step) % 9 + 1
    else:
        return (start_gong - 1 - step) % 9 + 1
