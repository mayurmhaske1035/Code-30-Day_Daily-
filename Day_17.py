import json

data = {
    "Name" : "Gayu",
    "Age"  : 19
}
with open("student.json", 'w') as f:
    json.dump(data, f,indent= 4)

class InvalidStudent(Exception):
    pass
try :
    with open("student.json", 'r') as f:
        file = json.load(f)

    if "Name" not in  file:
        raise InvalidStudent("Student name must be saved")
    if 'Age'  not  in file:
        raise InvalidStudent("Invalid student age")
    if not isinstance(file['Age'],int):
        raise InvalidStudent("Student age must be saved")
    if file["Age"] < 18:
        raise InvalidStudent("Student age must be at least 18")
    print("Student data is validated successfully")

except FileNotFoundError as e:
    print(e)
except InvalidStudent as e:
    print(e)
finally :
    print("validation Completed")