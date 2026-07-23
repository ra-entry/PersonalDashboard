from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QPushButton,
    QVBoxLayout,
    QSpinBox,
    QTextEdit,
    QListWidget,
    QListWidgetItem
)

from PySide6.QtCore import (
    QDate,
    Qt
)

import managers


class AddTaskDialog(QDialog):

    def __init__(
        self,
        task=None,
        priority="Medium",
        category="Personal",
        due_date=None,
        estimated_minutes=30,
        recurrence="None",
        notes="",
        depends_on=None,
        editing_task_id=None
    ):

        super().__init__()
        self.editing_task_id = editing_task_id

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


        self.recurrence_input = QComboBox()

        self.recurrence_input.addItems(
            [
                "None",
                "Daily",
                "Weekly",
                "Monthly",
                "Yearly"
            ]
        )

        index = self.recurrence_input.findText(
            recurrence
        )

        if index >= 0:

            self.recurrence_input.setCurrentIndex(
                index
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

        self.dependencies_list = QListWidget()
        self.estimated_input = QSpinBox()

        self.estimated_input.setRange(
            5,
            1440
        )

        self.estimated_input.setSingleStep(
            5
        )

        self.estimated_input.setValue(
            estimated_minutes
        )

        self.notes_input = QTextEdit()

        self.notes_input.setPlainText(
            notes
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
            "Recurrence:",
            self.recurrence_input
        )

        form.addRow(
            "Due Date:",
            self.date_input
        )

        form.addRow(
            "Estimated Time (minutes):",
            self.estimated_input
        )

        form.addRow(
            "Notes:",
            self.notes_input
        )

        form.addRow(
            "Depends On:",
            self.dependencies_list
        )

        depends_on = depends_on or []

        for task in managers.task_manager.tasks:

            if task.id == self.editing_task_id:
                continue

            item = QListWidgetItem(task.title)

            item.setFlags(
                item.flags() | Qt.ItemIsUserCheckable
            )

            item.setData(
                Qt.UserRole,
                task.id
            )

            if task.id in depends_on:

                item.setCheckState(Qt.Checked)

            else:

                item.setCheckState(Qt.Unchecked)

            self.dependencies_list.addItem(item)

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

        depends_on = []

        for i in range(self.dependencies_list.count()):

            item = self.dependencies_list.item(i)

            if item.checkState() == Qt.Checked:

                depends_on.append(
                    item.data(Qt.UserRole)
                )

        return (
            self.task_input.text(),

            self.priority_input.currentText(),

            self.category_input.currentText(),

            self.date_input.date().toString(
                "yyyy-MM-dd"
            ),
            self.estimated_input.value(),
            self.recurrence_input.currentText(),
            self.notes_input.toPlainText(),
            depends_on
        )