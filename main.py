from task_manager import TaskManager

if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task('Task 1', 'Description for Task 1')
    manager.add_task('Task 2', 'Description for Task 2')
    print('Tasks after adding:')
    print(manager.list_tasks())
    manager.complete_task('Task 1')
    print('Tasks after completing Task 1:')
    print(manager.list_tasks())
    manager.save_tasks('tasks.json')
    print('Tasks saved to tasks.json')
    manager.load_tasks('tasks.json')
    print('Tasks loaded from tasks.json:')
    print(manager.list_tasks())