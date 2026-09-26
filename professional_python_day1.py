# def mul(*args):
#     result = 1

#     for number in args:
#         result = result * number

#     return result


# print(mul(2, 3))
# print(mul(2, 3, 6))
# print(mul(5, 2, 3))

# def calculate_average(*args):
#     total=sum(args)
#     average=total / len(args)
#     return average

# result=calculate_average(40,66,77,88,99,55)
# print(f"{result:.3f}")

# ------------------KWARGS----------------------------

# def student_info(**kwargs):
#     print(kwargs)


# student_info(
#     name="Sufyan",
#     age=20,
#     course="AI",
#     university="ABC"
# )


# def student_info(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])
#     print(kwargs["course"])

# student_info(
#     name="Sufyan",
#     age=20,
#     course="AI",
#     university="ABC"
# )

# def student_result(*marks, **info):
#     print (f"Name: {info["name"]}")
#     print(f"Course: {info["course"]}")
#     total=sum(marks)
#     average=total/len(marks)
#     print(f"Total number:{total}")
#     print(f"Average: {average:.3f}")

# student_result(
#     80,75,90,85,
#     name="Sufyan",
#     course="AI"
# )

# def order_summary(*items, **customer):
#     print(f"Customer: {customer['name']}")
#     print(f"City: {customer['city']}")
#     print(f"Items: {items}")
#     print(f"Total Items: {len(items)}")

# order_summary(
#     "mouse","keyboard","laptop",
#     name="Sufyan",
#     city="Karachi"
# )


# -------------------------------decorater--------------------------------

# def logger(func):
#     def wrapper():
#         print("Starting function....")

#         func()

#         print("Ended function.....")

#     return wrapper

# @logger
# def calculate():
#     print("Calculating....")

# calculate()


# def logger(func):
#     def wrapper(*args,**kwargs):
#         print("Starting function")

#         result=func(*args,**kwargs)

#         print("Ending function")

#         return result
#     return wrapper

# @logger
# def multiply(a,b):
#     return a*b

# print(multiply(5,6))

# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()

#         result=func(*args,**kwargs)

#         end=time.time()

#         print(f"Excution time:{end - start:.2f} seconds")

#         return result
#     return wrapper

# @timer
# def calculate():
#     time.sleep(2)

#     return 100

# print(calculate())

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()

#         result=func(*args,**kwargs)

#         end=time.time()

#         print(f"Execution time:{end - start:.2f} Seconds")

#         return result
#     return wrapper

# @timer
# def mulitply(a,b):
#     time.sleep(1)
#     return a*b

# print(mulitply(5,6))

# -------------------------------Generator--------------------------------------------

# def even_number():
#     for i in range(2,11,2):
#         yield i

# numbers = even_number()

# for number in numbers:
#     print(number)

# def cube_number(n):
#     for i in range(1,n+1):
#         yield i**3

# for number in cube_number(4):
#     print(number)    

# students=["Sufyan","ALi","Saad","Ahmed"]

# def student_generator(students):
#     for student in students:
#         yield student

# for student in student_generator(students):
#     print(student)

# ------------------------with---------------------------

# from contextlib import contextmanager

# @contextmanager
# def text_context():
#     print("Before")

#     yield 

#     print("After")

# with text_context():
#     print("Inside")

# from contextlib import contextmanager

# @contextmanager
# def process():
#     print("Starting process....")

#     yield

#     print("Ending process......")

# with process():
#     print("Doing work....")

# ----------------Hint type---------------------------

# def multiply(a:int,b:int) -> int:
#     return a*b

# result=multiply(5,7)
# print(result)

# def student_info(name:str,age:int,course:str)-> str:
#     return f"{name} is {age} year old and studies in {course}."

# result=student_info("Sufyan",21,"AI")
# print(result)

# def get_marks()->list[int]:
#     return [80,85,76,98,76]

# marks=get_marks()
# print(marks)

# from typing import Union

# def student_info()-> dict[str,Union[str,int]]:
#     return {
#         "name":"Sufyan",
#         "age":21,
#         "course":"AI"
#     }

# info=student_info()
# print(info)

# def get_products()->list[dict[str,str|int]]:
#     return [
#         {"Name":"Mouse","Price":1200},
#         {"Name":"Keyboard","Price":1500}
#     ]

# product=get_products()
# print(product)

# def find_product(product_id:int)-> str| None:
#     if product_id==1:
#         return "Mouse"

#     return None

# product=find_product(5)
# print(product)

def calculate_average(marks:list[int])-> float:
    total=sum(marks)
    average=total/len(marks)
    return average

marks=[87,82,83,85,84]

result=calculate_average(marks)
print(result)