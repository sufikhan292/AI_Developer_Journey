import csv
import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def clean_records(rows):
    seen = set()
    clean_students = []
    invalid_students = []
    duplicates = []

    for row in rows:
        age = row["age"]
        course = row["course"]
        email = row["email"]

        if not age:
            invalid_students.append({
                **row,
                "reason": "Missing age"
            })

        elif int(age) <= 0:
            invalid_students.append({
                **row,
                "reason": "Age must be greater than zero"
            })

        elif not course.strip():
            invalid_students.append({
                **row,
                "reason": "Missing course"
            })

        elif not email.strip():
            invalid_students.append({
                **row,
                "reason": "Missing email"
            })

        elif not is_valid_email(email):
            invalid_students.append({
                **row,
                "reason": "Invalid email format"
            })

        else:
            student_key = (
                row["name"],
                row["age"],
                row["course"],
                row["email"]
            )

            if student_key in seen:
                duplicates.append(row)
            else:
                seen.add(student_key)
                clean_students.append(row)

    return clean_students, invalid_students, duplicates


with open("students_raw.csv", "r") as file:
    reader = csv.DictReader(file)

    clean_students, invalid_students, duplicates = clean_records(reader)


with open("students_clean.csv","w",newline="")as file:
    fieldnames=["id","name","age","course","email"]

    writer=csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(clean_students)


with open("invalid_students.csv","w",newline="")as file:
    fieldnames=["id","name","age","course","email","reason"]

    writer=csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(invalid_students)


with open("duplicates.csv","w",newline="")as file:
    fieldnames=["id","name","age","course","email"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(duplicates)


print("\n===== CLEANING SUMMARY =====")
print("Total records:", len(clean_students) + len(invalid_students) + len(duplicates))
print("Clean records:", len(clean_students))
print("Invalid records:", len(invalid_students))
print("Duplicate records:", len(duplicates))



