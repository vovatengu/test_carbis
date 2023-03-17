from state import State
from uistate import UiState
from person import Person
from db import Database as db
from ui import Ui
import time


class InputState(State):
    def launch(self, ui_main) -> None:
        connect = db()
        Ui.print_clean()
        print('Вход')
        Person.username = input("Введите имя пользователя: ")
        Person.password = input("Введите пароль: ")
        if connect.login_user(Person.username, Person.password):
            print("Вход выполнен")
            time.sleep(2)
            ui_main.set_state(UiState.END)
            return

        else:
            print("Неверный логин или пароль")
            time.sleep(2)
            ui_main.set_state(UiState.BEGINING)
            return

    def next(self, ui_main) -> None:
        pass
