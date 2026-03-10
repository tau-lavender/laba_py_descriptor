import time
import random
from typing import Iterable
from src.task import Task


class TaskSourceAPI:
    """
    Источник задач - API заглушка
    """

    def __init__(self) -> None:
        self.fake_data = ["task from api", "another task from api", "abababa"]

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """
        for i in range(len(self.fake_data)):
            time.sleep(random.randint(1, 4))
            yield Task(task_id="api_" + str(i), payload=self.fake_data[i])
