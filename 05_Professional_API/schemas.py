from pydantic import BaseModel


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


class UserCreate(BaseModel):
    username: str
    password: str