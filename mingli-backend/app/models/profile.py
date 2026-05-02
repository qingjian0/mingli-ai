from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Enum as SQLEnum, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)

    # 出生信息
    birth_date = Column(Date, nullable=False)
    birth_time = Column(String(10), nullable=False)  # 格式: HH:MM
    birth_time_type = Column(String(20), default="approx")  # precise, approx, unknown
    birth_place = Column(String(200), nullable=True)
    gender = Column(SQLEnum(Gender), nullable=True)

    # 经度信息（用于真太阳时计算）
    longitude = Column(String(20), nullable=True)

    # 命盘类型
    chart_type = Column(String(50), default="bazi")  # bazi, ziwei, ttmp, etc.

    # 备注
    notes = Column(Text, nullable=True)

    # 状态
    is_default = Column(Boolean, default=False, nullable=False)

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # 关系
    user = relationship("User", back_populates="profiles")
    charts = relationship("Chart", back_populates="profile", cascade="all, delete-orphan")
