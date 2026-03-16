from enum import Enum


class StatusEnum(Enum):
    SCHEDULED = "Scheduled"
    STARTED = "Started"
    COMPLETED = "Completed succesfully"
    ERROR = "Completed with error"
    CANCELLED = "Canceled"


TRANSITIONS = {StatusEnum.SCHEDULED: {StatusEnum.STARTED, StatusEnum.COMPLETED, StatusEnum.ERROR, StatusEnum.CANCELLED},
               StatusEnum.STARTED: {StatusEnum.COMPLETED, StatusEnum.ERROR, StatusEnum.CANCELLED},
               StatusEnum.COMPLETED: {},
               StatusEnum.ERROR: {},
               StatusEnum.CANCELLED: {}}
