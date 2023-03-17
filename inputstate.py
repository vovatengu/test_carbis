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
        Person.username = input("Введите имя пользователя: ")
        Person.password = input("Введите пароль: ")
        print(Person.username)
        print(Person.password)
        Ui.print_clean()
        if connect.login_user(Person.username, Person.password):
            print("Вход выполнен")
            ui_main.set_state(UiState.END)
            return

        else:
            print("Неверный логин или пароль")
            time.sleep(1)
            ui_main.set_state(UiState.BEGINING)
            return

    def next(self, ui_main) -> None:
        pass
