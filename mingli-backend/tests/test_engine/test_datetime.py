"""
真太阳时、儒略日转换测试
"""

import pytest
from datetime import datetime
from app.engine.datetime_utils import (
    gregorian_to_julian_day,
    julian_day_to_gregorian,
    calculate_sun_longitude,
    calculate_true_solar_time,
    calculate_four_pillars,
    get_year_stem_branch,
    get_month_stem_branch,
    get_day_stem_branch,
    get_hour_stem_branch,
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
)


class TestJulianDayConversion:
    """儒略日转换测试"""

    def test_gregorian_to_julian_day_basic(self):
        """测试基本格里高利历转儒略日"""
        jd = gregorian_to_julian_day(2000, 1, 1, 12, 0, 0)
        assert 2451544.5 <= jd <= 2451545.5

    def test_gregorian_to_julian_day_noon(self):
        """测试正午儒略日"""
        jd = gregorian_to_julian_day(2024, 6, 15, 12, 0, 0)
        assert 2460000 <= jd <= 2461000

    def test_julian_day_roundtrip(self):
        """测试儒略日往返转换"""
        original = datetime(2024, 3, 21, 14, 30, 45)
        jd = gregorian_to_julian_day(
            original.year, original.month, original.day,
            original.hour, original.minute, original.second
        )
        year, month, day, hour, minute, second = julian_day_to_gregorian(jd)

        assert year == original.year
        assert month == original.month
        assert day == original.day

    def test_julian_day_precision(self):
        """测试儒略日精度"""
        for year, month, day in [(2020, 1, 1), (1990, 6, 15), (1984, 2, 2)]:
            jd = gregorian_to_julian_day(year, month, day, 12, 0, 0)
            y, m, d, h, mi, s = julian_day_to_gregorian(jd)
            assert y == year
            assert m == month
            assert d == day

    def test_julian_day_leap_year(self):
        """测试闰年儒略日计算"""
        jd_2024 = gregorian_to_julian_day(2024, 2, 29, 12, 0, 0)
        jd_2023 = gregorian_to_julian_day(2023, 2, 28, 12, 0, 0)
        assert jd_2024 > jd_2023

    def test_julian_day_negative_year(self):
        """测试公元前日期"""
        jd = gregorian_to_julian_day(-1, 1, 1, 12, 0, 0)
        assert jd < 1721424.5


class TestSunLongitude:
    """太阳黄经计算测试"""

    def test_sun_longitude_range(self):
        """测试太阳黄经范围"""
        for month in range(1, 13):
            jd = gregorian_to_julian_day(2024, month, 15, 12, 0, 0)
            longitude = calculate_sun_longitude(jd)
            assert 0 <= longitude < 360

    def test_sun_longitude_equinox(self):
        """测试二分点太阳黄经"""
        jd_spring = gregorian_to_julian_day(2024, 3, 20, 12, 0, 0)
        spring_longitude = calculate_sun_longitude(jd_spring)
        assert abs(spring_longitude) < 5 or abs(spring_longitude - 360) < 5

        jd_autumn = gregorian_to_julian_day(2024, 9, 22, 12, 0, 0)
        autumn_longitude = calculate_sun_longitude(jd_autumn)
        assert 175 <= autumn_longitude <= 185

    def test_sun_longitude_solstice(self):
        """测试二至点太阳黄经"""
        jd_summer = gregorian_to_julian_day(2024, 6, 21, 12, 0, 0)
        summer_longitude = calculate_sun_longitude(jd_summer)
        assert 85 <= summer_longitude <= 95

        jd_winter = gregorian_to_julian_day(2024, 12, 21, 12, 0, 0)
        winter_longitude = calculate_sun_longitude(jd_winter)
        assert 265 <= winter_longitude <= 275


class TestTrueSolarTime:
    """真太阳时计算测试"""

    def test_true_solar_time_beijing(self):
        """测试北京真太阳时"""
        local_time = datetime(2024, 6, 15, 12, 0, 0)
        beijing_time = calculate_true_solar_time(
            local_time, longitude=116.4, timezone_offset=8.0
        )
        assert 0 <= beijing_time.hour <= 23
        assert 0 <= beijing_time.minute <= 59

    def test_true_solar_time_shanghai(self):
        """测试上海真太阳时"""
        local_time = datetime(2024, 1, 1, 8, 0, 0)
        shanghai_time = calculate_true_solar_time(
            local_time, longitude=121.4, timezone_offset=8.0
        )
        assert 0 <= shanghai_time.hour <= 23

    def test_true_solar_time_western_china(self):
        """测试西部城市真太阳时"""
        local_time = datetime(2024, 6, 15, 12, 0, 0)
        urumqi_time = calculate_true_solar_time(
            local_time, longitude=87.6, timezone_offset=6.0
        )
        assert 0 <= urumqi_time.hour <= 23

    def test_true_solar_time_eastern_china(self):
        """测试东部城市真太阳时"""
        local_time = datetime(2024, 6, 15, 12, 0, 0)
        nanjing_time = calculate_true_solar_time(
            local_time, longitude=118.8, timezone_offset=8.0
        )
        assert 0 <= nanjing_time.hour <= 23

    def test_true_solar_time_timezone_offset(self):
        """测试不同时区偏移"""
        local_time = datetime(2024, 6, 15, 12, 0, 0)
        time_offset_7 = calculate_true_solar_time(
            local_time, longitude=120, timezone_offset=7.0
        )
        time_offset_8 = calculate_true_solar_time(
            local_time, longitude=120, timezone_offset=8.0
        )
        assert time_offset_7.hour != time_offset_8.hour or \
               time_offset_7.minute != time_offset_8.minute


class TestStemBranch:
    """天干地支计算测试"""

    def test_year_stem_branch_1984(self):
        """测试1984年为甲子年"""
        stem, branch = get_year_stem_branch(1984)
        assert stem == "甲"
        assert branch == "子"

    def test_year_stem_branch_2024(self):
        """测试2024年为甲辰年"""
        stem, branch = get_year_stem_branch(2024)
        assert stem == "甲"
        assert branch == "辰"

    def test_year_stem_branch_1990(self):
        """测试1990年为庚午年"""
        stem, branch = get_year_stem_branch(1990)
        assert stem == "庚"
        assert branch == "午"

    def test_month_stem_branch(self):
        """测试月柱计算"""
        stem, branch = get_month_stem_branch("甲", 1)
        assert stem in HEAVENLY_STEMS
        assert branch in EARTHLY_BRANCHES
        assert branch == "寅"

    def test_day_stem_branch(self):
        """测试日柱计算"""
        stem, branch = get_day_stem_branch(2024, 6, 15)
        assert stem in HEAVENLY_STEMS
        assert branch in EARTHLY_BRANCHES

    def test_hour_stem_branch(self):
        """测试时柱计算"""
        stem, branch = get_hour_stem_branch("甲", 12)
        assert stem in HEAVENLY_STEMS
        assert branch in EARTHLY_BRANCHES
        assert branch == "午"

    def test_hour_stem_branch_all_hours(self):
        """测试所有时辰"""
        day_stem = "甲"
        for hour in range(24):
            stem, branch = get_hour_stem_branch(day_stem, hour)
            assert stem in HEAVENLY_STEMS
            assert branch in EARTHLY_BRANCHES


class TestFourPillars:
    """四柱八字计算测试"""

    def test_four_pillars_basic(self):
        """测试基本四柱计算"""
        pillars = calculate_four_pillars(2024, 6, 15, 12, 30)
        assert "year" in pillars
        assert "month" in pillars
        assert "day" in pillars
        assert "hour" in pillars

    def test_four_pillars_keys(self):
        """测试四柱键值"""
        pillars = calculate_four_pillars(2024, 1, 1, 0, 0)
        for pillar in pillars.values():
            assert "stem" in pillar
            assert "branch" in pillar
            assert pillar["stem"] in HEAVENLY_STEMS
            assert pillar["branch"] in EARTHLY_BRANCHES

    def test_four_pillars_consistency(self):
        """测试四柱计算一致性"""
        pillars1 = calculate_four_pillars(2024, 6, 15, 12, 0)
        pillars2 = calculate_four_pillars(2024, 6, 15, 12, 30)
        assert pillars1["year"] == pillars2["year"]
        assert pillars1["month"] == pillars2["month"]
        assert pillars1["day"] == pillars2["day"]

    def test_four_pillars_chinese_calendar(self):
        """测试农历换算（立春为界）"""
        pillars_before = calculate_four_pillars(2024, 2, 3, 12, 0)
        pillars_after = calculate_four_pillars(2024, 2, 4, 12, 0)
        assert pillars_before["year"] != pillars_after["year"]

    def test_four_pillars_midnight(self):
        """测试午夜时分"""
        pillars = calculate_four_pillars(2024, 6, 15, 0, 0)
        assert pillars["hour"]["branch"] in EARTHLY_BRANCHES

    def test_four_pillars_noon(self):
        """测试正午时分"""
        pillars = calculate_four_pillars(2024, 6, 15, 12, 0)
        assert pillars["hour"]["branch"] == "午"

    def test_four_pillars_甲子日(self):
        """测试甲子日"""
        jd = gregorian_to_julian_day(2024, 2, 9, 12, 0, 0)
        year, month, day = julian_day_to_gregorian(jd)[:3]
        stem, branch = get_day_stem_branch(year, month, day)
        assert stem == "甲"
        assert branch == "子"
