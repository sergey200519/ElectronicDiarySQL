import sqlite3
import os


class Database:
    def __init__(self, name_db):
        self.name_db = name_db
        path = os.getcwd()
        self.connstring = f"{path}/{name_db}.db"

    def create_table(self, name_table, fields, id=False, other=""):
        fields_list = ["ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE"] if id else []
        for key, value in fields.items():
            fields_list.append(f"{key} {value}")
        fields_str = ", ".join(fields_list)
        request_str = f"CREATE TABLE IF NOT EXISTS {name_table}({fields_str});"
        self.request_SQL(request_str)

    def request_SQL(self, request, get=False):
        con = sqlite3.connect(self.connstring)
        cursor = con.cursor()
        res = cursor.execute(request)
        if get:
            return res.fetchall()
        con.commit()
        con.close()

    def select_from_table(self, table):
        return self.request_SQL(f"SELECT * FROM {table}", get=True)

    def table_is_exists(self, table):
        res = self.request_SQL(f"""SELECT name FROM sqlite_master WHERE type='table' 
  AND name='{table}';""", get=True)
        if res == []:
            return True
        return False

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls, *args, **kwargs)
    