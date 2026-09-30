"""
    1
  2 2
3 3 3
"""

'''
student = [
    {"name" : "mayur ","age":22, "course":"ML"},
    {"name": "Rahul ", "age": 26, "course": "Data Scince"},
    {"name": "Shyam", "age": 20, "course": "BI"},

]
with open('student.json', 'w') as f:
    json.dump(student, f)
with open('student.json', 'r') as f:
    data = json.load(f)
    print(data[1]["name"])
    print(data[1]["course"])
----------------------------------------------------------
                Data Modification
              ----------------------  
s = [{"name":"mu","age":26,"course":"ml"}]
with open('student.json', 'r') as f:
    data = json.load(f)
data.append(s)
with open('student.json', 'w') as f:
    json.dump(data, f)
    print(data[4]["name"])

'''
# Searching
import json
with open('student1.json', 'r') as f:
    data = json.load(f)
ip = input("Enter your name: ")
flag = False
for i in data:
    if i["name"].lower().strip() == ip.lower().strip():
        print(i["name"])
        print(i["course"])
        flag = True
        break

if flag == False:
    print(f"{ip} is not in the list")
