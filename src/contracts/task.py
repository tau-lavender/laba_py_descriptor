'''
Атрибуты задачи:
- идентификатор задачи
- описание задачи
- приоритет
- статус задачи
- время создания
- вычисляемые свойства (например, готовность к выполнению)
'''

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    """
    Task dataclass
    Хранит данные о задаче
    """
    task_id: str
    payload: object
