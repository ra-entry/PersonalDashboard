from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PySide6.QtCore import Signal

class TaskDetailWidget(QWidget):

    edit_requested = Signal(dict)
    complete_requested = Signal(dict)

    def __init__(self):
        super().__init__()

        self.current_task = None

        layout = QVBoxLayout()


        self.title_label = QLabel(
            "Select a task"
        )

        self.category_label = QLabel("")
        self.priority_label = QLabel("")
        self.due_date_label = QLabel("")


        self.title_label.setStyleSheet(
            """
            font-size: 18px;
            font-weight: bold;
            """
        )


        self.edit_button = QPushButton(
            "✏ Edit Task"
        )

        self.complete_button = QPushButton(
            "✓ Complete Task"
        )


        self.edit_button.setEnabled(
            False
        )

        self.complete_button.setEnabled(
            False
        )

        self.edit_button.clicked.connect(
            self.request_edit
        )

        self.complete_button.clicked.connect(
            self.request_complete
        )

        layout.addWidget(
            self.title_label
        )

        layout.addWidget(
            self.category_label
        )

        layout.addWidget(
            self.priority_label
        )

        layout.addWidget(
            self.due_date_label
        )


        layout.addStretch()


        layout.addWidget(
            self.edit_button
        )

        layout.addWidget(
            self.complete_button
        )


        self.setLayout(
            layout
        )



    def show_task(
        self,
        task
    ):

        self.current_task = task


        self.title_label.setText(
            task["title"]
        )


        self.category_label.setText(
            f"Category: {task.get('category', 'Personal')}"
        )


        self.priority_label.setText(
            f"Priority: {task.get('priority', 'Medium')}"
        )


        self.due_date_label.setText(
            f"Due: {task.get('due_date', 'None')}"
        )


        self.edit_button.setEnabled(
            True
        )

        self.complete_button.setEnabled(
            True
        )
    def request_edit(self):

        if hasattr(self, "current_task"):

            self.edit_requested.emit(
                self.current_task
            )



    def request_complete(self):

        if hasattr(self, "current_task"):

            self.complete_requested.emit(
                self.current_task
            )