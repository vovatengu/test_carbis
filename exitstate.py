from state import State
from uistate import UiState


class ExitState(State):
    def launch(self, ui_main) -> None:
        print("Конец")
        ui_main.exit = UiState.EXIT
        ui_main.set_state(ui_main.exit)

    def next(self, ui_main) -> None:
        pass
