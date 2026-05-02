from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class KnowledgeCategoryEnum(str, Enum):
    """知识分类枚举"""
    CLASSICS = "classics"
    RULES = "rules"
    CASES = "cases"
    PARADIGMS = "paradigms"
    PRINCIPLES = "principles"
    TECHNIQUES = "techniques"


class KnowledgeTypeEnum(str, Enum):
    """知识类型枚举"""
    TEXT = "text"
    FORMULA = "formula"
    CHART = "chart"
    EXAMPLE = "example"
    PRINCIPLE = "principle"


class SourceTypeEnum(str, Enum):
    """来源类型枚举"""
    ANCIENT = "ancient"
    MODERN = "modern"
    PRACTICE = "practice"
    RESEARCH = "research"
    ORAL = "oral"


class VerificationLevel(str, Enum):
    """可信度等级"""
    A = "A"
    B = "B"
    C = "C"


class KnowledgeEntryBase(BaseModel):
    """知识条目基础Schema"""
    title: str = Field(..., min_length=1, max_length=500, description="标题")
    content: str = Field(..., min_length=1, description="内容")
    summary: Optional[str] = Field(None, max_length=1000, description="摘要")
    category: KnowledgeCategoryEnum = Field(..., description="分类")
    knowledge_type: KnowledgeTypeEnum = Field(..., description="知识类型")
    source_type: SourceTypeEnum = Field(..., description="来源类型")
    source: Optional[str] = Field(None, max_length=500, description="来源")
    source_author: Optional[str] = Field(None, max_length=200, description="作者")
    page_reference: Optional[str] = Field(None, max_length=200, description="页码参考")
    tags: List[str] = Field(default_factory=list, description="标签")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    verification_level: VerificationLevel = Field(VerificationLevel.C, description="可信度等级")


class KnowledgeEntryCreate(KnowledgeEntryBase):
    """创建知识条目"""
    pass


class KnowledgeEntryUpdate(BaseModel):
    """更新知识条目"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    content: Optional[str] = Field(None, min_length=1)
    summary: Optional[str] = Field(None, max_length=1000)
    category: Optional[KnowledgeCategoryEnum] = None
    knowledge_type: Optional[KnowledgeTypeEnum] = None
    source_type: Optional[SourceTypeEnum] = None
    source: Optional[str] = Field(None, max_length=500)
    source_author: Optional[str] = Field(None, max_length=200)
    page_reference: Optional[str] = Field(None, max_length=200)
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    verification_level: Optional[VerificationLevel] = None
    is_published: Optional[bool] = None


class KnowledgeEntryResponse(KnowledgeEntryBase):
    """知识条目响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    embedding: Optional[List[float]] = None
    is_verified: bool
    is_published: bool
    view_count: int
    like_count: int
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime


class KnowledgeEntryBrief(BaseModel):
    """知识条目简略信息"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category: KnowledgeCategoryEnum
    knowledge_type: KnowledgeTypeEnum
    source_type: SourceTypeEnum
    verification_level: VerificationLevel
    tags: List[str]
    created_at: datetime


class KnowledgeRelationBase(BaseModel):
    """知识关联基础Schema"""
    to_entry_id: int = Field(..., description="目标条目ID")
    relation_type: str = Field(..., min_length=1, max_length=50, description="关联类型")
    weight: int = Field(1, ge=1, le=10, description="权重")


class KnowledgeRelationCreate(KnowledgeRelationBase):
    """创建知识关联"""
    pass


class KnowledgeRelationResponse(KnowledgeRelationBase):
    """知识关联响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    from_entry_id: int
    created_at: datetime
    to_entry: Optional[KnowledgeEntryBrief] = None


class KnowledgeCategoryBase(BaseModel):
    """知识分类基础Schema"""
    name: str = Field(..., min_length=1, max_length=100, description="分类名称")
    code: str = Field(..., min_length=1, max_length=50, description="分类编码")
    description: Optional[str] = None
    icon: Optional[str] = Field(None, max_length=50)
    parent_id: Optional[int] = None
    sort_order: int = Field(0, description="排序")


class KnowledgeCategoryCreate(KnowledgeCategoryBase):
    """创建知识分类"""
    pass


class KnowledgeCategoryUpdate(BaseModel):
    """更新知识分类"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    icon: Optional[str] = Field(None, max_length=50)
    parent_id: Optional[int] = None
    sort_order: Optional[int] = None


class KnowledgeCategoryResponse(KnowledgeCategoryBase):
    """知识分类响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    children: List["KnowledgeCategoryResponse"] = []


class KnowledgeSearchRequest(BaseModel):
    """知识搜索请求"""
    query: str = Field(..., min_length=1, description="搜索查询")
    category: Optional[KnowledgeCategoryEnum] = Field(None, description="按分类筛选")
    knowledge_type: Optional[KnowledgeTypeEnum] = Field(None, description="按知识类型筛选")
    tags: Optional[List[str]] = Field(None, description="按标签筛选")
    verification_level: Optional[VerificationLevel] = Field(None, description="按可信度筛选")
    limit: int = Field(20, ge=1, le=100, description="返回数量")
    offset: int = Field(0, ge=0, description="偏移量")


class KnowledgeSearchResult(BaseModel):
    """知识搜索结果"""
    entry: KnowledgeEntryBrief
    score: float = Field(..., description="相似度分数")
    highlights: List[str] = Field(default_factory=list, description="高亮片段")


class KnowledgeSearchResponse(BaseModel):
    """知识搜索响应"""
    results: List[KnowledgeSearchResult]
    total: int
    query: str


class KnowledgeListResponse(BaseModel):
    """知识列表响应"""
    items: List[KnowledgeEntryResponse]
    total: int
    page: int
    page_size: int


class ClassicTextBase(BaseModel):
    """古籍基础Schema"""
    title: str = Field(..., min_length=1, max_length=500, description="书名")
    author: Optional[str] = Field(None, max_length=200, description="作者")
    dynasty: Optional[str] = Field(None, max_length=50, description="朝代")
    category: str = Field(..., description="分类")
    description: Optional[str] = None
    source_url: Optional[str] = Field(None, max_length=500)


class ClassicTextCreate(ClassicTextBase):
    """创建古籍"""
    full_text: Optional[str] = None
    chapters: List[Dict[str, Any]] = Field(default_factory=list)


class ClassicTextUpdate(BaseModel):
    """更新古籍"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    author: Optional[str] = Field(None, max_length=200)
    dynasty: Optional[str] = Field(None, max_length=50)
    category: Optional[str] = None
    description: Optional[str] = None
    full_text: Optional[str] = None
    chapters: Optional[List[Dict[str, Any]]] = None
    source_url: Optional[str] = Field(None, max_length=500)


class ClassicTextResponse(ClassicTextBase):
    """古籍响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_text: Optional[str] = None
    chapters: List[Dict[str, Any]]
    verification_level: str
    view_count: int
    like_count: int
    created_at: datetime
    updated_at: datetime


class ClassicSectionBase(BaseModel):
    """古籍章节基础Schema"""
    chapter: str = Field(..., description="章节")
    section: Optional[str] = Field(None, description="小节")
    content: str = Field(..., description="内容")
    page_number: Optional[int] = None
    line_start: Optional[int] = None
    line_end: Optional[int] = None


class ClassicSectionCreate(ClassicSectionBase):
    """创建古籍章节"""
    text_id: int


class ClassicSectionResponse(ClassicSectionBase):
    """古籍章节响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    text_id: int
    annotations: List[Dict[str, Any]]
    keywords: List[str]
    created_at: datetime
    updated_at: datetime


class CaseRecordBase(BaseModel):
    """案例基础Schema"""
    title: str = Field(..., min_length=1, max_length=500, description="案例标题")
    case_type: str = Field(..., description="案例类型")
    system: str = Field(..., description="命理体系")
    birth_info: Optional[Dict[str, Any]] = None
    chart_data: Optional[Dict[str, Any]] = None
    analysis_process: Optional[str] = None
    conclusion: Optional[str] = None
    result_feedback: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CaseRecordCreate(CaseRecordBase):
    """创建案例"""
    pass


class CaseRecordUpdate(BaseModel):
    """更新案例"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    case_type: Optional[str] = None
    system: Optional[str] = None
    birth_info: Optional[Dict[str, Any]] = None
    chart_data: Optional[Dict[str, Any]] = None
    analysis_process: Optional[str] = None
    conclusion: Optional[str] = None
    result_feedback: Optional[str] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    is_public: Optional[bool] = None


class CaseRecordResponse(CaseRecordBase):
    """案例响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_public: bool
    is_verified: bool
    created_by: Optional[int] = None
    verified_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    verified_at: Optional[datetime] = None


class CaseFeedbackBase(BaseModel):
    """案例反馈基础Schema"""
    feedback_type: str = Field(..., description="反馈类型")
    content: str = Field(..., description="反馈内容")
    rating: Optional[int] = Field(None, ge=1, le=5, description="评分")


class CaseFeedbackCreate(CaseFeedbackBase):
    """创建案例反馈"""
    case_id: int


class CaseFeedbackUpdate(BaseModel):
    """更新案例反馈"""
    content: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    is_resolved: Optional[bool] = None
    resolution: Optional[str] = None


class CaseFeedbackResponse(CaseFeedbackBase):
    """案例反馈响应"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    case_id: int
    user_id: Optional[int] = None
    is_resolved: bool
    resolution: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class CaseListResponse(BaseModel):
    """案例列表响应"""
    items: List[CaseRecordResponse]
    total: int
    page: int
    page_size: int
