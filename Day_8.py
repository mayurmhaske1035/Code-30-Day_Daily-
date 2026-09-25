class Student :
    def __init__(self,name,roll_no,marks) :
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def __str__(self):
        return f"{self.name} {self.roll_no} "
    @property
    def marks(self) :
        return self.__marks
    @marks .setter
    def marks(self,marks) :
        if marks > 0 :
            self.__marks = marks
        else:
            raise ValueError("marks cannot be less than 0")
s1 = Student("Smith",1,2)
print(s1)
print(s1.marks)