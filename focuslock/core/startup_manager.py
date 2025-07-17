import sys
import os
from startup import Startup

class StartupManager:
    def __init__(self):
        self.startup = Startup()

    def get_script_path(self):
        # Get the absolute path to the currently running script
        if getattr(sys, 'frozen', False):
            # If the script is running as a bundled executable (e.g., PyInstaller)
            return sys.executable
        else:
            # If the script is running as a .py file
            return os.path.abspath(sys.argv[0])

    def enable_startup(self):
        script_path = self.get_script_path()
        self.startup.add("FocusLock", f'python "{script_path}"')

    def disable_startup(self):
        self.startup.remove("FocusLock")

    def is_startup_enabled(self):
        return self.startup.find("FocusLock") is not None
