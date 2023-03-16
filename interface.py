from typing import Dict
from abc import ABC, abstractmethod
from enum import Enum
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class UiState(Enum):
    """Возможные состояния кофе-машины"""
    BEGINING = 0
    INPUT = 1
    REGISTATION = 2
    SEARCH = 3
    EXIT = 4

class State(ABC):
    """Базовый класс состояния,
    определяющий интерфейс"""

    @abstractmethod
    def launch(self, ui_main) -> None:
        ...
    @abstractmethod
    def next(self, ui_main) -> None:
        ...    

class BeginingState(State):
    
    def launch(self,ui_main)-> None:
        cls()
        print("Начальное состояние1")
        number = int(input("Доступные действия:1 -регис 2-вход 3-выход "))

        selector = {1: UiState.REGISTATION,
                    2: UiState.INPUT,
                    3: UiState.EXIT}

        name = selector[number]

        ui_main.set_state(name)
    
    def next(self, ui_main) -> None:
        pass

class InputState(State):
    
    def launch(self,ui_main)-> None:
        cls()
        print("Начальное состояние2")
        number = int(input("Доступные действия:1 -поиск 2-выход "))

        selector = {1: UiState.SEARCH,
                    2: UiState.EXIT}

        name = selector[number]

        ui_main.set_state(name)
    
    def next(self, ui_main) -> None:
        pass
    
class RegistrarionState(State):
    
    def launch(self,ui_main)-> None:
        cls()
        print("Начальное состояние3")
        print("Введите  имя")

        ui_main.set_state(UiState.BEGINING)
    def next(self, ui_main) -> None:
        pass
    
class SearchState(State):
    
    def launch(self,ui_main)-> None:
        cls()
        print("Начальное состояние4")
        print("Введите адрес")
        print("конец выполнения")
        
        number = int(input("Доступные действия:1 -поиск 2-выход 3-выход в главное меню "))

        selector = {1: UiState.SEARCH,
                    2: UiState.EXIT,
                    3: UiState.BEGINING}

        name = selector[number]

        ui_main.set_state(name)
    
    def next(self, ui_main) -> None:
        pass
    
class ExitState(State):
    
    def launch(self,ui_main)-> None:
        cls()
        print("Конец")
        ui_main.exit = UiState.EXIT 
        ui_main.set_state(ui_main.exit)

    
    def next(self, ui_main) -> None:
        pass
                    
class UiLogic:
    """Класс кофе-машины"""
    def __init__(self):

        self.__states: Dict[UiState, State] = {
            UiState.BEGINING: BeginingState(),
            UiState.INPUT: InputState(),
            UiState.REGISTATION: RegistrarionState(),
            UiState.SEARCH: SearchState(),
            UiState.EXIT: ExitState()
        }
        self.__state: State = self.__states[UiState.BEGINING] #хранится экземпляр состояния
        self.next_state: UiState = None
        
        self.exit: UiState = None
    
    def launch(self):
        print('Запуск')
        if self.exit == None:
            self.__state.launch(self)
        else: 
            return False

    def get_state(self, state: UiState):
        return self.__states[state]

    def set_state(self, state: UiState): # установка состояния 
        self.__state = self.__states[state]
    

if __name__ == "__main__":
    a = UiLogic()
    # while True:
    #     a.launch()

    while a.launch() != False:
        continue
    # print(a.next_state)
    # print(a._UI__states)
    # print(dir(a)) 
    # print(a._UI__state)
    
    # a.launch()
    # print(a.next_state)
    # print(a._UI__states)
    # print(dir(a)) 
    # print(a._UI__state)


    