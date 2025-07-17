import unittest
import os
from datetime import datetime, timedelta
from ..database import Database
from models.reminder import Reminder
from models.task import Task
from models.lockstate import LockState

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_path = "test.db"
        self.db = Database(self.db_path)
        self.db.connect()

    def tearDown(self):
        self.db.close()
        os.remove(self.db_path)

    def test_save_and_get_reminder(self):
        task = Task(title="Test Task", task_type="checkbox", requirement="Do it")
        self.db.save_task(task)
        reminder = Reminder(
            title="Test Reminder",
            description="Test Description",
            due_time=datetime.now(),
            lock_enabled=True,
            task_id=task.id
        )
        self.db.save_reminder(reminder)
        retrieved_reminder = self.db.get_reminder(reminder.id)
        self.assertEqual(retrieved_reminder.title, "Test Reminder")

    def test_save_and_get_task(self):
        task = Task(title="Test Task", task_type="checkbox", requirement="Do it")
        self.db.save_task(task)
        retrieved_task = self.db.get_task(task.id)
        self.assertEqual(retrieved_task.title, "Test Task")

    def test_save_and_get_lockstate(self):
        task = Task(title="Test Task", task_type="checkbox", requirement="Do it")
        self.db.save_task(task)
        lockstate = LockState(
            task_id=task.id,
            start_time=datetime.now(),
            forced_end_time=datetime.now() + timedelta(hours=1)
        )
        self.db.save_lockstate(lockstate)
        retrieved_lockstate = self.db.get_lockstate(lockstate.id)
        self.assertEqual(retrieved_lockstate.task_id, task.id)

if __name__ == '__main__':
    unittest.main()
