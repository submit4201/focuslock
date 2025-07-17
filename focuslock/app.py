import sys
from PyQt6.QtWidgets import QApplication
from focuslock.db.database import Database
from focuslock.core.scheduler import Scheduler
from focuslock.core.watchdog import Watchdog
from focuslock.ui.reminder_form import ReminderForm
from focuslock.core.startup_manager import StartupManager
from focuslock.utils.logger import Logger

def main():
    # Initialize the logger
    logger = Logger()

    # Initialize the database
    db = Database()
    db.connect()

    # Initialize the watchdog and check for active locks
    watchdog = Watchdog(db)
    watchdog.check_and_relock()

    # Initialize the scheduler
    scheduler = Scheduler(db)

    # Initialize the startup manager and enable startup
    startup_manager = StartupManager()
    if not startup_manager.is_startup_enabled():
        startup_manager.enable_startup()

    # Start the scheduler in a separate thread
    import threading
    scheduler_thread = threading.Thread(target=scheduler.run)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # Start the application UI
    app = QApplication(sys.argv)
    reminder_form = ReminderForm()
    reminder_form.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
