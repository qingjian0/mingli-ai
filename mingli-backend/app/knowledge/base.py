from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime
from enum import Enum


class KnowledgeCategory(str, Enum):
    """知识分类枚举"""
    CLASSICS = "classics"           # 古籍
    RULES = "rules"                 # 规则
    CASES = "cases"                 # 案例
    PARADIGMS = "paradigms"         # 范式
    PRINCIPLES = "principles"       # 原理
    TECHNIQUES = "techniques"       # 技法


class KnowledgeType(str, Enum):
    """知识类型枚举"""
    TEXT = "text"                   # 文本
    FORMULA = "formula"             # 公式/规则
    CHART = "chart"                 # 命盘
    EXAMPLE = "example"             # 示例
    PRINCIPLE = "principle"         # 原理


class SourceType(str, Enum):
    """来源类型枚举"""
    ANCIENT = "ancient"             # 古代典籍
    MODERN = "modern"               # 现代著作
    PRACTICE = "practice"           # 实践案例
    RESEARCH = "research"           # 学术研究
    ORAL = "oral"                   # 口传心授


class KnowledgeBase(ABC):
    """知识基类，定义知识条目的通用结构"""

    def __init__(
        self,
        id: Optional[int] = None,
        title: str = "",
        content: str = "",
        category: KnowledgeCategory = KnowledgeCategory.RULES,
        knowledge_type: KnowledgeType = KnowledgeType.TEXT,
        source_type: SourceType = SourceType.MODERN,
        source: Optional[str] = None,
        page_reference: Optional[str] = None,
        tags: List[str] = None,
        metadata: Dict[str, Any] = None,
        related_ids: List[int] = None,
        embedding: Optional[List[float]] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        created_by: Optional[int] = None,
        is_verified: bool = False,
        verification_level: str = "C"
    ):
        self.id = id
        self.title = title
        self.content = content
        self.category = category
        self.knowledge_type = knowledge_type
        self.source_type = source_type
        self.source = source
        self.page_reference = page_reference
        self.tags = tags or []
        self.metadata = metadata or {}
        self.related_ids = related_ids or []
        self.embedding = embedding
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by
        self.is_verified = is_verified
        self.verification_level = verification_level

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        pass

    @abstractmethod
    def validate(self) -> bool:
        """验证知识条目"""
        pass

    def get_summary(self, max_length: int = 200) -> str:
        """获取摘要"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."

    def add_tag(self, tag: str) -> None:
        """添加标签"""
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """移除标签"""
        if tag in self.tags:
            self.tags.remove(tag)

    def add_related(self, related_id: int) -> None:
        """添加关联"""
        if related_id not in self.related_ids:
            self.related_ids.append(related_id)

    def remove_related(self, related_id: int) -> None:
        """移除关联"""
        if related_id in self.related_ids:
            self.related_ids.remove(related_id)

    def to_search_text(self) -> str:
        """生成用于搜索的文本"""
        parts = [self.title, self.content]
        if self.source:
            parts.append(f"来源: {self.source}")
        if self.tags:
            parts.append(f"标签: {', '.join(self.tags)}")
        return " | ".join(parts)
