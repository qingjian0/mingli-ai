"""案例模式定义"""

from datetime import datetime, date, time
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class CaseBase(BaseModel):
    """案例基础模式"""
    case_name: Optional[str] = Field(None, max_length=255, description="案例名称")
    system: str = Field(..., description="所属体系")
    case_type: str = Field(..., description="案例类型：historical/public/volunteer")

    birth_date: Optional[date] = Field(None, description="出生日期")
    birth_time: Optional[time] = Field(None, description="出生时间")
    gender: Optional[str] = Field(None, max_length=20, description="性别")
    birth_location: Optional[str] = Field(None, max_length=255, description="出生地")

    chart_data: dict = Field(default_factory=dict, description="命盘原始数据")
    chart_type: str = Field(..., description="命盘类型")

    analysis: str = Field(..., description="分析过程")
    result: str = Field(..., description="分析结论")
    reasoning_chain: List[dict] = Field(default_factory=list, description="推理链")

    source: str = Field(..., description="案例来源")
    source_reference: Optional[str] = Field(None, description="来源参考")

    accuracy_rating: Optional[float] = Field(None, ge=0, le=5, description="准确性评分")
    user_feedback: Optional[str] = Field(None, description="用户反馈")
    actual_outcome: Optional[str] = Field(None, description="实际结果")
    prediction_match: Optional[str] = Field(None, description="预测匹配度")

    related_rules: List[str] = Field(default_factory=list, description="关联规则")
    related_entries: List[str] = Field(default_factory=list, description="关联知识")


class CaseCreate(CaseBase):
    """创建案例"""
    pass


class CaseUpdate(BaseModel):
    """更新案例"""
    case_name: Optional[str] = Field(None, max_length=255)
    system: Optional[str] = None
    case_type: Optional[str] = None
    birth_date: Optional[date] = None
    birth_time: Optional[time] = None
    gender: Optional[str] = Field(None, max_length=20)
    birth_location: Optional[str] = Field(None, max_length=255)
    chart_data: Optional[dict] = None
    chart_type: Optional[str] = None
    analysis: Optional[str] = None
    result: Optional[str] = None
    reasoning_chain: Optional[List[dict]] = None
    source: Optional[str] = None
    source_reference: Optional[str] = None
    accuracy_rating: Optional[float] = Field(None, ge=0, le=5)
    user_feedback: Optional[str] = None
    actual_outcome: Optional[str] = None
    prediction_match: Optional[str] = None
    related_rules: Optional[List[str]] = None
    related_entries: Optional[List[str]] = None


class CaseResponse(CaseBase):
    """案例响应"""
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime


class CaseListResponse(BaseModel):
    """案例列表响应"""
    items: List[CaseResponse]
    total: int
    page: int
    page_size: int


class CaseSearchQuery(BaseModel):
    """案例搜索查询"""
    system: Optional[str] = Field(None, description="体系筛选")
    case_type: Optional[str] = Field(None, description="案例类型筛选")
    birth_date_from: Optional[date] = Field(None, description="出生日期起")
    birth_date_to: Optional[date] = Field(None, description="出生日期止")
    prediction_match: Optional[str] = Field(None, description="预测匹配度筛选")


class CaseStatistics(BaseModel):
    """案例统计"""
    total_cases: int
    verified_cases: int
    avg_accuracy: float
    by_system: dict
    by_case_type: dict
