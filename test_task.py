from core.task import Task


task = Task(
    "Test Task",
    "High",
    "Work",
    "2026-07-22"
)


print(task.title)
print(task.to_dict())