import uuid
from datetime import datetime

class Reminder:
    def __init__(self, title: str, description: str, due_time: datetime, lock_enabled: bool, task_id: str, whitelist: list[str] = None, reminder_id: str = None, completed: bool = False):
        self.id = reminder_id if reminder_id else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_time = due_time
        self.lock_enabled = lock_enabled
        self.whitelist = whitelist if whitelist else []
        self.task_id = task_id
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_time": self.due_time.isoformat(),
            "lock_enabled": self.lock_enabled,
            "whitelist": self.whitelist,
            "task_id": self.task_id,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        return Reminder(
            reminder_id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            due_time=datetime.fromisoformat(data.get("due_time")),
            lock_enabled=data.get("lock_enabled"),
            whitelist=data.get("whitelist"),
            task_id=data.get("task_id"),
            completed=data.get("completed")
        )
