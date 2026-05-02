"""知识条目模型"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    Index,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class KnowledgeEntry(Base):
    """知识条目模型"""
    __tablename__ = "knowledge_entries"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    term: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    pinyin: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    system: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )

    source_type: Mapped[str] = mapped_column(String(50), nullable=False)
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
    source_author: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source_url: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)

    original_content: Mapped[str] = mapped_column(Text, nullable=False)
    interpretation: Mapped[str] = mapped_column(Text, nullable=False)
    verification_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending"
    )

    related_entries: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    tags: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    difficulty_level: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    view_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    reference_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    accuracy_rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    review_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending"
    )
    reviewed_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
            onupdate="CASCADE"
        ),
        nullable=True
    )
    reviewed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
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
        Index("ix_knowledge_entries_system_category", "system", "category"),
        Index("ix_knowledge_entries_term_pinyin", "term", "pinyin"),
        Index("ix_knowledge_entries_review_status", "review_status"),
        Index("ix_knowledge_entries_verification_status", "verification_status"),
    )

    def __repr__(self) -> str:
        return f"<KnowledgeEntry(id={self.id}, term='{self.term}', system='{self.system}')>"
