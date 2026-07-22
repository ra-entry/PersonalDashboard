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
            "All Tasks"
        )

        title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        self.task_list = QListWidget()

        self.task_list.setSpacing(5)


        add_button = QPushButton(
            "+ Add Task"
        )

        add_button.clicked.connect(
            self.add_task
        )


        layout.addWidget(title)
        layout.addWidget(self.task_list)
        layout.addWidget(add_button)

        self.setLayout(layout)


        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )


        self.task_list.itemDoubleClicked.connect(
            self.edit_task
        )


        self.task_list.setContextMenuPolicy(
            Qt.CustomContextMenu
        )


        self.task_list.customContextMenuRequested.connect(
            self.show_task_menu
        )


        self.refresh_tasks()



    def refresh_tasks(self):

        self.task_list.clear()


        tasks = managers.task_manager.get_active_tasks()


        for task in tasks:

            priority_icon = {
                "High": "🔴",
                "Medium": "🟡",
                "Low": "🟢"
            }.get(
                task.get("priority"),
                "⚪"
            )


            due_text = get_due_description(
                task.get("due_date")
            )


            text = (
                f"{priority_icon} {task['title']}"
            )


            if due_text:

                text += (
                    f"\n    {due_text}"
                )


            item = QListWidgetItem(
                text
            )


            # Store unique task ID
            item.setData(
                Qt.UserRole,
                task["id"]
            )


            self.task_list.addItem(
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


        if task_id is None:

            return



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



        print(
            "OPENING EDIT:",
            task
        )


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


            print(
                "EDIT RESULT:",
                new_title,
                priority,
                due_date
            )


            managers.task_manager.update_task(
                task_id,
                new_title,
                priority,
                due_date
            )



    def show_task_menu(self, position):

        item = self.task_list.itemAt(
            position
        )


        if item is None:

            return


        task_id = item.data(
            Qt.UserRole
        )


        if task_id is None:

            return



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
            self.task_list.mapToGlobal(position)
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