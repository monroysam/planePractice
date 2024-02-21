import random

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def flight_calc(self):
        self.flight = random.randint(0, 10)

    def get_wings(self):
        return self.wings
    
    def get_legs(self):
        return self.legs
    
    def get_miles(self):
        return self.flight