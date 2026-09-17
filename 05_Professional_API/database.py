import sqlite3


def get_db():
    connection = sqlite3.connect("../02_FastAPI/students.db")
    connection.row_factory = sqlite3.Row
    return connection