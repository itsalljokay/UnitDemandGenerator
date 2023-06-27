#IMPORTS
import random
import numpy
import pandas

#VARIABLES
unit_size = ["Platoon", "Company", "MLR"]
unit_state = ["Competition", "Crisis", "Conflict"]

def generator():
    for size in unit_size:
        for state in unit_state:
            unit = UnitFactors(size, state)
            UnitFactors.size(unit)
            UnitFactors.state(unit)
class UnitFactors:
    def __init__(self, type, state):
        self.type = type
        self.state = state
        self.inflation_factor = 0
        self.attrition_size = 0
        
    def size(self):  
        if self.type == "Platoon":
            self.size = 50
        if self.type == "Company":
            self.size = 400
        if self.type == "MLR":
            self.size = 2000
        print("Unit Type: ", self.type)
        print("Unit Size: ", self.size)

    def state(self):
        size = self.size
        if self.state == "Crisis":
            self.inflation_factor = 1.5
            attrition_factor = random.uniform(0.01, 0.1)
            self.attrition_size = (size - size * attrition_factor)

        if self.state == "Conflict":
            self.inflation_factor = 2
            attrition_factor = random.uniform(1, 3)
            self.attrition_size = (size - size * attrition_factor)

        print("Unit State: ", self.state)
        print("Inflation Factor: ", self.inflation_factor)
        print("Attrition Size: ", self.attrition_size)

generator()