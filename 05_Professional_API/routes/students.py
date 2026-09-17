from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from database import get_db


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=list[StudentResponse])
def get_students(
    age: int | None = None,
    course: str | None = None
):
    connection = get_db()
    cursor = connection.cursor()

    if age is not None and course is not None:

        cursor.execute(
            "SELECT * FROM students WHERE age = ? AND course = ?",
            (age, course)
        )

    elif age is not None:

        cursor.execute(
            "SELECT * FROM students WHERE age = ?",
            (age,)
        )

    elif course is not None:

        cursor.execute(
            "SELECT * FROM students WHERE course = ?",
            (course,)
        )

    else:

        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    connection.close()

    return [dict(student) for student in students]


@router.post("/", status_code=201)
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



@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()
    connection.close()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return dict(student)


@router.put("/{student_id}")
def update_student(student_id: int, student: StudentCreate):

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (
        student.name,
        student.age,
        student.course,
        student_id
    ))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    connection.commit()
    connection.close()

    return {
        "message": "Student updated successfully",
        "id": student_id
    }


@router.delete("/{student_id}")
def delete_student(student_id: int):

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    connection.commit()
    connection.close()

    return {
        "message": "Student deleted successfully",
        "id": student_id
    }