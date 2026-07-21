from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QPushButton,
    QVBoxLayout
)

from PySide6.QtCore import QDate


class AddTaskDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Add Task"
        )

        self.task_input = QLineEdit()

        self.priority_input = QComboBox()

        self.priority_input.addItems(
            [
                "High",
                "Medium",
                "Low"
            ]
        )


        self.date_input = QDateEdit()

        self.date_input.setCalendarPopup(
            True
        )

        self.date_input.setDate(
            QDate.currentDate()
        )


        form = QFormLayout()

        form.addRow(
            "Task:",
            self.task_input
        )

        form.addRow(
            "Priority:",
            self.priority_input
        )

        form.addRow(
            "Due Date:",
            self.date_input
        )


        button = QPushButton(
            "Add Task"
        )

        button.clicked.connect(
            self.accept
        )


        layout = QVBoxLayout()

        layout.addLayout(
            form
        )

        layout.addWidget(
            button
        )


        self.setLayout(
            layout
        )



    def get_task_data(self):

        return (
            self.task_input.text(),

            self.priority_input.currentText(),

            self.date_input.date().toString(
                "yyyy-MM-dd"
            )
        )