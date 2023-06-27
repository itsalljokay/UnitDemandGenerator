#THIS IS DEMAND PER DAY

#IMPORTS
import random
import numpy
import pandas

#VARIABLES
unit_size = ["Platoon", "Company", "MLR"]
unit_state = ["Competition", "Crisis", "Conflict"]
 
#DEFINE DATA
class UnitFactors:
    def __init__(self, type, state):
        self.type = type
        self.state = state
        self.inflation_factor = 1
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

    #CLASS ONE: FOOD
    def demand(self):
        #CLASS ONE: FOOD
        #3 MREs per Marine
        class_one_individual_mean = 3
        class_one_mean = (class_one_individual_mean * self.size) * self.inflation_factor
        class_one_stdev = 1
        self.class_one_demand = numpy.random.normal(class_one_mean, class_one_stdev) - self.attrition_size

        #CLASS TWO: EQUIPMENT
        # SOURCE
        class_two_individual_mean = 3
        class_two_mean = (class_two_individual_mean * self.size) * self.inflation_factor
        class_two_stdev = 1
        self.class_two_demand = numpy.random.normal(class_two_mean, class_two_stdev) - self.attrition_size


#DATA STORAGE
class Data:
    #Contains all of the base data. The demand here is amount needed for one day.
    all_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Attrition Size": [],
        "Class One Demand": [],
        "Class Two Demand": [],
        "Class Three Demand": [],
        "Class Five Demand": [],
        "Class Six Demand": [],
        "Class Seven Demand": [],
        "Class Nine Demand": [],
        "Class Ten Demand": []
    })

    def add_data(unit):
        Data.all_data = Data.all_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.inflation_factor,
            "Attrition Size": unit.attrition_size,
            "Class One Demand": unit.class_one_demand,
            "Class Two Demand": unit.class_two_demand,
            "Class Three Demand": unit.class_three_demand,
            "Class Five Demand": unit.class_five_demand,
            "Class Six Demand": unit.class_six_demand,
            "Class Seven Demand": unit.class_seven_demand,
            "Class Nine Demand": unit.class_nine_demand,
            "Class Ten Demand": unit.class_ten_demand
        }, ignore_index=True)

#ITERATE THE DATA
def generator():
    for size in unit_size:
        for state in unit_state:
            unit = UnitFactors(size, state)
            UnitFactors.size(unit)
            UnitFactors.state(unit)
            UnitFactors.demand(unit)
            Data.add_data(unit)

#RUN
generator()
print(Data.all_data)