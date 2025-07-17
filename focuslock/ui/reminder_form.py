import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDateTimeEdit, QCheckBox
from PyQt6.QtCore import QDateTime

class ReminderForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add/Edit Reminder")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Title:"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)

        layout.addWidget(QLabel("Due Time:"))
        self.due_time_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.due_time_input.setCalendarPopup(True)
        layout.addWidget(self.due_time_input)

        self.lock_enabled_checkbox = QCheckBox("Enable Lock")
        layout.addWidget(self.lock_enabled_checkbox)

        self.save_button = QPushButton("Save")
        layout.addWidget(self.save_button)

    def get_data(self):
        return {
            "title": self.title_input.text(),
            "description": self.description_input.text(),
            "due_time": self.due_time_input.dateTime().toPyDateTime(),
            "lock_enabled": self.lock_enabled_checkbox.isChecked()
        }

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reminder_form = ReminderForm()
    reminder_form.show()
    sys.exit(app.exec())
