#!usr/bin/python
#############
#  Name :maureen june
#  file:operations_module.py
#  date :6/6/2022
#####################

import operations   
from students import Student
from classes import Classes
from teachers import Teachers

print(operations.add_num(35,45))
print(operations.sub_num(67,23))
print(operations.mult_num(4,78))
print(operations.div_num(55,11))


new_student=Student("melvin","dancing","2003")
Student.greet_student()

new_class=Classes("green",50,"A")
Classes.build_classes()

new_teacher=Teachers("Mr john",254647,"literature",25000)
Teachers.get_tsc_number()

