from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class ChartType(str, enum.Enum):
    BAZI = "bazi"  # 八字
    ZIWEI = "ziwei"  # 紫微斗数
    TMPM = "tmp"  # 铁板神数
    LIUYAO = "liuyao"  # 六爻
    QIMEN = "qimen"  # 奇门遁甲
    MEIHUA = "meihua"  # 梅花易数


class Chart(Base):
    __tablename__ = "charts"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    chart_type = Column(SQLEnum(ChartType), nullable=False, default=ChartType.BAZI)

    # 命盘数据（JSON格式存储）
    chart_data = Column(JSON, nullable=False)

    # 命盘名称/标题
    name = Column(String(200), nullable=True)

    # 分析版本
    version = Column(String(50), default="1.0", nullable=False)

    # 是否已分析
    is_analyzed = Column(Boolean, default=False, nullable=False)

    # 备注
    notes = Column(Text, nullable=True)

    # 分享信息
    is_public = Column(Boolean, default=False, nullable=False)
    share_code = Column(String(100), unique=True, nullable=True, index=True)

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # 关系
    profile = relationship("Profile", back_populates="charts")
    analyses = relationship("Analysis", back_populates="chart", cascade="all, delete-orphan")
