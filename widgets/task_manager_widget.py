from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMenu
)

from PySide6.QtCore import Qt

from core.task_utils import get_due_description

import managers


class TaskManagerWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()


        title = QLabel(
            "Task Management"
        )

        title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)


        active_label = QLabel(
            "Active Tasks"
        )

        active_label.setStyleSheet("""
            font-weight: bold;
        """)


        self.active_task_list = QListWidget()

        self.active_task_list.setSpacing(5)



        completed_label = QLabel(
            "Completed Tasks"
        )

        completed_label.setStyleSheet("""
            font-weight: bold;
        """)


        self.completed_task_list = QListWidget()

        self.completed_task_list.setSpacing(5)



        add_button = QPushButton(
            "+ Add Task"
        )

        add_button.clicked.connect(
            self.add_task
        )



        layout.addWidget(title)

        layout.addWidget(active_label)
        layout.addWidget(self.active_task_list)

        layout.addWidget(completed_label)
        layout.addWidget(self.completed_task_list)

        layout.addWidget(add_button)


        self.setLayout(layout)



        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )



        # Active task interactions

        self.active_task_list.itemDoubleClicked.connect(
            self.edit_task
        )

        self.active_task_list.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        self.active_task_list.customContextMenuRequested.connect(
            self.show_task_menu
        )



        # Completed task interactions

        self.completed_task_list.itemDoubleClicked.connect(
            self.edit_task
        )

        self.completed_task_list.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        self.completed_task_list.customContextMenuRequested.connect(
            self.show_task_menu
        )



        self.refresh_tasks()



    def refresh_tasks(self):

        self.active_task_list.clear()

        self.completed_task_list.clear()



        active_tasks = (
            managers.task_manager.get_active_tasks()
        )


        completed_tasks = (
            managers.task_manager.get_completed_tasks()
        )



        for task in active_tasks:

            self.add_task_item(
                self.active_task_list,
                task
            )



        for task in completed_tasks:

            self.add_task_item(
                self.completed_task_list,
                task,
                completed=True
            )



    def add_task_item(
        self,
        list_widget,
        task,
        completed=False
    ):

        if completed:

            icon = "✓"

        else:

            icon = {
                "High": "🔴",
                "Medium": "🟡",
                "Low": "🟢"
            }.get(
                task.get("priority"),
                "⚪"
            )



        text = (
            f"{icon} {task['title']}"
        )


        due_text = get_due_description(
            task.get("due_date")
        )


        if due_text and not completed:

            text += (
                f"\n    {due_text}"
            )


        item = QListWidgetItem(
            text
        )


        item.setData(
            Qt.UserRole,
            task["id"]
        )


        list_widget.addItem(
            item
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



    def edit_task(self, item):

        task_id = item.data(
            Qt.UserRole
        )


        task = next(
            (
                t
                for t in managers.task_manager.tasks
                if t["id"] == task_id
            ),
            None
        )


        if task is None:

            return



        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog(
            task["title"],
            task.get(
                "priority",
                "Medium"
            ),
            task.get(
                "due_date"
            )
        )



        if dialog.exec():

            new_title, priority, due_date = (
                dialog.get_task_data()
            )


            managers.task_manager.update_task(
                task_id,
                new_title,
                priority,
                due_date
            )



    def show_task_menu(self, position):

        sender = self.sender()


        item = sender.itemAt(
            position
        )


        if item is None:

            return


        task_id = item.data(
            Qt.UserRole
        )


        menu = QMenu()


        edit_action = menu.addAction(
            "✏ Edit Task"
        )

        complete_action = menu.addAction(
            "✓ Complete Task"
        )

        delete_action = menu.addAction(
            "🗑 Delete Task"
        )


        action = menu.exec(
            sender.mapToGlobal(position)
        )


        if action == edit_action:

            self.edit_task(item)


        elif action == complete_action:

            managers.task_manager.complete_task(
                task_id
            )


        elif action == delete_action:

            managers.task_manager.delete_task(
                task_id
            )