#Demand Details Found in MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
#4030 Logistics Planning Factors Marine Expeditionary Force Supply Requirements
#IV-57

#ALL DEMAND IS DAILY
#Using a folded normal distribution as we are sampling from what is basically the absolute value of a normal distribution.
#This is equivalent to taking the absoulte value of a normal distribution, which is what we do in the code.

#IMPORTS
import os
import math
import random
import numpy
import pandas

#FILE STRUCTURE
#Get Current Working Directory
current_location = os.getcwd()
#All The Folders/Directories We Want To Put Outputs
directories = [
    "outputs",
    "outputs/class",
    "outputs/unit",
    "outputs/state"
]
#If That Folder/Directory Doesn't Already Exist, Make It
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

#VARIABLES
unit_size = ["Platoon", "Company", "MLR", "MEF"]
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
        if self.type == "MEF":
            self.size = mef_size
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
        class_one_demand_raw = abs(numpy.random.normal(class_one_mean, class_one_stdev))
        self.class_one_demand = round(class_one_demand_raw, 2)

        #WATER
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        260300 gallons daily for MEF sized element.
        """
        water_data = 196
        water_individual_mean = water_data / mef_size
        water_mean = (water_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        water_stdev = 1
        water_demand_raw = abs(numpy.random.normal(water_mean, water_stdev))
        self.water_demand = round(water_demand_raw, 2)
        
        #CLASS TWO: EQUIPMENT
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        83 stons daily for MEF sized element.
        """
        class_two_data = 83
        class_two_individual_mean = class_two_data / mef_size
        class_two_mean = (class_two_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_two_stdev = 1
        class_two_demand_raw = abs(numpy.random.normal(class_two_mean, class_two_stdev))
        self.class_two_demand = round(class_two_demand_raw, 2)
        
        #CLASS THREE: FUEL
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        950,010 gallons daily for MEF sized element.
        """
        class_three_data = 950010
        class_three_individual_mean = class_three_data / mef_size
        class_three_mean = (class_three_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_three_stdev = 1
        class_three_demand_raw = abs(numpy.random.normal(class_three_mean, class_three_stdev))
        self.class_three_demand = round(class_three_demand_raw, 2)
        
        #CLASS FOUR: CONSTRUCTION AND BARRIER MATERIAL
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        139 stons daily for MEF sized element.
        """
        class_four_data = 139
        class_four_individual_mean = class_four_data / mef_size
        class_four_mean = (class_four_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_four_stdev = 1
        class_four_demand_raw = abs(numpy.random.normal(class_four_mean, class_four_stdev))
        self.class_four_demand = round(class_four_demand_raw, 2)
        
        #CLASS FIVE: AMMO
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        1600 stons daily for MEF sized element.
        """
        class_five_data = 1600
        class_five_individual_mean = class_five_data / mef_size
        class_five_mean = (class_five_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_five_stdev = 1
        class_five_demand_raw = abs(numpy.random.normal(class_five_mean, class_five_stdev))
        self.class_five_demand = round(class_five_demand_raw, 2)

        #CLASS SIX: PERSONAL ITEMS
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        1600 stons daily for MEF sized element.
        """
        class_six_data = 26
        class_six_individual_mean = class_six_data / mef_size
        class_six_mean = (class_six_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_six_stdev = 1
        class_six_demand_raw = abs(numpy.random.normal(class_six_mean, class_six_stdev))
        self.class_six_demand = round(class_six_demand_raw, 2)

        #CLASS NINE: REPAIR PARTS
        """
        MSTP Pamphlet 5-0.3 MAGTF Planner's Reference Manual
        41 stons daily for MEF sized element.
        """
        class_nine_data = 26
        class_nine_individual_mean = class_nine_data / mef_size
        class_nine_mean = (class_nine_individual_mean * (self.size - self.attrition_size)) * self.inflation_factor
        class_nine_stdev = 1
        class_nine_demand_raw = abs(numpy.random.normal(class_nine_mean, class_nine_stdev))
        self.class_nine_demand = round(class_nine_demand_raw, 2)


#DATA STORAGE
class Data:
    #Contains all of the base data. The demand here is amount needed for one day.
    all_data = pandas.DataFrame({
        "Unit Type": [],
        "Unit Size": [],
        "Unit State": [],
        "Inflation Factor": [],
        "Attrition Size": [],
        "Class One Demand (stons)": [],
        "Water Demand (gal)": [],
        "Class Two Demand (stons)": [],
        "Class Three Demand (gal)": [],
        "Class Four Demand (stons)": [],
        "Class Five Demand (stons)": [],
        "Class Six Demand (stons)": [],
        "Class Nine Demand (stons)": []
    })

    def add_data(unit):
        Data.all_data = Data.all_data.append({
            "Unit Type": unit.type,
            "Unit Size": unit.size,
            "Unit State": unit.state,
            "Inflation Factor": unit.inflation_factor,
            "Attrition Size": unit.attrition_size,
            "Class One Demand (stons)": unit.class_one_demand,
            "Water Demand (gal)": unit.water_demand,
            "Class Two Demand (stons)": unit.class_two_demand,
            "Class Three Demand (gal)": unit.class_three_demand,
            "Class Four Demand (stons)": unit.class_four_demand,
            "Class Five Demand (stons)": unit.class_five_demand,
            "Class Six Demand (stons)": unit.class_six_demand,
            "Class Nine Demand (stons)": unit.class_nine_demand
        }, ignore_index=True)

class Outputs:
    def by_class():
        class_one_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class One Demand (stons)",
            "Water Demand (gal)"
        ]].copy()
        print("CLASS ONE")
        print(class_one_data)
        class_one_data.to_csv("outputs/class/class_one.csv")

        class_two_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Two Demand (stons)"
        ]].copy()
        print("CLASS TWO")
        print(class_two_data)
        class_two_data.to_csv("outputs/class/class_two.csv")

        class_three_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Three Demand (gal)"
        ]].copy()
        print("CLASS THREE")
        print(class_three_data)
        class_three_data.to_csv("outputs/class/class_three.csv")

        class_four_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Four Demand (stons)"
        ]].copy()
        print("CLASS FOUR")
        print(class_four_data)
        class_four_data.to_csv("outputs/class/class_four.csv")

        class_five_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Five Demand (stons)"
        ]].copy()
        print("CLASS FIVE")
        print(class_five_data)
        class_five_data.to_csv("outputs/class/class_five.csv")

        class_six_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Six Demand (stons)"
        ]].copy()
        print("CLASS SIX")
        print(class_six_data)
        class_six_data.to_csv("outputs/class/class_six.csv")

        class_nine_data = Data.all_data[[
            "Unit Type",
            "Unit Size",
            "Unit State",
            "Inflation Factor",
            "Attrition Size",
            "Class Nine Demand (stons)"
        ]].copy()
        print("CLASS NINE")
        print(class_nine_data)
        class_nine_data.to_csv("outputs/class/class_nine.csv")

    def by_unit():
        unit_data = Data.all_data.copy()
        
        platoon_grouped = unit_data.groupby("Unit Type")
        platoon_data = platoon_grouped.get_group("Platoon")
        print("PLATOON")
        print(platoon_data)
        platoon_data.to_csv("outputs/unit/platoon.csv")

        company_grouped = unit_data.groupby("Unit Type")
        company_data = company_grouped.get_group("Company")
        print("COMPANY")
        print(company_data)
        company_data.to_csv("outputs/unit/company.csv")

        mlr_grouped = unit_data.groupby("Unit Type")
        mlr_data = mlr_grouped.get_group("MLR")
        print("MLR")
        print(mlr_data)
        mlr_data.to_csv("outputs/unit/MLR.csv")

        mef_grouped = unit_data.groupby("Unit Type")
        mef_data = mef_grouped.get_group("Platoon")
        print("MEF")
        print(mef_data)
        mef_data.to_csv("outputs/unit/MEF.csv")

    def by_state():
        state_data = Data.all_data.copy()
        
        competition_grouped = state_data.groupby("Unit State")
        competition_data = competition_grouped.get_group("Competition")
        print("COMPETITION")
        print(competition_data)
        competition_data.to_csv("outputs/state/competition.csv")

        crisis_grouped = state_data.groupby("Unit State")
        crisis_data = crisis_grouped.get_group("Crisis")
        print("CRISIS")
        print(crisis_data)
        crisis_data.to_csv("outputs/state/crisis.csv")

        conflict_grouped = state_data.groupby("Unit State")
        conflict_data = conflict_grouped.get_group("Conflict")
        print("CONFLICT")
        print(conflict_data)
        conflict_data.to_csv("outputs/state/conflict.csv")






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
Outputs.by_class()
print("ALL DATA")
print(Data.all_data)
print("BY CLASS")
print(Outputs.by_class())
print("BY UNIT")
print(Outputs.by_unit())
print("BY STATE")
print(Outputs.by_state())