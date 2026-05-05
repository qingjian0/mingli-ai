from fastapi import APIRouter
from app.api.v1 import auth, profiles, charts, analysis
from app.api.v1 import knowledge, webhooks, plugins

api_router = APIRouter(prefix="/v1")

api_router.include_router(auth.router)
api_router.include_router(profiles.router)
api_router.include_router(charts.router)
api_router.include_router(analysis.router)
api_router.include_router(knowledge.router)
api_router.include_router(webhooks.router)
api_router.include_router(plugins.router)

__all__ = ["api_router"]
