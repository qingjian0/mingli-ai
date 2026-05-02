"""古籍数据库仓储模块"""

from app.knowledge.repository.ancient_book_repo import AncientBookRepository
from app.knowledge.repository.knowledge_repo import KnowledgeRepository
from app.knowledge.repository.rule_repo import RuleRepository

__all__ = [
    "AncientBookRepository",
    "KnowledgeRepository",
    "RuleRepository",
]
