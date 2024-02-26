import random

class Insect:

    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n

    def flight_calc(self):
        self.flight = random.randint(0, 10)

    def get_wings(self):
        return self.wings
    
    def get_legs(self):
        return self.legs
    
    def get_miles(self):
        return self.flight
    
    def get_name(self):
        return self.name