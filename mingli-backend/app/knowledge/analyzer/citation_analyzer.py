from typing import Dict, List, Set, Optional


class CitationAnalyzer:
    """引用分析器"""

    def __init__(self):
        self.citation_patterns = {
            "ancient_book": r"《([^》]+)》",
            "chapter": r"卷[一二三四五六七八九十百千万\d]+",
            "author": r"（[^）]+）|^([^（]+)",
            "dynasty": r"【([^】]+)】"
        }

    def analyze_citations(self, content: str) -> Dict:
        """分析内容中的引用"""
        import re

        citations = {
            "books": [],
            "chapters": [],
            "authors": [],
            "dynasties": [],
            "raw_matches": []
        }

        book_pattern = re.compile(self.citation_patterns["ancient_book"])
        matches = book_pattern.findall(content)
        citations["books"] = list(set(matches))

        chapter_pattern = re.compile(self.citation_patterns["chapter"])
        citations["chapters"] = chapter_pattern.findall(content)

        dynasty_pattern = re.compile(self.citation_patterns["dynasty"])
        citations["dynasties"] = dynasty_pattern.findall(content)

        return {
            "citation_count": len(citations["books"]),
            "unique_books": len(set(citations["books"])),
            "citations": citations,
            "has_chapter_reference": len(citations["chapters"]) > 0,
            "has_author_reference": len(citations["authors"]) > 0
        }

    def verify_citation_chain(self, entry: Dict) -> Dict:
        """验证引用链"""
        issues = []
        warnings = []

        source = entry.get("source", {})
        if not source:
            issues.append("缺少来源信息")
            return {"is_valid": False, "issues": issues, "warnings": warnings}

        if not source.get("book"):
            issues.append("缺少典籍名称")

        if source.get("author") and not source.get("dynasty"):
            warnings.append("有作者但无朝代信息")

        content = entry.get("original_content", "")
        if content:
            analysis = self.analyze_citations(content)
            if analysis["citation_count"] > 0:
                cited_books = analysis["citations"]["books"]
                if source.get("book") not in cited_books:
                    warnings.append("内容中未明确引用来源典籍")

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings
        }

    def build_citation_network(self, entries: List[Dict]) -> Dict:
        """构建引用网络"""
        nodes = []
        edges = []

        for entry in entries:
            entry_id = entry.get("id", "unknown")
            source = entry.get("source", {})
            book = source.get("book", "unknown")

            nodes.append({
                "id": entry_id,
                "label": entry.get("term", "unknown"),
                "book": book
            })

            content = entry.get("interpretation", "")
            analysis = self.analyze_citations(content)

            for cited_book in analysis["citations"]["books"]:
                edges.append({
                    "from": entry_id,
                    "to": cited_book,
                    "type": "cites"
                })

        return {
            "nodes": nodes,
            "edges": edges,
            "total_nodes": len(nodes),
            "total_edges": len(edges)
        }

    def calculate_citation_importance(
        self,
        entry_id: str,
        citation_network: Dict
    ) -> float:
        """计算引用重要性"""
        edges = citation_network.get("edges", [])

        incoming = sum(1 for e in edges if e.get("to") == entry_id)
        outgoing = sum(1 for e in edges if e.get("from") == entry_id)

        importance = (incoming * 2 + outgoing) / 10

        return min(1.0, importance)

    def detect_unverified_citations(self, content: str) -> List[Dict]:
        """检测未经验证的引用"""
        analysis = self.analyze_citations(content)
        unverified = []

        for book in analysis["citations"]["books"]:
            unverified.append({
                "book": book,
                "status": "unverified",
                "reason": "需人工核实"
            })

        return unverified

    def generate_citation_report(self, entries: List[Dict]) -> Dict:
        """生成引用报告"""
        total_entries = len(entries)
        entries_with_citations = 0
        all_books: Set[str] = set()

        for entry in entries:
            content = entry.get("original_content", "") + entry.get("interpretation", "")
            analysis = self.analyze_citations(content)

            if analysis["citation_count"] > 0:
                entries_with_citations += 1
                all_books.update(analysis["citations"]["books"])

        return {
            "total_entries": total_entries,
            "entries_with_citations": entries_with_citations,
            "citation_rate": entries_with_citations / total_entries if total_entries > 0 else 0,
            "unique_books_count": len(all_books),
            "unique_books": list(all_books)
        }
