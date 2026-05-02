"""
跨会话记忆模块

管理命盘状态追踪、重大事件记录等信息。
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import json
import hashlib


class EventType(str, Enum):
    """事件类型"""
    ANALYSIS_COMPLETED = "analysis_completed"
    CHART_UPDATED = "chart_updated"
    MILESTONE_REACHED = "milestone_reached"
    PREDICTION_FULFILLED = "prediction_fulfilled"
    PREDICTION_FAILED = "prediction_failed"
    PROFILE_CHANGED = "profile_changed"
    SIGNIFICANT_EVENT = "significant_event"


class EventSignificance(str, Enum):
    """事件重要性"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class LifeEvent:
    """人生事件"""
    event_id: str
    profile_id: int
    event_type: EventType
    description: str
    occurred_at: datetime
    significance: EventSignificance = EventSignificance.MEDIUM
    predicted: bool = False
    prediction_source: Optional[str] = None
    outcome: Optional[str] = None
    related_predictions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "profile_id": self.profile_id,
            "event_type": self.event_type.value,
            "description": self.description,
            "occurred_at": self.occurred_at.isoformat(),
            "significance": self.significance.value,
            "predicted": self.predicted,
            "prediction_source": self.prediction_source,
            "outcome": self.outcome,
            "related_predictions": self.related_predictions,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "LifeEvent":
        data = data.copy()
        data["event_type"] = EventType(data["event_type"])
        data["significance"] = EventSignificance(data["significance"])
        data["occurred_at"] = datetime.fromisoformat(data["occurred_at"])
        return cls(**data)


@dataclass
class ChartState:
    """命盘状态"""
    chart_id: int
    profile_id: int
    chart_type: str
    current_dasyun: str = ""
    current_liunian: str = ""
    life_phases: List[Dict[str, Any]] = field(default_factory=list)
    predictions: List[Dict[str, Any]] = field(default_factory=list)
    last_updated: datetime = field(default_factory=datetime.now)
    version: str = "1.0"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chart_id": self.chart_id,
            "profile_id": self.profile_id,
            "chart_type": self.chart_type,
            "current_dasyun": self.current_dasyun,
            "current_liunian": self.current_liunian,
            "life_phases": self.life_phases,
            "predictions": self.predictions,
            "last_updated": self.last_updated.isoformat(),
            "version": self.version
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChartState":
        data = data.copy()
        data["last_updated"] = datetime.fromisoformat(data["last_updated"])
        return cls(**data)


class CrossSessionMemory:
    """跨会话记忆管理器

    管理命盘状态追踪、人生事件记录、预测验证等信息。
    """

    def __init__(self):
        self._chart_states: Dict[int, ChartState] = {}
        self._life_events: Dict[int, List[LifeEvent]] = {}
        self._prediction_index: Dict[str, List[str]] = {}
        self._event_counters: Dict[int, int] = {}

    def create_chart_state(
        self,
        chart_id: int,
        profile_id: int,
        chart_type: str,
        **kwargs
    ) -> ChartState:
        state = ChartState(
            chart_id=chart_id,
            profile_id=profile_id,
            chart_type=chart_type,
            **kwargs
        )
        self._chart_states[chart_id] = state
        return state

    def get_chart_state(self, chart_id: int) -> Optional[ChartState]:
        return self._chart_states.get(chart_id)

    def update_chart_state(
        self,
        chart_id: int,
        **kwargs
    ) -> bool:
        state = self._chart_states.get(chart_id)
        if not state:
            return False

        for key, value in kwargs.items():
            if hasattr(state, key):
                setattr(state, key, value)

        state.last_updated = datetime.now()
        return True

    def add_prediction(
        self,
        chart_id: int,
        prediction: Dict[str, Any]
    ) -> bool:
        state = self._chart_states.get(chart_id)
        if not state:
            return False

        prediction_id = self._generate_prediction_id(prediction)
        prediction["prediction_id"] = prediction_id
        prediction["created_at"] = datetime.now().isoformat()

        state.predictions.append(prediction)
        state.last_updated = datetime.now()

        self._prediction_index[prediction_id] = [chart_id, str(len(state.predictions) - 1)]
        return True

    def _generate_prediction_id(self, prediction: Dict[str, Any]) -> str:
        content = json.dumps(prediction, sort_keys=True)
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def get_prediction(
        self,
        chart_id: int,
        prediction_id: str
    ) -> Optional[Dict[str, Any]]:
        state = self._chart_states.get(chart_id)
        if not state:
            return None

        for pred in state.predictions:
            if pred.get("prediction_id") == prediction_id:
                return pred
        return None

    def verify_prediction(
        self,
        chart_id: int,
        prediction_id: str,
        outcome: str,
        fulfilled: bool
    ) -> bool:
        state = self._chart_states.get(chart_id)
        if not state:
            return False

        for pred in state.predictions:
            if pred.get("prediction_id") == prediction_id:
                pred["outcome"] = outcome
                pred["fulfilled"] = fulfilled
                pred["verified_at"] = datetime.now().isoformat()
                state.last_updated = datetime.now()
                return True

        return False

    def record_event(
        self,
        profile_id: int,
        event_type: EventType,
        description: str,
        occurred_at: Optional[datetime] = None,
        significance: EventSignificance = EventSignificance.MEDIUM,
        predicted: bool = False,
        prediction_source: Optional[str] = None,
        **kwargs
    ) -> LifeEvent:
        if profile_id not in self._life_events:
            self._life_events[profile_id] = []

        counter = self._event_counters.get(profile_id, 0)
        event_id = f"evt_{profile_id}_{counter}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self._event_counters[profile_id] = counter + 1

        event = LifeEvent(
            event_id=event_id,
            profile_id=profile_id,
            event_type=event_type,
            description=description,
            occurred_at=occurred_at or datetime.now(),
            significance=significance,
            predicted=predicted,
            prediction_source=prediction_source,
            **kwargs
        )

        self._life_events[profile_id].append(event)
        return event

    def get_events(
        self,
        profile_id: int,
        event_type: Optional[EventType] = None,
        significance: Optional[EventSignificance] = None,
        limit: Optional[int] = None
    ) -> List[LifeEvent]:
        if profile_id not in self._life_events:
            return []

        events = self._life_events[profile_id]

        if event_type:
            events = [e for e in events if e.event_type == event_type]

        if significance:
            events = [e for e in events if e.significance == significance]

        events.sort(key=lambda x: x.occurred_at, reverse=True)

        if limit:
            events = events[:limit]

        return events

    def get_significant_events(
        self,
        profile_id: int,
        limit: int = 10
    ) -> List[LifeEvent]:
        return self.get_events(
            profile_id,
            significance=EventSignificance.HIGH,
            limit=limit
        )

    def link_event_to_prediction(
        self,
        profile_id: int,
        event_id: str,
        prediction_id: str
    ) -> bool:
        if profile_id not in self._life_events:
            return False

        for event in self._life_events[profile_id]:
            if event.event_id == event_id:
                if prediction_id not in event.related_predictions:
                    event.related_predictions.append(prediction_id)
                return True

        return False

    def get_events_by_prediction(
        self,
        profile_id: int,
        prediction_id: str
    ) -> List[LifeEvent]:
        if profile_id not in self._life_events:
            return []

        return [
            e for e in self._life_events[profile_id]
            if prediction_id in e.related_predictions
        ]

    def get_prediction_accuracy(
        self,
        chart_id: int
    ) -> Dict[str, Any]:
        state = self._chart_states.get(chart_id)
        if not state:
            return {"total": 0, "fulfilled": 0, "accuracy": 0.0}

        predictions = state.predictions
        verified = [p for p in predictions if p.get("verified_at")]

        if not verified:
            return {
                "total": len(predictions),
                "verified": 0,
                "accuracy": 0.0
            }

        fulfilled = sum(1 for p in verified if p.get("fulfilled", False))

        return {
            "total": len(predictions),
            "verified": len(verified),
            "fulfilled": fulfilled,
            "accuracy": round(fulfilled / len(verified), 2) if verified else 0.0
        }

    def get_life_timeline(
        self,
        profile_id: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict[str, Any]]:
        events = self.get_events(profile_id)

        if start_date:
            events = [e for e in events if e.occurred_at >= start_date]
        if end_date:
            events = [e for e in events if e.occurred_at <= end_date]

        timeline = []
        for event in sorted(events, key=lambda x: x.occurred_at):
            timeline.append({
                "date": event.occurred_at.isoformat(),
                "type": event.event_type.value,
                "description": event.description,
                "significance": event.significance.value,
                "predicted": event.predicted
            })

        return timeline

    def get_chart_states_by_profile(
        self,
        profile_id: int
    ) -> List[ChartState]:
        return [
            state for state in self._chart_states.values()
            if state.profile_id == profile_id
        ]

    def serialize(self) -> str:
        data = {
            "chart_states": {
                str(cid): state.to_dict()
                for cid, state in self._chart_states.items()
            },
            "life_events": {
                str(pid): [e.to_dict() for e in events]
                for pid, events in self._life_events.items()
            },
            "prediction_index": self._prediction_index,
            "event_counters": self._event_counters
        }
        return json.dumps(data)

    def deserialize(self, data: str) -> bool:
        try:
            loaded = json.loads(data)
            self._chart_states = {
                int(cid): ChartState.from_dict(s)
                for cid, s in loaded.get("chart_states", {}).items()
            }
            self._life_events = {
                int(pid): [LifeEvent.from_dict(e) for e in events]
                for pid, events in loaded.get("life_events", {}).items()
            }
            self._prediction_index = loaded.get("prediction_index", {})
            self._event_counters = loaded.get("event_counters", {})
            return True
        except Exception:
            return False

    def delete_profile_data(self, profile_id: int) -> int:
        deleted_count = 0

        chart_ids_to_delete = [
            cid for cid, state in self._chart_states.items()
            if state.profile_id == profile_id
        ]
        for cid in chart_ids_to_delete:
            del self._chart_states[cid]
            deleted_count += 1

        if profile_id in self._life_events:
            deleted_count += len(self._life_events[profile_id])
            del self._life_events[profile_id]

        if profile_id in self._event_counters:
            del self._event_counters[profile_id]

        return deleted_count
