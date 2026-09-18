# class  Employee :
#     def __init__(self,name,salary ):
#         self.name = name
#         self.salary = salary
#     def work(self):
#         print("Empolyee is  Working ")
#
# class Manager(Employee):
#     def work(self):
#         print(f"{self.name} is managing team")
#
# class Developer(Manager):
#     def work(self):
#         print(f"{self.name} is developing  ")
#     def show_salary(self):
#         print(f"salary : {self.salary}")
#
# d1 = Developer("Mayur",25000)
# d1.work()
# d1.show_salary()
# d2 = Manager("Mayur", 50000)
# d2.work()

#---------------------------------------------
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print("Animal making sound ")
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} Barks")
#         super().speak()
# class Labrador(Dog):
#     def speak(self):
#         print(f"{self.name} is labrador")
#         super().speak()
#
# l = Labrador("Bruno")
# l.speak()

c