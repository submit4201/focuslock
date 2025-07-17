import unittest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from core.scheduler import Scheduler
from models.reminder import Reminder
from models.task import Task

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.db = Mock()
        self.scheduler = Scheduler(self.db)

    def test_check_due_reminders(self):
        task = Task(title="Test Task", task_type="checkbox", requirement="Do it")
        reminder = Reminder(
            title="Test Reminder",
            description="Test Description",
            due_time=datetime.now() - timedelta(minutes=1),
            lock_enabled=True,
            task_id=task.id
        )
        self.db.get_all_reminders.return_value = [reminder]

        with patch('core.locker.Locker') as mock_locker:
            self.scheduler.locker = mock_locker.return_value
            self.scheduler.check_due_reminders()
            self.db.save_lockstate.assert_called_once()
            self.scheduler.locker.start_lock.assert_called_once()
            self.db.save_reminder.assert_called_once()

if __name__ == '__main__':
    unittest.main()
