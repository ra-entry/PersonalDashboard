from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Signal


class TaskDetailWidget(QWidget):

    edit_requested = Signal(object)
    complete_requested = Signal(object)
    delete_requested = Signal(object)


    def __init__(self):
        super().__init__()


        self.current_task = None


        layout = QVBoxLayout()


        self.title_label = QLabel(
            "Select a task"
        )


        self.category_label = QLabel(
            ""
        )


        self.priority_label = QLabel(
            ""
        )


        self.due_date_label = QLabel(
            ""
        )


        self.status_label = QLabel(
            ""
        )


        self.notes_label = QLabel(
            ""
        )


        self.notes_label.setWordWrap(
            True
        )


        self.title_label.setStyleSheet(
            """
            font-size: 18px;
            font-weight: bold;
            """
        )

        self.created_label = QLabel("")
        self.completed_label = QLabel("")
        self.time_label = QLabel("")


        self.edit_button = QPushButton(
            "✏ Edit Task"
        )


        self.complete_button = QPushButton(
            "✓ Complete Task"
        )


        self.delete_button = QPushButton(
            "🗑 Delete Task"
        )


        self.edit_button.setEnabled(
            False
        )

        self.complete_button.setEnabled(
            False
        )

        self.delete_button.setEnabled(
            False
        )


        self.edit_button.clicked.connect(
            self.request_edit
        )


        self.complete_button.clicked.connect(
            self.request_complete
        )


        self.delete_button.clicked.connect(
            self.request_delete
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


        layout.addWidget(
            self.status_label
        )


        layout.addWidget(
            self.notes_label
        )


        layout.addStretch()


        layout.addWidget(
            self.edit_button
        )


        layout.addWidget(
            self.complete_button
        )


        layout.addWidget(
            self.delete_button
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
            task.title
        )


        self.category_label.setText(
            f"Category: {task.category}"
        )


        self.priority_label.setText(
            f"Priority: {task.priority}"
        )


        self.due_date_label.setText(
            f"Due: {task.due_date or 'None'}"
        )

        self.created_label.setText(
            f"Created: {task.created_date[:10]}"
            if task.created_date
            else "Created: Unknown"
        )


        self.notes_label.setText(
            f"Notes:\n{task.notes or 'No notes'}"
        )


        if task.completed:

            self.status_label.setText(
                "Status: ✓ Completed"
            )


            self.complete_button.setText(
                "↩ Mark Active"
            )


        else:

            self.status_label.setText(
                "Status: Active"
            )


            self.complete_button.setText(
                "✓ Complete Task"
            )

        if task.completed and task.completed_date:

            self.completed_label.setText(
                f"Completed: {task.completed_date[:10]}"
            )

        else:

            self.completed_label.setText(
                "Completed: —"
            )

        self.edit_button.setEnabled(
            True
        )

        self.time_label.setText(
            f"Estimated Time: {task.estimated_minutes} min"
        )


        self.complete_button.setEnabled(
            True
        )


        self.delete_button.setEnabled(
            True
        )



    def clear_task(
        self
    ):

        self.current_task = None


        self.title_label.setText(
            "Select a task"
        )


        self.category_label.setText(
            ""
        )


        self.priority_label.setText(
            ""
        )


        self.due_date_label.setText(
            ""
        )


        self.status_label.setText(
            ""
        )


        self.notes_label.setText(
            ""
        )


        self.edit_button.setEnabled(
            False
        )


        self.complete_button.setEnabled(
            False
        )


        self.delete_button.setEnabled(
            False
        )

        self.created_label.setText("")
        self.completed_label.setText("")
        self.time_label.setText("")



    def request_edit(
        self
    ):

        if self.current_task:

            self.edit_requested.emit(
                self.current_task
            )



    def request_complete(
        self
    ):

        if self.current_task:

            self.complete_requested.emit(
                self.current_task
            )



    def request_delete(
        self
    ):

        if self.current_task:

            self.delete_requested.emit(
                self.current_task
            )