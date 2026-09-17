# Q1. Student Class
#
# Create a Student class with:
#
# name
# marks
# display() method
# class student:
#     def __init__(self, name , marks):
#          self.name = name
#          self.marks = marks
#     def display(self):
#         print("name: ", self.name, "Marks : ",self.marks )
#
# s1 =student("Mayur ", 34)
# s1.display()


#Create an Employee class with a private variable:
# Rules:
#
# Salary cannot be negative.
# Salary must be at least 10,000.
# If invalid salary is assigned, raise ValueError.
#
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary =salary
#
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, salary):
#         if salary < 10000:
#             raise ValueError (" Invalid salary ")
#         else:
#             self.__salary = salary
#
#     def display(self):
#         print(f" Name: {self.name} salary {self.salary} ")
#
# e1 = Employee("mayur",10000)
# e1.display()
# e1.salary = 1500
# e1.display

# class temprature:
#
#     def __init__(self,celsius ):
#         self.celsius = celsius
#
#     @property
#     def celsius(self):
#         print(self.__celsius)
#     @celsius.setter
#     def celsius(self,value):
#         if value > -273.15:
#             self.__celsius = value
#         else:
#             raise ValueError("Temprature is not satble ")
#         self.__celsius = value
#     def display(self):
#         print(f" Temperature is {self.__celsius}")
#
# t = temprature(-273)
# t.display()

