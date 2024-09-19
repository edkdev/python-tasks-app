import json


def save_tasks_to_file(tasks, filename):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)


def load_tasks_from_file(filename):
    with open(filename, 'r') as f:
        tasks_data = json.load(f)
        return [Task(**data) for data in tasks_data]