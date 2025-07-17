import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_file='focuslock.log'):
        self.log_file = log_file
        self.setup_logger()

    def setup_logger(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )

    def log_event(self, event_type, details):
        logging.info(f"[{event_type}] - {details}")

    def log_lock(self, task_id):
        self.log_event("LOCK", f"System locked for task: {task_id}")

    def log_unlock(self, task_id):
        self.log_event("UNLOCK", f"System unlocked for task: {task_id}")

    def log_error(self, error_message):
        logging.error(error_message)
