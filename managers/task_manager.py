import json
import os
import uuid

from PySide6.QtCore import QObject, Signal

from core.task import Task
from datetime import datetime


class TaskManager(QObject):

    tasks_updated = Signal()


    def __init__(self):
        super().__init__()

        self.file_path = "data/tasks.json"

        self.tasks = []

        self.load_tasks()



    def load_tasks(self):

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r"
            ) as file:

                data = json.load(file)


            self.tasks = []


            for item in data:

                if "id" not in item:

                    item["id"] = str(uuid.uuid4())


                if "category" not in item:

                    item["category"] = "Personal"


                self.tasks.append(
                    Task.from_dict(item)
                )


        else:

            self.tasks = []


        self.tasks_updated.emit()



    def save_tasks(self):

        os.makedirs(
            "data",
            exist_ok=True
        )

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                [
                    task.to_dict()
                    for task in self.tasks
                ],
                file,
                indent=4
            )



    def add_task(
        self,
        title,
        priority,
        category,
        due_date=None,
        estimated_minutes=30,
        recurrence=None,
        notes=""
    ):

        self.tasks.append(
            Task(
                title=title,
                priority=priority,
                category=category,
                due_date=due_date,
                completed=False,
                task_id=str(uuid.uuid4()),
                estimated_minutes=estimated_minutes,
                created_date=datetime.now().isoformat(),
                completed_date=None,
                recurrence=recurrence,
                notes = notes
            )
        )


        self.save_tasks()

        self.tasks_updated.emit()



    def update_task(
        self,
        task_id,
        new_title,
        priority,
        category,
        due_date,
        estimated_minutes=30,
        recurrence="None",
        notes=""
    ):

        task = self.get_task_by_id(
            task_id
        )


        if task:

            task.title = new_title.strip()
            task.priority = priority
            task.category = category
            task.due_date = due_date
            task.estimated_minutes = estimated_minutes
            task.recurrence = recurrence
            task.notes = notes

            self.save_tasks()

            self.tasks_updated.emit()

    def complete_task(
        self,
        task_id
    ):

        from datetime import datetime


        for task in self.tasks:

            if task.id == task_id:

                task.completed = True

                task.completed_date = (
                    datetime.now().isoformat()
                )

                break


        self.save_tasks()

        self.tasks_updated.emit()



    def restore_task(
        self,
        task_id
    ):

        for task in self.tasks:

            if task.id == task_id:

                task.completed = False

                task.completed_date = None

                break


        self.save_tasks()

        self.tasks_updated.emit()

    def get_task_by_id(
        self,
        task_id
    ):

        for task in self.tasks:

            if task.id == task_id:

                return task


        return None

    def get_active_tasks(self):

        return [
            task
            for task in self.tasks
            if not task.completed
        ]



    def get_completed_tasks(self):

        return [
            task
            for task in self.tasks
            if task.completed
        ]


    def get_all_tasks(self):

        return self.tasks


    def delete_task(
        self,
        task_id
    ):

        self.tasks = [
            task
            for task in self.tasks
            if task.id != task_id
        ]


        self.save_tasks()

        self.tasks_updated.emit()

    def task_is_available(
        self,
        task
    ):

        for dependency in task.depends_on:

            dependency_task = self.get_task_by_id(
                dependency
            )

            if dependency_task and not dependency_task.completed:

                return False

        return True