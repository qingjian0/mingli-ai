from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from app.models.profile import Gender


class ProfileBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    birth_date: date
    birth_time: str = Field(..., pattern=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    birth_time_type: str = Field(default="approx", pattern=r"^(precise|approx|unknown)$")
    birth_place: Optional[str] = Field(None, max_length=200)
    gender: Optional[Gender] = None
    longitude: Optional[str] = Field(None, max_length=20)
    chart_type: str = Field(default="bazi", max_length=50)
    notes: Optional[str] = None
    is_default: bool = False


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    birth_date: Optional[date] = None
    birth_time: Optional[str] = Field(None, pattern=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    birth_time_type: Optional[str] = Field(None, pattern=r"^(precise|approx|unknown)$")
    birth_place: Optional[str] = Field(None, max_length=200)
    gender: Optional[Gender] = None
    longitude: Optional[str] = Field(None, max_length=20)
    chart_type: Optional[str] = Field(None, max_length=50)
    notes: Optional[str] = None
    is_default: Optional[bool] = None


class ProfileResponse(ProfileBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: date
    updated_at: date


class ProfileBrief(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    birth_date: date
    chart_type: str
    is_default: bool
