"""推演规则模型"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
    Index,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class Rule(Base):
    """推演规则模型"""
    __tablename__ = "rules"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    rule_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    rule_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    system: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    source_book_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "ancient_books.id",
            ondelete="SET NULL",
            onupdate="CASCADE"
        ),
        nullable=True,
        index=True
    )
    source_chapter: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source_page: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    condition: Mapped[str] = mapped_column(Text, nullable=False)
    result: Mapped[str] = mapped_column(Text, nullable=False)
    explanation: Mapped[str] = mapped_column(Text, nullable=False)

    verification_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending"
    )
    verification_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="theory"
    )
    verified_cases: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    disputes: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)

    school: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    alternative_rules: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)

    review_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending"
    )

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

    source_book: Mapped[Optional["AncientBook"]] = relationship(
        "AncientBook",
        foreign_keys=[source_book_id]
    )

    __table_args__ = (
        Index("ix_rules_system_rule_type", "system", "rule_type"),
        Index("ix_rules_school", "school"),
        Index("ix_rules_review_status", "review_status"),
    )

    def __repr__(self) -> str:
        return f"<Rule(id={self.id}, rule_name='{self.rule_name}', system='{self.system}')>"
