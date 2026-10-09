# import json
#
# from Day_11 import data
#
#
# class StudnetData(Exception):
#     pass
#
# try:
#      with open("student.json", "r") as file:
#          data = json.load(file)
#      if "Name" not in data or data["Name"] == " ":
#          raise StudnetData("Student Name is not valid ")
#      if "Age" not in data or data["Age"] is None:
#          raise StudnetData("Student Age is not valid ")
#      if  isinstance('Age',int) and  data["Age"] <=18 and data["Age"] <= 100:
#          raise StudnetData("Student Age is less than 18 or Not Valid")
#
#      print("student data is validated")
#
# except FileNotFoundError:
#     print("Student data not found ")
# except StudnetData as e :
#    print(e)
# except json.decoder.JSONDecodeError as e:
#     print(e)
import logging
logging.basicconfig(levle = logging.DEBUG)
logging.debug("in this detailed debuging info ")