from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.schemas.profile import ProfileCreate, ProfileUpdate, ProfileResponse, ProfileBrief
from app.models.profile import Profile
from app.models.user import User
from app.api.deps import get_current_user_optional, get_pagination_params
from typing import List

router = APIRouter(prefix="/profiles", tags=["命盘信息管理"])


@router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: ProfileCreate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """创建命盘信息"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    if profile_data.is_default:
        result = await db.execute(
            select(Profile).where(
                Profile.user_id == current_user.id,
                Profile.is_default == True
            )
        )
        default_profile = result.scalar_one_or_none()
        if default_profile:
            default_profile.is_default = False

    profile = Profile(
        user_id=current_user.id,
        **profile_data.model_dump()
    )
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile


@router.get("/", response_model=List[ProfileBrief])
async def list_profiles(
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
    pagination: dict = Depends(get_pagination_params)
):
    """获取当前用户的命盘列表"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Profile)
        .where(Profile.user_id == current_user.id)
        .offset(pagination["skip"])
        .limit(pagination["limit"])
        .order_by(Profile.created_at.desc())
    )
    profiles = result.scalars().all()
    return profiles


@router.get("/{profile_id}", response_model=ProfileResponse)
async def get_profile(
    profile_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """获取指定命盘信息"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Profile).where(
            Profile.id == profile_id,
            Profile.user_id == current_user.id
        )
    )
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘信息不存在"
        )

    return profile


@router.put("/{profile_id}", response_model=ProfileResponse)
async def update_profile(
    profile_id: int,
    profile_data: ProfileUpdate,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """更新命盘信息"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Profile).where(
            Profile.id == profile_id,
            Profile.user_id == current_user.id
        )
    )
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘信息不存在"
        )

    if profile_data.is_default and not profile.is_default:
        default_result = await db.execute(
            select(Profile).where(
                Profile.user_id == current_user.id,
                Profile.is_default == True,
                Profile.id != profile_id
            )
        )
        old_default = default_result.scalar_one_or_none()
        if old_default:
            old_default.is_default = False

    update_data = profile_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(profile, field, value)

    await db.commit()
    await db.refresh(profile)
    return profile


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    profile_id: int,
    current_user: User = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    """删除命盘信息"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登录"
        )

    result = await db.execute(
        select(Profile).where(
            Profile.id == profile_id,
            Profile.user_id == current_user.id
        )
    )
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="命盘信息不存在"
        )

    await db.delete(profile)
    await db.commit()
