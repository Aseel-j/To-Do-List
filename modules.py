import json
from validation import input_and_validate_task_number, input_and_validate_priority

# ---------- Task Class ----------
class Task:
    last_id = 0

    def __init__(self, task_number, title, description, priority, status=False):
        self.task_number = task_number
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "task_number": self.task_number,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }


# ---------- Task Manager ----------
class TaskManager:
    def __init__(self):
        self.tasks = []

    # Load tasks from file
    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]
                if self.tasks:
                    Task.last_id = max(task.task_number for task in self.tasks)
                else:
                    Task.last_id = 0
        except FileNotFoundError:
            self.tasks = []
            Task.last_id = 0

    # Save tasks to file
    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print("Tasks Saved\n")

    # Add task
    def add_task(self, title, description, priority):
        Task.last_id += 1
        task = Task(Task.last_id, title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print("Task Added\n")

    # Find task by ID
    def find_task(self, task_number):
        for task in self.tasks:
            if task.task_number == task_number:
                return task
        return None

    # Display all tasks
    def print_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            for task in self.tasks:
                print(f"Task_number: {task.task_number}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Priority: {task.priority}")
                print(f"Status: {'Done' if task.status else 'Not Done'}")
                print("-------------------------")

    # Sort by priority
    def sort_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority)
        for task in sorted_tasks:
            print(f"Task_number: {task.task_number}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority}")
            print(f"Status: {'Done' if task.status else 'Not Done'}")
            print("-------------------------")

    # Update status
    def update_status(self):
        if not self.tasks:
            print("No tasks found")
            return
        self.print_tasks()
        task_number = input_and_validate_task_number(self.tasks)
        task = self.find_task(task_number)
        if task:
            task.status = True
            self.save_tasks()
            print("Task Status Updated\n")
        else:
            print("Task not found\n")

    # Update priority
    def update_priority(self):
        if not self.tasks:
            print("No tasks found")
            return
        self.print_tasks()
        task_number = input_and_validate_task_number(self.tasks)
        task = self.find_task(task_number)
        if task:
            task.priority = input_and_validate_priority()
            self.save_tasks()
            print("Task Priority Updated\n")
        else:
            print("Task not found\n")

    # Delete task
    def delete_task(self):
        if not self.tasks:
            print("No tasks found")
            return
        self.print_tasks()
        task_number = input_and_validate_task_number(self.tasks)
        task = self.find_task(task_number)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print("Task Deleted\n")
        else:
            print("Task not found\n")