#!usr/bin/python
#############
#  Name :maureen june
#  date :06/08/2022
#  gui_examples using ktinker
#####################

#program to check if a number or word is a palindrome
#ask user to select which input to check number or letter
#after user enters their input the program should print based on the input inserted
print("Do you wish to enter a palindrome")

num = input('Enter any number : ')
try:
   val = int(num)
   if num == str(num)[::-1]:
      print('The given number is PALINDROME')
   else:
      print('The given number is NOT a palindrome')
except ValueError:
   print("That's not a valid number, Try Again !")


word=input('Enter any word : ')
try:
    val=word
    if word==(word)[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")
except ValueError:
    print("That's not a valid word, try again !")            