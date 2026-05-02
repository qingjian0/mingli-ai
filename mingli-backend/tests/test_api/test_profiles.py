import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_profile(authenticated_client: AsyncClient):
    """测试创建命盘信息"""
    response = await authenticated_client.post(
        "/api/v1/profiles/",
        json={
            "name": "Test Profile",
            "birth_date": "1990-01-01",
            "birth_time": "08:30",
            "birth_time_type": "precise",
            "birth_place": "北京",
            "gender": "male",
            "chart_type": "bazi"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Profile"
    assert data["birth_place"] == "北京"


@pytest.mark.asyncio
async def test_list_profiles(authenticated_client: AsyncClient):
    """测试获取命盘列表"""
    response = await authenticated_client.get("/api/v1/profiles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_profile_not_found(authenticated_client: AsyncClient):
    """测试获取不存在的命盘信息"""
    response = await authenticated_client.get("/api/v1/profiles/99999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_and_get_profile(authenticated_client: AsyncClient):
    """测试创建并获取命盘信息"""
    create_response = await authenticated_client.post(
        "/api/v1/profiles/",
        json={
            "name": "My Profile",
            "birth_date": "1995-06-15",
            "birth_time": "14:00",
            "birth_time_type": "approx",
            "chart_type": "bazi"
        }
    )
    assert create_response.status_code == 201
    profile_id = create_response.json()["id"]

    get_response = await authenticated_client.get(f"/api/v1/profiles/{profile_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "My Profile"
