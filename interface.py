from typing import Dict


from state import State
from uistate import UiState
from beginingstate import BeginingState
from inputstate import InputState
from registrationstate import RegistrationState
from searchstate import SearchState
from exitstate import ExitState
from endstate import EndState


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
