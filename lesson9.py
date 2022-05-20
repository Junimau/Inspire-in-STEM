#lists: use box brackets/ Has index/ single quotes
motorcycle=['Yamaha','Duncatti','Honda']
plate_number=['Y123\n','D123\n','H123']
motorcycle_owner="Harvey Specter"
print (motorcycle)

#Accessing list items using index
print(motorcycle[2])

#changing element in a list
motorcycle[1]='Ducatti'
print("I love" +str(motorcycle[1]))

#add item into a list .append('')
motorcycle.append('Navi')
print(motorcycle)


print(motorcycle[0] + plate_number[0], motorcycle[1] +plate_number[1], motorcycle[2] +plate_number[2])
#working with lists
#loops :while/for

#delete item from list
del motorcycle[1]
print (motorcycle)

#delete item from list method 
popped_motorcycle=motorcycle.pop()
print(motorcycle)
print(f"my name is {motorcycle_owner} and i own a {motorcycle[1]} motorcycle{plate_number[1]}")

#removing an item from a list
motorcycle.remove('Yamaha')
print(motorcycle)