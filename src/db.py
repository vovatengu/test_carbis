import sqlite3
from .singleton import MetaSingleton


class Database(metaclass=MetaSingleton):
    """class to work with database2"""

    database = None

    def __init__(self):
        if self.database is None:
            self.database = sqlite3.connect("test.db")
            self.cursor = self.database.cursor()
            self._check_table()

    def _check_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY,
            Username TEXT,
            Password TEXT,
            Token TEXT,
            Secret TEXT,
            Language TEXT DEFAULT 'ru'
            )
            """
        )
        self.database.commit()

    def create_user(self, username, password, token, secret, language):
        self.cursor.execute(
            """INSERT INTO users (Username, Password, Token, Secret,Language) VALUES (?, ?, ?, ?,?)""",
            (username, password, token, secret, language),
        )
        self.database.commit()

    def check_user(self, username):
        self.cursor.execute("""SELECT * FROM users WHERE Username = ?""", (username,))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def login_user(self, username, password):
        self.cursor.execute(
            """SELECT * FROM users WHERE Username = ? AND Password = ?""",
            (username, password),
        )
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def get_token_and_secret(self, username):
        self.cursor.execute(
            """SELECT Token, Secret,Language FROM users WHERE Username = ?""",
            (username,),
        )
        token_and_secret = self.cursor.fetchone()
        if token_and_secret:
            return token_and_secret
        else:
            return False
