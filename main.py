"""
UNIT DEMAND GENERATOR FOR COMPETITION, CRISIS, AND CONFLICT CONTIUUM 
By: 2ndLt Jessi Lanum

PROBLEM: Realistic demand generation is neccessary for increasing realism for logistics-based wargames. 
PURPOSE: Provide realistic demand generation for each class of supply depending on unit size and state.
OBJECTIVE: Provide quantitative demand data output for logistics-based wargames.

LAST UPDATED: xx JUL 23

#NOTE
This one will be all classes of supply outputted for each state of existance.

INTERNAL PROBLEM: I dislike having so many variables defined, but I can't think of a slicker option...
SOLUTION: Attempting for the first time some tuple unpacking. 

FUTURE USEAGE THOUGHTS: If adding to a larger program, probably refactor to seperate program into multiple
files. This way all variables can be in their own variables.py file. Potentially refactor this in the end to
do this. Add one option for all classes per state, and then one class with all states.
"""
#IMPORTS
import random
import numpy
import pandas

#VARIABLES
units = [platoon, company, mlr]
states = [competition, crisis, conflict]

#Base Unit Sizes
platoon_size = 50
company_size = 400
mlr_size = 2000

#Attrition Rate For Crisis and Conflict
#Crisis attrition rate is randomly selected anywhere from 0.01% and 0.1%.
#Conflict attrition rate is randomly selected anywhere from 1% to 3%.
crisis_attrition_factor = random.uniform(0.01, 0.1)
conflict_attrition_factor = random.uniform(1, 3)

platoon_crisis_attrition = platoon_size - (platoon_size * crisis_attrition_factor)
company_crisis_attrition = company_size - (company_size * crisis_attrition_factor)
mlr_crisis_attrition = mlr_size - (company_size * crisis_attrition_factor)

platoon_conflict_attrition = platoon_size - (platoon_size * conflict_attrition_factor)
company_conflict_attrition = company_size - (company_size * conflict_attrition_factor)
mlr_conflict_attrition = mlr_size - (mlr_size * conflict_attrition_factor)

"""
Class 1: Food
"""
class ClassOneVariables:
    #Usual Request Based on MAGTF Planning
    #3 MREs per Marine per Day
    individual_mean = 3
    for unit 
    platoon_mean = platoon_size * individual_mean
    company_mean = company_size * individual_mean
    mlr_mean = mlr_size * individual_mean
    
    #Demand Inflation Factor Depending on Continuum State
    competition_inflation_factor = 1
    crisis_inflation_factor = 1.5
    conflict_inflation_factor = 2

    #Competition Mean Calculations
    competition_demand_mean_platoon = competition_inflation_factor * platoon_mean
    competition_demand_mean_company = competition_inflation_factor * company_mean
    competition_demand_mean_mlr = competition_inflation_factor * mlr_mean

    #Crisis Mean Calculations
    crisis_demand_mean_platoon = crisis_inflation_factor * platoon_mean
    crisis_demand_mean_company = crisis_inflation_factor * company_mean
    crisis_demand_mean_mlr = crisis_inflation_factor * mlr_mean

    #Conflict Mean Calculations
    conflict_demand_mean_platoon = conflict_inflation_factor * platoon_mean
    conflict_demand_mean_company = conflict_inflation_factor * company_mean
    conflict_demand_mean_mlr = conflict_inflation_factor * mlr_mean
    
    #Standard Deviations
    competition_demand_stdev, crisis_demand_stdev, conflict_demand_stdev = 1, 1, 1

"""
Class 2: Equipment
"""
"""
Class 3: Fuel
"""
"""
Class 5: Ammo
"""
"""
Class 6: Personal Items 
"""
"""
Class 7: Major End Items
"""
"""
Class 9: Repair Parts
"""
"""
Class 10: Non-Military Items
"""

#DATAFRAMES
class Track:
    competition_platoon_dataframe = pandas.DataFrame({
        "Class One": [],
        "Class Two": [],
        "Class Three": [],
        "Class Five": [],
        "Class Six": [],
        "Class Seven": [],
        "Class Nine": [],
        "Class Ten": []

    })


#DEMAND GENERATION
"""
Break each into functions.
"""
#Competition
def competition_demand_generator():
    print("COMPETITION")
    #Platoon
    competition_class_one_demand_platoon = numpy.random.normal(ClassOneVariables.competition_demand_mean_platoon, ClassOneVariables.competition_demand_stdev)
    print("Platoon, Class One:", round(competition_class_one_demand_platoon))
    
    #Company
    competition_class_one_demand_company = numpy.random.normal(ClassOneVariables.competition_demand_mean_company, ClassOneVariables.competition_demand_stdev)
    print("Company, Class One:", round(competition_class_one_demand_company))
    
    #MLR
    competition_class_one_demand_mlr = numpy.random.normal(ClassOneVariables.competition_demand_mean_mlr, ClassOneVariables.competition_demand_stdev)
    print("MLR, Class One:", round(competition_class_one_demand_mlr))

    #Class Two

#Crisis
def crisis_demand_generator():
    print("CRISIS")
    #Platoon
    crisis_class_one_demand_platoon = numpy.random.normal(ClassOneVariables.crisis_demand_mean_platoon, ClassOneVariables.crisis_demand_stdev) - platoon_crisis_attrition
    print("Platoon, Class One:", round(crisis_class_one_demand_platoon))
    
    #Company
    crisis_class_one_demand_company = numpy.random.normal(ClassOneVariables.crisis_demand_mean_company, ClassOneVariables.crisis_demand_stdev) - company_crisis_attrition
    print("Company, Class One:", round(crisis_class_one_demand_company))
    
    #MLR
    crisis_class_one_demand_mlr = numpy.random.normal(ClassOneVariables.crisis_demand_mean_mlr, ClassOneVariables.crisis_demand_stdev) - mlr_crisis_attrition
    print("MLR, Class One:", round(crisis_class_one_demand_mlr))

#conflict

print(competition_demand_generator())
print(crisis_demand_generator())