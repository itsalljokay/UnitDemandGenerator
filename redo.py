#THIS IS DEMAND PER DAY
#GENERAL INFLATION FACTOR IS IF SPECIFIC STATE DATA IS NOT PRESENT

#IMPORTS
import math
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
            #Inflation Factors
            self.inflation_factor = 1.5
            #Attrition Factors
            attrition_factor = random.uniform(0.01, 0.1)
            self.attrition_size = (size - size * attrition_factor)

        if self.state == "Conflict":
            #Inflation Factors
            self.general_inflation_factor = 2
            #Attrition Factors
            attrition_factor = random.uniform(1, 3)
            self.attrition_size = (size - size * attrition_factor)

        print("Unit State: ", self.state)
        print("Inflation Factor: ", self.inflation_factor)
        print("Attrition Size: ", self.attrition_size)

    #CLASS ONE: FOOD
    def demand(self):
        #CLASS ONE: FOOD
        """
        3 MREs per Marine per Day
        12 MREs in a Case
        Each Case is 16lbs
        Lbs divided by 2000 is Short Tons
        Keep in mind, we want full MREs. If given a decimal number of MREs, automatically round up with ceil.
        """
        class_one_individual_mean = 3
        class_one_mean = (class_one_individual_mean * self.size) * self.inflation_factor
        class_one_stdev = 1
        self.class_one_demand_raw = numpy.random.normal(class_one_mean, class_one_stdev) - self.attrition_size
        self.class_one_demand_mres = math.ceil(self.class_one_demand_raw)
        self.class_one_demand_cases = math.ceil(self.class_one_demand_mres / 12)
        self.class_one_demand_pounds = round((self.class_one_demand_cases * 16), 2)
        self.class_one_demand = round((self.class_one_demand_pounds / 2000), 2)

        #CLASS TWO: EQUIPMENT
        #CLASS THREE: FUEL
        """
        The MEU uses 48,145 gallons daily in a sustained situation.
        """
        class_three_individual_mean = 48145
        class_three_mean = class_three_individual_mean * self.inflation_factor
        class_three_stdev = 1
        self.class_three_raw = numpy.random.normal(class_three_mean, class_three_stdev)
        self.class_three_demand = round(self.class_three_raw, 2)
        print(class_three_individual_mean)
        print(class_three_mean)
        print(self.class_three_demand)

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
        "Math MREs": [],
        "Actual MREs": [],
        "Cases": [],
        "Pounds": [],
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
            "Math MREs": unit.class_one_demand_raw,
            "Actual MREs": unit.class_one_demand_mres,
            "Cases": unit.class_one_demand_cases,
            "Pounds": unit.class_one_demand_pounds,
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