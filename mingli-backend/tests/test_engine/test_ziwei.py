"""
紫微斗数排盘测试
验证紫微斗数排盘算法的准确性
"""

import pytest
from datetime import datetime
from app.engine.ziwei.chart import ZiweiEngine, PalaceData
from app.engine.base import BirthInfo, ChartMetadata, LocationInfo, GenderType, ChartType


class TestZiweiEngine:
    """紫微斗数引擎测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    @pytest.fixture
    def sample_birth_info(self):
        return BirthInfo(
            birth_time=datetime(1990, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

    def test_engine_initialization(self, ziwei_engine):
        """测试引擎初始化"""
        assert ziwei_engine.chart_type == ChartType.ZIWEI
        assert len(ziwei_engine.main_stars) > 0
        assert len(ziwei_engine.palaces) == 12
        assert len(ziwei_engine.branch_list) == 12

    def test_validate_input_valid(self, ziwei_engine, sample_birth_info):
        """测试有效输入验证"""
        assert ziwei_engine.validate_input(sample_birth_info) is True

    def test_validate_input_invalid_year(self, ziwei_engine):
        """测试无效年份验证"""
        invalid_info = BirthInfo(
            birth_time=datetime(1800, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        assert ziwei_engine.validate_input(invalid_info) is False


class TestZiweiCalculation:
    """紫微斗数计算测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    def test_basic_chart_generation(self, ziwei_engine):
        """测试基本命盘生成"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        assert chart.metadata is not None
        assert chart.data is not None

    def test_four_pillars_extraction(self, ziwei_engine):
        """测试四柱提取"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        assert "four_pillars" in chart.data
        pillars = chart.data["four_pillars"]
        for pillar_name in ["year", "month", "day", "hour"]:
            assert pillar_name in pillars
            assert "stem" in pillars[pillar_name]
            assert "branch" in pillars[pillar_name]

    def test_ming_gong_calculation(self, ziwei_engine):
        """测试命宫计算"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        assert "ming_gong" in chart.data

    def test_sheng_gong_calculation(self, ziwei_engine):
        """测试身宫计算"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        assert "sheng_gong" in chart.data

    def test_birth_transforms(self, ziwei_engine):
        """测试生年四化"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        transforms = chart.data.get("birth_transforms", {})
        assert isinstance(transforms, dict)

    def test_day_master_extraction(self, ziwei_engine):
        """测试日主提取"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=120, latitude=30, timezone=8.0),
            gender=GenderType.FEMALE
        )
        chart = ziwei_engine.calculate(birth_info)
        assert chart.data["day_master"] in ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]


class TestZiweiPalaces:
    """紫微斗数宫位测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    def test_twelve_palaces_count(self, ziwei_engine):
        """测试十二宫数量"""
        assert len(ziwei_engine.palaces) == 12

    def test_palaces_structure(self, ziwei_engine):
        """测试宫位结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})
        assert len(palaces) == 12
        for palace_data in palaces.values():
            assert "name" in palace_data
            assert "branch" in palace_data
            assert "stars" in palace_data

    def test_main_stars_placement(self, ziwei_engine):
        """测试主星排布"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        main_stars = chart.data.get("main_stars_positions", {})
        assert "紫微" in main_stars
        assert all(isinstance(pos, int) for pos in main_stars.values())


class TestZiweiBigFatePeriods:
    """紫微斗数大限测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    def test_big_fate_periods_count(self, ziwei_engine):
        """测试大限数量"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        big_fate_periods = chart.data.get("big_fate_periods", [])
        assert len(big_fate_periods) == 12

    def test_big_fate_structure(self, ziwei_engine):
        """测试大限结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2000, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        big_fate_periods = chart.data.get("big_fate_periods", [])
        for period in big_fate_periods:
            assert "index" in period
            assert "palace" in period
            assert "start_age" in period
            assert "end_age" in period
            assert "direction" in period

    def test_male_female_direction(self, ziwei_engine):
        """测试男女大限方向"""
        male_info = BirthInfo(
            birth_time=datetime(2000, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        female_info = BirthInfo(
            birth_time=datetime(2000, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.FEMALE
        )
        male_chart = ziwei_engine.calculate(male_info)
        female_chart = ziwei_engine.calculate(female_info)
        male_direction = male_chart.data["big_fate_periods"][0]["direction"]
        female_direction = female_chart.data["big_fate_periods"][0]["direction"]
        assert male_direction != female_direction


class TestZiweiGenderDifference:
    """紫微斗数性别差异测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    def test_different_gender_different_chart(self, ziwei_engine):
        """测试不同性别生成不同命盘"""
        birth_info_male = BirthInfo(
            birth_time=datetime(1990, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        birth_info_female = BirthInfo(
            birth_time=datetime(1990, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.FEMALE
        )
        male_chart = ziwei_engine.calculate(birth_info_male)
        female_chart = ziwei_engine.calculate(birth_info_female)
        assert male_chart.data.get("ming_gong") != female_chart.data.get("ming_gong")


class TestZiweiNatalPalaceMapping:
    """命宫分布测试"""

    @pytest.fixture
    def ziwei_engine(self):
        return ZiweiEngine()

    def test_natal_palace_map_structure(self, ziwei_engine):
        """测试命宫映射结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})
        assert len(palaces) == 12

    def test_year_branch_extraction(self, ziwei_engine):
        """测试年支提取"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = ziwei_engine.calculate(birth_info)
        year_branch = chart.data.get("year_branch")
        assert year_branch is not None
        assert year_branch in ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
