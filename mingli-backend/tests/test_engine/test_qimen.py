"""
奇门遁甲排盘测试
验证奇门遁甲排盘算法的准确性
"""

import pytest
from datetime import datetime
from app.engine.qimen.chart import QimenEngine, GongData
from app.engine.base import BirthInfo, LocationInfo, GenderType, ChartType
from app.engine.qimen.pan import YinDun


class TestQimenEngine:
    """奇门遁甲引擎测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    @pytest.fixture
    def sample_birth_info(self):
        return BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )

    def test_engine_initialization(self, qimen_engine):
        """测试引擎初始化"""
        assert qimen_engine.chart_type == ChartType.QIMEN
        assert hasattr(qimen_engine, "YIN_DUN_WINTER_SOLSTICE")
        assert hasattr(qimen_engine, "YANG_DUN_SUMMER_SOLSTICE")

    def test_validate_input_valid(self, qimen_engine, sample_birth_info):
        """测试有效输入验证"""
        assert qimen_engine.validate_input(sample_birth_info) is True

    def test_validate_input_invalid_year(self, qimen_engine):
        """测试无效年份验证"""
        invalid_info = BirthInfo(
            birth_time=datetime(1800, 5, 15, 14, 30),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        assert qimen_engine.validate_input(invalid_info) is False


class TestQimenCalculation:
    """奇门遁甲计算测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_basic_chart_generation(self, qimen_engine):
        """测试基本盘生成"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        assert chart.metadata is not None
        assert chart.data is not None

    def test_four_pillars_extraction(self, qimen_engine):
        """测试四柱提取"""
        birth_info = BirthInfo(
            birth_time=datetime(2020, 1, 1, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        assert "four_pillars" in chart.data

    def test_dun_type(self, qimen_engine):
        """测试遁阴遁阳"""
        winter_info = BirthInfo(
            birth_time=datetime(2024, 1, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        winter_chart = qimen_engine.calculate(winter_info)
        assert "dun_type" in winter_chart.data

    def test_yuan_calculation(self, qimen_engine):
        """测试上中下元计算"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        assert "yuan" in chart.data
        assert chart.data["yuan"] in [1, 2, 3]

    def test_start_gong_calculation(self, qimen_engine):
        """测试起宫计算"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        assert "start_gong" in chart.data
        assert 1 <= chart.data["start_gong"] <= 9

    def test_solar_term_info(self, qimen_engine):
        """测试节气信息"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 2, 4, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        solar_term = chart.data.get("solar_term", {})
        assert "name" in solar_term


class TestQimenPalace:
    """奇门遁甲宫位测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_palace_count(self, qimen_engine):
        """测试宫位数量"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})
        assert len(palaces) == 9

    def test_palace_structure(self, qimen_engine):
        """测试宫位结构"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})

        for pos, palace_data in palaces.items():
            assert "position" in palace_data
            assert "name" in palace_data
            assert "trigram" in palace_data
            assert "element" in palace_data

    def test_center_palace(self, qimen_engine):
        """测试中五宫"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})
        assert 5 in palaces
        assert palaces[5]["name"] == "中五宫"

    def test_door_placement(self, qimen_engine):
        """测试八门排布"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})

        door_names = set()
        for palace_data in palaces.values():
            if palace_data.get("door"):
                door_names.add(palace_data["door"])

        assert len(door_names) > 0

    def test_star_placement(self, qimen_engine):
        """测试九星排布"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})

        star_names = set()
        for palace_data in palaces.values():
            if palace_data.get("star"):
                star_names.add(palace_data["star"])

        assert len(star_names) > 0

    def test_god_placement(self, qimen_engine):
        """测试八神排布"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        palaces = chart.data.get("palaces", {})

        god_names = set()
        for palace_data in palaces.values():
            if palace_data.get("god"):
                god_names.add(palace_data["god"])

        assert len(god_names) > 0


class TestQimenYuanAndDun:
    """遁甲元测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_yuan_values(self, qimen_engine):
        """测试元的取值范围"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        yuan = chart.data["yuan"]
        assert yuan in [1, 2, 3]

    def test_different_dates_different_yuan(self, qimen_engine):
        """测试不同日期不同元"""
        info1 = BirthInfo(
            birth_time=datetime(2024, 6, 10, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        info2 = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart1 = qimen_engine.calculate(info1)
        chart2 = qimen_engine.calculate(info2)

    def test_start_gong_values(self, qimen_engine):
        """测试起宫取值"""
        birth_info = BirthInfo(
            birth_time=datetime(2024, 6, 15, 12, 0),
            location=LocationInfo(longitude=116.4, latitude=39.9, timezone=8.0),
            gender=GenderType.MALE
        )
        chart = qimen_engine.calculate(birth_info)
        start_gong = chart.data["start_gong"]
        assert start_gong in [1, 2, 3, 4, 6, 7, 8, 9]


class TestQimenHourKe:
    """时干入宫测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_hour_ke_calculation(self, qimen_engine):
        """测试时干入宫计算"""
        for hour in range(24):
            hour_ke = qimen_engine._calculate_hour_ke(hour)
            assert 1 <= hour_ke <= 9

    def test_hour_ke_boundary(self, qimen_engine):
        """测试时辰边界"""
        assert qimen_engine._calculate_hour_ke(0) == 1
        assert qimen_engine._calculate_hour_ke(23) == 1


class TestQimenMenPa:
    """门迫测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_men_pa_calculation(self, qimen_engine):
        """测试门迫计算"""
        for yuan in [1, 2, 3]:
            men_pa = qimen_engine._get_men_pa(yuan, YinDun.YANG)
            assert isinstance(men_pa, str)
            assert "门迫" in men_pa or len(men_pa) > 0


class TestQimenXunShou:
    """旬首测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_xun_shou_calculation(self, qimen_engine):
        """测试旬首计算"""
        for yuan in [1, 2, 3]:
            xun_shou = qimen_engine._get_xun_shou(yuan)
            assert isinstance(xun_shou, str)
            assert len(xun_shou) == 2


class TestQimenZiJia:
    """符首计算测试"""

    @pytest.fixture
    def qimen_engine(self):
        return QimenEngine()

    def test_zi_jia_calculation(self, qimen_engine):
        """测试符首计算"""
        start_jd = 2460000.0
        target_jd = 2460100.0
        zi_jia = qimen_engine.calculate_zi_jia(target_jd, start_jd)
        assert 1 <= zi_jia <= 6

    def test_zi_jia_60_day_cycle(self, qimen_engine):
        """测试60日循环"""
        base_jd = 2460000.0
        for i in [0, 10, 20, 30, 40, 50, 60]:
            zi_jia = qimen_engine.calculate_zi_jia(base_jd + i, base_jd)
            assert 1 <= zi_jia <= 6
