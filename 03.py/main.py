from fastapi import FastAPI
import sqlite3

app=FastAPI()

def get_db():
    connection = sqlite3.connect("../02_FastAPI/students.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.get("/seacrh")
def seacrh_student(age:int):
    return{"age":age}

@app.get("/search")
def search_student(age: int = 20):
    return {"age": age}


@app.get("/search")
def search_student(age: int | None=None):
    return {"age": age}


@app.get("/search")
def search_student(age: int | None=None, course: str | None=None):
    return {
        "age": age,
        "course":course
        }

# @app.get("/students")
# def find_student(age:int | None=None , course: str|None=None):
#     return{
#         "age":age,
#         "course":course
#     }

# @app.get("/students")
# def find_students(age: int | None = None, course: str | None = None):

#     connection = get_db()
#     cursor = connection.cursor()

#     cursor.execute(
#         "SELECT * FROM students WHERE age = ? AND course = ?",
#         (age, course)
#     )

#     students = cursor.fetchall()
#     connection.close()

#     return [dict(student) for student in students]

@app.get("/students")
def find_students(age: int | None = None, course: str | None = None):

    if age is not None and course is not None:

        connection=get_db()

        cursor=connection.cursor()

        cursor.execute(
            "Select * from students WHERE age=? and course=?",
            (age,course)
        )

        students=cursor.fetchall()

        connection.close()

        return [dict(student)for student in students]
        

    elif age is not None:

        connection=get_db()
        
        cursor=connection.cursor()
        
        cursor.execute(
            "Select * from students WHERE age=?",
                (age,)
            )
        
        students=cursor.fetchall()
        
        connection.close()
        
        return [dict(student)for student in students]
        

    elif course is not None:

        connection=get_db()
                
        cursor=connection.cursor()
                
        cursor.execute(
            "Select * from students WHERE course=?",
                (course,)
            )
                
        students=cursor.fetchall()
                
        connection.close()
                
        return [dict(student)for student in students]
    
    else:
        connection = get_db()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()
        connection.close()

        return [dict(student) for student in students]
           