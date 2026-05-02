"""审核任务模型"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    Index,
    JSON,
    Integer,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class ReviewTask(Base):
    """审核任务模型"""
    __tablename__ = "review_tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    entry_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    entry_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )
    review_level: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1
    )
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending",
        index=True
    )
    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="medium"
    )

    reviewer_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
            onupdate="CASCADE"
        ),
        nullable=True,
        index=True
    )
    review_notes: Mapped[str] = mapped_column(Text, nullable=False, default="")
    review_result: Mapped[str] = mapped_column(String(50), nullable=False, default="")
    review_evidence: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)

    has_dispute: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    dispute_reason: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    dispute_resolution: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    assigned_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    __table_args__ = (
        Index("ix_review_tasks_entry", "entry_type", "entry_id"),
        Index("ix_review_tasks_status_priority", "status", "priority"),
        Index("ix_review_tasks_reviewer_status", "reviewer_id", "status"),
    )

    def __repr__(self) -> str:
        return f"<ReviewTask(id={self.id}, entry_type='{self.entry_type}', status='{self.status}')>"
