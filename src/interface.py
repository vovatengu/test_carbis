from typing import Dict


# from .state import State
from .state.uistate import UiState
from .state.beginingstate import BeginingState
from .state.inputstate import InputState
from .state.registrationstate import RegistrationState
from .state.searchstate import SearchState
from .state.exitstate import ExitState
from .state.endstate import EndState


class UiLogic:
    """Класс main"""

    def __init__(self):

        self.__states: Dict[UiState, State] = {
            UiState.BEGINING: BeginingState(),
            UiState.INPUT: InputState(),
            UiState.REGISTATION: RegistrationState(),
            UiState.SEARCH: SearchState(),
            UiState.EXIT: ExitState(),
            UiState.END: EndState(),
        }
        self.__state: State = self.__states[
            UiState.BEGINING
        ]  # хранится экземпляр состояния
        self.next_state: UiState = None
        self.exit: UiState = None

    def launch(self):
        if self.exit == None:
            self.__state.launch(self)
        else:
            return False

    def get_state(self, state: UiState):
        return self.__states[state]

    def set_state(self, state: UiState):  # установка состояния
        self.__state = self.__states[state]
