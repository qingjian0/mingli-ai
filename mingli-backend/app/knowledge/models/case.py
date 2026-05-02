"""验证案例模型"""

import uuid
from datetime import datetime, date, time
from typing import Optional, List

from sqlalchemy import (
    Column,
    String,
    Text,
    Float,
    Date,
    Time,
    DateTime,
    Index,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class Case(Base):
    """验证案例模型"""
    __tablename__ = "cases"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    case_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    system: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    case_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    birth_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    birth_time: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    gender: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    birth_location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    chart_data: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    chart_type: Mapped[str] = mapped_column(String(50), nullable=False)

    analysis: Mapped[str] = mapped_column(Text, nullable=False)
    result: Mapped[str] = mapped_column(Text, nullable=False)
    reasoning_chain: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)

    source: Mapped[str] = mapped_column(String(255), nullable=False)
    source_reference: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    accuracy_rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    user_feedback: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    actual_outcome: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    prediction_match: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    related_rules: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    related_entries: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    __table_args__ = (
        Index("ix_cases_system_case_type", "system", "case_type"),
        Index("ix_cases_birth_date", "birth_date"),
        Index("ix_cases_prediction_match", "prediction_match"),
    )

    def __repr__(self) -> str:
        return f"<Case(id={self.id}, case_name='{self.case_name}', system='{self.system}')>"
