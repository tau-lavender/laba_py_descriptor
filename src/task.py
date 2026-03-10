from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    """
    Task dataclass
    Хранит данные о задаче
    """
    task_id: str
    payload: object
