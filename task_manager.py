import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'Pending'

    def complete(self):
        self.status = 'Completed'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def list_tasks(self):
        return [(task.title, task.description, task.status) for task in self.tasks]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self, filename):
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            self.tasks = [Task(**data) for data in tasks_data]