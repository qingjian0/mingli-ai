"""
命盘API测试
"""

import pytest
from httpx import AsyncClient


class TestChartsAPI:
    """命盘API测试"""

    @pytest.fixture
    async def created_chart_id(self, authenticated_client: AsyncClient):
        """创建测试命盘"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi",
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "birth_place": "北京",
                "gender": "male"
            }
        )
        if response.status_code == 201:
            return response.json()["id"]
        return None

    @pytest.mark.asyncio
    async def test_create_bazi_chart(self, authenticated_client: AsyncClient):
        """测试创建八字命盘"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi",
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "birth_place": "北京",
                "gender": "male"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["chart_type"] == "bazi"

    @pytest.mark.asyncio
    async def test_create_ziwei_chart(self, authenticated_client: AsyncClient):
        """测试创建紫微斗数命盘"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "ziwei",
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "birth_place": "上海",
                "gender": "female"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["chart_type"] == "ziwei"

    @pytest.mark.asyncio
    async def test_create_qimen_chart(self, authenticated_client: AsyncClient):
        """测试创建奇门遁甲命盘"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "qimen",
                "birth_date": "2024-01-01",
                "birth_time": "08:00",
                "birth_place": "广州",
                "gender": "male"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["chart_type"] == "qimen"

    @pytest.mark.asyncio
    async def test_list_charts(self, authenticated_client: AsyncClient):
        """测试获取命盘列表"""
        response = await authenticated_client.get("/api/v1/charts/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_get_chart_by_id(self, authenticated_client: AsyncClient, created_chart_id):
        """测试根据ID获取命盘"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.get(f"/api/v1/charts/{created_chart_id}")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_get_chart_not_found(self, authenticated_client: AsyncClient):
        """测试获取不存在的命盘"""
        response = await authenticated_client.get("/api/v1/charts/99999")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_delete_chart(self, authenticated_client: AsyncClient, created_chart_id):
        """测试删除命盘"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.delete(f"/api/v1/charts/{created_chart_id}")
        assert response.status_code == 204


class TestChartValidation:
    """命盘参数验证测试"""

    @pytest.mark.asyncio
    async def test_invalid_chart_type(self, authenticated_client: AsyncClient):
        """测试无效命盘类型"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "invalid_type",
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "gender": "male"
            }
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_invalid_birth_date(self, authenticated_client: AsyncClient):
        """测试无效出生日期"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi",
                "birth_date": "not-a-date",
                "birth_time": "14:30",
                "gender": "male"
            }
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_invalid_gender(self, authenticated_client: AsyncClient):
        """测试无效性别"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi",
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "gender": "unknown"
            }
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_missing_required_fields(self, authenticated_client: AsyncClient):
        """测试缺少必填字段"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi"
            }
        )
        assert response.status_code == 422


class TestChartCalculation:
    """命盘计算测试"""

    @pytest.mark.asyncio
    async def test_chart_contains_four_pillars(self, authenticated_client: AsyncClient):
        """测试命盘包含四柱"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "bazi",
                "birth_date": "2000-01-01",
                "birth_time": "12:00",
                "gender": "male"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert "four_pillars" in data

    @pytest.mark.asyncio
    async def test_ziwei_chart_contains_palaces(self, authenticated_client: AsyncClient):
        """测试紫微斗数命盘包含宫位"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "ziwei",
                "birth_date": "2000-01-01",
                "birth_time": "12:00",
                "gender": "female"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert "palaces" in data or "ming_gong" in data

    @pytest.mark.asyncio
    async def test_qimen_chart_contains_palaces(self, authenticated_client: AsyncClient):
        """测试奇门遁甲命盘包含九宫"""
        response = await authenticated_client.post(
            "/api/v1/charts/",
            json={
                "chart_type": "qimen",
                "birth_date": "2024-01-01",
                "birth_time": "12:00",
                "gender": "male"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert "palaces" in data or "dun_type" in data
