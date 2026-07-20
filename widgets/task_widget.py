from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QInputDialog
)

import managers


class TaskWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Today's Tasks")

        self.task_list = QListWidget()

        add_button = QPushButton("Add Task")

        add_button.clicked.connect(
            self.add_task
        )

        layout.addWidget(title)
        layout.addWidget(self.task_list)
        layout.addWidget(add_button)

        self.setLayout(layout)


        # Listen for task changes
        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )


        self.refresh_tasks()


    def refresh_tasks(self):

        self.task_list.clear()

        tasks = managers.task_manager.get_active_tasks()

        for task in tasks:

            self.task_list.addItem(
                task["title"]
            )


    def add_task(self):

        task, ok = QInputDialog.getText(
            self,
            "New Task",
            "Task:"
        )

        if ok and task:

            managers.task_manager.add_task(task)