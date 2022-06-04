#!usr/bin/python
#############
#  Name :maureen june
#  date :6/3/2022
#####################

#maximum speed and mileage distance
class vehicle:
    def __init__(self,_max_speed,_mileage):
        self.speed=_max_speed
        self.mileage=_mileage
    def vehicleSpeed(self):
        print (f"the maximum speed of the vehicle is {self.speed} and the mileage is {self.mileage}  kilometers")
toyota=vehicle(55 ,200)
toyota.vehicleSpeed()

mercedes=vehicle (60,80)
mercedes.vehicleSpeed()