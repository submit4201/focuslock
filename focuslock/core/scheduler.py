import schedule
import time
from datetime import datetime, timedelta
from focuslock.db.database import Database
from focuslock.core.locker import Locker
from focuslock.models.lockstate import LockState

class Scheduler:
    def __init__(self, db: Database):
        self.db = db
        self.locker = Locker()

    def check_due_reminders(self):
        now = datetime.now()
        reminders = self.db.get_all_reminders()
        for reminder in reminders:
            if not reminder.completed and reminder.due_time <= now:
                if reminder.lock_enabled:
                    lock_end_time = now + timedelta(hours=1)  # Default lock time
                    lock_state = LockState(
                        task_id=reminder.task_id,
                        start_time=now,
                        forced_end_time=lock_end_time
                    )
                    self.db.save_lockstate(lock_state)
                    self.locker.start_lock(lock_state)
                reminder.completed = True
                self.db.save_reminder(reminder)

    def run(self):
        schedule.every(1).minutes.do(self.check_due_reminders)
        while True:
            schedule.run_pending()
            time.sleep(1)
