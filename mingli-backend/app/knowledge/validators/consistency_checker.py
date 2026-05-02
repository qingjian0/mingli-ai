from typing import Dict, List


class ConsistencyChecker:
    """一致性检查器"""

    def check_rule_consistency(self, rules: List[Dict]) -> List[Dict]:
        """检查规则之间的一致性"""
        inconsistencies = []

        for i, rule1 in enumerate(rules):
            for rule2 in rules[i+1:]:
                if rule1.get("condition") == rule2.get("condition"):
                    if rule1.get("result") != rule2.get("result"):
                        inconsistencies.append({
                            "type": "contradictory_results",
                            "rule1": rule1.get("id"),
                            "rule2": rule2.get("id"),
                            "condition": rule1.get("condition"),
                            "result1": rule1.get("result"),
                            "result2": rule2.get("result")
                        })

                if self._are_contradictory(rule1.get("condition"), rule2.get("condition")):
                    inconsistencies.append({
                        "type": "contradictory_conditions",
                        "rule1": rule1.get("id"),
                        "rule2": rule2.get("id")
                    })

        return inconsistencies

    def _are_contradictory(self, cond1: str, cond2: str) -> bool:
        """判断两个条件是否矛盾"""
        contradictory_pairs = [
            ("阳", "阴"),
            ("吉", "凶"),
            ("旺", "衰"),
            ("生", "克")
        ]

        if not cond1 or not cond2:
            return False

        for word1, word2 in contradictory_pairs:
            if word1 in cond1 and word2 in cond2:
                return True
            if word2 in cond1 and word1 in cond2:
                return True

        return False

    def check_within_entry_consistency(self, entry: Dict) -> List[Dict]:
        """检查单个条目内部的一致性"""
        inconsistencies = []

        original = entry.get("original_content", "")
        interpretation = entry.get("interpretation", "")

        if not original or not interpretation:
            return inconsistencies

        if original in interpretation:
            inconsistencies.append({
                "type": "content_duplication",
                "severity": "warning",
                "description": "原典内容与解读存在重复"
            })

        original_keywords = self._extract_keywords(original)
        interpretation_keywords = self._extract_keywords(interpretation)

        overlap = original_keywords & interpretation_keywords
        if len(overlap) < len(original_keywords) * 0.3:
            inconsistencies.append({
                "type": "keyword_mismatch",
                "severity": "warning",
                "description": "原典与解读关键词重合度较低"
            })

        return inconsistencies

    def _extract_keywords(self, text: str) -> set:
        """提取关键词"""
        keywords = set()
        important_markers = ["吉", "凶", "旺", "衰", "生", "克", "制", "化"]
        for marker in important_markers:
            if marker in text:
                keywords.add(marker)
        return keywords

    def check_cross_reference_consistency(self, entries: List[Dict]) -> List[Dict]:
        """检查跨条目引用的一致性"""
        inconsistencies = []
        term_index = {}

        for entry in entries:
            term = entry.get("term", "")
            if term in term_index:
                term_index[term].append(entry)
            else:
                term_index[term] = [entry]

        for term, term_entries in term_index.items():
            if len(term_entries) > 1:
                for i, entry1 in enumerate(term_entries):
                    for entry2 in term_entries[i+1:]:
                        result = self.check_contradictions(entry1, entry2)
                        if result and result.get("has_contradiction"):
                            inconsistencies.append(result)

        return inconsistencies

    def check_system_consistency(self, rules: List[Dict], system: str) -> Dict:
        """检查特定命理系统的一致性"""
        system_rules = [r for r in rules if r.get("system") == system]
        inconsistencies = self.check_rule_consistency(system_rules)

        return {
            "system": system,
            "total_rules": len(system_rules),
            "inconsistencies": inconsistencies,
            "consistency_score": self._calculate_consistency_score(inconsistencies, len(system_rules))
        }

    def _calculate_consistency_score(self, inconsistencies: List[Dict], total: int) -> float:
        """计算一致性分数"""
        if total == 0:
            return 100.0

        penalty = len(inconsistencies) * 10
        return max(0, 100 - penalty)
