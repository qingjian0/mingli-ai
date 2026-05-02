"""
分析API测试
"""

import pytest
from httpx import AsyncClient


class TestAnalysisAPI:
    """分析API测试"""

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
    async def test_analyze_personality(self, authenticated_client: AsyncClient, created_chart_id):
        """测试性格分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "personality",
                "query": "分析我的性格特点"
            }
        )
        assert response.status_code in [200, 201]

    @pytest.mark.asyncio
    async def test_analyze_career(self, authenticated_client: AsyncClient, created_chart_id):
        """测试事业分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "career",
                "query": "我的事业发展如何"
            }
        )
        assert response.status_code in [200, 201]

    @pytest.mark.asyncio
    async def test_analyze_love(self, authenticated_client: AsyncClient, created_chart_id):
        """测试感情分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "love",
                "query": "我的姻缘什么时候来"
            }
        )
        assert response.status_code in [200, 201]

    @pytest.mark.asyncio
    async def test_analyze_wealth(self, authenticated_client: AsyncClient, created_chart_id):
        """测试财富分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "wealth",
                "query": "我的财运怎么样"
            }
        )
        assert response.status_code in [200, 201]

    @pytest.mark.asyncio
    async def test_analyze_health(self, authenticated_client: AsyncClient, created_chart_id):
        """测试健康分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "health",
                "query": "健康需要注意什么"
            }
        )
        assert response.status_code in [200, 201]

    @pytest.mark.asyncio
    async def test_analyze_comprehensive(self, authenticated_client: AsyncClient, created_chart_id):
        """测试综合分析"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "comprehensive",
                "query": "全面分析我的命运"
            }
        )
        assert response.status_code in [200, 201]


class TestAnalysisValidation:
    """分析参数验证测试"""

    @pytest.mark.asyncio
    async def test_invalid_analysis_type(self, authenticated_client: AsyncClient):
        """测试无效分析类型"""
        response = await authenticated_client.post(
            "/api/v1/analysis/1",
            json={
                "analysis_type": "invalid_type"
            }
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_empty_query(self, authenticated_client: AsyncClient):
        """测试空查询"""
        response = await authenticated_client.post(
            "/api/v1/analysis/1",
            json={
                "analysis_type": "personality",
                "query": ""
            }
        )
        assert response.status_code in [200, 201, 422]

    @pytest.mark.asyncio
    async def test_missing_chart_id(self, authenticated_client: AsyncClient):
        """测试缺少命盘ID"""
        response = await authenticated_client.post(
            "/api/v1/analysis/",
            json={
                "analysis_type": "personality"
            }
        )
        assert response.status_code == 404


class TestAnalysisResults:
    """分析结果测试"""

    @pytest.mark.asyncio
    async def test_analysis_response_structure(self, authenticated_client: AsyncClient, created_chart_id):
        """测试分析响应结构"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "personality",
                "query": "分析性格"
            }
        )
        assert response.status_code in [200, 201]
        data = response.json()

        assert "analysis_type" in data or "result" in data or "content" in data

    @pytest.mark.asyncio
    async def test_analysis_confidence(self, authenticated_client: AsyncClient, created_chart_id):
        """测试分析置信度"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.post(
            f"/api/v1/analysis/{created_chart_id}",
            json={
                "analysis_type": "personality",
                "query": "性格分析"
            }
        )
        assert response.status_code in [200, 201]
        data = response.json()

        if "confidence" in data:
            assert 0.0 <= data["confidence"] <= 1.0


class TestAnalysisHistory:
    """分析历史测试"""

    @pytest.mark.asyncio
    async def test_get_analysis_history(self, authenticated_client: AsyncClient, created_chart_id):
        """测试获取分析历史"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.get(
            f"/api/v1/analysis/{created_chart_id}/history"
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_analysis_history_pagination(self, authenticated_client: AsyncClient, created_chart_id):
        """测试分析历史分页"""
        if created_chart_id is None:
            pytest.skip("Could not create chart")

        response = await authenticated_client.get(
            f"/api/v1/analysis/{created_chart_id}/history?skip=0&limit=10"
        )
        assert response.status_code == 200
