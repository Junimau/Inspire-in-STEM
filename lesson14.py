#how to find divisibility
num = int(input("enter a number"))
x = int(input("enter number"))
y =int (input("enter number"))

if (x%num==0) and (y%num==0):
    print ("the number is divisible")
else:
    print ("the number is not divisible")
     
#a program to check if a number is divisible by 5 or 7
number = int (input("enter a number"))
if (number%x==0) or (number%y==0):
    print(f"the number{number} is divisible by {x} or {y}")
elif(number%x==0) or not (number%y==0):
    print(f"the number{number} is divisible by {x} or not divisible by {y}")
elif(number%y==0) or not (number%x==0):
    print(f"the number{number} is divisible by {y} or not divisible by {x}")
else:
    
    print(f"the number{number} is not divisible by {x} or {y}")


