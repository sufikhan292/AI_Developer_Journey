# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "My first FastAPI is working!"}

# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/")
# def home():
#     return{"message":"My first FastApi us working!"}

# @app.get("/users")
# def get_users():
#     users = [
#         {"id": 1, "name": "Ali", "age": 20},
#         {"id": 2, "name": "Ahmed", "age": 21},
#         {"id": 3, "name": "Sufyan", "age": 20}
#     ]

#     return users

# @app.post("/users")
# def create_user(name:str,age:int):
#     return{
#         "message":"user created successfully",
#         "name":name,
#         "age":age
#     }



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int


# @app.get("/")
# def home():
#     return {"message": "My first FastAPI is working!"}


# @app.get("/users")
# def get_users():
#     users = [
#         {"id": 1, "name": "Ali"},
#         {"id": 2, "name": "Ahmed"}
#     ]
#     return users


# @app.post("/users")
# def create_user(user: User):
#     return {
#         "message": "User created successfully",
#         "name": user.name,
#         "age": user.age
#     }

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int


# @app.get("/")
# def home():
#     return {"message": "My first FastAPI is working!"}


# @app.get("/users")
# def get_users():
#     users = [
#         {"id": 1, "name": "Ali"},
#         {"id": 2, "name": "Ahmed"}
#     ]
#     return users


# @app.post("/users")
# def create_user(user: User):
#     return {
#         "message": "User created successfully",
#         "name": user.name,
#         "age": user.age
#     }

# @app.put("/users/{user_id}")
# def update_user(user_id:int,user:User):
#     return{
#         "message":"User updated Successfully",
#         "user_id":user_id,
#         "name":user.name,
#         "age":user.age
#     }



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "My first FastAPI is working!"}


@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Ahmed"}
    ]
    return users


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "name": user.name,
        "age": user.age
    }

@app.put("/users/{user_id}")
def update_user(user_id:int,user:User):
    return{
        "message":"User updated Successfully",
        "user_id":user_id,
        "name":user.name,
        "age":user.age
    }

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    return{
        "message":"User delete Successfully",
        "user_id": user_id
    }