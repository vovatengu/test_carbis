from enum import Enum


class UiState(Enum):
    """Возможные состояния"""

    BEGINING = 0
    INPUT = 1
    REGISTATION = 2
    SEARCH = 3
    EXIT = 4
    END = 5
