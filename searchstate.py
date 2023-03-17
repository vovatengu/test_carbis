import time

from state import State
from uistate import UiState
from person import Person
from db import Database as db
from api import Api
from ui import Ui

class SearchState(State):
    def launch(self, ui_main) -> None:
        Ui.clean()
        print("Поиск")
        connect = db()
        list_api = connect.get_token_and_secret(Person.username)
        Api.correct_data(token=list_api[0], secret=list_api[1], language=list_api[2])
        print("Kонец выполнения")
        time.sleep(2)
        ui_main.set_state(UiState.END)

    def next(self, ui_main) -> None:
        pass
