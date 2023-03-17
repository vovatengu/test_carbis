import os


class Ui:

    clean = lambda: os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def print_begining(cls):
        cls.clean()
        print("Все действия:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

    @classmethod
    def print_clean(cls):
        cls.clean()

    @classmethod
    def print_input(cls):
        print("Все действия:")
        print("1. Поиск")
        print("2. Выход")

    @classmethod
    def print_end(cls):
        cls.clean()
        print("Все действия:")
        print("1. Поиск")
        print("2. Выход")
        print("3. Выход в главное меню")
