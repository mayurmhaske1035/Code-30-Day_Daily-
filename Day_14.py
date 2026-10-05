import json

data = [
        {
         "name": "Mayur",
         "age": 22,
         "course": "ML"
         },
       {
        "name": "Rahul",
        "age": 26,
        "course": "DL"
        },
      {
        "name": "Shyam",
        "age": 20,
        "course": "BI"
      }
]
# creating  new file with code and inserting data
with open ("student_data.json",'x') as f :
    json.dump(data,f,indent=4)
    print("created and saved")

with open("student_data.json", "r") as f:
    data_ = json.load(f)
    print(data_)
    print("read data")
name = input("enter name")
flag = 0
for i in data_ :
    if name.strip().lower() == i['name'].strip().lower():
        course = input("enter new course")
        i["course"] = course
        print("course updated")
        flag = 1
        break
if flag :
    with open("student_data.json", "w") as f:
        json.dump(data_,f,indent = 4)
        print("updated data is saved")
        print(data_)

else:
    print("name not found")

