import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    """测试根路径"""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """测试健康检查"""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    """测试用户注册"""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword123",
            "full_name": "New User"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["username"] == "newuser"
    assert "id" in data


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient, test_user):
    """测试重复邮箱注册"""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "anotheruser",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert "邮箱已被注册" in response.json()["detail"]


@pytest.mark.asyncio
async def test_login(client: AsyncClient, test_user):
    """测试登录"""
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, test_user):
    """测试错误密码登录"""
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user(authenticated_client: AsyncClient):
    """测试获取当前用户信息"""
    response = await authenticated_client.get("/api/v1/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_update_current_user(authenticated_client: AsyncClient):
    """测试更新当前用户信息"""
    response = await authenticated_client.put(
        "/api/v1/auth/me",
        json={"full_name": "Updated Name"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Updated Name"
