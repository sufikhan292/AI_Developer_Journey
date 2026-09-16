from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection


students = [
    {"id": 1, "name": "Sufyan", "age": 23, "course": "AI"},
    {"id": 2, "name": "Saad", "age": 22, "course": "AI"}
]


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str


# @app.post("/Student")
# def create_stu(stu: Student):
#     return {
#         "message": "Enroll Successfully",
#         "name": stu.name,
#         "age": stu.age,
#         "course": stu.course
#     }

# @app.post("/Students")
# def create_stu(stu: Student):
@app.post("/Students", status_code=201)
def create_stu(stu: StudentCreate):
    connection = get_db()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students(name, age, course)
    VALUES (?, ?, ?)
    """, (stu.name, stu.age, stu.course))

    connection.commit()

    connection.close()

    return {
        "message": "Student save successfully",
        "name": stu.name,
        "age": stu.age,
        "course": stu.course
    }


# @app.get("/Student")
# def get_stu():
#     return students

@app.get("/Student", response_model=list[StudentResponse])
def get_stu():

    connection = get_db()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return [dict(student) for student in students]


# Old list-based GET route
# @app.get("/Student/{stu_id}")
# def stu_user(stu_id: int):
#
#     for student in students:
#         if student["id"] == stu_id:
#             return student
#
#     return {"message": "Student not found"}


@app.get("/Student/{stu_id}", response_model=StudentResponse)
def get_stu(stu_id: int):

    connection = get_db()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (stu_id,)
    )

    student = cursor.fetchone()

    connection.close()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
        # return {"message": "Student not found"}

    return dict(student)


@app.put("/Student/{stu_id}")
def update_student(stu_id: int, stu: StudentCreate):

    connection = get_db()

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, course = ?
    WHERE id = ?
    """, (stu.name, stu.age, stu.course, stu_id))

    if cursor.rowcount==0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.commit()

    connection.close()

    return {
        "message": "Student save successfully",
        "id": stu_id
    }


@app.delete("/Student/{stu_id}")
def delete_student(stu_id: int):

    connection = get_db()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (stu_id,)
    )

    if cursor.rowcount==0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found at this id"
        )

    connection.commit()

    connection.close()

    return {
        "message": "Student deleted successfully",
        "id": stu_id
    }