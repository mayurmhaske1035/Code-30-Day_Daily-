# try:
#     a = int(input("enter age"))
#     print(a)
# except ValueError:
#     print("Age is not valid")
# else:
#     print("there is no excption")
# finally:
#     print("it is finally ")
import json

# try :
#     salary= int(input("enter salary"))
#     if salary < 10000 :
#         raise ValueError("salary must be greater than 10000")
# except ValueError as e:
#     print(e)
# else:
#     print("salary is valid")
# finally:
#     print("validation is completed")
#
# a = [1,2,3,4,5,6,8]
# try:
#     index = int(input("enter index"))
# except ValueError:
#     print("enter correct index")
# except IndexError:
#     print("enter correct index")
# except Exception as e:
#     print(e)
try:
   file = input("Enter file name: ")
except FileNotFoundError:
    print("File not found")
else:
    open(file, "r")
    dara = file.read()
    print(dara)
finally:
    if file is not None:
        file.close()

    print("file is closed")
