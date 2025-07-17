import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class LockScreen(QWidget):
    def __init__(self, task_title, task_requirement):
        super().__init__()
        self.setWindowTitle("FocusLock")
        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel(f"Task: {task_title}")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        requirement_label = QLabel(task_requirement)
        requirement_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(requirement_label)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.unlock_button = QPushButton("Unlock")
        layout.addWidget(self.unlock_button)

    def get_input(self):
        return self.input_box.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lock_screen = LockScreen("Example Task", "Type 'unlock' to continue.")
    lock_screen.show()
    sys.exit(app.exec())
