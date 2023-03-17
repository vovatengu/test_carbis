from .state import State
from .uistate import UiState
from ..ui import Ui


class EndState(State):
    def launch(self, ui_main) -> None:
        Ui.print_end()
        number = int(input("Выберите действие: "))
        selector = {1: UiState.SEARCH, 2: UiState.EXIT, 3: UiState.BEGINING}
        name = selector[number]
        ui_main.set_state(name)

    def next(self, ui_main) -> None:
        pass
