import json
with open('student1.json', 'r') as f:
    data = json.load(f)
ip = input("Enter your name: ")
flag = False
for i in data:
    if ip == i["name"]:
        print(i["name"])
        print(i["course"])
        flag = True
        break

if flag == False:
    print(f"{ip} is not in the list")
