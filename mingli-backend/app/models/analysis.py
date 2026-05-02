from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    chart_id = Column(Integer, ForeignKey("charts.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # 分析类型
    analysis_type = Column(String(50), nullable=False)  # personality, career, love, health, fortune, etc.

    # 分析内容（JSON格式存储）
    content = Column(JSON, nullable=False)

    # 分析摘要
    summary = Column(Text, nullable=True)

    # 置信度（0-1）
    confidence = Column(Float, nullable=True)

    # AI模型使用
    ai_model = Column(String(100), nullable=True)
    ai_tokens_used = Column(Integer, nullable=True)

    # 状态
    is_completed = Column(Boolean, default=True, nullable=False)
    is_shared = Column(Boolean, default=False, nullable=False)

    # 版本
    version = Column(String(50), default="1.0", nullable=False)

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # 关系
    chart = relationship("Chart", back_populates="analyses")
