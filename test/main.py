from abc import ABC, abstractmethod
from typing import List, Callable
from function import search , set_token , set_language, set_secret
 
class IStateMachine(ABC):
    def __init__(self, initial_state: "IState") -> None:
        self.current_state = initial_state
        self.back_state = None
    
    @property
    def title(self) -> 'IState':
        return self.current_state
    
    @abstractmethod
    def run(self) -> None:
        ...


class IState(ABC):
    def init(self, title: str, states: List["IState"]) -> None:
        self.title = title
        self.states = states

    @abstractmethod
    def draw(self, state_machine: IStateMachine) -> None:
        ...

class Menu(IStateMachine):
    def run(self) -> None:
        while True:
            self.current_state.draw(self)

class SelectorState(IState):
    
    def __init__(self, title: str, states: List[IState]) -> None:
        self.__title__ = title
        self.__states__ = states
        self.__back_state__ = None

    @property
    def back_state(self) -> 'IState':
        return self
    
    @property
    def title(self) -> 'IState':
        return self.__title__
    
    def draw(self, state_machine: IStateMachine) -> None:
        
        print(f"====={self.title}=====\n")
        for idx,state in enumerate(self.__states__):
            print(f'{idx +1} {state.title}')
            # if idx == len(self.states) - 1:
            #     print(f'100 {state_machine.current_state.title}')
        print(f'0 Выход')
        try:
            user_input = int(input('>>'))
        except ValueError:
            return
        

        if user_input > 0 and user_input <= len (self.__states__):
            state_machine.current_state = (self.__states__[user_input - 1])
            state_machine.back_state = self
        elif user_input == 0:
            state_machine.current_state = state_machine.back_state

class FunctionState(IState):
    def __init__(self, title:str, fun: Callable) -> None:
        # super().__init__(title = title, states = [] )
        self.title = title
        self.function = fun
    
    def draw(self, state_machine: IStateMachine) -> None:
        self.function()
        state_machine.current_state = state_machine.back_state


def test():
    Menu(SelectorState(
        'Главное меню',
        [
            FunctionState('Поиск',search),
            SelectorState('Настройки', [
                FunctionState('Токен',set_token),
                FunctionState('Секрет',set_secret),
                FunctionState('Язык',set_language),
            ])
        ]
    )).run()


if __name__ == "__main__":
    test()