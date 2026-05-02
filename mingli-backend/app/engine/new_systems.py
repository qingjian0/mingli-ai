"""
新命理系统模块
邵子易数、皇极数、大六壬、梅花易数、六爻等
"""

from .base import (
    BaseEngine, BaseChartData, BirthInfo, ChartType, EngineRegistry
)
from enum import Enum
from typing import List, Dict, Any
from datetime import datetime
import random


class DivinationMethod(str, Enum):
    """占卜方法"""
    TIME = "time"           # 时占法
    NUMBER = "number"      # 数占法
    TEXT = "text"          # 字占法
    OBJECT = "object"      # 物占法


# ==================== 基础命理模型 ====================

class YijingHexagram(BaseModel):
    """易经卦象"""
    name: str
    number: int
    original: str  # 本卦
    changed: str   # 变卦
    changing_lines: List[int]
    description: str


class DayanResult(BaseModel):
    """大衍筮法结果"""
    original_gua: YijingHexagram
    changed_gua: YijingHexagram
    dayan_number: int
    process: List[str]


# ==================== 邵子易数 ====================

@EngineRegistry.register(ChartType.SHAOZI_YISHU)
class ShaoziYishuEngine(BaseEngine):
    """邵子易数引擎"""
    chart_type = ChartType.SHAOZI_YISHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        """计算邵子易数卦象"""
        metadata = self._create_metadata(birth_info)
        
        # 邵子易数核心算法（简化版）
        year_stem, year_branch = self._get_year_stem_branch(birth_info.birth_time)
        day_stem, day_branch = self._get_day_stem_branch(birth_info.birth_time)
        gua = self._calculate_gua(year_stem, day_branch)
        
        data = {
            "gua": gua,
            "year_stem": year_stem,
            "year_branch": year_branch,
            "day_stem": day_stem,
            "day_branch": day_branch,
            "description": "邵子易数卦象计算结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _get_year_stem_branch(self, dt: datetime):
        stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        year = dt.year - 4
        return stems[year % 10], branches[year % 12]
    
    def _get_day_stem_branch(self, dt: datetime):
        return "甲", "子"  # 简化版，实际需要复杂计算
    
    def _calculate_gua(self, stem1: str, stem2: str):
        guas = ["乾", "坤", "震", "巽", "坎", "离", "艮", "兑"]
        return guas[random.randint(0, 7)]


# ==================== 皇极数 ====================

@EngineRegistry.register(ChartType.HUANGJI_SHU)
class HuangjiShuEngine(BaseEngine):
    """皇极数引擎"""
    chart_type = ChartType.HUANGJI_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 皇极数核心算法（简化版）
        year_num = birth_info.birth_time.year
        month_num = birth_info.birth_time.month
        day_num = birth_info.birth_time.day
        
        huangji_number = self._calculate_huangji_number(year_num, month_num, day_num)
        
        data = {
            "huangji_number": huangji_number,
            "year": year_num,
            "month": month_num,
            "day": day_num,
            "description": "皇极数计算结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _calculate_huangji_number(self, y: int, m: int, d: int):
        return (y * 10000 + m * 100 + d) % 100000


# ==================== 大六壬 ====================

@EngineRegistry.register(ChartType.DALIU_REN)
class DaliuRenEngine(BaseEngine):
    """大六壬引擎"""
    chart_type = ChartType.DALIU_REN

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 大六壬排盘（简化版）
        hour_branch = self._get_hour_branch(birth_info.birth_time.hour)
        tianpan = self._calculate_tianpan(hour_branch)
        
        data = {
            "tianpan": tianpan,
            "dipan": ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"],
            "six_gods": ["青龙", "朱雀", "勾陈", "六合", "白虎", "玄武"],
            "four_classes": ["初传", "中传", "末传", "四课"],
            "description": "大六壬排盘结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _get_hour_branch(self, hour: int):
        branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        return branches[(hour + 1) // 2 % 12]
    
    def _calculate_tianpan(self, hour_branch: str):
        tianpan = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        idx = tianpan.index(hour_branch)
        return tianpan[idx:] + tianpan[:idx]


# ==================== 梅花易数 ====================

@EngineRegistry.register(ChartType.MEIHUA_YISHU)
class MeihuaYishuEngine(BaseEngine):
    """梅花易数引擎"""
    chart_type = ChartType.MEIHUA_YISHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 梅花易数排盘
        year = birth_info.birth_time.year % 12
        month = birth_info.birth_time.month
        day = birth_info.birth_time.day
        hour = birth_info.birth_time.hour // 2
        
        shang_gua = (year + month + day) % 8
        xia_gua = (year + month + day + hour) % 8
        yao = (year + month + day + hour) % 6
        
        gua_names = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
        
        data = {
            "shang_gua": gua_names[shang_gua],
            "xia_gua": gua_names[xia_gua],
            "bian_yao": yao + 1,
            "full_gua": f"{gua_names[shang_gua]}{gua_names[xia_gua]}卦",
            "calculation_method": "年月日时起卦",
            "description": "梅花易数排盘结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)


# ==================== 六爻 ====================

@EngineRegistry.register(ChartType.LIUYAO)
class LiuyaoEngine(BaseEngine):
    """六爻引擎"""
    chart_type = ChartType.LIUYAO

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 六爻排盘（简化版）
        liuyao_gua = self._generate_liuyao_gua()
        
        data = {
            "liuyao": liuyao_gua,
            "six_relations": ["世", "应", "官", "鬼", "财", "福"],
            "method": "六爻纳甲",
            "description": "六爻排盘结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _generate_liuyao_gua(self):
        yaos = []
        for _ in range(6):
            num = random.randint(6, 9)
            yaos.append({
                "number": num,
                "nature": "动" if num in [6, 9] else "静",
                "yin_yang": "阴" if num in [6, 8] else "阳"
            })
        return list(reversed(yaos))


# ==================== 小成图 ====================

@EngineRegistry.register(ChartType.XIAOCHENG_TU)
class XiaochengTuEngine(BaseEngine):
    """小成图引擎"""
    chart_type = ChartType.XIAOCHENG_TU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 小成图排盘
        year = birth_info.birth_time.year
        month = birth_info.birth_time.month
        day = birth_info.birth_time.day
        
        tianpan, dipan = self._calculate_xiaocheng(year, month, day)
        
        data = {
            "tianpan": tianpan,
            "dipan": dipan,
            "method": "小成图法",
            "description": "小成图排盘结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _calculate_xiaocheng(self, y: int, m: int, d: int):
        positions = ["坎", "坤", "震", "巽", "中", "乾", "兑", "艮", "离"]
        tianpan = positions[d % 9:] + positions[:d % 9]
        return tianpan, positions


# ==================== 大衍筮法 ====================

@EngineRegistry.register(ChartType.DAYAN_SHIFA)
class DayanShifaEngine(BaseEngine):
    """大衍筮法引擎"""
    chart_type = ChartType.DAYAN_SHIFA

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        
        # 大衍筮法计算
        guas = self._perform_dayan_shifa()
        
        data = {
            "original_gua": guas["original"],
            "changed_gua": guas["changed"],
            "changing_lines": guas["changing_lines"],
            "dayan_number": 50,
            "description": "大衍筮法结果"
        }
        
        return BaseChartData(metadata=metadata, data=data)
    
    def _perform_dayan_shifa(self):
        gua_names = ["乾", "坤", "震", "巽", "坎", "离", "艮", "兑"]
        original = random.choice(gua_names)
        changed = random.choice(gua_names)
        changing_lines = [i for i in range(1, 7) if random.random() < 0.2]
        return {"original": original, "changed": changed, "changing_lines": changing_lines}


# ==================== 其他数术 ====================

@EngineRegistry.register(ChartType.SHENYI_SHU)
class ShenyiShuEngine(BaseEngine):
    chart_type = ChartType.SHENYI_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "number": 42,
            "description": "神易数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.DADING_SHU)
class DadingShuEngine(BaseEngine):
    chart_type = ChartType.DADING_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "number": 108,
            "description": "大定数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.CEGUI_SHU)
class CeguiShuEngine(BaseEngine):
    chart_type = ChartType.CEGUI_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "ce_number": 49,
            "gui_number": 81,
            "description": "策轨数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.HELUO_SHU)
class HeluoShuEngine(BaseEngine):
    chart_type = ChartType.HELUO_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "he_tu_number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "luo_shu_number": [9, 5, 1, 3, 7, 2, 8, 4, 6],
            "description": "河洛数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.YUZI_SHU)
class YuziShuEngine(BaseEngine):
    chart_type = ChartType.YUZI_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "number": 64,
            "description": "愚子数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.FANWEI_SHU)
class FanweiShuEngine(BaseEngine):
    chart_type = ChartType.FANWEI_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "range_start": 1,
            "range_end": 100,
            "selected_number": random.randint(1, 100),
            "description": "范围数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.SUANPAN_SHU)
class SuanpanShuEngine(BaseEngine):
    chart_type = ChartType.SUANPAN_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "upper_beads": 5,
            "lower_beads": 5,
            "result_number": random.randint(1, 1000),
            "description": "算盘数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


@EngineRegistry.register(ChartType.YELV_SHU)
class YelvShuEngine(BaseEngine):
    chart_type = ChartType.YELV_SHU

    def validate_input(self, birth_info: BirthInfo) -> bool:
        return True

    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        metadata = self._create_metadata(birth_info)
        data = {
            "yelv_number": 72,
            "description": "耶律数计算结果"
        }
        return BaseChartData(metadata=metadata, data=data)


__all__ = [
    "ShaoziYishuEngine",
    "HuangjiShuEngine",
    "DaliuRenEngine",
    "MeihuaYishuEngine",
    "LiuyaoEngine",
    "XiaochengTuEngine",
    "DayanShifaEngine",
    "ShenyiShuEngine",
    "DadingShuEngine",
    "CeguiShuEngine",
    "HeluoShuEngine",
    "YuziShuEngine",
    "FanweiShuEngine",
    "SuanpanShuEngine",
    "YelvShuEngine"
]
