# import bcrypt


# password = "mypassword123"

# hashed_password = bcrypt.hashpw(
#     password.encode("utf-8"),
#     bcrypt.gensalt()
# )

# print("Original Password:", password)
# print("Hashed Password:", hashed_password.decode("utf-8"))

import bcrypt


password = "mypassword123"

# Password ko hash karna
hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print("Hashed Password:", hashed_password.decode("utf-8"))


# Password verify karna
correct_password = bcrypt.checkpw(
    password.encode("utf-8"),
    hashed_password
)

print("Correct password:", correct_password)


# Galat password test
wrong_password = "wrongpassword"

wrong_result = bcrypt.checkpw(
    wrong_password.encode("utf-8"),
    hashed_password
)

print("Wrong password:", wrong_result)