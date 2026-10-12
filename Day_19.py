print("Student Data Records ")


def Add_student():
    print("Enter Student Name")
    Name = input()
def Search_student():
    pass

def Delete_Student():
    pass

def Update_Marks():
    pass

Choice = int(input("Enter Choice to perform :  \n 1: Add Student \n 2: Serach Student \n 3: Delete Student \n 4:Update MArks   \n == >>   "))
match Choice:
    case 1: Add_student()
    case 2: Search_student()
    case 3: Delete_Student ()
    case 4: Update_Marks()
    case __ : print("Please Enter Correct Choice")