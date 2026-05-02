"""古籍原典和章节模型"""

import uuid
from datetime import datetime
from typing import Optional, List

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
    Index,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class AncientBook(Base):
    """古籍原典模型"""
    __tablename__ = "ancient_books"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    author: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    dynasty: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    version: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    chapters: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    keywords: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    citations: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
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

    sections: Mapped[List["BookSection"]] = relationship(
        "BookSection",
        back_populates="book",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    __table_args__ = (
        Index("ix_ancient_books_category_dynasty", "category", "dynasty"),
        Index("ix_ancient_books_created_at", "created_at"),
    )

    def __repr__(self) -> str:
        return f"<AncientBook(id={self.id}, title='{self.title}', dynasty='{self.dynasty}')>"


class BookSection(Base):
    """古籍章节模型"""
    __tablename__ = "book_sections"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "ancient_books.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=False,
        index=True
    )
    chapter: Mapped[str] = mapped_column(String(255), nullable=False)
    section: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    page_start: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    page_end: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    key_concepts: Mapped[dict] = mapped_column(JSON, nullable=False, default=list)
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

    book: Mapped["AncientBook"] = relationship(
        "AncientBook",
        back_populates="sections"
    )

    __table_args__ = (
        Index("ix_book_sections_book_chapter", "book_id", "chapter"),
    )

    def __repr__(self) -> str:
        return f"<BookSection(id={self.id}, book_id={self.book_id}, chapter='{self.chapter}')>"
