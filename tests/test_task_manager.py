import pytest
from task_manager import TaskManager


def test_add_task():
    manager = TaskManager()
    manager.add_task('Test Task', 'Test Description')
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == 'Test Task'


def test_complete_task():
    manager = TaskManager()
    manager.add_task('Test Task', 'Test Description')
    manager.complete_task('Test Task')
    assert manager.tasks[0].status == 'Completed'