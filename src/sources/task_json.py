import json
from typing import Any, Iterable
from src.task import Task


def parse_json_file(line: str, path: str, line_no: int) -> dict[str, Any]:
    """
    Парсит json
    :line: строка из json
    :path: путь к файлу
    :line_no: номер строки в файле
    :return: словарь айди:полезная нагрузка
    """

    try:
        return json.loads(line)
    except json.JSONDecodeError as error:
        raise ValueError(f"bad JSON at {path}:{line_no}: {error}") from error


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
                raw = parse_json_file(line, self.filename, line_no)
                task_id = str(raw.get("id", f"{self.filename}:{line_no}"))
                payload = raw.get("payload", "")
                yield Task(task_id, payload)
