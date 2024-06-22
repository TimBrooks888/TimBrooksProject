# simple_task_manager.py
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return f"Task '{title}' marked as completed"
        return f"Task '{title}' not found"

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

task_manager = TaskManager()
task_manager.add_task(Task("Learn Python", "Complete the Python tutorial"))
task_manager.add_task(Task("Buy Groceries", "Milk, Eggs, Bread"))

print(task_manager.complete_task("Learn Python"))
print(task_manager.complete_task("Go Running"))

print("Pending Tasks:")
for task in task_manager.get_pending_tasks():
    print(f"- {task.title}")

print("Completed Tasks:")
for task in task_manager.get_completed_tasks():
    print(f"- {task.title}")
