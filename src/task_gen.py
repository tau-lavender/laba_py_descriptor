import random
import string
from typing import Iterable
from src.task import Task


class TaskSourceGen:
    """
    Источник задач - генератор
    """

    def __init__(self) -> None:
        self.count = random.randint(2, 5)

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """
        for i in range(1, self.count + 1):
            yield Task(task_id=str(i * random.randint(100, 999)), payload="".join(random.choices(string.ascii_lowercase, k=20)))
