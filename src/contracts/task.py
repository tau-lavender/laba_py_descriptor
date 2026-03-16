from dataclasses import dataclass
from datetime import datetime
from itertools import count

from src.enums.priority_enum import PriorityEnum
from src.enums.status_enum import StatusEnum, TRANSITIONS

'''
Атрибуты задачи:
- идентификатор задачи X
- описание задачи X
- приоритет X
- статус задачи X
- время создания X
'''


@dataclass(slots=True)
class Task:
    """
    Task dataclass
    Хранит данные о задаче
    """
    __payload: object
    __priority: PriorityEnum
    __status: StatusEnum

    __creation_time: datetime
    __id: int
    __id_counter: count = count(-1)

    def __init__(self,
                 payload: object = None,
                 priority: PriorityEnum = PriorityEnum.NORMAL,
                 status: StatusEnum = StatusEnum.SCHEDULED):
        if payload is None:
            raise ValueError("Payload cannot be None")
        if not isinstance(priority, PriorityEnum):
            raise ValueError(f"Priority ({priority}) must be from priority enum")
        if not isinstance(status, StatusEnum):
            raise ValueError(f"Status ({status}) must be from status enum")

        self.__payload = payload
        self.__priority = priority
        self.__status = status

        self.__id = next(self.__id_counter)
        self.__creation_time = datetime.now()

    @property
    def payload(self) -> object:
        return self.__payload

    @property
    def priority(self) -> PriorityEnum:
        return self.__priority

    @property
    def status(self) -> StatusEnum:
        return self.__status

    @status.setter
    def status(self, value: StatusEnum) -> None:
        if not isinstance(value, StatusEnum):
            raise ValueError(f"Status ({value}) must be from status enum")
        if value in TRANSITIONS[self.__status]:
            self.__status = value
        else:
            raise ValueError(f"Impossible to set from {self.__status} to {value}")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def creation_time(self) -> datetime:
        return self.__creation_time
