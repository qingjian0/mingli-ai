"""
排盘引擎基础模块
定义所有排盘引擎的抽象基类和通用数据结构
"""

from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict
import hashlib
import json


class ChartType(str, Enum):
    """命盘类型枚举"""
    ZIWEI = "ziwei"           # 紫微斗数
    BAZI = "bazi"             # 子平八字
    QIMEN = "qimen"           # 奇门遁甲
    QIZHENG_SIYU = "qizheng_siyu"  # 七政四余
    SHAOZI_YISHU = "shaozi_yishu"  # 邵子易数
    HUANGJI_SHU = "huangji_shu"      # 皇极数
    DALIU_REN = "daliu_ren"            # 大六壬
    MEIHUA_YISHU = "meihua_yishu"      # 梅花易数
    LIUYAO = "liuyao"                  # 六爻
    XIAOCHENG_TU = "xiaocheng_tu"      # 小成图
    DAYAN_SHIFA = "dayan_shifa"        # 大衍筮法
    SHENYI_SHU = "shenyi_shu"          # 神易术
    DADING_SHU = "dading_shu"          # 大定数
    CEGUI_SHU = "cegui_shu"            # 策轨数
    HELUO_SHU = "heluo_shu"            # 河洛数
    YUZI_SHU = "yuzi_shu"              # 愚子数
    FANWEI_SHU = "fanwei_shu"          # 范围数
    SUANPAN_SHU = "suanpan_shu"        # 算盘数
    YELV_SHU = "yelv_shu"              # 耶律数


class Gender(str, Enum):
    """性别枚举"""
    MALE = "male"
    FEMALE = "female"


class Location(BaseModel):
    """地理位置"""
    longitude: float = Field(description="经度")
    latitude: float = Field(description="纬度")
    timezone: str = Field(default="Asia/Shanghai", description="时区")
    name: Optional[str] = Field(default=None, description="地点名称")


class BirthInfo(BaseModel):
    """出生信息"""
    birth_time: datetime = Field(description="出生时间")
    gender: Gender = Field(description="性别")
    location: Location = Field(description="出生地点")
    is_lunar: bool = Field(default=False, description="是否农历")

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ChartMetadata(BaseModel):
    """命盘元数据"""
    chart_id: str = Field(description="命盘ID")
    chart_type: ChartType = Field(description="命盘类型")
    birth_info: BirthInfo = Field(description="出生信息")
    generated_at: datetime = Field(default_factory=datetime.now, description="生成时间")
    calculation_version: str = Field(default="1.0.0", description="计算版本")
    source: str = Field(default="mingli-engine", description="计算来源")
    notes: Optional[str] = Field(default=None, description="备注")

    @classmethod
    def generate_id(cls, birth_time: datetime, chart_type: ChartType) -> str:
        """根据出生时间和类型生成唯一ID"""
        content = f"{birth_time.isoformat()}_{chart_type.value}"
        return hashlib.md5(content.encode()).hexdigest()[:12]


class BaseChartData(BaseModel):
    """命盘数据基类"""
    metadata: ChartMetadata = Field(description="命盘元数据")
    data: Dict[str, Any] = Field(default_factory=dict, description="命盘数据")

    def to_json(self, **kwargs) -> str:
        """序列化为JSON"""
        return self.model_dump_json(**kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        """序列化为字典"""
        return self.model_dump(**kwargs)


class BaseEngine(ABC):
    """排盘引擎抽象基类"""

    chart_type: ChartType = None

    @abstractmethod
    def calculate(self, birth_info: BirthInfo) -> BaseChartData:
        """
        执行排盘计算

        Args:
            birth_info: 出生信息

        Returns:
            命盘数据
        """
        pass

    @abstractmethod
    def validate_input(self, birth_info: BirthInfo) -> bool:
        """
        验证输入参数

        Args:
            birth_info: 出生信息

        Returns:
            是否有效
        """
        pass

    def _create_metadata(self, birth_info: BirthInfo) -> ChartMetadata:
        """创建命盘元数据"""
        return ChartMetadata(
            chart_id=ChartMetadata.generate_id(birth_info.birth_time, self.chart_type),
            chart_type=self.chart_type,
            birth_info=birth_info,
        )


class EngineRegistry:
    """引擎注册表"""

    _engines: Dict[ChartType, type] = {}

    @classmethod
    def register(cls, chart_type: ChartType):
        """注册引擎"""
        def decorator(engine_class: type):
            cls._engines[chart_type] = engine_class
            return engine_class
        return decorator

    @classmethod
    def get_engine(cls, chart_type: ChartType) -> Optional[type]:
        """获取引擎类"""
        return cls._engines.get(chart_type)

    @classmethod
    def list_engines(cls) -> List[ChartType]:
        """列出所有注册的引擎"""
        return list(cls._engines.keys())


def export_chart(chart: BaseChartData, format: str = "json") -> str:
    """
    导出命盘

    Args:
        chart: 命盘数据
        format: 导出格式 (json/dict)

    Returns:
        导出字符串
    """
    if format == "json":
        return chart.to_json(indent=2)
    elif format == "dict":
        return str(chart.to_dict())
    else:
        raise ValueError(f"Unsupported format: {format}")
