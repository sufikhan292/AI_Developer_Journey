from fastapi import FastAPI,status,HTTPException
import sqlite3
from pydantic import BaseModel

app = FastAPI()


# POST ke waqt jo data user bhejega
class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


# GET ke waqt database se jo data wapas jayega
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str


# Database connection
def get_db():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection


# Students table create karna
def create_table():
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)

    connection.commit()
    connection.close()


# Program start hote hi table create/check hogi
create_table()


# Student add karna
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students(name, age, course)
    VALUES (?, ?, ?)
    """, (student.name, student.age, student.course))

    connection.commit()
    connection.close()

    return {
        "message": "Student save successfully",
        "name": student.name,
        "age": student.age,
        "course": student.course
    }


# Saare students get karna
@app.get("/students", response_model=list[StudentResponse])
def get_students(
    age : int | None=None,
    course: str | None=None
    ):

    if age is not None or course is not None:
        connection=get_db()
        cursor=connection.cursor()
        
        cursor.execute("SELECT * FROM students WHERE age =? AND course=?",
                (age,course))
        
        students=cursor.fetchall()
        connection.close()
        
        return[dict(student)for student in students]

    elif age is not None:
        connection=get_db()
        cursor=connection.cursor()

        cursor.execute("SELECT * FROM students WHERE age= ?",
                       (age,))

        students= cursor.fetchall()
        connection.close()

        return[dict(student)for student in students]

    elif course is not None:
        connection=get_db()
        cursor=connection.cursor()

        cursor.execute("SELECT * FROM students WHERE course =?",
                       (course,))

        students=cursor.fetchall()
        connection.close()

        return[dict(student)for student in students]
        
    else:
        print("No filter")

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
    """)

    students = cursor.fetchall()
    connection.close()

    return [dict(student) for student in students]

@app.get("/students/{student_id}",response_model=StudentResponse)
def get_student(student_id:int):

    connection=get_db()
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?",
                   (student_id,))

    student= cursor.fetchone()
    connection.close()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return dict(student)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):

    connection=get_db()
    cursor=connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?,age=?,course=?
    WHERE id=?""",(student.name,student.age,student.course,student_id))

    if cursor.rowcount==0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    connection.commit()
    connection.close()

    return{
        "message":"Student updated successfully",
        "id":student_id
    }

@app.delete("/students/{student_id}")
def delete_student(student_id:int):

    connection=get_db()
    cursor=connection.cursor()

    cursor.execute("DELETE FROM students WHERE id=?",
                   (student_id,))

    if cursor.rowcount==0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student deleted successfully"
        )

    connection.commit()
    
    connection.close()
    
    return {
        "message": "Student deleted successfully",
        "id": student_id
    }