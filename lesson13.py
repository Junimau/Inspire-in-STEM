#!usr/bin/f
 
#arithmetic progression

from this import d

a = (int(input("enter first number")))
b = (int(input("enter first number")))
n = (int(input("enter first number")))

i =1
for i in range (i,n + 1):
     n_term =a + (i - 1) * d
     print (n_term)

sum_n =(n_term/2) * (2*a +(n-1)*d)
print(sum_n)