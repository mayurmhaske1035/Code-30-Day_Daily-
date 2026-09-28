# import json
# student = {
#     "Name" : "Mayur",
#     "Age"  : 25,
#     "Skills" : ['python','sql','power BI']
#
# }
#
# with open("demo.json","r") as f :
#     json.dumps(student)
#     s = json.load(f)
# print(s)
# print(type(s))

sum = 0
for i in range(1,22):
    if i % 2 == 0:
        sum =+ i
        print(sum)