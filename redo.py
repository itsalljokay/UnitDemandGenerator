#Demand Details Found in MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
#4030 Logistics Planning Factors Marine Expeditionary Force Supply Requirements
#IV-57

#ALL DEMAND IS DAILY

#IMPORTS
import math
import random
import numpy
import pandas

#VARIABLES
unit_size = ["Platoon", "Company", "MLR"]
unit_state = ["Competition", "Crisis", "Conflict"]
mef_size = 5300
 
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
            #Inflation Factors
            self.inflation_factor = 1.5
            #Attrition Factors
            attrition_factor = random.uniform(0.01, 0.1)
            attrition_size_raw = (size * attrition_factor)
            self.attrition_size = math.ceil(attrition_size_raw)

        if self.state == "Conflict":
            #Inflation Factors
            self.inflation_factor = 2
            #Attrition Factors
            attrition_factor = random.uniform(0.1, 0.4)
            attrition_size_raw = (size * attrition_factor)
            self.attrition_size = math.ceil(attrition_size_raw)

        print("Unit State: ", self.state)
        print("Inflation Factor: ", self.inflation_factor)
        print("Attrition Size: ", self.attrition_size)

    #CLASS ONE: FOOD
    def demand(self):
        #CLASS ONE: FOOD
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        196 stons daily for MEF sized element.
        """
        class_one_data = 196
        class_one_individual_mean = class_one_data / mef_size
        class_one_mean = (class_one_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_one_stdev = 1
        self.class_one_demand_raw = numpy.random.normal(class_one_mean, class_one_stdev)
        self.class_one_demand = round(self.class_one_demand_raw, 2)

        #CLASS TWO: EQUIPMENT
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        83 stons daily for MEF sized element.
        """
        class_two_data = 83
        class_two_individual_mean = class_two_data / mef_size
        
        #CLASS THREE: FUEL
        """
        """
        

        #CLASS FIVE: AMMO
        #CLASS SIX: PERSONAL ITEMS
        #CLASS SEVEN: MAJOR END ITEMS
        #CLASS NINE: REPAIR PARTS
        #CLASS TEN: NON-MILITARY ITEMS


#DATA STORAGE
class Data:
    #Contains all of the base data. The demand here is amount needed for one day.
    all_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Attrition Size": [],
        "Class One Demand (tn)": [],
        "Class Three Demand (gal)": []
    })

    class_one_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Attrition Size": [],
        "Short Tones": []
    })

    class_three_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Gallons": []
    })

    def add_data(unit):
        Data.all_data = Data.all_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.inflation_factor,
            "Attrition Size": unit.attrition_size,
            "Class One Demand (tn)": unit.class_one_demand,
            "Class Three Demand (gal)": unit.class_three_demand
        }, ignore_index=True)

        Data.class_one_data = Data.class_one_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.inflation_factor,
            "Attrition Size": unit.attrition_size,
            "Short Tones": unit.class_one_demand
        }, ignore_index=True)

        Data.class_three_data = Data.class_three_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.inflation_factor,
            "Gallons": unit.class_three_demand,
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
print("ALL DATA")
print(Data.all_data)
print("CLASS ONE")
print(Data.class_one_data)
print("CLASS THREE")
print(Data.class_three_data)