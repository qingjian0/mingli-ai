from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.schemas.chart import ChartCreate, ChartUpdate, ChartResponse, ChartBrief, ChartShareResponse
from app.models.chart import Chart
from app.models.profile import Profile
from app.models.user import User
from app.api.deps import get_current_user_optional, get_pagination_params
from typing import List
import uuid
import secrets

router = APIRouter(prefix="/charts", tags=["命盘管理"])


@router.post("/", response_model=ChartResponse, status_code=status.HTTP_201_CREATED)
async def create_chart(
    chart_data: ChartCreate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """创建命盘"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Profile).where(
            Profile.id == chart_data.profile_id,
            Profile.user_id == current_user.id
        )
    )
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘信息不存在"
        )

    chart = Chart(
        profile_id=chart_data.profile_id,
        chart_type=chart_data.chart_type,
        chart_data=chart_data.chart_data,
        name=chart_data.name,
        notes=chart_data.notes,
        is_public=chart_data.is_public
    )
    db.add(chart)
    await db.commit()
    await db.refresh(chart)
    return chart


@router.get("/", response_model=List[ChartBrief])
async def list_charts(
    profile_id: int = Query(None, description="按命盘信息ID筛选"),
    chart_type: str = Query(None, description="按命盘类型筛选"),
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
    pagination: dict = Depends(get_pagination_params)
):
    """获取命盘列表"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    query = (
        select(Chart)
        .join(Profile)
        .where(Profile.user_id == current_user.id)
    )

    if profile_id:
        query = query.where(Chart.profile_id == profile_id)
    if chart_type:
        query = query.where(Chart.chart_type == chart_type)

    result = await db.execute(
        query
        .offset(pagination["skip"])
        .limit(pagination["limit"])
        .order_by(Chart.created_at.desc())
    )
    charts = result.scalars().all()
    return charts


@router.get("/{chart_id}", response_model=ChartResponse)
async def get_chart(
    chart_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """获取命盘详情"""
    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == chart_id,
            Profile.user_id == current_user.id if current_user else None
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    if not chart.is_public and (not current_user or chart.profile.user_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权访问此命盘"
        )

    return chart


@router.put("/{chart_id}", response_model=ChartResponse)
async def update_chart(
    chart_id: int,
    chart_data: ChartUpdate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """更新命盘"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == chart_id,
            Profile.user_id == current_user.id
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    update_data = chart_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(chart, field, value)

    await db.commit()
    await db.refresh(chart)
    return chart


@router.delete("/{chart_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chart(
    chart_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """删除命盘"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == chart_id,
            Profile.user_id == current_user.id
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    await db.delete(chart)
    await db.commit()


@router.post("/{chart_id}/share", response_model=ChartShareResponse)
async def share_chart(
    chart_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """生成分享链接"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == chart_id,
            Profile.user_id == current_user.id
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    if not chart.share_code:
        chart.share_code = secrets.token_urlsafe(16)

    chart.is_public = True
    await db.commit()

    return ChartShareResponse(
        share_code=chart.share_code,
        share_url=f"/share/{chart.share_code}"
    )
