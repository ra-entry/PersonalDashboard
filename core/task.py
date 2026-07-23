from datetime import datetime


class Task:

    def __init__(
        self,
        title,
        priority="Medium",
        category="Personal",
        due_date=None,
        completed=False,
        task_id=None,
        created_date=None,
        completed_date=None,
        estimated_minutes=30,
        notes="",
        recurrence="None",
        depends_on=None
    ):

        self.id = task_id

        self.title = title
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.notes = notes
        self.recurrence = recurrence
        self.completed = completed
        self.depends_on = depends_on or []

        self.created_date = (
            created_date
            or datetime.now().isoformat()
        )

        self.completed_date = completed_date

        self.estimated_minutes = estimated_minutes

        self.notes = notes



    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "category": self.category,
            "due_date": self.due_date,
            "completed": self.completed,
            "created_date": self.created_date,
            "completed_date": self.completed_date,
            "estimated_minutes": self.estimated_minutes,
            "notes": self.notes,
            "depends_on": self.depends_on,
            "recurrence": self.recurrence
        }



    @classmethod
    def from_dict(
        cls,
        data
    ):

        return cls(
            title=data.get(
                "title",
                ""
            ),

            priority=data.get(
                "priority",
                "Medium"
            ),

            category=data.get(
                "category",
                "Personal"
            ),

            due_date=data.get(
                "due_date"
            ),

            completed=data.get(
                "completed",
                False
            ),

            task_id=data.get(
                "id"
            ),

            created_date=data.get(
                "created_date"
            ),

            completed_date=data.get(
                "completed_date"
            ),

            estimated_minutes=data.get(
                "estimated_minutes",
                30
            ),

            notes=data.get(
                "notes",
                ""
            ),

            recurrence=data.get(
                "recurrence",
                "None"
            )
        )



    # Compatibility helpers
    # Lets old widget code still work

    def get(
        self,
        key,
        default=None
    ):

        return getattr(
            self,
            key,
            default
        )


    def __getitem__(
        self,
        key
    ):

        return getattr(
            self,
            key
        )