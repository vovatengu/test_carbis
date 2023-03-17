from state import State
from uistate import UiState
from ui import Ui


class BeginingState(State):
    def launch(self, ui_main) -> None:
        Ui.print_begining()
        number = int(input("Выберите действие: "))
        selector = {1: UiState.REGISTATION, 2: UiState.INPUT, 3: UiState.EXIT}
        name = selector[number]
        ui_main.set_state(name)

    def next(self, ui_main) -> None:
        pass
