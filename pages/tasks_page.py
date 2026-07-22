from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from widgets.task_manager_widget import TaskManagerWidget


class TasksPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            TaskManagerWidget()
        )

        self.setLayout(layout)