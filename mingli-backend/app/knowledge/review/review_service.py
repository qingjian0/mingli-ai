import uuid
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class ReviewService:
    """审核服务"""

    def __init__(self):
        self.review_levels = {
            1: "format_review",
            2: "content_review",
            3: "expert_review"
        }
        self.pending_tasks: Dict[str, Dict] = {}

    def create_review_task(self, entry: Dict, level: int) -> Dict:
        """创建审核任务"""
        task = {
            "task_id": str(uuid.uuid4()),
            "entry_id": entry.get("id"),
            "entry_type": entry.get("category"),
            "level": level,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "required_reviewers": self._get_required_reviewers(level),
            "deadline": self._calculate_deadline(level),
            "completed_reviews": [],
            "entry_summary": {
                "term": entry.get("term"),
                "category": entry.get("category"),
                "system": entry.get("system")
            }
        }

        self.pending_tasks[task["task_id"]] = task
        return task

    def _get_required_reviewers(self, level: int) -> int:
        """获取所需审核人数"""
        return {1: 1, 2: 2, 3: 3}.get(level, 1)

    def _calculate_deadline(self, level: int) -> str:
        """计算截止日期"""
        hours_map = {1: 24, 2: 72, 3: 168}
        hours = hours_map.get(level, 24)
        deadline = datetime.now() + timedelta(hours=hours)
        return deadline.isoformat()

    def process_review_result(self, task: Dict, result: Dict) -> Dict:
        """处理审核结果"""
        task_id = task.get("task_id")

        if task_id in self.pending_tasks:
            task = self.pending_tasks[task_id]

        task["completed_reviews"].append({
            "reviewer_id": result.get("reviewer_id"),
            "decision": result.get("decision"),
            "timestamp": datetime.now().isoformat()
        })

        required = task.get("required_reviewers", 1)
        completed = len(task["completed_reviews"])

        if result["decision"] == "approved":
            if completed >= required:
                return self._approve_entry(task, result)
            else:
                task["status"] = "in_progress"
                return {
                    "status": "awaiting_more_reviews",
                    "task_id": task_id,
                    "completed": completed,
                    "required": required
                }

        elif result["decision"] == "rejected":
            return self._reject_entry(task, result)

        else:
            return self._request_revisions(task, result)

    def _approve_entry(self, task: Dict, result: Dict) -> Dict:
        """批准条目"""
        task["status"] = "approved"
        return {
            "status": "approved",
            "entry_id": task["entry_id"],
            "verification_status": "verified",
            "approved_by": result["reviewer_id"],
            "approved_at": datetime.now().isoformat(),
            "review_notes": result.get("notes", ""),
            "task_id": task.get("task_id")
        }

    def _reject_entry(self, task: Dict, result: Dict) -> Dict:
        """拒绝条目"""
        task["status"] = "rejected"
        return {
            "status": "rejected",
            "entry_id": task["entry_id"],
            "rejection_reason": result.get("reason", ""),
            "rejected_by": result["reviewer_id"],
            "rejected_at": datetime.now().isoformat(),
            "task_id": task.get("task_id")
        }

    def _request_revisions(self, task: Dict, result: Dict) -> Dict:
        """要求修改"""
        task["status"] = "revision_requested"
        return {
            "status": "revision_requested",
            "entry_id": task["entry_id"],
            "revision_notes": result.get("revision_notes", []),
            "requested_by": result["reviewer_id"],
            "requested_at": datetime.now().isoformat(),
            "deadline": result.get("revision_deadline"),
            "task_id": task.get("task_id")
        }

    def get_task_status(self, task_id: str) -> Optional[Dict]:
        """获取任务状态"""
        return self.pending_tasks.get(task_id)

    def get_pending_tasks(self, level: Optional[int] = None) -> List[Dict]:
        """获取待处理任务"""
        tasks = [t for t in self.pending_tasks.values() if t["status"] == "pending"]

        if level is not None:
            tasks = [t for t in tasks if t.get("level") == level]

        return tasks

    def escalate_task(self, task_id: str) -> Optional[Dict]:
        """提升任务级别"""
        task = self.pending_tasks.get(task_id)
        if not task:
            return None

        current_level = task.get("level", 1)
        if current_level >= 3:
            return {"error": "已到达最高审核级别"}

        new_level = current_level + 1
        task["level"] = new_level
        task["required_reviewers"] = self._get_required_reviewers(new_level)
        task["deadline"] = self._calculate_deadline(new_level)
        task["status"] = "pending"
        task["escalated_from"] = current_level

        return {
            "task_id": task_id,
            "old_level": current_level,
            "new_level": new_level,
            "new_deadline": task["deadline"]
        }

    def cancel_task(self, task_id: str) -> bool:
        """取消任务"""
        if task_id in self.pending_tasks:
            self.pending_tasks[task_id]["status"] = "cancelled"
            return True
        return False
