from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict


class AnalysisBase(BaseModel):
    analysis_type: str = Field(..., max_length=50)
    summary: Optional[str] = None


class AnalysisCreate(AnalysisBase):
    chart_id: int
    content: Dict[str, Any]


class AnalysisUpdate(BaseModel):
    summary: Optional[str] = None
    content: Optional[Dict[str, Any]] = None


class AnalysisResponse(AnalysisBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chart_id: int
    user_id: int
    content: Dict[str, Any]
    confidence: Optional[float]
    ai_model: Optional[str]
    ai_tokens_used: Optional[int]
    is_completed: bool
    is_shared: bool
    version: str
    created_at: datetime
    updated_at: datetime


class AnalysisBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    analysis_type: str
    summary: Optional[str]
    is_completed: bool
    created_at: datetime


class AnalysisRequest(BaseModel):
    chart_id: int
    analysis_type: str = Field(..., max_length=50)
    options: Optional[Dict[str, Any]] = None


class AnalysisResult(BaseModel):
    analysis_id: int
    analysis_type: str
    content: Dict[str, Any]
    summary: str
    confidence: float
    tokens_used: int


class AnalysisListResponse(BaseModel):
    items: List[AnalysisBrief]
    total: int
    page: int
    page_size: int
