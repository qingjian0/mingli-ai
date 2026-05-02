from typing import Dict, List


class QualityScorer:
    """质量评分器"""

    def calculate_quality_score(self, entry: Dict) -> Dict:
        """
        计算知识条目质量分

        Returns:
            {
                "total_score": float,
                "dimension_scores": {
                    "source_score": float,
                    "content_score": float,
                    "completeness_score": float,
                    "accuracy_score": float
                },
                "grade": str
            }
        """
        source_score = self._score_source(entry.get("source", {}))
        content_score = self._score_content(entry)
        completeness_score = self._score_completeness(entry)
        accuracy_score = self._score_accuracy(entry)

        total = source_score + content_score + completeness_score + accuracy_score

        return {
            "total_score": total,
            "dimension_scores": {
                "source_score": source_score,
                "content_score": content_score,
                "completeness_score": completeness_score,
                "accuracy_score": accuracy_score
            },
            "grade": self._score_to_grade(total)
        }

    def _score_source(self, source: Dict) -> float:
        """来源评分 (0-25)"""
        score = 0.0

        if source.get("book"):
            score += 10
        if source.get("author"):
            score += 5
        if source.get("chapter"):
            score += 5
        if source.get("page"):
            score += 5

        return min(25, score)

    def _score_content(self, entry: Dict) -> float:
        """内容评分 (0-25)"""
        score = 0.0

        if entry.get("original_content"):
            score += 10
        if entry.get("interpretation"):
            score += 10
        if entry.get("keywords"):
            score += 5

        return min(25, score)

    def _score_completeness(self, entry: Dict) -> float:
        """完整性评分 (0-25)"""
        required_fields = ["term", "category", "system", "source", "original_content"]
        completed = sum(1 for f in required_fields if entry.get(f))
        return (completed / len(required_fields)) * 25

    def _score_accuracy(self, entry: Dict) -> float:
        """准确性评分 (0-25)"""
        status = entry.get("verification_status", "pending")
        scores = {"verified": 25, "pending": 15, "disputed": 5}
        return scores.get(status, 0)

    def _score_to_grade(self, score: float) -> str:
        """分数转等级"""
        if score >= 90:
            return "A"
        elif score >= 75:
            return "B"
        elif score >= 60:
            return "C"
        else:
            return "D"

    def batch_score(self, entries: List[Dict]) -> List[Dict]:
        """批量评分"""
        results = []
        for entry in entries:
            score_result = self.calculate_quality_score(entry)
            results.append({
                "entry_id": entry.get("id"),
                "term": entry.get("term"),
                **score_result
            })
        return results

    def get_score_summary(self, scores: List[Dict]) -> Dict:
        """获取评分汇总"""
        if not scores:
            return {
                "total_entries": 0,
                "average_score": 0,
                "grade_distribution": {}
            }

        total_scores = [s["total_score"] for s in scores]
        grades = [s["grade"] for s in scores]

        grade_distribution = {}
        for grade in ["A", "B", "C", "D"]:
            grade_distribution[grade] = grades.count(grade)

        return {
            "total_entries": len(scores),
            "average_score": sum(total_scores) / len(total_scores),
            "max_score": max(total_scores),
            "min_score": min(total_scores),
            "grade_distribution": grade_distribution
        }

    def compare_entries(self, entry1: Dict, entry2: Dict) -> Dict:
        """比较两个条目质量"""
        score1 = self.calculate_quality_score(entry1)
        score2 = self.calculate_quality_score(entry2)

        score_diff = score1["total_score"] - score2["total_score"]

        return {
            "entry1_id": entry1.get("id"),
            "entry2_id": entry2.get("id"),
            "entry1_score": score1["total_score"],
            "entry2_score": score2["total_score"],
            "score_diff": score_diff,
            "winner": entry1.get("id") if score_diff > 0 else entry2.get("id") if score_diff < 0 else "tie",
            "dimensions": {
                dim: score1["dimension_scores"][dim] - score2["dimension_scores"][dim]
                for dim in score1["dimension_scores"]
            }
        }
