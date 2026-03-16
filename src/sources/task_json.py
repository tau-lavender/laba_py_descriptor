import json
from typing import Iterable
from src.contracts.task import Task


class TaskSourceJSON:
    """
    Источник задач - из JSON файла
    """

    def __init__(self, filename: str) -> None:
        if not filename.endswith(".jsonl"):
            raise NameError(f"{filename} is not json")
        self.filename = filename

    def get_tasks(self) -> Iterable[Task]:
        """
        Метод получения задач соответствующий протоколу TaskSource
        """

        with open(self.filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                raw = json.loads(line)
                payload = raw.get("payload", "")
                if payload == "":
                    raise ValueError("No payload in json {filename}, line {line_no}")
                priority = raw.get("priority", "")
                status = raw.get("status", "")
                if priority == "" and status == "":
                    yield Task(payload)
                if priority != "" and status == "":
                    yield Task(payload, priority=priority)
                if priority == "" and status != "":
                    yield Task(payload, status=status)
                if priority != "" and status != "":
                    yield Task(payload, priority=priority, status=status)
