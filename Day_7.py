class Student :
    def __init__(self,name,age,roll_no,marks) :
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks
s1 = Student("James",22,123,96)
print(F"NAME:{s1.name}\nROLL NO:{s1.roll_no}\nMARKS: {s1.marks}")
