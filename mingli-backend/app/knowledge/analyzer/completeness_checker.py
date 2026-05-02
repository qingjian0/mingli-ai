from typing import Dict, List, Set


class CompletenessChecker:
    """完整性检查器"""

    REQUIRED_FIELDS = {
        "basic": ["term", "category", "system"],
        "source": ["book", "author"],
        "content": ["original_content", "interpretation"],
        "metadata": ["created_at", "updated_at"]
    }

    OPTIONAL_FIELDS = {
        "keywords": "关键词",
        "examples": "应用示例",
        "related_terms": "相关术语",
        "notes": "备注说明",
        "page": "页码",
        "chapter": "章节"
    }

    SYSTEM_REQUIREMENTS = {
        "八字": ["十神", "六亲", "日主", "用神"],
        "紫微斗数": ["主星", "宫位", "星曜"],
        "六爻": ["六亲", "六神", "世应"],
        "风水": ["理气", "峦头", "方位"],
        "易经": ["卦象", "卦辞", "爻辞"]
    }

    def check_completeness(self, entry: Dict) -> Dict:
        """检查条目完整性"""
        missing_fields = []
        present_fields = []
        suggestions = []

        for field_group, fields in self.REQUIRED_FIELDS.items():
            for field in fields:
                if field in entry and entry[field]:
                    present_fields.append(field)
                else:
                    missing_fields.append(f"{field_group}.{field}")

        system = entry.get("system", "")
        if system in self.SYSTEM_REQUIREMENTS:
            system_fields = self.SYSTEM_REQUIREMENTS[system]
            for sfield in system_fields:
                if sfield not in entry or not entry.get(sfield):
                    suggestions.append(f"系统 '{system}' 建议补充: {sfield}")

        completeness_rate = len(present_fields) / self._total_required_fields()

        return {
            "is_complete": len(missing_fields) == 0,
            "completeness_rate": completeness_rate,
            "missing_fields": missing_fields,
            "present_fields": present_fields,
            "suggestions": suggestions
        }

    def _total_required_fields(self) -> int:
        """计算必需字段总数"""
        return sum(len(fields) for fields in self.REQUIRED_FIELDS.values())

    def check_field_coverage(self, entries: List[Dict]) -> Dict:
        """检查字段覆盖率"""
        field_coverage: Dict[str, int] = {}
        total = len(entries)

        if total == 0:
            return {"field_coverage": {}, "average_coverage": 0}

        all_fields = set()
        for entry in entries:
            all_fields.update(entry.keys())

        for field in all_fields:
            count = sum(1 for e in entries if field in e and e[field])
            field_coverage[field] = count / total

        average_coverage = sum(field_coverage.values()) / len(field_coverage) if field_coverage else 0

        return {
            "field_coverage": field_coverage,
            "average_coverage": average_coverage,
            "total_entries": total,
            "total_fields": len(all_fields)
        }

    def identify_gaps(self, entry: Dict) -> List[Dict]:
        """识别知识缺口"""
        gaps = []

        system = entry.get("system", "")
        category = entry.get("category", "")

        if not entry.get("examples"):
            gaps.append({
                "type": "missing_examples",
                "severity": "medium",
                "description": "缺少应用示例"
            })

        if not entry.get("related_terms"):
            gaps.append({
                "type": "missing_relations",
                "severity": "low",
                "description": "缺少相关术语链接"
            })

        if not entry.get("keywords"):
            gaps.append({
                "type": "missing_keywords",
                "severity": "medium",
                "description": "缺少关键词标注"
            })

        if system in self.SYSTEM_REQUIREMENTS:
            required = self.SYSTEM_REQUIREMENTS[system]
            for req in required:
                if req not in entry or not entry.get(req):
                    gaps.append({
                        "type": "system_specific",
                        "severity": "high",
                        "description": f"系统 '{system}' 缺少必要字段: {req}"
                    })

        return gaps

    def suggest_enrichment(self, entry: Dict) -> List[str]:
        """建议内容丰富化"""
        suggestions = []

        original = entry.get("original_content", "")
        interpretation = entry.get("interpretation", "")

        if len(original) < 50:
            suggestions.append("原典内容较短，建议补充更多原文引用")

        if len(interpretation) < 100:
            suggestions.append("解读内容较简略，建议增加详细解释")

        if not entry.get("examples"):
            suggestions.append("建议添加具体应用示例")

        if not entry.get("related_terms"):
            suggestions.append("建议关联相关术语")

        if not entry.get("keywords"):
            suggestions.append("建议添加关键词标签")

        if not entry.get("source", {}).get("chapter"):
            suggestions.append("建议补充章节信息")

        if not entry.get("source", {}).get("page"):
            suggestions.append("建议补充页码信息")

        return suggestions

    def validate_schema(self, entry: Dict, schema: Dict) -> Dict:
        """验证是否符合Schema"""
        issues = []
        warnings = []

        required = schema.get("required", [])
        properties = schema.get("properties", {})

        for field in required:
            if field not in entry or not entry[field]:
                issues.append(f"缺少必需字段: {field}")

        for field, value in entry.items():
            if field in properties:
                expected_type = properties[field].get("type")
                actual_type = type(value).__name__

                if expected_type == "string" and actual_type != "str":
                    warnings.append(f"字段 {field} 类型应为 string，实际为 {actual_type}")
                elif expected_type == "array" and actual_type != "list":
                    warnings.append(f"字段 {field} 类型应为 array，实际为 {actual_type}")
                elif expected_type == "object" and actual_type != "dict":
                    warnings.append(f"字段 {field} 类型应为 object，实际为 {actual_type}")

        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings
        }

    def generate_completeness_report(self, entries: List[Dict]) -> Dict:
        """生成完整性报告"""
        completeness_results = [self.check_completeness(e) for e in entries]

        rates = [r["completeness_rate"] for r in completeness_results]
        average_rate = sum(rates) / len(rates) if rates else 0

        missing_field_counts: Dict[str, int] = {}
        for result in completeness_results:
            for field in result["missing_fields"]:
                missing_field_counts[field] = missing_field_counts.get(field, 0) + 1

        return {
            "total_entries": len(entries),
            "complete_entries": sum(1 for r in completeness_results if r["is_complete"]),
            "average_completeness_rate": average_rate,
            "most_common_gaps": sorted(
                missing_field_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5],
            "entries_by_completeness": {
                "full": sum(1 for r in completeness_results if r["completeness_rate"] == 1.0),
                "partial": sum(1 for r in completeness_results if 0.5 <= r["completeness_rate"] < 1.0),
                "incomplete": sum(1 for r in completeness_results if r["completeness_rate"] < 0.5)
            }
        }
