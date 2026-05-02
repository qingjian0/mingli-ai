from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.database import get_db
from app.schemas.analysis import (
    AnalysisCreate, AnalysisUpdate, AnalysisResponse, AnalysisBrief,
    AnalysisRequest, AnalysisResult, AnalysisListResponse
)
from app.models.analysis import Analysis
from app.models.chart import Chart
from app.models.profile import Profile
from app.models.user import User
from app.api.deps import get_current_user_optional, get_pagination_params
from typing import List

router = APIRouter(prefix="/analysis", tags=["命盘分析"])


@router.post("/", response_model=AnalysisResponse, status_code=status.HTTP_201_CREATED)
async def create_analysis(
    analysis_data: AnalysisCreate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """创建分析记录"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == analysis_data.chart_id,
            Profile.user_id == current_user.id
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    analysis = Analysis(
        chart_id=analysis_data.chart_id,
        user_id=current_user.id,
        analysis_type=analysis_data.analysis_type,
        content=analysis_data.content,
        summary=analysis_data.summary
    )
    db.add(analysis)
    await db.commit()
    await db.refresh(analysis)
    return analysis


@router.get("/", response_model=AnalysisListResponse)
async def list_analyses(
    chart_id: int = Query(None, description="按命盘ID筛选"),
    analysis_type: str = Query(None, description="按分析类型筛选"),
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
    pagination: dict = Depends(get_pagination_params)
):
    """获取分析列表"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    query = (
        select(Analysis)
        .join(Chart)
        .join(Profile)
        .where(Profile.user_id == current_user.id)
    )

    if chart_id:
        query = query.where(Analysis.chart_id == chart_id)
    if analysis_type:
        query = query.where(Analysis.analysis_type == analysis_type)

    count_query = select(func.count()).select_from(query.subquery())
    count_result = await db.execute(count_query)
    total = count_result.scalar()

    result = await db.execute(
        query
        .offset(pagination["skip"])
        .limit(pagination["limit"])
        .order_by(Analysis.created_at.desc())
    )
    analyses = result.scalars().all()

    return AnalysisListResponse(
        items=analyses,
        total=total,
        page=pagination["page"],
        page_size=pagination["page_size"]
    )


@router.get("/{analysis_id}", response_model=AnalysisResponse)
async def get_analysis(
    analysis_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """获取分析详情"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Analysis)
        .join(Chart)
        .join(Profile)
        .where(
            Analysis.id == analysis_id,
            Profile.user_id == current_user.id
        )
    )
    analysis = result.scalar_one_or_none()

    if not analysis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分析记录不存在"
        )

    return analysis


@router.put("/{analysis_id}", response_model=AnalysisResponse)
async def update_analysis(
    analysis_id: int,
    analysis_data: AnalysisUpdate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """更新分析记录"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Analysis)
        .join(Chart)
        .join(Profile)
        .where(
            Analysis.id == analysis_id,
            Profile.user_id == current_user.id
        )
    )
    analysis = result.scalar_one_or_none()

    if not analysis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分析记录不存在"
        )

    update_data = analysis_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(analysis, field, value)

    await db.commit()
    await db.refresh(analysis)
    return analysis


@router.delete("/{analysis_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_analysis(
    analysis_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """删除分析记录"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Analysis)
        .join(Chart)
        .join(Profile)
        .where(
            Analysis.id == analysis_id,
            Profile.user_id == current_user.id
        )
    )
    analysis = result.scalar_one_or_none()

    if not analysis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分析记录不存在"
        )

    await db.delete(analysis)
    await db.commit()


@router.post("/request", response_model=AnalysisResponse, status_code=status.HTTP_202_ACCEPTED)
async def request_analysis(
    request: AnalysisRequest,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """请求AI命盘分析"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Chart)
        .join(Profile)
        .where(
            Chart.id == request.chart_id,
            Profile.user_id == current_user.id
        )
    )
    chart = result.scalar_one_or_none()

    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘不存在"
        )

    analysis = Analysis(
        chart_id=request.chart_id,
        user_id=current_user.id,
        analysis_type=request.analysis_type,
        content={},
        is_completed=False
    )
    db.add(analysis)
    await db.commit()
    await db.refresh(analysis)

    return analysis
