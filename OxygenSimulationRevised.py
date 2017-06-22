"""
Created on Thu Apr 13 23:06:42 2017

@author: Aniket Pant
"""

'''
Code must be able to return percentage abundance of O, O2, and O3 after recieving informaiton on cell numbers and molecule amount
Needs: Molecule Amount Checker
Issue: totalMoleculeAmount does not count molecule amount correctly. Generally, totalMoleculeAmount > moleculeAmount
Need to recursively generate probabilities.
Issue: Division by Zero. Some cases lead to division by zero in totalMoleculeAmount.
'''

# Importing Libraries. Random for initial probability assignment, matplotlib for graphing functionality.
import random
import matplotlib.pyplot as plt
import numpy as np

'''
Needed variables and constraints + why:
moleculeAmount is used to set a starting molecule amount (initial amount found in space)
totalMoleculeAmount is used to make sure molecule affected by simulation does not go above moleculeAmount (Conservation Of Mass)
Each molecule has to be counted individually:
    MonoOxygen values:
        MonoOxygenCount counts the number of MonoAtomic Oxygen Molecules
        MonoOxygenProbability repesents the probability of a MonoAtomic Atom being Hit in the ice grain.
        monoCaseRate is the random float that assigns random probability for each MonoAtomic specific reaction
    DiOyxgen values:
        DiOxygenCount counts the number of DiAtomic Oxygen Molecules
        DiOxygenProbability represents the probability of a DiAtomic atom being hit in the ice grain.
        diCaseRate is the random float that assigns random probability for each DiAtomic specific reaction
    TriOxygen values:
        TriOxygenCount counts the number of TriAtomic Oxygen Molecules
        TriOxygenProbability represents the probability of a TriAtomic Molecule being hit in the ice grain.
        triCaseRate is the random float that assigns random probability for each TriAtomic specific reaction.
    Global values:
        totalMoleculeAmount counts the total Molecule amounts (Mono + Di + Tri counts). Strictly an (int) value and is always less or equal to the previously assigned moleculeAmount. Cannot be negative
        TotalProbability = 1.0. Should always equal 1
        runCount counts the numbers of runs to provide timeline for graph.
        photonHitRate is a random float that assigns probability for each oxygen case.
'''

runCount = 0
moleculeAmount = 10000
MonoOxygenCount = 0
DiOxygenCount = 0
TriOxygenCount = 0

# Defining of Graph variables. Append values using "arrayName.append(value)". Graph using matplotlib.
MonoOxygenCountGraph = []
DiOxygenCountGraph = []
TriOxygenCountGraph = []
runCountGraph = []

# Set only for first run of simulation. This is because all molecules are originally zero except DiAtomic.
while (runCount < 0):
    MonoOxygenCount = 0
    DiOxygenCount = moleculeAmount*2
    TriOxygenCount = 0

# Simulation speific code
while (runCount < 1000):
    photonHitRate = random.random()
    runCount += 1
    if (0.0 <= photonHitRate <= 0.241):
        monoCaseRate = random.random()
        if (monoCaseRate <= 0.241):
            print("Case 1: O1")
            MonoOxygenCount += 1
            MonoOxygenCountGraph.append(MonoOxygenCount)
            runCountGraph.append(runCount)
        elif (0.241 < monoCaseRate <= 0.841):
            print("Case 2: O1")
            MonoOxygenCount += 2
            MonoOxygenCountGraph.append(MonoOxygenCount)
            runCountGraph.append(runCount)
        elif (0.841 < monoCaseRate <= 1.0):
            print("Case 3: O1")
            MonoOxygenCount += 3
            MonoOxygenCountGraph.append(MonoOxygenCount)
            runCountGraph.append(runCount)
        print("O1 Cases")
    elif (0.241 < photonHitRate <= 0.841):
        diCaseRate = random.random()
        if (diCaseRate <= 0.241):
            print("Case 1: O2")
            DiOxygenCount += 1
            DiOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        elif (0.241 < diCaseRate <= 0.841):
            print("Case 2: :O2")
            DiOxygenCount += 2
            DiOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        elif (0.841 < diCaseRate <= 1.0):
            DiOxygenCount += 3
            DiOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        print("O2 Cases")
    elif (0.841 < photonHitRate <= 1.0):
        triCaseRate = random.random()
        if (triCaseRate <= 0.241):
            print("Case 1: O3")
            TriOxygenCount += 1
            TriOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        elif (0.241 < triCaseRate <= 0.841):
            print("Case 2: O3")
            TriOxygenCount += 2
            TriOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        elif (0.841 < triCaseRate <= 1.0):
            print("Case 3: O3")
            TriOxygenCount += 3
            TriOxygenCountGraph.append(DiOxygenCount)
            runCountGraph.append(runCount)
        print("O3 Cases")
print("Simulation Finished")

# Change recursively
DiOxygenCount = moleculeAmount*2 - ((MonoOxygenCount) + (TriOxygenCount*3))
MonoOxygenCount = moleculeAmount*2 - ((DiOxygenCount) + (TriOxygenCount*3))
TriOxygenCount = moleculeAmount*2 - ((DiOxygenCount) + MonoOxygenCount)

# Printing Values
print("Int Values")
print("MonoOxygen Count")
print(MonoOxygenCount)
print("DiOxygen Count")
print(DiOxygenCount)
print("TriOxygen Count")
print(TriOxygenCount)
print("Graph Values")
print("Array: Mono Oxygen Count Values")
print(MonoOxygenCountGraph)
print("Array: Di Oxygen Count Values")
print(DiOxygenCountGraph)
print("Array: Tri Oxygen Count Values")
print(TriOxygenCountGraph)
print("Array: Run Count Values")
print(runCountGraph)
