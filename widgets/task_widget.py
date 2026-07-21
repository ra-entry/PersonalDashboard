from tkinter import dialog

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QDialog,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QDateEdit
)

from PySide6.QtCore import Qt

from core.task_utils import get_due_description
import managers


class TaskWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Today's Tasks (double-click to complete)")
        title.setAlignment(Qt.AlignLeft)

        self.task_list = QListWidget()
        self.task_list.setStyleSheet("""
            QListWidget {
                font-size: 13px;
            }
        """)
        self.summary_label = QLabel()

        self.summary_label.setAlignment(Qt.AlignCenter)
        self.summary_label.setStyleSheet("""
            font-size: 12px;
            color: #555555;
        """)

        self.task_list.setMinimumHeight(90)
        self.task_list.setMaximumHeight(190)

        self.task_list.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.task_list.setSpacing(2)

        add_button = QPushButton("+ Add Task")

        add_button.clicked.connect(
            self.add_task
        )


        layout.addWidget(title)
        layout.addWidget(self.task_list)
        layout.addWidget(self.summary_label)
        layout.addWidget(add_button)

        self.setLayout(layout)


        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )

        self.refresh_tasks()


        self.task_list.itemDoubleClicked.connect(
            self.complete_selected_task
        )


    def refresh_tasks(self):

        self.task_list.clear()

        tasks = managers.task_manager.get_active_tasks()


        max_display = 3


        for task in tasks[:max_display]:

            priority_icon = {
                "High": "🔴",
                "Medium": "🟡",
                "Low": "🟢"
            }.get(
                task.get("priority", "Medium"),
                "⚪"
            )


            due_text = get_due_description(
                task.get("due_date")
            )


            display_text = (
                f"{priority_icon} {task['title']}"
            )


            if due_text:
                display_text += (
                    f"\n    {due_text}"
                )


            item = QListWidgetItem(
                display_text
            )


            # Store actual task title separately
            item.setData(
                Qt.UserRole,
                task["title"]
            )


            self.task_list.addItem(item)



        remaining = len(tasks) - max_display


        if remaining > 0:

            self.task_list.addItem(
                f"+ {remaining} more tasks..."
            )
        
        active_count = len(tasks)

        high_priority = len(
            [
                task
                for task in tasks
                if task.get("priority") == "High"
            ]
        )

        completed_count = len(
            [
                task
                for task in managers.task_manager.tasks
                if task.get("completed")
            ]
        )

        self.summary_label.setText(
            f"Active: {active_count} | 🔴 {high_priority} High | ✓ {completed_count} Done"
        )

    def add_task(self):

        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog()


        if dialog.exec():

            task, priority, due_date = (
                dialog.get_task_data()
            )


            if task:

                managers.task_manager.add_task(
                    task,
                    priority,
                    due_date
                )

    def complete_selected_task(self, item):

        title = item.data(
            Qt.UserRole
        )


        if title is None:
            return


        managers.task_manager.complete_task(
            title
        )