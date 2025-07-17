import unittest
import os
import logging
from focuslock.utils.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test.log"
        self.logger = Logger(self.log_file)

    def tearDown(self):
        # Ensure all handlers are removed to prevent file locking issues on Windows
        for handler in logging.getLogger().handlers[:]:
            handler.close()
            logging.getLogger().removeHandler(handler)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_event(self):
        self.logger.log_event("TEST_EVENT", "This is a test event.")
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            self.assertIn("TEST_EVENT", log_content)
            self.assertIn("This is a test event.", log_content)

if __name__ == '__main__':
    unittest.main()
