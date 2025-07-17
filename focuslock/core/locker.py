from focuslock.models.lockstate import LockState

class Locker:
    def __init__(self):
        self.is_locked = False

    def start_lock(self, lock_state: LockState):
        self.is_locked = True
        print(f"System locked for task: {lock_state.task_id}")

    def end_lock(self):
        self.is_locked = False
        print("System unlocked.")
