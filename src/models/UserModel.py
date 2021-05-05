from pydantic import BaseModel
import sqlite3
con = sqlite3.connect('./data/db.sqlite')
cur = con.cursor()

#    def __init__():
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    email       TEXT    NOT NULL,
    password    TEXT    NOT NULL,
    is_admin    TEXT    NOT NULL
    );''')

class UserModel(BaseModel):
    id: int
    name: str
    password: str
    email: str
    is_admin: bool = False
