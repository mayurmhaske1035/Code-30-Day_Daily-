# import json
# data = [{"name": "Mayur", "age": 22, "course": "ML"},
#     {"name": "Rahul", "age": 26, "course": "DL"},
#     {"name": "Shyam", "age": 20, "course": "BI"}]
# # with open("student_data.json",'x+') as f:
# #     json.dump(data,f,indent = 4)
#
# with open("student_data.json","r") as f:
#     data = json.load(f)
#     with open("student_data.json","w") as f:
#         flag = 0
#         name = input("Enter student name: ")
#         for i in data:
#             if i["name"].strip().lower() == name.strip().lower():
#                 course = input("enter course :")
#                 i['course'] = course
#                 print("succssful")
#                 flag = 1
#                 break
#         if flag == 0:
#             print(f"{name} is not in the list")
#         json.dump(data, f, indent=4)
#
#     print(data)
#


import json

with open("student_data.json", "r") as f:
    data = json.load(f)

flag = False
name = input("Enter student name: ")

for i in data:
    if i["name"].strip().lower() == name.strip().lower():
        course = input("Enter course: ")
        i["course"] = course
        flag = True
        break

if flag:
    with open("student_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Successful")
    print(data)
else:
    print(f"{name} is not in the list")