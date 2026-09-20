from abc import  ABC ,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class FullTime(Employee):
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
    def __str__(self):
        return self.name
    def salary(self):
        print(f"Salary{self.monthly_salary}")
class PartTime(Employee):
    def __init__(self,name,hours,rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def __str__(self):
        return self.name
    def salary(self):
        print(f"Salary{self.hours*self.rate})")

emp = [FullTime("Mayur",50000),PartTime("Rahul",180,150)]
for e in emp:
    print(e)
    e.salary()