# # import requests

# # url="https://jsonplaceholder.typicode.com/users"

# # response=requests.get(url)

# # print(response.status_code)

# # data = response.json()

# # # print(data)

# # print(data[4]["name"])

# # import requests

# # url="https://jsonplaceholder.typicode.com/users"

# # response=requests.get(url)

# # print("Status Code:",response.status_code)

# # data = response.json()

# # for user in data:
# #     if "biz" in user["email"]:
# #         print("Name",user["name"])
# #         print("Email",user["email"])

# #     # print("Name",user["name"])
# #     # print("Email",user["email"])

# import requests

# url="https://jsonplaceholder.typicode.com/users"

# response=requests.get(url)

# data = response.json()

# search_name=input("Enter username: ")

# found= False

# for user in data:
#     if user ["name"].lower() == search_name.lower():
#         print("User Found!")
#         print("Name:",user["name"])
#         print("Email:",user["email"])
#         print("City:",user["address"]["city"])
#         found=True

# if not found:
#     print("User not found")

# ---------------- PAGINATION PRACTICE ----------------

import requests

page = 1
limit = 5

url = f"https://jsonplaceholder.typicode.com/users?_page={page}&_limit={limit}"

response = requests.get(url)

data = response.json()

print("Users on this page:")

for user in data:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("----------------")