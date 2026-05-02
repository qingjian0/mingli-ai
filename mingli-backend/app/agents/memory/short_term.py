"""
短期记忆模块

管理会话上下文信息，包括对话历史、当前分析状态等。
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import json
import uuid


@dataclass
class Message:
    """对话消息"""
    message_id: str
    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message_id": self.message_id,
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        data = data.copy()
        data["timestamp"] = datetime.fromisoformat(data["timestamp"])
        return cls(**data)


@dataclass
class SessionContext:
    """会话上下文"""
    session_id: str
    user_id: int
    profile_id: int
    created_at: datetime = field(default_factory=datetime.now)
    last_active: datetime = field(default_factory=datetime.now)
    messages: List[Message] = field(default_factory=list)
    current_analysis_state: Dict[str, Any] = field(default_factory=dict)
    context_variables: Dict[str, Any] = field(default_factory=dict)

    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> Message:
        message = Message(
            message_id=str(uuid.uuid4())[:8],
            role=role,
            content=content,
            metadata=metadata or {}
        )
        self.messages.append(message)
        self.last_active = datetime.now()
        return message

    def get_recent_messages(self, count: int = 10) -> List[Message]:
        return self.messages[-count:]

    def set_analysis_state(self, key: str, value: Any) -> None:
        self.current_analysis_state[key] = value
        self.last_active = datetime.now()

    def get_analysis_state(self, key: str) -> Optional[Any]:
        return self.current_analysis_state.get(key)

    def clear_analysis_state(self) -> None:
        self.current_analysis_state = {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "profile_id": self.profile_id,
            "created_at": self.created_at.isoformat(),
            "last_active": self.last_active.isoformat(),
            "messages": [m.to_dict() for m in self.messages],
            "current_analysis_state": self.current_analysis_state,
            "context_variables": self.context_variables
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SessionContext":
        data = data.copy()
        data["created_at"] = datetime.fromisoformat(data["created_at"])
        data["last_active"] = datetime.fromisoformat(data["last_active"])
        data["messages"] = [Message.from_dict(m) for m in data.get("messages", [])]
        return cls(**data)


class ShortTermMemory:
    """短期记忆管理器

    管理单个会话的上下文信息，支持对话历史存储和状态追踪。
    """

    def __init__(self, ttl_minutes: int = 60):
        self._sessions: Dict[str, SessionContext] = {}
        self._ttl_minutes = ttl_minutes

    def create_session(
        self,
        user_id: int,
        profile_id: int,
        session_id: Optional[str] = None
    ) -> SessionContext:
        session_id = session_id or str(uuid.uuid4())
        session = SessionContext(
            session_id=session_id,
            user_id=user_id,
            profile_id=profile_id
        )
        self._sessions[session_id] = session
        return session

    def get_session(self, session_id: str) -> Optional[SessionContext]:
        session = self._sessions.get(session_id)
        if session and self._is_session_valid(session):
            return session
        return None

    def _is_session_valid(self, session: SessionContext) -> bool:
        elapsed = (datetime.now() - session.last_active).total_seconds() / 60
        return elapsed < self._ttl_minutes

    def add_user_message(
        self,
        session_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[Message]:
        session = self.get_session(session_id)
        if session:
            return session.add_message("user", content, metadata)
        return None

    def add_assistant_message(
        self,
        session_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[Message]:
        session = self.get_session(session_id)
        if session:
            return session.add_message("assistant", content, metadata)
        return None

    def get_conversation_history(
        self,
        session_id: str,
        count: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        session = self.get_session(session_id)
        if not session:
            return []

        messages = session.messages
        if count:
            messages = messages[-count:]

        return [m.to_dict() for m in messages]

    def update_context(
        self,
        session_id: str,
        key: str,
        value: Any
    ) -> bool:
        session = self.get_session(session_id)
        if session:
            session.context_variables[key] = value
            session.last_active = datetime.now()
            return True
        return False

    def get_context(self, session_id: str, key: str) -> Optional[Any]:
        session = self.get_session(session_id)
        if session:
            return session.context_variables.get(key)
        return None

    def set_analysis_progress(
        self,
        session_id: str,
        stage: str,
        data: Dict[str, Any]
    ) -> bool:
        session = self.get_session(session_id)
        if session:
            session.set_analysis_state(stage, data)
            return True
        return False

    def get_analysis_progress(self, session_id: str) -> Dict[str, Any]:
        session = self.get_session(session_id)
        if session:
            return session.current_analysis_state
        return {}

    def clear_session(self, session_id: str) -> bool:
        if session_id in self._sessions:
            del self._sessions[session_id]
            return True
        return False

    def cleanup_expired_sessions(self) -> int:
        expired = [
            sid for sid, session in self._sessions.items()
            if not self._is_session_valid(session)
        ]
        for sid in expired:
            del self._sessions[sid]
        return len(expired)

    def serialize_session(self, session_id: str) -> Optional[str]:
        session = self._sessions.get(session_id)
        if session:
            return json.dumps(session.to_dict())
        return None

    def deserialize_session(self, data: str) -> Optional[SessionContext]:
        try:
            session_dict = json.loads(data)
            return SessionContext.from_dict(session_dict)
        except Exception:
            return None

    def list_active_sessions(self, user_id: Optional[int] = None) -> List[str]:
        session_ids = list(self._sessions.keys())
        if user_id is not None:
            session_ids = [
                sid for sid in session_ids
                if self._sessions[sid].user_id == user_id
                and self._is_session_valid(self._sessions[sid])
            ]
        return session_ids

    def get_session_count(self) -> int:
        return len(self._sessions)
