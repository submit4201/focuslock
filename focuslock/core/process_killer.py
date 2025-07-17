import psutil
import time

class ProcessKiller:
    def __init__(self, whitelist_manager):
        self.whitelist_manager = whitelist_manager
        self.running = False

    def __init__(self, whitelist_manager):
        self.whitelist_manager = whitelist_manager
        self.running = False
        import logging
        self.logger = logging.getLogger(__name__)

    def start(self):
        self.running = True
        while self.running:
            for proc in psutil.process_iter(['pid', 'name']):
                if not self.whitelist_manager.is_whitelisted(proc.info['name']):
                    try:
                        p = psutil.Process(proc.info['pid'])
                        p.kill()
                        self.logger.info(f"Killed process: {proc.info['name']}")
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
            time.sleep(5)

    def stop(self):
        self.running = False
