#!usr/bin/python
#############
#  Name :maureen june
#  date :6/3/2022
#####################

print ("WELCOME TO OUR PASSWORD GENERATOR")
#Ask user number of passwords they would like to generate
#num_passwords
#convert the input to integer
#Ask user for password length and convert len password to interger
#len_password

import random
name = input("Enter your full name:")
email = input ("enter your email address:")
print ("Enter the number of passwords you would like to generate")
character=str("1234567890")
num_password=int(input("what is your number of password you would like to generate:"))
len_password=int(input("what length do u wish your password to be:"))
print ("\n Here are your passwords!")

for password in range (num_password):
    password=''
    for c in range (len_password):
        password += random.choice(character)
    print(password)


