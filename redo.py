#IMPORTS
import random
import numpy
import pandas

#VARIABLES
size = ["platoon", "company", "mlr"]
state = ["competition", "crisis", "conflict"]

def generator(self):
    for size in size:
        for state in state:
            unit = Unit()
            Unit.size(unit)
            Unit.state(unit)
class Unit:
    def __init__(self, type, state, inflation, attrition):
        self.type = type
        self.state = state
        self.inflation = inflation
        self.attrition = attrition
        
    def size(self, unit):  
        if unit.type == "platoon":
            self.size = 50
        if unit.type == "company":
            self.size = 400
        if unit.type == "mlr":
            self.size = 2000

    def state(self):
        if self.state == "crisis":
            self.inflation = 1.5
            crisis_attrition_factor = random.uniform(0.01, 0.1)
            self.platoon_crisis_attrition = (size - size * crisis_attrition_factor)

        if self.state == "conflict":
            self.inflation = 2
            conflict_attrition_factor = random.uniform(1, 3)
            self.platoon_crisis_attrition = (size - size * crisis_attrition_factor)

