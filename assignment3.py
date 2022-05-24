age =input("what is your age")
gender=input("what gender are you: male/female")


account_balance=0


if (int(age) > 25) and (int(age) < 30):
    account_balance=account_balance +10000
    print("confirmed you have received ksh 10000")
else:
    print("sorry no money for you")


