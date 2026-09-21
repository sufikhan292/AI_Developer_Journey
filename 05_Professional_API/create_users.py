from database import get_db

connection=get_db()
cursor=connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL)""")

connection.commit()
connection.close()

print("User table created successfully")