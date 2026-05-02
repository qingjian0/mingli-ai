"""知识条目模式定义"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class KnowledgeEntryBase(BaseModel):
    """知识条目基础模式"""
    term: str = Field(..., min_length=1, max_length=255, description="术语名称")
    pinyin: Optional[str] = Field(None, max_length=255, description="拼音")
    category: str = Field(..., description="分类：star/palace/combination/principle/technique")
    system: str = Field(..., description="所属体系：ziwei/bazi/qimen/yijing/other")

    source_type: str = Field(..., description="来源类型：source/ancient_book/case/expert")
    source_book_id: Optional[UUID] = Field(None, description="古籍来源ID")
    source_chapter: Optional[str] = Field(None, max_length=255, description="古籍章节")
    source_page: Optional[int] = Field(None, ge=0, description="页码")
    source_author: Optional[str] = Field(None, max_length=255, description="作者来源")
    source_url: Optional[str] = Field(None, max_length=1024, description="URL来源")

    original_content: str = Field(..., description="原典内容")
    interpretation: str = Field(..., description="权威解读")
    verification_status: str = Field("pending", description="验证状态：verified/pending/disputed")

    related_entries: List[str] = Field(default_factory=list, description="关联条目")
    tags: List[str] = Field(default_factory=list, description="标签")
    difficulty_level: int = Field(1, ge=1, le=5, description="难度等级 1-5")


class KnowledgeEntryCreate(KnowledgeEntryBase):
    """创建知识条目"""
    pass


class KnowledgeEntryUpdate(BaseModel):
    """更新知识条目"""
    term: Optional[str] = Field(None, min_length=1, max_length=255)
    pinyin: Optional[str] = Field(None, max_length=255)
    category: Optional[str] = None
    system: Optional[str] = None
    source_type: Optional[str] = None
    source_book_id: Optional[UUID] = None
    source_chapter: Optional[str] = Field(None, max_length=255)
    source_page: Optional[int] = Field(None, ge=0)
    source_author: Optional[str] = Field(None, max_length=255)
    source_url: Optional[str] = Field(None, max_length=1024)
    original_content: Optional[str] = None
    interpretation: Optional[str] = None
    verification_status: Optional[str] = None
    related_entries: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    difficulty_level: Optional[int] = Field(None, ge=1, le=5)


class KnowledgeEntryResponse(KnowledgeEntryBase):
    """知识条目响应"""
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    view_count: int
    reference_count: int
    accuracy_rating: float
    review_status: str
    reviewed_by: Optional[UUID] = None
    reviewed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime


class KnowledgeEntryListResponse(BaseModel):
    """知识条目列表响应"""
    items: List[KnowledgeEntryResponse]
    total: int
    page: int
    page_size: int


class KnowledgeEntrySearchQuery(BaseModel):
    """知识条目搜索查询"""
    term: Optional[str] = Field(None, description="术语名称关键词")
    category: Optional[str] = Field(None, description="分类筛选")
    system: Optional[str] = Field(None, description="体系筛选")
    verification_status: Optional[str] = Field(None, description="验证状态筛选")
    tags: Optional[List[str]] = Field(None, description="标签筛选")
