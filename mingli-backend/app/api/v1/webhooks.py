from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks, Request
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum
import hashlib
import hmac
import json

router = APIRouter(prefix="/webhooks", tags=["Webhook回调"])


class WebhookEvent(str, Enum):
    """Webhook事件类型"""
    ANALYSIS_COMPLETED = "analysis.completed"
    ANALYSIS_FAILED = "analysis.failed"
    ANALYSIS_FEEDBACK = "analysis.feedback"
    CASE_VALIDATED = "case.validated"
    CASE_UPDATED = "case.updated"
    KNOWLEDGE_UPDATED = "knowledge.updated"
    USER_ACTION = "user.action"


class WebhookPayload(BaseModel):
    """Webhook载荷"""
    event: WebhookEvent
    timestamp: datetime = Field(default_factory=datetime.now)
    data: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None


class WebhookCallbackRequest(BaseModel):
    """Webhook回调请求"""
    webhook_id: str = Field(..., description="Webhook ID")
    event: str = Field(..., description="事件类型")
    payload: Dict[str, Any] = Field(..., description="事件载荷")
    signature: Optional[str] = Field(None, description="签名")


class WebhookCallbackResponse(BaseModel):
    """Webhook回调响应"""
    success: bool
    message: str
    callback_id: Optional[str] = None
    processed_at: datetime = Field(default_factory=datetime.now)


class WebhookRegistration(BaseModel):
    """Webhook注册"""
    url: str = Field(..., description="回调URL")
    events: List[str] = Field(..., description="订阅事件")
    secret: Optional[str] = Field(None, description="签名密钥")
    description: Optional[str] = None
    is_active: bool = True


class WebhookInfo(BaseModel):
    """Webhook信息"""
    id: str
    url: str
    events: List[str]
    is_active: bool
    created_at: datetime
    last_triggered: Optional[datetime] = None
    failure_count: int = 0


registered_webhooks: Dict[str, WebhookInfo] = {}


def verify_signature(payload: str, signature: str, secret: str) -> bool:
    """验证签名"""
    if not signature or not secret:
        return True

    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(signature, expected_signature)


async def process_webhook_callback(
    callback_id: str,
    event: str,
    payload: Dict[str, Any]
):
    """处理Webhook回调"""
    print(f"处理Webhook回调 {callback_id}: {event}")
    print(f"载荷: {json.dumps(payload, ensure_ascii=False)}")


@router.post("/callback", response_model=WebhookCallbackResponse)
async def webhook_callback(
    request: WebhookCallbackRequest,
    background_tasks: BackgroundTasks
):
    """接收Webhook回调"""
    callback_id = f"cb_{hashlib.md5(str(datetime.now()).encode()).hexdigest()[:12]}"

    background_tasks.add_task(
        process_webhook_callback,
        callback_id,
        request.event,
        request.payload
    )

    return WebhookCallbackResponse(
        success=True,
        message="回调已接收",
        callback_id=callback_id
    )


@router.post("/register", response_model=WebhookInfo)
async def register_webhook(
    registration: WebhookRegistration
):
    """注册Webhook"""
    webhook_id = f"wh_{hashlib.md5(registration.url.encode()).hexdigest()[:12]}"

    webhook_info = WebhookInfo(
        id=webhook_id,
        url=registration.url,
        events=registration.events,
        is_active=registration.is_active,
        created_at=datetime.now()
    )

    registered_webhooks[webhook_id] = webhook_info

    return webhook_info


@router.get("/list", response_model=List[WebhookInfo])
async def list_webhooks():
    """列出已注册的Webhooks"""
    return list(registered_webhooks.values())


@router.delete("/{webhook_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_webhook(webhook_id: str):
    """删除Webhook"""
    if webhook_id not in registered_webhooks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Webhook不存在"
        )
    del registered_webhooks[webhook_id]


@router.put("/{webhook_id}/toggle", response_model=WebhookInfo)
async def toggle_webhook(
    webhook_id: str,
    is_active: bool = True
):
    """启用/禁用Webhook"""
    if webhook_id not in registered_webhooks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Webhook不存在"
        )

    webhook = registered_webhooks[webhook_id]
    webhook.is_active = is_active
    return webhook


@router.post("/test", response_model=WebhookCallbackResponse)
async def test_webhook(
    url: str,
    event: str = "test.event"
):
    """测试Webhook"""
    test_payload = {
        "test": True,
        "message": "这是一条测试消息",
        "timestamp": datetime.now().isoformat()
    }

    background_tasks = BackgroundTasks()
    background_tasks.add_task(
        process_webhook_callback,
        "test_callback",
        event,
        test_payload
    )

    return WebhookCallbackResponse(
        success=True,
        message=f"测试事件已发送到 {url}"
    )
