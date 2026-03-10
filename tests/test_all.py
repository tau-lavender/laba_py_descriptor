import pytest  # type: ignore

from src.main import main
from src.task import Task
from src.task_source import TaskSource
from src.task_json import TaskSourceJSON
from src.task_gen import TaskSourceGen
from src.task_api import TaskSourceAPI


class TestMain:
    def test_main(self):
        main()


class TestTask:
    def test_task_init(self):
        task_id = "1"
        payload = "ababa"
        task = Task(task_id=task_id, payload=payload)
        assert task.task_id == task_id
        assert task.payload == payload


class TestTaskSource:
    def test_duck_typing(self):
        a = TaskSourceJSON("example.jsonl")
        b = TaskSourceGen()
        c = TaskSourceAPI()
        assert isinstance(a, TaskSource)
        assert isinstance(b, TaskSource)
        assert isinstance(c, TaskSource)
        assert all([isinstance(x, Task) for x in a.get_tasks()])
        assert all([isinstance(x, Task) for x in b.get_tasks()])
        assert all([isinstance(x, Task) for x in c.get_tasks()])

    def test_bad_duck_typing(self):
        class Ababa:
            ...
        a = Ababa()
        assert not isinstance(a, TaskSource)


class TestTaskSourceJSON:
    def test_not_json(self):
        with pytest.raises(NameError):
            TaskSourceJSON("tests/not_json.txt")

    def test_bad_json(self):
        with pytest.raises(ValueError):
            for task in TaskSourceJSON("tests/bad_json.jsonl").get_tasks():
                assert isinstance(task, Task)
