"""古籍模式定义"""

from datetime import datetime
from typing import Optional, List, Any
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class BookSectionBase(BaseModel):
    """古籍章节基础模式"""
    chapter: str = Field(..., min_length=1, max_length=255, description="章节名")
    section: Optional[str] = Field(None, max_length=255, description="小节名")
    page_start: int = Field(0, ge=0, description="起始页")
    page_end: int = Field(0, ge=0, description="结束页")
    content: str = Field(..., description="章节内容")
    key_concepts: List[str] = Field(default_factory=list, description="关键概念")


class BookSectionCreate(BookSectionBase):
    """创建古籍章节"""
    book_id: UUID = Field(..., description="关联古籍ID")


class BookSectionUpdate(BaseModel):
    """更新古籍章节"""
    chapter: Optional[str] = Field(None, min_length=1, max_length=255)
    section: Optional[str] = Field(None, max_length=255)
    page_start: Optional[int] = Field(None, ge=0)
    page_end: Optional[int] = Field(None, ge=0)
    content: Optional[str] = None
    key_concepts: Optional[List[str]] = None


class BookSectionResponse(BookSectionBase):
    """古籍章节响应"""
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    book_id: UUID
    created_at: datetime
    updated_at: datetime


class AncientBookBase(BaseModel):
    """古籍基础模式"""
    title: str = Field(..., min_length=1, max_length=255, description="书名")
    author: Optional[str] = Field(None, max_length=255, description="作者")
    dynasty: str = Field(..., min_length=1, max_length=50, description="朝代")
    category: str = Field(..., description="分类：ziwei/bazi/qimen/yijing/other")
    version: Optional[str] = Field(None, max_length=255, description="版本信息")
    source: str = Field(..., description="来源：public_domain/authorized/unknown")
    content: str = Field(..., description="完整文本内容")
    chapters: dict = Field(default_factory=dict, description="章节结构")
    keywords: List[str] = Field(default_factory=list, description="关键词索引")
    citations: List[dict] = Field(default_factory=list, description="引用关系")
    notes: Optional[str] = Field(None, description="备注")


class AncientBookCreate(AncientBookBase):
    """创建古籍"""
    pass


class AncientBookUpdate(BaseModel):
    """更新古籍"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, max_length=255)
    dynasty: Optional[str] = Field(None, min_length=1, max_length=50)
    category: Optional[str] = None
    version: Optional[str] = Field(None, max_length=255)
    source: Optional[str] = None
    content: Optional[str] = None
    chapters: Optional[dict] = None
    keywords: Optional[List[str]] = None
    citations: Optional[List[dict]] = None
    notes: Optional[str] = None


class AncientBookResponse(AncientBookBase):
    """古籍响应"""
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime


class AncientBookDetailResponse(AncientBookResponse):
    """古籍详情响应（含章节）"""
    sections: List[BookSectionResponse] = Field(default_factory=list)


class AncientBookListResponse(BaseModel):
    """古籍列表响应"""
    items: List[AncientBookResponse]
    total: int
    page: int
    page_size: int
