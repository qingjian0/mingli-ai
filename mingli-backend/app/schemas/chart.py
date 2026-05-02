from datetime import datetime
from typing import Optional, List, Any, Dict
from pydantic import BaseModel, Field, ConfigDict
from app.models.chart import ChartType


class ChartBase(BaseModel):
    chart_type: ChartType = ChartType.BAZI
    name: Optional[str] = Field(None, max_length=200)
    notes: Optional[str] = None
    is_public: bool = False


class ChartCreate(ChartBase):
    profile_id: int
    chart_data: Dict[str, Any]


class ChartUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200)
    notes: Optional[str] = None
    is_public: Optional[bool] = None


class ChartResponse(ChartBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    chart_data: Dict[str, Any]
    version: str
    is_analyzed: bool
    share_code: Optional[str]
    created_at: datetime
    updated_at: datetime


class ChartBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chart_type: ChartType
    name: Optional[str]
    is_analyzed: bool
    created_at: datetime


class ChartShareResponse(BaseModel):
    share_code: str
    share_url: str


class ChartDataUpdate(BaseModel):
    chart_data: Dict[str, Any]
    version: Optional[str] = Field(None, max_length=50)
