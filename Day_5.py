# class product():
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return self.name + str(self.price)
#     def __add__(self,other):
#         total =  self.price+other.price
#         return total
# p1 = product("Laptop ",10000)
# p2 = product("Mouse  ",2000)
# print(p1)
# print(p2)
# total = p1 + p2
# print(total)

# class student():
#     def __init__(self,name,roll_no):
#         self.name = name
#         self.roll_no = roll_no
#     def __eq__(self,other):
#         return self.roll_no == other.roll_no
# s1 = student("Rahul",1)
# s2 = student("Ram",2)
# s3 = student("Rohan",1)
# print(s1 == s3)
# print(s2 == s3)

# class songs ():
#     def __init__(self,name):
#         self.name = name
#     def __getitem__(self,index):
#         return self.name[index]
#
# songs = songs(["s1","s2","s3"])
# print(songs[0])
# for i in songs:
#     print(i)

class Number ():
    def __init__(self,no):
        self.no = no
    def __getitem__(self,index):
        return self.no[index]
    def __contains__(self,index):
        return index in self.no

n  = Number([1,2,3,4,5,6])
print(n[0])
for i in n:
    print(i)
print(1 in n)