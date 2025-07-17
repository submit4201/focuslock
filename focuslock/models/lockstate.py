import uuid
from datetime import datetime

class LockState:
    def __init__(self, task_id: str, start_time: datetime, forced_end_time: datetime, lockstate_id: str = None, active: bool = True, override_used: bool = False):
        self.id = lockstate_id if lockstate_id else str(uuid.uuid4())
        self.active = active
        self.start_time = start_time
        self.forced_end_time = forced_end_time
        self.task_id = task_id
        self.override_used = override_used

    def to_dict(self):
        return {
            "id": self.id,
            "active": self.active,
            "start_time": self.start_time.isoformat(),
            "forced_end_time": self.forced_end_time.isoformat(),
            "task_id": self.task_id,
            "override_used": self.override_used
        }

    @staticmethod
    def from_dict(data: dict):
        return LockState(
            lockstate_id=data.get("id"),
            active=data.get("active"),
            start_time=datetime.fromisoformat(data.get("start_time")),
            forced_end_time=datetime.fromisoformat(data.get("forced_end_time")),
            task_id=data.get("task_id"),
            override_used=data.get("override_used")
        )
