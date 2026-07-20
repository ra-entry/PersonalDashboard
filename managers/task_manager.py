import json
import os

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



    def add_task(self, title):

        self.tasks.append(
            {
                "title": title,
                "priority": "Medium",
                "completed": False
            }
        )

        self.save_tasks()

        self.tasks_updated.emit()



    def get_active_tasks(self):

        return [
            task
            for task in self.tasks
            if not task["completed"]
        ]