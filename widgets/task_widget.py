from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QInputDialog
)

from PySide6.QtCore import Qt

import managers


class TaskWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Today's Tasks")
        title.setAlignment(Qt.AlignLeft)

        self.task_list = QListWidget()

        self.task_list.setMaximumHeight(120)

        self.task_list.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.task_list.setSpacing(5)


        add_button = QPushButton("+ Add Task")

        add_button.clicked.connect(
            self.add_task
        )


        layout.addWidget(title)
        layout.addWidget(self.task_list)
        layout.addWidget(add_button)

        self.setLayout(layout)


        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )


        self.refresh_tasks()


    def refresh_tasks(self):

        self.task_list.clear()

        tasks = managers.task_manager.get_active_tasks()


        max_display = 3


        for task in tasks[:max_display]:

            self.task_list.addItem(
                "☐ " + task["title"]
            )


        remaining = len(tasks) - max_display


        if remaining > 0:

            self.task_list.addItem(
                f"+ {remaining} more tasks..."
            )


    def add_task(self):

        task, ok = QInputDialog.getText(
            self,
            "New Task",
            "Task:"
        )


        if ok and task:

            managers.task_manager.add_task(task)