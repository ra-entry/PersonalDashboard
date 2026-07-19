import json
import os

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QInputDialog
)


class TaskWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.file_path = "data/tasks.json"

        self.tasks = self.load_tasks()

        layout = QVBoxLayout()

        title = QLabel("Today's Tasks")

        self.task_list = QListWidget()

        add_button = QPushButton("Add Task")

        add_button.clicked.connect(self.add_task)

        layout.addWidget(title)
        layout.addWidget(self.task_list)
        layout.addWidget(add_button)

        self.setLayout(layout)

        self.refresh_tasks()


    def load_tasks(self):

        if os.path.exists(self.file_path):

            with open(self.file_path, "r") as file:
                return json.load(file)

        return []


    def save_tasks(self):

        os.makedirs("data", exist_ok=True)

        with open(self.file_path, "w") as file:
            json.dump(
                self.tasks,
                file,
                indent=4
            )


    def refresh_tasks(self):

        self.task_list.clear()

        for task in self.tasks:
            self.task_list.addItem(task)


    def add_task(self):

        task, ok = QInputDialog.getText(
            self,
            "New Task",
            "Task:"
        )

        if ok and task:

            self.tasks.append(task)

            self.save_tasks()

            self.refresh_tasks()