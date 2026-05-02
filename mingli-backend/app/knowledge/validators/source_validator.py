from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel


class SourceReference(BaseModel):
    """来源参考"""
    book_title: str
    author: Optional[str] = None
    dynasty: Optional[str] = None
    chapter: Optional[str] = None
    page: Optional[int] = None
    url: Optional[str] = None
    is_verified: bool = False


class SourceValidator:
    """来源验证器"""

    KNOWN_ANCIENT_BOOKS = {
        "紫微斗数全书": {"author": "陈公献", "dynasty": "明"},
        "渊海子平": {"author": "徐子平", "dynasty": "宋"},
        "滴天髓": {"author": "任铁樵", "dynasty": "清"},
        "穷通宝鉴": {"author": "余春台", "dynasty": "清"},
        "子平真诠": {"author": "沈孝瞻", "dynasty": "清"},
        "三命通会": {"author": "万民英", "dynasty": "明"},
        "奇门遁甲全书": {"author": None, "dynasty": "明"},
        "烟波钓叟赋": {"author": None, "dynasty": "宋"},
        "易经": {"author": "孔子", "dynasty": "春秋"},
        "周易正义": {"author": "王弼、孔颖达", "dynasty": "魏唐"},
    }

    def validate_source(self, source: SourceReference) -> Dict:
        """
        验证来源真实性

        Returns:
            {
                "is_valid": bool,
                "confidence": float,
                "issues": List[str],
                "suggestions": List[str]
            }
        """
        issues = []
        suggestions = []
        confidence = 1.0

        if source.book_title in self.KNOWN_ANCIENT_BOOKS:
            book_info = self.KNOWN_ANCIENT_BOOKS[source.book_title]

            if source.author and book_info.get("author"):
                if source.author != book_info["author"]:
                    issues.append(f"作者 '{source.author}' 与典籍记录不符")
                    confidence -= 0.2

            if source.dynasty and book_info.get("dynasty"):
                if source.dynasty != book_info["dynasty"]:
                    issues.append(f"朝代 '{source.dynasty}' 可能不正确")
                    confidence -= 0.1
        else:
            issues.append(f"典籍 '{source.book_title}' 未在已知列表中")
            confidence -= 0.3
            suggestions.append("请核实典籍名称是否正确")

        if not source.author:
            suggestions.append("建议补充作者信息")
            confidence -= 0.1

        if not source.chapter:
            suggestions.append("建议补充章节信息")
            confidence -= 0.05

        return {
            "is_valid": len(issues) == 0,
            "confidence": max(0, confidence),
            "issues": issues,
            "suggestions": suggestions
        }

    def check_source_credibility(self, source: SourceReference) -> str:
        """
        检查来源可信度等级

        Returns:
            "A" - 权威原典
            "B" - 可靠来源
            "C" - 待验证
            "D" - 可疑来源
        """
        if source.book_title in self.KNOWN_ANCIENT_BOOKS:
            return "A"

        if source.author and source.dynasty:
            return "B"

        if source.book_title:
            return "C"

        return "D"

    def add_known_book(self, book_title: str, author: Optional[str] = None, dynasty: Optional[str] = None) -> None:
        """添加已知典籍到验证库"""
        self.KNOWN_ANCIENT_BOOKS[book_title] = {
            "author": author,
            "dynasty": dynasty
        }

    def is_ancient_book(self, book_title: str) -> bool:
        """检查是否是已知古籍"""
        return book_title in self.KNOWN_ANCIENT_BOOKS

    def get_book_info(self, book_title: str) -> Optional[Dict]:
        """获取典籍信息"""
        return self.KNOWN_ANCIENT_BOOKS.get(book_title)
