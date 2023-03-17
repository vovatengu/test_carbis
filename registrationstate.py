from state import State
from uistate import UiState
from db import Database as db
from ui import Ui
import time


class RegistrationState(State):
    def launch(self, ui_main) -> None:
        connect = db()
        Ui.print_clean()
        username = input("Введите имя пользователя: ")
        if connect.check_user(username):
            print(
                f"Пользователь с таким именем уже существует\nВыберите уникальное имя\n"
            )
            time.sleep(2)
            ui_main.set_state(UiState.BEGINING)
            return
        password = input("Введите пароль: ")
        token = input("Введите токен (API-ключ): ")
        secret = input("Введите секрет (Секретный ключ): ")
        language = input("Введите язык: ru или en: ")
        print("Пользователь создан")
        time.sleep(2)
        connect.create_user(
            username=username,
            password=password,
            token=token,
            secret=secret,
            language=language,
        )
        ui_main.set_state(UiState.BEGINING)

    def next(self, ui_main) -> None:
        pass
