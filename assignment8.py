#program to write numbers in reverse

def reverse(number):
  y=0
  while(number>=1):
   z = number % 10
   y = 10 * y + z
   number = number / 10
   number = int(number)
  return y
Number=int(input("Enter a number: "))
reverse_number=reverse(Number)
print("Reverse of the number",Number," is ",reverse_number)
