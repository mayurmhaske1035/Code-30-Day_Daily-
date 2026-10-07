#
# class InsufficentBalanceError(Exception):
#     pass
# class invalidAmountError(Exception):
#     pass
# class Bank:
#     bank_name ="SBI"
#     def __init__(self, Name :str , Balance: float= 0.0):
#         self.Balance = Balance
#         self.Name = Name
#
#     def withdraw(self, amount: float):
#         if amount <= 0 :
#             raise invalidAmountError("error Amount")
#         elif(self.Balance >= amount) :
#             self.Balance -= amount
#             print(f"Withdraw amount {amount }. And reaming Balance is {self.Balance}")
#         else:
#             raise InsufficentBalanceError("Insufficent Balance")
#
#     def deposit(self, amount: float):
#         if amount > 0:
#             self.Balance +=amount
#             self.Balance= self.Balance
#             print(f"{amount} Deposited Successfully. Balance is {self.Balance}")
#         else:
#             print(f"Amount should be positive. Try again ! ")
#
#     def check_balance(self):
#         print(f"{self.Name} Balance is {self.Balance}")
#
# c1 = Bank("Mayur",250.0)
# try:
#     c1.withdraw(0)
# except InsufficentBalanceError as e:
#     print(e)
# except invalidAmountError as e:
#     print(e)
# #
# from asyncio import exceptions
#
#
# class Balance(exceptions):
#     def __init__(self, balance,message):
#         self.balance = balance
#         self.message = message
#         super.__init__(message)
#
#
# balance = 1000
#
# if balance >= 5000:
#     print(balance)
# else:
#     raise Balance(balance,"balance must 5000 ")
import json
from textwrap import indent
class Invalidstudnet(Exception):
    pass


data = {
    "Name" : "Mayur",
    "age"  : 23
}
with open("student.json","w") as file:
    json.dump(data,file)
try:

    with open("student.json", "r") as file:
        data = json.load(file)
    Name = "Mayur"
    if "Name" not in data:
        raise Invalidstudnet("Invalid student name")
except FileNotFoundError:
    print("Student file not found")

except json.decoder.JSONDecodeError:
    print("Student file not valid")
finally:
    print("Student validation completed")
