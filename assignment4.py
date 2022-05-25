acc_bal =input("enter your account balance")

if (int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal=int(acc_bal) - 25000
    print("we have deducted ksh 25000")
    
elif (int(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal = int(0.3*acc_bal)
    print("we have deducted 30 percent ")

elif (int(acc_bal) > 1000000):
         acc_bal=int(acc_bal) -15000
         print("we have deducted ksh 15000")
else : 
    print("no deductiion")
