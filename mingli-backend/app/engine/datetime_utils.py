"""
时间处理工具模块
包含儒略日计算、真太阳时、节气计算、天干地支计算等功能
"""

from datetime import datetime, timedelta
from typing import Tuple, Optional
import math


# 天干表
HEAVENLY_STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

# 地支表
EARTHLY_BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 节气表（按中气排列，每月一个中气）
SOLAR_TERMS = [
    "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰",
    "春分", "清明", "谷雨", "立夏", "小满", "芒种",
    "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
    "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"
]

# 节气对应的太阳黄经度数
SOLAR_TERM_DEGREES = {
    "冬至": 270, "小寒": 285, "大寒": 300, "立春": 315, "雨水": 330, "惊蛰": 345,
    "春分": 0, "清明": 15, "谷雨": 30, "立夏": 45, "小满": 60, "芒种": 75,
    "夏至": 90, "小暑": 105, "大暑": 120, "立秋": 135, "处暑": 150, "白露": 165,
    "秋分": 180, "寒露": 195, "霜降": 210, "立冬": 225, "小雪": 240, "大雪": 255
}

# 地支对应的月份（正月为寅）
MONTH_BRANCH_MAP = {
    1: "寅", 2: "卯", 3: "辰", 4: "巳", 5: "午", 6: "未",
    7: "申", 8: "酉", 9: "戌", 10: "亥", 11: "子", 12: "丑"
}


def gregorian_to_julian_day(year: int, month: int, day: int,
                             hour: int = 0, minute: int = 0, second: int = 0) -> float:
    """
    格里高利历转儒略日

    使用天文计算公式，将公历日期时间转换为儒略日数

    Args:
        year: 年
        month: 月
        day: 日
        hour: 小时
        minute: 分钟
        second: 秒

    Returns:
        儒略日数（JD）
    """
    if month <= 2:
        year -= 1
        month += 12

    A = int(year / 100)
    B = 2 - A + int(A / 4)

    JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
    JD += (hour + minute / 60.0 + second / 3600.0) / 24.0

    return JD


def julian_day_to_gregorian(jd: float) -> Tuple[int, int, int, int, int, int]:
    """
    儒略日转格里高利历

    Args:
        jd: 儒略日数

    Returns:
        (年, 月, 日, 时, 分, 秒)
    """
    jd += 0.5
    Z = int(jd)
    F = jd - Z

    if Z < 2299161:
        A = Z
    else:
        alpha = int((Z - 1867216.25) / 36524.25)
        A = Z + 1 + alpha - int(alpha / 4)

    B = A + 1524
    C = int((B - 122.1) / 365.25)
    D = int(365.25 * C)
    E = int((B - D) / 30.6001)

    day = B - D - int(30.6001 * E)
    month = E - 1 if E < 14 else E - 13
    year = C - 4716 if month > 2 else C - 4715

    hours = F * 24
    hour = int(hours)
    minutes = (hours - hour) * 60
    second = int((minutes - int(minutes)) * 60)

    return year, month, day, hour, int(minutes), second


def calculate_sun_longitude(jd: float) -> float:
    """
    计算太阳黄经（天文算法）

    基于VSOP87理论简化算法，计算给定儒略日的太阳黄经

    Args:
        jd: 儒略日数

    Returns:
        太阳黄经度数（0-360）
    """
    T = (jd - 2451545.0) / 36525.0

    L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T
    M = 357.52911 + 35999.05029 * T - 0.0001537 * T * T
    M = math.radians(M)

    e = 0.016708634 - 0.000042037 * T - 0.0000001267 * T * T
    C = ((1.914602 - 0.004817 * T - 0.000014 * T * T) * math.sin(M) +
         (0.019993 - 0.000101 * T) * math.sin(2 * M) +
         0.000289 * math.sin(3 * M))

    sun_longitude = L0 + C

    while sun_longitude < 0:
        sun_longitude += 360
    while sun_longitude >= 360:
        sun_longitude -= 360

    return sun_longitude


def calculate_solar_term(year: int, term_index: int) -> datetime:
    """
    计算指定年份和节气的精确时间

    使用二分法逼近计算节气时间

    Args:
        year: 年份
        term_index: 节气索引（0-23），0=冬至

    Returns:
        节气时间
    """
    target_longitude = SOLAR_TERM_DEGREES[SOLAR_TERMS[term_index]]

    jd_start = gregorian_to_julian_day(year, 1, 1)
    if term_index >= 12:
        jd_start = gregorian_to_julian_day(year + 1, 1, 1)

    jd_end = gregorian_to_julian_day(year if term_index < 12 else year + 1, 7, 1)

    for _ in range(20):
        jd_mid = (jd_start + jd_end) / 2
        sun_long = calculate_sun_longitude(jd_mid)

        diff = sun_long - target_longitude
        if abs(diff) < 0.1:
            break

        if term_index >= 12:
            if diff > 0:
                jd_end = jd_mid
            else:
                jd_start = jd_mid
        else:
            if sun_long < target_longitude or sun_long > 360 - target_longitude:
                jd_start = jd_mid
            else:
                jd_end = jd_mid

    year_r, month_r, day_r, hour_r, min_r, sec_r = julian_day_to_gregorian(jd_mid)
    return datetime(year_r, month_r, day_r, hour_r, min_r, sec_r)


def get_current_solar_term(dt: datetime) -> Tuple[str, datetime, datetime]:
    """
    获取指定时间所在的节气

    Args:
        dt: 日期时间

    Returns:
        (节气名称, 本节气时间, 下节气时间)
    """
    year = dt.year
    month = dt.month

    for i in range(24):
        term_date = calculate_solar_term(year, i)
        if dt < term_date:
            if i == 0:
                prev_term_date = calculate_solar_term(year - 1, 23)
            else:
                prev_term_date = calculate_solar_term(year, i - 1)
            return SOLAR_TERMS[i - 1 if i > 0 else 23], prev_term_date, term_date

    next_year_term = calculate_solar_term(year + 1, 0)
    return SOLAR_TERMS[23], calculate_solar_term(year, 23), next_year_term


def calculate_true_solar_time(local_time: datetime, longitude: float,
                               timezone_offset: float = 8.0) -> datetime:
    """
    计算真太阳时（地方时）

    Args:
        local_time: 当地标准时间
        longitude: 经度
        timezone_offset: 时区偏移（小时）

    Returns:
        真太阳时
    """
    jd = gregorian_to_julian_day(
        local_time.year, local_time.month, local_time.day,
        local_time.hour, local_time.minute, local_time.second
    )

    sun_long = calculate_sun_longitude(jd)

    T = (jd - 2451545.0) / 36525.0
    L0 = math.radians(280.46646 + 36000.76983 * T)
    e = math.radians(23.439291 - 0.0130042 * T)
    M = math.radians(357.52911 + 35999.05029 * T)

    EoT = (L0 - 0.0057183 - sun_long * math.pi / 180 +
           2 * math.sin(M) * math.cos(e) - 0.000139 * math.sin(2 * M)) * 12 / math.pi
    EoT = EoT * 4

    timezone_minutes = timezone_offset * 60
    longitude_minutes = longitude * 4

    true_solar_minutes = timezone_minutes - EoT / 60 + longitude_minutes / 60

    total_minutes = local_time.hour * 60 + local_time.minute + true_solar_minutes
    total_minutes = max(0, min(total_minutes, 1439))

    hour = int(total_minutes / 60)
    minute = int(total_minutes % 60)

    return local_time.replace(hour=hour, minute=minute)


def calculate_stem_branch_index(jd: float, base_jd: float) -> Tuple[int, int]:
    """
    计算指定儒略日的天干地支索引

    Args:
        jd: 目标儒略日
        base_jd: 基准儒略日（甲子日）

    Returns:
        (天干索引0-9, 地支索引0-11)
    """
    days_diff = int(jd - base_jd)
    stem_index = days_diff % 10
    branch_index = days_diff % 12
    return stem_index, branch_index


BASE_JD_1984_JIAZI = gregorian_to_julian_day(1984, 2, 2)


def get_year_stem_branch(year: int) -> Tuple[str, str]:
    """
    计算年柱天干地支

    Args:
        year: 年份

    Returns:
        (天干, 地支)
    """
    jd = gregorian_to_julian_day(year, 7, 1)
    stem_idx, branch_idx = calculate_stem_branch_index(jd, BASE_JD_1984_JIAZI)

    year_offset = year - 1984
    stem_idx = (year_offset + 6) % 10
    branch_idx = (year_offset + 4) % 12

    return HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx]


def get_month_stem_branch(year_stem: str, month: int) -> Tuple[str, str]:
    """
    计算月柱天干地支

    Args:
        year_stem: 年柱天干
        month: 月份（1-12）

    Returns:
        (天干, 地支)
    """
    stem_base = HEAVENLY_STEMS.index(year_stem)
    branch = MONTH_BRANCH_MAP[month]

    stem_index = (stem_base * 2 + month - 1) % 10
    branch_index = EARTHLY_BRANCHES.index(branch)

    return HEAVENLY_STEMS[stem_index], branch


def get_day_stem_branch(year: int, month: int, day: int) -> Tuple[str, str]:
    """
    计算日柱天干地支

    Args:
        year: 年
        month: 月
        day: 日

    Returns:
        (天干, 地支)
    """
    jd = gregorian_to_julian_day(year, month, day, 12, 0, 0)
    stem_idx, branch_idx = calculate_stem_branch_index(jd, BASE_JD_1984_JIAZI)

    return HEAVENLY_STEMS[stem_idx], EARTHLY_BRANCHES[branch_idx]


def get_hour_stem_branch(day_stem: str, hour: int) -> Tuple[str, str]:
    """
    计算时柱天干地支

    Args:
        day_stem: 日柱天干
        hour: 小时（0-23）

    Returns:
        (天干, 地支)
    """
    stem_base = HEAVENLY_STEMS.index(day_stem)

    branch_index = (hour + 1) // 2 % 12
    stem_index = (stem_base * 2 + branch_index) % 10

    return HEAVENLY_STEMS[stem_index], EARTHLY_BRANCHES[branch_index]


def calculate_four_pillars(year: int, month: int, day: int,
                           hour: int, minute: int = 0) -> dict:
    """
    计算四柱八字

    Args:
        year: 年
        month: 月
        day: 日
        hour: 小时
        minute: 分钟

    Returns:
        包含年柱、月柱、日柱、时柱的字典
    """
    year_stem, year_branch = get_year_stem_branch(year)
    month_stem, month_branch = get_month_stem_branch(year_stem, month)

    day_stem, day_branch = get_day_stem_branch(year, month, day)
    hour_stem, hour_branch = get_hour_stem_branch(day_stem, hour)

    return {
        "year": {"stem": year_stem, "branch": year_branch},
        "month": {"stem": month_stem, "branch": month_branch},
        "day": {"stem": day_stem, "branch": day_branch},
        "hour": {"stem": hour_stem, "branch": hour_branch}
    }


def calculate_solar_term_index(dt: datetime) -> int:
    """
    计算指定时间的中气索引（用于判断三元）

    Args:
        dt: 日期时间

    Returns:
        中气索引（0-11），0=冬至子月
    """
    year = dt.year
    month = dt.month

    for i in range(0, 24, 2):
        term_date = calculate_solar_term(year, i)
        next_term_date = calculate_solar_term(year, (i + 2) % 24)

        if dt >= term_date and dt < next_term_date:
            return i // 2

    if month == 12:
        return 0
    return (month - 1) % 12


def get_xiang(shichen: str) -> str:
    """
    获取时辰对应的象

    Args:
        shichen: 地支

    Returns:
        象（少阳、老阳、少阴、老阴）
    """
    yang_branches = ["寅", "卯", "辰", "巳", "午"]
    yin_branches = ["申", "酉", "戌", "亥", "子", "丑"]

    if shichen in yang_branches[:3]:
        return "少阳"
    elif shichen in yang_branches[3:]:
        return "老阳"
    elif shichen in yin_branches[:3]:
        return "少阴"
    else:
        return "老阴"
