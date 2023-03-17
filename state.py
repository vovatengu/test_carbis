from abc import ABC, abstractmethod


class State(ABC):
    """Базовый класс состояния,
    определяющий интерфейс"""

    @abstractmethod
    def launch(self, ui_main) -> None:
        ...

    @abstractmethod
    def next(self, ui_main) -> None:
        ...
