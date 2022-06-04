#!usr/bin/python
#############
#  Name :maureen june
#  date :5/31/2022
#####################

#a function is a block of code executed as one
##initializing fuctions
#calling function

def say_hello():
    print ("hello from JKUAT")

    x=0
    y=7
    z= x + y
    print(z)

say_hello() #calling function

def bark():
    print("dogs woof woof")
def moo():
    print("cows moo moo")
def neighs():
    print("horse neigh neigh")

#bark()
#moo()
#neighs()

#function to add two numbers

def add_numbers (x,y):
    sum_numbers = x + y
    print ("the sum of numbers:" ,sum_numbers)

add_numbers(40,50)
add_numbers(100,400)
add_numbers(1,4)

#function for product of numbers
def multiply_numbers(x,y):
    prod_numbers = (x * y)
    print("the product of numbers:",prod_numbers)

multiply_numbers(4,5)
multiply_numbers(60,43)

#using default parameters
def print_name(name="maureen june"):
    print (name)

print_name("jane")

#return from a function
def get_sum(num1,num2):
    sum_nums=num1 + num2
    return sum_nums
print(get_sum(7,12))

#getting the power of numbers 
def get_power(number, power):
    pow_num= number**power
    return pow_num
print(get_power(3,5))=

def get_full_name(f_name,s_name):
    full_name=f_name +"" + s_name
    return full_name
print(get_full_name("maureen","june"))

#passing a list in a function
def greet_friends(names):
    for name in names:
        msg="hello " + name.title()+"!"
        print (msg)
friends=['margi','lesly','john']
greet_friends(friends)
 