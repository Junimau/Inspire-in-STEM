#name and salary
#should have two functions
#one that would display employee name and salary

class Employee:
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age
    def sayEmployee (self):
        print(f"name of employee is {self.name} and salary is {self.age}")
employee1=Employee('Daniel',24000)
employee1.sayEmployee()