"""
八字排盘测试
使用已知命盘数据验证排盘算法
"""

import pytest
from datetime import datetime
from app.engine.bazi.chart import BaziEngine, BaziStrengthResult
from app.engine.base import BirthInfo, ChartMetadata, LocationInfo, GenderType, ChartType


class TestBaziEngine:
    """八字排盘引擎测试"""

    @pytest.fixture
    def bazi_engine(self):
        """创建八字引擎实例"""
        return BaziEngine()

    @pytest.fixture
    def sample_birth_info(self):
        """创建样本出生信息"""
        return BirthInfo(
            birth_time=datetime(1990, 5, 15, 14, 30),
            location=LocationInfo(
                longitude=116.4,
                latitude=39.9,
                timezone=8.0
            ),
            gender=GenderType.MALE
        )

    def test_engine_initialization(self, bazi_engine):
        """测试引擎初始化"""
        assert bazi_engine.chart_type == ChartType.BAZI
        assert len(bazi_engine.stems) == 10
        assert len(bazi_engine.branches) == 12

    def test_validate_input_valid(self, bazi_engine, sample_birth_info):
        """测试有效输入验证"""
        assert bazi_engine.validate_input(sample_birth_info) is True

    def test_validate_input_invalid_year(self, bazi_engine):
        """测试无效年份验证"""
        invalid_info = BirthInfo(
            birth_time=datetime(1800, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        assert bazi_engine.validate_input(invalid_info) is False

    def test_validate_input_future_year(self, bazi_engine):
        """测试未来年份验证"""
        invalid_info = BirthInfo(
            birth_time=datetime(2200, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        assert bazi_engine.validate_input(invalid_info) is False

    def test_validate_input_invalid_hour(self, bazi_engine):
        """测试无效小时验证"""
        invalid_info = BirthInfo(
            birth_time=datetime(2020, 5, 15, 25, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        assert bazi_engine.validate_input(invalid_info) is False


class TestBaziCalculation:
    """八字计算测试"""

    @pytest.fixture
    def bazi_engine(self):
        return BaziEngine()

    def test_four_pillars_structure(self, bazi_engine, sample_birth_info=None):
        """测试四柱结构"""
        if sample_birth_info is None:
            sample_birth_info = BirthInfo(
                birth_time=datetime(1990, 5, 15, 14, 30),
                location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
                gender=GenderType.MALE
            )

        chart = bazi_engine.calculate(sample_birth_info)
        data = chart.data

        assert "four_pillars" in data
        pillars = data["four_pillars"]

        for pillar_name in ["year", "month", "day", "hour"]:
            assert pillar_name in pillars
            assert "stem" in pillars[pillar_name]
            assert "branch" in pillars[pillar_name]

    def test_1990_5_15_result(self, bazi_engine):
        """测试1990年5月15日14:30的命盘"""
        birth_info = BirthInfo(
            birth_time=datetime(1990, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        data = chart.data
        pillars = data["four_pillars"]

        assert pillars["year"]["stem"] in ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        assert pillars["year"]["branch"] in ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

    def test_day_master_extraction(self, bazi_engine):
        """测试日主提取"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=120, latitude=30, timezone=8.0),
            gender=GenderType.FEMALE
        )

        chart = bazi_engine.calculate(birth_info)
        assert chart.data["day_master"] in ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    def test_strength_analysis(self, bazi_engine):
        """测试日主强弱分析"""
        birth_info = BirthInfo(
            birth_time=datetime(2000, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        strength = chart.data.get("strength_analysis", {})

        if strength:
            assert "day_master_strength" in strength
            assert "level" in strength
            assert 0 <= strength["day_master_strength"] <= 100
            assert strength["level"] in ["极强", "强", "中和", "弱", "极弱"]

    def test_dayun_structure(self, bazi_engine):
        """测试大运结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2000, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        dayun = chart.data.get("dayun", [])

        assert len(dayun) == 10
        for d in dayun:
            assert "stem" in d
            assert "branch" in d
            assert "element" in d

    def test_male_female_dayun_direction(self, bazi_engine):
        """测试男女大运方向"""
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

        male_chart = bazi_engine.calculate(male_info)
        female_chart = bazi_engine.calculate(female_info)

        assert male_chart.data["dayun"] != female_chart.data["dayun"]


class TestBaziRelations:
    """八字关系测试"""

    @pytest.fixture
    def bazi_engine(self):
        return BaziEngine()

    def test_pillar_relations_structure(self, bazi_engine):
        """测试柱关系结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        relations = chart.data.get("relations", {})

        assert isinstance(relations, dict)

    def test_hidden_stems(self, bazi_engine):
        """测试地支藏干"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        pillars = chart.data["four_pillars"]

        for pillar in pillars.values():
            if "hidden_stems" in pillar:
                assert isinstance(pillar["hidden_stems"], list)


class TestUsableGodSelection:
    """用神选取测试"""

    @pytest.fixture
    def bazi_engine(self):
        return BaziEngine()

    def test_usable_god_extraction(self, bazi_engine):
        """测试用神提取逻辑"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 3, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        pillars = chart.data["four_pillars"]

        strength = bazi_engine._calculate_day_master_strength(pillars)
        usable_gods = bazi_engine.select_usable_god(strength, pillars)

        assert "main" in usable_gods
        assert "auxiliary" in usable_gods
        assert isinstance(usable_gods["auxiliary"], list)

    def test_strong_day_master_usable_god(self, bazi_engine):
        """测试日主强时用神选取"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 8, 8, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        pillars = chart.data["four_pillars"]
        strength = bazi_engine._calculate_day_master_strength(pillars)
        usable_gods = bazi_engine.select_usable_god(strength, pillars)

        assert usable_gods["main"] != ""


class TestBaziEdgeCases:
    """八字边界情况测试"""

    @pytest.fixture
    def bazi_engine(self):
        return BaziEngine()

    def test_leap_month(self, bazi_engine):
        """测试闰月处理"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 5, 20, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        assert chart.metadata is not None

    def test_dst_transition(self, bazi_engine):
        """测试夏令时转换"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 4, 1, 2, 30),
            location=LocationInfo(longitude=120, latitude=30, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        assert chart.data is not None

    def test_year_boundary(self, bazi_engine):
        """测试年份边界"""
        for year in [1900, 2000, 2024, 2100]:
            birth_info = BirthInfo(
                birth_time=datetime(year, 1, 1, 12, 0),
                location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
                gender=GenderType.MALE
            )

            if bazi_engine.validate_input(birth_info):
                chart = bazi_engine.calculate(birth_info)
                assert chart.data is not None

    def test_midnight_birth(self, bazi_engine):
        """测试午夜出生"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 0, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.FEMALE
        )

        chart = bazi_engine.calculate(birth_info)
        assert chart.data["four_pillars"]["hour"]["branch"] == "子"

    def test_noon_birth(self, bazi_engine):
        """测试正午出生"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        assert chart.data["four_pillars"]["hour"]["branch"] == "午"


class TestSolarTermIntegration:
    """节气集成测试"""

    @pytest.fixture
    def bazi_engine(self):
        return BaziEngine()

    def test_solar_term_info(self, bazi_engine):
        """测试节气信息"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 2, 4, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

        chart = bazi_engine.calculate(birth_info)
        solar_term = chart.data.get("solar_term", {})

        if solar_term:
            assert "name" in solar_term
            assert solar_term["name"] in [
                "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰",
                "春分", "清明", "谷雨", "立夏", "小满", "芒种",
                "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
                "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"
            ]
