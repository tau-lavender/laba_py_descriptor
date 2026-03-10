from src.task_source import TaskSource
from src.task_json import TaskSourceJSON
from src.task_gen import TaskSourceGen
from src.task_api import TaskSourceAPI


def main() -> None:
    """
    Функция вызывает источники задач через единный контракт
    для добавления новых необходимо импортировать их и добавить в source_list
    :return: Данная функция ничего не возвращает
    """
    source_list: list[TaskSource] = [TaskSourceJSON("example.jsonl"), TaskSourceGen(), TaskSourceAPI()]
    for source in source_list:
        if not isinstance(source, TaskSource):
            print(f"bad task source {source.__class__.__name__}")
            continue

        print(f"collecting tasks from {source.__class__.__name__}")
        for task in source.get_tasks():
            print(f"do task payload: {task.task_id}")
            if not isinstance(task.payload, str):
                raise TypeError(f"{task.payload} not string")
            print(task.payload)
        print()


if __name__ == "__main__":
    main()
