from focuslock.db.database import Database
from focuslock.core.locker import Locker

class Watchdog:
    def __init__(self, db: Database):
        self.db = db
        self.locker = Locker()

    def check_and_relock(self):
        active_lock_state = self.db.get_active_lockstate()
        if active_lock_state:
            print("Active lock state found on startup. Re-engaging lock.")
            self.locker.start_lock(active_lock_state)
