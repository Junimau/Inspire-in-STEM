#!usr/bin/python
#############
#  Name :maureen june
#  date :6/2/2022
#####################

class Person:
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age
    def sayHi(self):
        print(f"Hello , my name is  {self.name} and i am {self.age} years old")
person1=Person('bob',14)
person1.sayHi()

person2=Person('james',22)
person2.sayHi()


