# import sqlite3

# connection = sqlite3.connect("students.db")

# cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     course TEXT
# )
# """)

# connection.commit()

# connection.close()

# import sqlite3

# # Database se connection
# connection = sqlite3.connect("students.db")

# # Cursor
# cursor = connection.cursor()

# # Students table create
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     course TEXT
# )
# """)

# # Pehla student add
# cursor.execute("""
# INSERT INTO students (name, age, course)
# VALUES (?, ?, ?)
# """, ("Sufyan", 23, "AI"))

# # Dusra student add
# cursor.execute("""
# INSERT INTO students (name, age, course)
# VALUES (?, ?, ?)
# """, ("Saad", 22, "AI"))

# # Changes save
# connection.commit()

# # Database se students read karo
# cursor.execute("SELECT * FROM students")

# students = cursor.fetchall()

# # Students terminal mein show karo
# print("Students in database:")
# print(students)

# # Connection close
# connection.close()

