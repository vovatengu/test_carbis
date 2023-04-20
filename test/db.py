import sqlite3


class Database():
    """class to work with database2"""

    database = None

    def __init__(self):
        if self.database is None:
            self.database = sqlite3.connect("test.db")
            self.cursor = self.database.cursor()
            self._check_table()

    def _check_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS settings (
            ID INTEGER PRIMARY KEY,
            Token TEXT,
            Secret TEXT ,
            Language TEXT DEFAULT 'ru' )
            """
        )
        # a = self.cursor.execute("""SELECT * FROM settings""").fetchone()
        # print(a)
        if self.cursor.execute("""SELECT * FROM settings""").fetchone() == None:
            self.cursor.execute("""INSERT INTO settings (Token, Secret) VALUES ('default', 'default')""")
            print("good")

        self.database.commit()

    def set_token(self, token):
        self.cursor.execute(
            """UPDATE settings set Token = ? WHERE ID = 1 """,
            (token,),
        )
        self.database.commit()
    
    def set_secret(self, secret):
        self.cursor.execute(
            """UPDATE settings set Secret = ? WHERE ID = 1 """,
            (secret,),
        )
        self.database.commit()
        
    def set_language(self, language):
        self.cursor.execute(
            """UPDATE settings set Language = ? WHERE ID = 1 """,
            (language,),
        )
        self.database.commit()        

    def get_token(self):
        self.cursor.execute(
            """SELECT Token FROM settings WHERE ID = 1 """,
        )
        token = self.cursor.fetchone()[0]
        
        return token
    
    def get_secret(self):
        self.cursor.execute(
            """SELECT Secret FROM settings WHERE ID = 1 """,
        )
        secret = self.cursor.fetchone()[0]

        return secret    
    
    def get_language(self):
        self.cursor.execute(
            """SELECT Language FROM settings WHERE ID = 1 """,
        )
        language = self.cursor.fetchone()[0]

        return language