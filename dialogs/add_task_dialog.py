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

    def __init__(
        self,
        task=None,
        priority="Medium",
        category="Personal",
        due_date=None
    ):

        super().__init__()

        self.setWindowTitle(
            "Task"
        )


        self.task_input = QLineEdit()


        if task:
            self.task_input.setText(
                task
            )


        self.priority_input = QComboBox()

        self.priority_input.addItems(
            [
                "High",
                "Medium",
                "Low"
            ]
        )


        index = self.priority_input.findText(
            priority
        )

        if index >= 0:
            self.priority_input.setCurrentIndex(
                index
            )

        self.category_input = QComboBox()

        self.category_input.addItems(
            [
                "Personal",
                "Work",
                "Health",
                "Home",
                "Projects",
                "Errands"
            ]
        )

        category_index = self.category_input.findText(
            category
        )

        if category_index >= 0:

            self.category_input.setCurrentIndex(
                category_index
            )

        self.date_input = QDateEdit()

        self.date_input.setCalendarPopup(
            True
        )


        if due_date:

            self.date_input.setDate(
                QDate.fromString(
                    due_date,
                    "yyyy-MM-dd"
                )
            )

        else:

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
            "Category:",
            self.category_input
        )

        form.addRow(
            "Due Date:",
            self.date_input
        )


        button = QPushButton(
            "Save Task"
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

            self.category_input.currentText(),

            self.date_input.date().toString(
                "yyyy-MM-dd"
            )
        )