from typing import Dict, List, Optional


class ContentValidator:
    """内容验证器"""

    def validate_knowledge_entry(self, entry: Dict) -> Dict:
        """验证知识条目"""
        issues = []
        warnings = []

        required_fields = ["term", "category", "system", "source", "original_content"]
        for field in required_fields:
            if field not in entry or not entry[field]:
                issues.append(f"缺少必填字段: {field}")

        if "original_content" in entry:
            if len(entry["original_content"]) < 10:
                issues.append("原典内容过短")
            if len(entry["original_content"]) > 10000:
                warnings.append("原典内容较长，建议分段")

        if "source" in entry:
            source = entry["source"]
            if isinstance(source, dict):
                if not source.get("book"):
                    issues.append("缺少来源典籍信息")

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings
        }

    def check_contradictions(self, entry1: Dict, entry2: Dict) -> Optional[Dict]:
        """检测两条知识的矛盾"""
        conflicting_keywords = {
            "吉": ["凶", "煞"],
            "凶": ["吉", "祥"],
            "阳": ["阴"],
            "阴": ["阳"]
        }

        content1 = entry1.get("interpretation", "")
        content2 = entry2.get("interpretation", "")

        for pos_word, neg_word in conflicting_keywords.items():
            if pos_word in content1 and neg_word in content2:
                if abs(content1.find(pos_word) - content2.find(neg_word)) < 50:
                    return {
                        "has_contradiction": True,
                        "entry1_id": entry1.get("id"),
                        "entry2_id": entry2.get("id"),
                        "conflict_type": "semantic_opposition",
                        "description": f"'{pos_word}' 与 '{neg_word}' 在相近位置出现"
                    }

        return {"has_contradiction": False}

    def validate_category_system(self, category: str, system: str) -> bool:
        """验证分类与体系的匹配"""
        valid_combinations = {
            "八字": ["十神", "六亲", "大运", "流年", "格局", "用神", "神煞"],
            "紫微斗数": ["主星", "辅星", "四化", "宫位", "星情"],
            "六爻": ["六亲", "六神", "世应", "动变"],
            "风水": ["理气", "峦头", "八卦", "五行"],
            "易经": ["象数", "义理", "卦辞", "爻辞"]
        }

        if system not in valid_combinations:
            return False

        if category not in valid_combinations:
            return False

        return True

    def check_content_depth(self, content: str) -> Dict:
        """检查内容深度"""
        result = {
            "has_interpretation": False,
            "has_examples": False,
            "has_applications": False,
            "depth_level": 0
        }

        if len(content) > 100:
            result["has_interpretation"] = True
            result["depth_level"] += 1

        if any(marker in content for marker in ["例如", "比如", "案例", "实例"]):
            result["has_examples"] = True
            result["depth_level"] += 1

        if any(marker in content for marker in ["应用", "用法", "用法", "使用"]):
            result["has_applications"] = True
            result["depth_level"] += 1

        return result

    def validate_citation_format(self, citation: str) -> Dict:
        """验证引用格式"""
        issues = []
        warnings = []

        if not citation:
            issues.append("引用内容为空")
            return {"is_valid": False, "issues": issues, "warnings": warnings}

        if len(citation) < 5:
            issues.append("引用内容过短")

        if "《" in citation and "》" not in citation:
            warnings.append("书名号不匹配")

        if "卷" in citation:
            import re
            if not re.search(r"卷[一二三四五六七八九十百千万零\d]", citation):
                warnings.append("卷数格式不规范")

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings
        }
