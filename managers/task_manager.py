import json
import os
import uuid

from PySide6.QtCore import QObject, Signal


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

                self.tasks = json.load(file)
    
            for task in self.tasks:

                if "id" not in task:

                    task["id"] = str(uuid.uuid4())
                
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
                self.tasks,
                file,
                indent=4
            )



    def add_task(
        self,
        title,
        priority,
        due_date=None
    ):

        self.tasks.append(
            {
                "id": str(uuid.uuid4()),
                "title": title,
                "priority": priority,
                "due_date": due_date,
                "completed": False
            }
        )

        self.save_tasks()

        self.tasks_updated.emit()



    def update_task(
        self,
        task_id,
        new_title,
        priority,
        due_date
    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["title"] = new_title
                task["priority"] = priority
                task["due_date"] = due_date

                break


        self.save_tasks()

        self.tasks_updated.emit()



    def complete_task(
        self,
        task_id
    ):

        for task in self.tasks:

            if task["id"] == task_id:

                task["completed"] = True

                break


        self.save_tasks()

        self.tasks_updated.emit()



    def get_active_tasks(self):

        return [
            task
            for task in self.tasks
            if not task["completed"]
        ]
    def delete_task(
        self,
        task_id
    ):

        self.tasks = [
            task
            for task in self.tasks
            if task["title"] != title
        ]


        self.save_tasks()

        self.tasks_updated.emit()