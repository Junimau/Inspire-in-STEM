#!usr/bin/python
#############
#  Name :maureen june
#  date :5/31/2022
#####################

#function of quadratic equation
a= int(input("enter coefficient of the first term"))
b= int(input("enter coefficient of the second term"))
c= int(input("enter the constant"))


import math

w= math.sqrt(b**2 -4 * a * c)
def find_roots (a,b,c):
    y1 =(-b + w) /(2*a)
    y2 =(-b - w) /(2*a)
    print("the roots of the quadratic equation are:", y1, y2)

find_roots(a,b,c)