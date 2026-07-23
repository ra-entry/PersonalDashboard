from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMenu,
    QComboBox,
    QHBoxLayout,
    QSplitter,
    QMessageBox
)

from widgets.task_detail_widget import TaskDetailWidget

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

        title.setStyleSheet(
            """
            font-size: 18px;
            font-weight: bold;
            """
        )


        controls_layout = QHBoxLayout()


        sort_label = QLabel(
            "Sort:"
        )


        self.sort_box = QComboBox()

        self.sort_box.addItems(
            [
                "Default",
                "Priority",
                "Due Date"
            ]
        )


        filter_label = QLabel(
            "Filter:"
        )


        self.filter_box = QComboBox()

        self.filter_box.addItems(
            [
                "All",
                "High Priority",
                "Medium Priority",
                "Low Priority",
                "Due Today"
            ]
        )


        controls_layout.addWidget(
            sort_label
        )

        controls_layout.addWidget(
            self.sort_box
        )

        controls_layout.addSpacing(
            20
        )

        controls_layout.addWidget(
            filter_label
        )

        controls_layout.addWidget(
            self.filter_box
        )

        self.active_label = QLabel(
            "Active Tasks (0)"
        )

        self.completed_label = QLabel(
            "Completed Tasks (0)"
        )


        self.active_label.setStyleSheet(
            "font-weight: bold;"
        )

        self.completed_label.setStyleSheet(
            "font-weight: bold;"
        )


        self.active_task_list = QListWidget()

        self.completed_task_list = QListWidget()


        self.task_detail = TaskDetailWidget()


        self.task_detail.edit_requested.connect(
            self.edit_selected_task
        )

        self.task_detail.complete_requested.connect(
            self.complete_selected_task
        )

        self.task_detail.delete_requested.connect(
            self.delete_selected_task
        )

        add_button = QPushButton(
            "+ Add Task"
        )

        add_button.clicked.connect(
            self.add_task
        )

        layout.addWidget(
            title
        )

        layout.addLayout(
            controls_layout
        )


        splitter = QSplitter()


        left_layout = QVBoxLayout()


        left_layout.addWidget(
            self.active_label
        )

        left_layout.addWidget(
            self.active_task_list
        )

        left_layout.addWidget(
            self.completed_label
        )

        left_layout.addWidget(
            self.completed_task_list
        )


        left_widget = QWidget()

        left_widget.setLayout(
            left_layout
        )


        splitter.addWidget(
            left_widget
        )


        splitter.addWidget(
            self.task_detail
        )


        layout.addWidget(
            splitter
        )


        layout.addWidget(
            add_button
        )


        self.setLayout(
            layout
        )


        managers.task_manager.tasks_updated.connect(
            self.refresh_tasks
        )

        self.active_task_list.itemClicked.connect(
            self.select_task
        )

        self.completed_task_list.itemClicked.connect(
            self.select_task
        )


        self.active_task_list.itemDoubleClicked.connect(
            self.edit_task
        )

        self.completed_task_list.itemDoubleClicked.connect(
            self.edit_task
        )

        self.active_task_list.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        self.completed_task_list.setContextMenuPolicy(
            Qt.CustomContextMenu
        )


        self.active_task_list.customContextMenuRequested.connect(
            self.show_task_menu
        )

        self.completed_task_list.customContextMenuRequested.connect(
            self.show_task_menu
        )


        self.sort_box.currentIndexChanged.connect(
            self.refresh_tasks
        )


        self.filter_box.currentIndexChanged.connect(
            self.refresh_tasks
        )

        self.refresh_tasks()


    def select_task(
        self,
        item
    ):


        task_id = item.data(
            Qt.UserRole
        )

        task = managers.task_manager.get_task_by_id(
            task_id
        )

        if task:

            self.task_detail.show_task(
                task
            )

    def filter_tasks(
        self,
        tasks
    ):

        filter_value = self.filter_box.currentText()


        if filter_value == "High Priority":

            return [
                task
                for task in tasks
                if task.priority == "High"
            ]


        elif filter_value == "Medium Priority":

            return [
                task
                for task in tasks
                if task.priority == "Medium"
            ]


        elif filter_value == "Low Priority":

            return [
                task
                for task in tasks
                if task.priority == "Low"
            ]


        elif filter_value == "Due Today":

            from datetime import date

            today = str(
                date.today()
            )


            return [
                task
                for task in tasks
                if task.due_date == today
            ]


        return tasks


    def sort_tasks(
        self,
        tasks
    ):

        sort_value = self.sort_box.currentText()



        if sort_value == "Priority":

            priority_order = {
                "High": 1,
                "Medium": 2,
                "Low": 3
            }


            return sorted(
                tasks,
                key=lambda task:
                    priority_order.get(
                        task.priority,
                        4
                    )
            )



        elif sort_value == "Due Date":

            return sorted(
                tasks,
                key=lambda task:
                    task.due_date or "9999-99-99"
            )


        return tasks

    def refresh_tasks(
        self
    ):

        self.active_task_list.clear()

        self.completed_task_list.clear()


        active_tasks = (
            managers.task_manager.get_active_tasks()
        )


        completed_tasks = (
            managers.task_manager.get_completed_tasks()
        )


        active_tasks = self.filter_tasks(
            active_tasks
        )

        completed_tasks = self.filter_tasks(
            completed_tasks
        )


        self.active_label.setText(
            f"Active Tasks ({len(active_tasks)})"
        )


        self.completed_label.setText(
            f"Completed Tasks ({len(completed_tasks)})"
        )


        active_tasks = self.sort_tasks(
            active_tasks
        )

        completed_tasks = self.sort_tasks(
            completed_tasks
        )


        if active_tasks:

            for task in active_tasks:

                self.add_task_item(
                    self.active_task_list,
                    task
                )

        else:

            empty_item = QListWidgetItem(
                "🎉 No active tasks"
            )

            empty_item.setFlags(
                Qt.NoItemFlags
            )

            self.active_task_list.addItem(
                empty_item
            )


        if completed_tasks:

            for task in completed_tasks:

                self.add_task_item(
                    self.completed_task_list,
                    task,
                    completed=True
                )

        else:

            empty_item = QListWidgetItem(
                "No completed tasks yet"
            )

            empty_item.setFlags(
                Qt.NoItemFlags
            )

            self.completed_task_list.addItem(
                empty_item
            )


        # Refresh details panel if selected task still exists

        if self.task_detail.current_task:

            task_id = self.task_detail.current_task.id


            updated_task = next(
                (
                    task
                    for task in managers.task_manager.tasks
                    if task.id == task_id
                ),
                None
            )


            if updated_task:

                self.task_detail.show_task(
                    updated_task
                )

            else:

                self.task_detail.clear_task()
    

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
                task.priority,
                "⚪"
            )


        text = (
            f"{icon} {task.title}"
        )


        text += (
            f"\n    {task.category}"
        )


        due_text = get_due_description(
            task.due_date
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
            task.id
        )


        list_widget.addItem(
            item
        )



    def add_task(
        self
    ):

        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog()


        if dialog.exec():

            (
                title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            ) = dialog.get_task_data()


            if title:

                managers.task_manager.add_task(
                    title,
                    priority,
                    category,
                    due_date,
                    estimated_minutes,
                    recurrence,
                    notes
                )



    def edit_task(
        self,
        item
    ):

        task_id = item.data(
            Qt.UserRole
        )


        task = managers.task_manager.get_task_by_id(
            task_id
        )


        if task is None:

            return


        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog(
            task.title,
            task.priority,
            task.category,
            task.due_date,
            task.estimated_minutes,
            task.recurrence,
            task.notes
        )


        if dialog.exec():

            (
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            ) = dialog.get_task_data()


            managers.task_manager.update_task(
                task.id,
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            )



    def edit_selected_task(
        self,
        task
    ):

        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog(
            task.title,
            task.priority,
            task.category,
            task.due_date,
            task.estimated_minutes,
            task.recurrence,
            task.notes
        )


        if dialog.exec():

            (
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            ) = dialog.get_task_data()


            managers.task_manager.update_task(
                task.id,
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            )

    def edit_selected_task(
        self,
        task
    ):

        from dialogs.add_task_dialog import AddTaskDialog


        dialog = AddTaskDialog(
            task.title,
            task.priority,
            task.category,
            task.due_date,
            task.estimated_minutes,
            task.recurrence,
            task.notes
        )


        if dialog.exec():

            (
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            ) = dialog.get_task_data()


            managers.task_manager.update_task(
                task.id,
                new_title,
                priority,
                category,
                due_date,
                estimated_minutes,
                recurrence,
                notes
            )

    def complete_selected_task(
        self,
        task
    ):

        if task.completed:

            managers.task_manager.restore_task(
                task.id
            )

        else:

            managers.task_manager.complete_task(
                task.id
            )

    def complete_selected_task(
        self,
        task
    ):

        if task.completed:

            managers.task_manager.restore_task(
                task.id
            )

        else:

            managers.task_manager.complete_task(
                task.id
            )



    def delete_selected_task(
        self,
        task
    ):

        confirmation = QMessageBox.question(
            self,
            "Delete Task",
            f"Are you sure you want to delete:\n\n{task.title}?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirmation == QMessageBox.Yes:

            managers.task_manager.delete_task(
                task.id
            )


            if (
                self.task_detail.current_task
                and self.task_detail.current_task.id == task.id
            ):

                self.task_detail.clear_task()

    def show_task_menu(
        self,
        position
    ):

        sender = self.sender()


        item = sender.itemAt(
            position
        )


        if item is None:

            return


        task_id = item.data(
            Qt.UserRole
        )


        task = managers.task_manager.get_task_by_id(
            task_id
        )


        if task is None:

            return


        menu = QMenu()


        edit_action = menu.addAction(
            "✏ Edit Task"
        )


        if task.completed:

            complete_action = menu.addAction(
                "↩ Mark Active"
            )

        else:

            complete_action = menu.addAction(
                "✓ Complete Task"
            )


        delete_action = menu.addAction(
            "🗑 Delete Task"
        )


        action = menu.exec(
            sender.mapToGlobal(
                position
            )
        )


        if action == edit_action:

            self.edit_task(
                item
            )


        elif action == complete_action:

            self.complete_selected_task(
                task
            )


        elif action == delete_action:

            confirmation = QMessageBox.question(
                self,
                "Delete Task",
                f"Are you sure you want to delete:\n\n{task.title}?",
                QMessageBox.Yes | QMessageBox.No
            )


            if confirmation == QMessageBox.Yes:

                managers.task_manager.delete_task(
                    task.id
                )


                if (
                    self.task_detail.current_task
                    and self.task_detail.current_task.id == task.id
                ):

                    self.task_detail.clear_task()