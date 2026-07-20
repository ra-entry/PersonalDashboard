from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class TasksPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(
            "Task Management Coming Soon"
        )

        layout.addWidget(label)

        self.setLayout(layout)