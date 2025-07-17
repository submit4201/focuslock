import uuid

class Task:
    def __init__(self, title: str, task_type: str, requirement: str, task_id: str = None, fulfilled: bool = False, notes: str = ""):
        self.id = task_id or str(uuid.uuid4())
        self.title = title
        self.type = task_type
        self.requirement = requirement
        self.fulfilled = fulfilled
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "type": self.type,
            "requirement": self.requirement,
            "fulfilled": self.fulfilled,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data: dict):
        return Task(
            task_id=data.get("id"),
            title=data.get("title"),
            task_type=data.get("type"),
            requirement=data.get("requirement"),
            fulfilled=data.get("fulfilled"),
            notes=data.get("notes")
        )
