#THIS IS DEMAND PER DAY
#GENERAL INFLATION FACTOR IS IF SPECIFIC STATE DATA IS NOT PRESENT

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
        self.general_inflation_factor = 1
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
            self.general_inflation_factor = 1.5
            attrition_factor = random.uniform(0.01, 0.1)
            self.attrition_size = (size - size * attrition_factor)

        if self.state == "Conflict":
            self.general_inflation_fact = 2
            attrition_factor = random.uniform(1, 3)
            self.attrition_size = (size - size * attrition_factor)

        print("Unit State: ", self.state)
        print("Inflation Factor: ", self.general_inflation_fact)
        print("Attrition Size: ", self.attrition_size)

    #CLASS ONE: FOOD
    def demand(self):
        #CLASS ONE: FOOD
        """
        3 MREs per Marine per Day
        12 MREs in a Case
        Each Case is 16lbs
        Lbs divided by 2000 is Short Tons
        """
        class_one_individual_mean = 3
        class_one_mean = (class_one_individual_mean * self.size) * self.general_inflation_fact
        class_one_stdev = 1
        self.class_one_demand_mres = numpy.random.normal(class_one_mean, class_one_stdev) - self.attrition_size
        self.class_one_demand_cases = round(self.class_one_demand_mres / 12)
        self.class_one_demand_pounds = round((self.class_one_demand_cases * 16), 2)
        self.class_one_demand = round((self.class_one_demand_pounds / 2000), 2)

        #CLASS TWO: EQUIPMENT
        #CLASS THREE: FUEL
        """
        The MEU uses 48,145 gallons daily in a sustained situation.
        63,842 in an assault situation.
        Project this into what we estimate the MLR would utilize...
        Competition: Same sustained, 48,145
        Crisis: Middle ground, 55,992
        Conflict: Same assault, 63,842
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
        "Class One Demand (tn)": []
    })

    class_one_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Attrition Size": [],
        "MREs": [],
        "Cases": [],
        "Pounds": [],
        "Short Tones": []

    })

    def add_data(unit):
        Data.all_data = Data.all_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.general_inflation_factor,
            "Attrition Size": unit.attrition_size,
            "Class One Demand (tn)": unit.class_one_demand
        }, ignore_index=True)

        Data.class_one_data = Data.class_one_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.general_inflation_factor,
            "Attrition Size": unit.attrition_size,
            "MREs": unit.class_one_demand_mres,
            "Cases": unit.class_one_demand_cases,
            "Pounds": unit.class_one_demand_pounds,
            "Short Tones": unit.class_one_demand
        })

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