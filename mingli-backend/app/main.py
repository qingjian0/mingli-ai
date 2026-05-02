from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

from app.config import settings
from app.database import init_db, close_db
from app.core.logging import setup_logging, logger
from app.api.v1 import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    setup_logging()
    logger.info(f"启动 {settings.app_name} v{settings.app_version}")
    await init_db()
    logger.info("数据库连接已初始化")
    yield
    logger.info("正在关闭应用...")
    await close_db()
    logger.info("应用已关闭")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="""
    # 明理AI命理平台 API

    专业的AI命理分析平台，提供八字、紫微斗数、奇门遁甲等命理体系的分析服务。

    ## 功能特性

    - **用户认证**: JWT Token + API Key 双认证机制
    - **命盘管理**: 支持八字、紫微斗数、奇门遁甲三大命理体系
    - **AI分析**: 基于古籍知识的智能命盘分析
    - **知识库**: 丰富的命理古籍和案例库
    - **插件系统**: 可扩展的插件管理

    ## 认证方式

    ### Bearer Token
    ```
    Authorization: Bearer <access_token>
    ```

    ### API Key
    ```
    X-API-Key: <your_api_key>
    ```

    ## 速率限制

    - 匿名用户: 100请求/分钟
    - 已认证用户: 500请求/分钟
    - API Key用户: 1000请求/分钟
    - 管理员: 2000请求/分钟

    ## 可信度等级

    - **A**: 权威一手文献 / 核心期刊
    - **B**: 学位论文 / 学术专著
    - **C**: 网络文章 / 待验证
    """,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    openapi_tags=[
        {
            "name": "认证",
            "description": "用户注册、登录、Token管理"
        },
        {
            "name": "命盘",
            "description": "命盘排盘和管理"
        },
        {
            "name": "分析",
            "description": "命盘分析服务"
        },
        {
            "name": "知识库",
            "description": "知识条目CRUD和分类管理"
        },
        {
            "name": "古籍库",
            "description": "紫微斗数、八字、奇门古籍查询"
        },
        {
            "name": "案例库",
            "description": "命理案例管理和反馈"
        },
        {
            "name": "Webhook回调",
            "description": "Webhook注册和回调处理"
        },
        {
            "name": "插件管理",
            "description": "插件注册、启用、禁用"
        }
    ],
    contact={
        "name": "明理AI团队",
        "email": "support@mingli-ai.com",
        "url": "https://mingli-ai.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://mingli-ai.com/terms"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=settings.allowed_methods_list,
    allow_headers=settings.allowed_headers_list,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """请求验证异常处理"""
    logger.warning(f"请求验证失败: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "请求参数验证失败",
            "errors": exc.errors()
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """数据库异常处理"""
    logger.error(f"数据库错误: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "数据库操作失败"
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """通用异常处理"""
    logger.error(f"未处理的异常: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "服务器内部错误"
        }
    )


app.include_router(api_router, prefix="/api")


@app.get("/", tags=["信息"])
async def root():
    """根路径"""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": settings.app_description,
        "docs": "/docs",
        "openapi": "/openapi.json"
    }


@app.get("/health", tags=["信息"])
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "version": settings.app_version,
        "timestamp": "2026-05-02T00:00:00Z"
    }


@app.get("/api/info", tags=["信息"])
async def api_info():
    """API信息"""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "endpoints": {
            "auth": "/api/v1/auth",
            "profiles": "/api/v1/profiles",
            "charts": "/api/v1/charts",
            "analysis": "/api/v1/analysis",
            "knowledge": "/api/v1/knowledge",
            "classics": "/api/v1/classics",
            "cases": "/api/v1/cases",
            "webhooks": "/api/v1/webhooks",
            "plugins": "/api/v1/plugins"
        },
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json"
        }
    }
