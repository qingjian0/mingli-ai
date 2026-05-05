from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Enum as SQLEnum, JSON, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class KnowledgeCategory(str, enum.Enum):
    """知识分类枚举"""
    CLASSICS = "classics"           # 古籍
    RULES = "rules"                 # 规则
    CASES = "cases"                 # 案例
    PARADIGMS = "paradigms"         # 范式
    PRINCIPLES = "principles"       # 原理
    TECHNIQUES = "techniques"       # 技法


class KnowledgeType(str, enum.Enum):
    """知识类型枚举"""
    TEXT = "text"                   # 文本
    FORMULA = "formula"             # 公式/规则
    CHART = "chart"                 # 命盘
    EXAMPLE = "example"             # 示例
    PRINCIPLE = "principle"         # 原理


class SourceType(str, enum.Enum):
    """来源类型枚举"""
    ANCIENT = "ancient"             # 古代典籍
    MODERN = "modern"               # 现代著作
    PRACTICE = "practice"           # 实践案例
    RESEARCH = "research"           # 学术研究
    ORAL = "oral"                   # 口传心授


class KnowledgeEntry(Base):
    """知识条目模型"""
    __tablename__ = "knowledge_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False, index=True)
    content = Column(Text, nullable=False)
    summary = Column(String(1000), nullable=True)

    category = Column(SQLEnum(KnowledgeCategory), nullable=False, index=True)
    knowledge_type = Column(SQLEnum(KnowledgeType), nullable=False, index=True)
    source_type = Column(SQLEnum(SourceType), nullable=False)

    source = Column(String(500), nullable=True)
    source_author = Column(String(200), nullable=True)
    page_reference = Column(String(200), nullable=True)

    tags = Column(JSON, default=list)
    entry_metadata = Column(JSON, default=dict)

    embedding = Column(JSON, nullable=True)

    verification_level = Column(String(10), default="C")
    is_verified = Column(Boolean, default=False)
    is_published = Column(Boolean, default=True)

    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)

    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    updated_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    creator = relationship("User", foreign_keys=[created_by], backref="created_knowledge")
    updater = relationship("User", foreign_keys=[updated_by], backref="updated_knowledge")
    related_from = relationship(
        "KnowledgeRelation",
        foreign_keys="KnowledgeRelation.from_entry_id",
        back_populates="from_entry",
        cascade="all, delete-orphan"
    )
    related_to = relationship(
        "KnowledgeRelation",
        foreign_keys="KnowledgeRelation.to_entry_id",
        back_populates="to_entry",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_knowledge_category_type", "category", "knowledge_type"),
        Index("idx_knowledge_created_at", "created_at"),
    )


class KnowledgeRelation(Base):
    """知识关联模型"""
    __tablename__ = "knowledge_relations"

    id = Column(Integer, primary_key=True, index=True)
    from_entry_id = Column(Integer, ForeignKey("knowledge_entries.id", ondelete="CASCADE"), nullable=False)
    to_entry_id = Column(Integer, ForeignKey("knowledge_entries.id", ondelete="CASCADE"), nullable=False)
    relation_type = Column(String(50), nullable=False, index=True)
    weight = Column(Integer, default=1)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    from_entry = relationship("KnowledgeEntry", foreign_keys=[from_entry_id], back_populates="related_from")
    to_entry = relationship("KnowledgeEntry", foreign_keys=[to_entry_id], back_populates="related_to")

    __table_args__ = (
        Index("idx_relation_from", "from_entry_id"),
        Index("idx_relation_to", "to_entry_id"),
    )


class KnowledgeCategoryModel(Base):
    """知识分类模型"""
    __tablename__ = "knowledge_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    code = Column(String(50), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(50), nullable=True)
    parent_id = Column(Integer, ForeignKey("knowledge_categories.id", ondelete="SET NULL"), nullable=True)
    sort_order = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    parent = relationship("KnowledgeCategoryModel", remote_side=[id], backref="children")


class ClassicText(Base):
    """古籍文本模型"""
    __tablename__ = "classic_texts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False, index=True)
    author = Column(String(200), nullable=True)
    dynasty = Column(String(50), nullable=True)
    category = Column(String(100), nullable=False, index=True)

    description = Column(Text, nullable=True)
    full_text = Column(Text, nullable=True)
    chapters = Column(JSON, default=list)

    source_url = Column(String(500), nullable=True)
    verification_level = Column(String(10), default="A")

    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    sections = relationship("ClassicSection", back_populates="text", cascade="all, delete-orphan")


class ClassicSection(Base):
    """古籍章节模型"""
    __tablename__ = "classic_sections"

    id = Column(Integer, primary_key=True, index=True)
    text_id = Column(Integer, ForeignKey("classic_texts.id", ondelete="CASCADE"), nullable=False)
    chapter = Column(String(200), nullable=False)
    section = Column(String(200), nullable=True)
    content = Column(Text, nullable=False)

    page_number = Column(Integer, nullable=True)
    line_start = Column(Integer, nullable=True)
    line_end = Column(Integer, nullable=True)

    annotations = Column(JSON, default=list)
    keywords = Column(JSON, default=list)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    text = relationship("ClassicText", back_populates="sections")

    __table_args__ = (
        Index("idx_section_text_chapter", "text_id", "chapter"),
    )


class CaseRecord(Base):
    """案例记录模型"""
    __tablename__ = "case_records"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    case_type = Column(String(100), nullable=False, index=True)
    system = Column(String(50), nullable=False, index=True)

    birth_info = Column(JSON, nullable=True)
    chart_data = Column(JSON, nullable=True)

    analysis_process = Column(Text, nullable=True)
    conclusion = Column(Text, nullable=True)
    result_feedback = Column(Text, nullable=True)

    tags = Column(JSON, default=list)
    entry_metadata = Column(JSON, default=dict)

    is_public = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    verified_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    verified_at = Column(DateTime(timezone=True), nullable=True)

    creator = relationship("User", foreign_keys=[created_by], backref="created_cases")
    verifier = relationship("User", foreign_keys=[verified_by], backref="verified_cases")

    __table_args__ = (
        Index("idx_case_type_system", "case_type", "system"),
    )


class CaseFeedback(Base):
    """案例反馈模型"""
    __tablename__ = "case_feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("case_records.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    feedback_type = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=True)

    is_resolved = Column(Boolean, default=False)
    resolution = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    case = relationship("CaseRecord", backref="feedbacks")
    user = relationship("User", backref="case_feedbacks")
