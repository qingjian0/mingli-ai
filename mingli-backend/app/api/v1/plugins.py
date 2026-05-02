from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum
import hashlib
import json

router = APIRouter(prefix="/plugins", tags=["插件管理"])


class PluginType(str, Enum):
    """插件类型"""
    ANALYSIS = "analysis"
    VISUALIZATION = "visualization"
    EXPORT = "export"
    IMPORT = "import"
    NOTIFICATION = "notification"
    CUSTOM = "custom"


class PluginStatus(str, Enum):
    """插件状态"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"
    UPDATING = "updating"


class PluginRegistration(BaseModel):
    """插件注册信息"""
    name: str = Field(..., min_length=1, max_length=100, description="插件名称")
    version: str = Field(..., description="插件版本")
    plugin_type: PluginType = Field(..., description="插件类型")
    description: Optional[str] = Field(None, description="插件描述")
    author: Optional[str] = Field(None, description="插件作者")
    homepage: Optional[str] = Field(None, description="插件主页")
    config_schema: Optional[Dict[str, Any]] = Field(None, description="配置Schema")
    capabilities: List[str] = Field(default_factory=list, description="插件能力")


class PluginInfo(BaseModel):
    """插件信息"""
    id: str
    name: str
    version: str
    plugin_type: PluginType
    description: Optional[str] = None
    author: Optional[str] = None
    homepage: Optional[str] = None
    status: PluginStatus = PluginStatus.INACTIVE
    config_schema: Optional[Dict[str, Any]] = None
    capabilities: List[str] = []
    installed_at: datetime
    last_updated: Optional[datetime] = None
    usage_count: int = 0


class PluginConfigUpdate(BaseModel):
    """插件配置更新"""
    config: Dict[str, Any]


class PluginResponse(BaseModel):
    """插件操作响应"""
    success: bool
    message: str
    plugin_id: Optional[str] = None


plugins_registry: Dict[str, PluginInfo] = {}
plugin_instances: Dict[str, Any] = {}


def generate_plugin_id(name: str) -> str:
    """生成插件ID"""
    return f"plg_{hashlib.md5(name.encode()).hexdigest()[:12]}"


async def initialize_plugin(plugin_info: PluginInfo) -> bool:
    """初始化插件"""
    try:
        plugin_id = plugin_info.id
        print(f"初始化插件 {plugin_id}: {plugin_info.name}")
        plugin_instances[plugin_id] = {
            "initialized": True,
            "timestamp": datetime.now()
        }
        return True
    except Exception as e:
        print(f"插件初始化失败: {e}")
        return False


async def shutdown_plugin(plugin_id: str) -> bool:
    """关闭插件"""
    try:
        if plugin_id in plugin_instances:
            del plugin_instances[plugin_id]
        return True
    except Exception as e:
        print(f"插件关闭失败: {e}")
        return False


@router.get("/", response_model=List[PluginInfo])
async def list_plugins(
    plugin_type: Optional[PluginType] = None,
    status: Optional[PluginStatus] = None
):
    """获取插件列表"""
    plugins = list(plugins_registry.values())

    if plugin_type:
        plugins = [p for p in plugins if p.plugin_type == plugin_type]
    if status:
        plugins = [p for p in plugins if p.status == status]

    return plugins


@router.get("/{plugin_id}", response_model=PluginInfo)
async def get_plugin(plugin_id: str):
    """获取插件详情"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )
    return plugins_registry[plugin_id]


@router.post("/register", response_model=PluginInfo)
async def register_plugin(
    registration: PluginRegistration,
    background_tasks: BackgroundTasks
):
    """注册插件"""
    plugin_id = generate_plugin_id(registration.name)

    if plugin_id in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="插件已存在"
        )

    plugin_info = PluginInfo(
        id=plugin_id,
        name=registration.name,
        version=registration.version,
        plugin_type=registration.plugin_type,
        description=registration.description,
        author=registration.author,
        homepage=registration.homepage,
        config_schema=registration.config_schema,
        capabilities=registration.capabilities,
        installed_at=datetime.now()
    )

    plugins_registry[plugin_id] = plugin_info

    background_tasks.add_task(initialize_plugin, plugin_info)

    return plugin_info


@router.delete("/{plugin_id}", response_model=PluginResponse)
async def uninstall_plugin(
    plugin_id: str,
    background_tasks: BackgroundTasks
):
    """卸载插件"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]

    background_tasks.add_task(shutdown_plugin, plugin_id)

    del plugins_registry[plugin_id]

    return PluginResponse(
        success=True,
        message=f"插件 {plugin_info.name} 已卸载",
        plugin_id=plugin_id
    )


@router.put("/{plugin_id}/config", response_model=PluginResponse)
async def update_plugin_config(
    plugin_id: str,
    config_update: PluginConfigUpdate
):
    """更新插件配置"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]
    print(f"更新插件 {plugin_id} 配置: {config_update.config}")

    return PluginResponse(
        success=True,
        message="配置已更新",
        plugin_id=plugin_id
    )


@router.post("/{plugin_id}/enable", response_model=PluginInfo)
async def enable_plugin(plugin_id: str):
    """启用插件"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]
    plugin_info.status = PluginStatus.ACTIVE

    success = await initialize_plugin(plugin_info)
    if not success:
        plugin_info.status = PluginStatus.ERROR
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="插件启用失败"
        )

    return plugin_info


@router.post("/{plugin_id}/disable", response_model=PluginInfo)
async def disable_plugin(
    plugin_id: str,
    background_tasks: BackgroundTasks
):
    """禁用插件"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]
    plugin_info.status = PluginStatus.INACTIVE

    background_tasks.add_task(shutdown_plugin, plugin_id)

    return plugin_info


@router.post("/{plugin_id}/invoke", response_model=Dict[str, Any])
async def invoke_plugin(
    plugin_id: str,
    action: str,
    params: Optional[Dict[str, Any]] = None
):
    """调用插件能力"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]

    if plugin_info.status != PluginStatus.ACTIVE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="插件未启用"
        )

    if action not in plugin_info.capabilities:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"插件不支持 {action} 能力"
        )

    plugin_info.usage_count += 1

    return {
        "success": True,
        "plugin_id": plugin_id,
        "action": action,
        "result": f"插件 {plugin_info.name} 执行了 {action}",
        "params": params or {}
    }


@router.get("/{plugin_id}/capabilities", response_model=List[str])
async def get_plugin_capabilities(plugin_id: str):
    """获取插件能力列表"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    return plugins_registry[plugin_id].capabilities


@router.post("/{plugin_id}/update", response_model=PluginResponse)
async def update_plugin(
    plugin_id: str,
    new_version: str
):
    """更新插件版本"""
    if plugin_id not in plugins_registry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="插件不存在"
        )

    plugin_info = plugins_registry[plugin_id]
    plugin_info.status = PluginStatus.UPDATING
    plugin_info.version = new_version
    plugin_info.last_updated = datetime.now()

    return PluginResponse(
        success=True,
        message=f"插件已更新到版本 {new_version}",
        plugin_id=plugin_id
    )
