#a dictionary is a collection of key value pairs  
#syntax:dictionary ={'key':'value}

list_names =['june','joy']
colours={'colour':'red'}
vehicles={'type':'toyota','plate_number':'KYS'}
#print (colours)

#print(type(list_names)) #we use the type of method
#accessing values in a dictionary
#print (vehicles['type']) #you can access the value of an element inside a dictionary using the key
#print (vehicles['plate_number'])

#Dictionary person
person={'name':'june',
        'gender':'female',
        'phone_no':'digits',
        'address':'sotik'}
person['age']='21'
person['colour']="black"
#print(type['person'])
#print(person)
print(person['name'])
print(person['age'])
print(person['colour'])
del person['phone_no']
print(person)

#names={'f_name':'jack','s_name':'wanyama'}
#gender={'male':'yes'}
#phone_no={'home_number':'070998755'}
#print(names['f_name'])
#print(gender['male'])
#print(phone_no['home_number'])

#looping over dictionaries
#for key, value in person.items():
 #  print(f"(key):(value)")

print(person.get ('password','the location key is non-existent'))

#returning a dictionary from a function
def create_full_name(f_name,s_name):
    person ={'first':f_name,
             'second':s_name}
    return person
student=create_full_name('derrick','kiptoo')
print (student)





