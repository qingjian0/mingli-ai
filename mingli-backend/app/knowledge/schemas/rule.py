"""规则模式定义"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class RuleBase(BaseModel):
    """规则基础模式"""
    rule_name: str = Field(..., min_length=1, max_length=255, description="规则名称")
    rule_type: str = Field(..., description="类型：calculation/interpretation/judgment")
    system: str = Field(..., description="所属体系")

    source_book_id: Optional[UUID] = Field(None, description="来源古籍ID")
    source_chapter: Optional[str] = Field(None, max_length=255, description="古籍章节")
    source_page: Optional[int] = Field(None, ge=0, description="页码")

    condition: str = Field(..., description="触发条件")
    result: str = Field(..., description="推演结果")
    explanation: str = Field(..., description="规则解释")

    verification_status: str = Field("pending", description="验证状态")
    verification_method: str = Field("theory", description="验证方法")
    verified_cases: List[dict] = Field(default_factory=list, description="验证案例")
    disputes: List[dict] = Field(default_factory=list, description="争议说明")

    school: Optional[str] = Field(None, max_length=100, description="所属流派")
    alternative_rules: List[str] = Field(default_factory=list, description="替代规则")


class RuleCreate(RuleBase):
    """创建规则"""
    pass


class RuleUpdate(BaseModel):
    """更新规则"""
    rule_name: Optional[str] = Field(None, min_length=1, max_length=255)
    rule_type: Optional[str] = None
    system: Optional[str] = None
    source_book_id: Optional[UUID] = None
    source_chapter: Optional[str] = Field(None, max_length=255)
    source_page: Optional[int] = Field(None, ge=0)
    condition: Optional[str] = None
    result: Optional[str] = None
    explanation: Optional[str] = None
    verification_status: Optional[str] = None
    verification_method: Optional[str] = None
    verified_cases: Optional[List[dict]] = None
    disputes: Optional[List[dict]] = None
    school: Optional[str] = Field(None, max_length=100)
    alternative_rules: Optional[List[str]] = None


class RuleResponse(RuleBase):
    """规则响应"""
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    review_status: str
    created_at: datetime
    updated_at: datetime


class RuleListResponse(BaseModel):
    """规则列表响应"""
    items: List[RuleResponse]
    total: int
    page: int
    page_size: int


class RuleSearchQuery(BaseModel):
    """规则搜索查询"""
    rule_name: Optional[str] = Field(None, description="规则名称关键词")
    rule_type: Optional[str] = Field(None, description="类型筛选")
    system: Optional[str] = Field(None, description="体系筛选")
    school: Optional[str] = Field(None, description="流派筛选")
    verification_status: Optional[str] = Field(None, description="验证状态筛选")
