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

# ADD DO NOTHING!!!
# Instead of using If-else statements, try arrays and loops to iterate through sims


runCount = 0
moleculeAmount = 10000
MonoOxygenCount = 0
DiOxygenCount = 0
TriOxygenCount = 0

# Defining of Graph variables. Append values using "arrayName = np.append(arrayName, value)". Graph using matplotlib.
MonoOxygenCountGraph = np.array([])
DiOxygenCountGraph = np.array([])
TriOxygenCountGraph = np.array([])
totalMoleculeAmountGraph = np.array([])
runCountGraph = np.array([])

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
            print("Hit Nothing [Mono Case]")
            MonoOxygenCount += 0
            DiOxygenCount += 0
            TriOxygenCount += 0
            MonoOxygenCountGraph = np.append(MonoOxygenCountGraph,MonoOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        elif (0.241 < monoCaseRate <= 0.841):
            print("Created O2 Molecule [Synthesis Reaction: O + O -> O2]")
            MonoOxygenCount += 2
            DiOxygenCount += 1
            TriOxygenCount += 1
            MonoOxygenCountGraph = np.append(MonoOxygenCountGraph,MonoOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        elif (0.841 < monoCaseRate <= 1.0):
            print("Created O3 Molecule [Synthesis Reaction: O + O2 -> O3]")
            MonoOxygenCount += 3
            DiOxygenCount += 1
            TriOxygenCount += 1
            MonoOxygenCountGraph = np.append(MonoOxygenCountGraph,MonoOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        print("MonoOxygen Cases")
    elif (0.241 < photonHitRate <= 0.841):
        diCaseRate = random.random()
        if (diCaseRate <= 0.241):
            print("Hit Nothing [Di Case]")
            DiOxygenCount += 1
            MonoOxygenCount += 1
            TriOxygenCount += 1
            DiOxygenCountGraph = np.append(DiOxygenCountGraph,DiOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        elif (0.241 < diCaseRate <= 0.841):
            print("Photolysis Decomp: O2 -> O + O")
            DiOxygenCount += 2
            MonoOxygenCount += 1
            TriOxygenCount += 1
            DiOxygenCountGraph = np.append(DiOxygenCountGraph,DiOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        elif (0.841 < diCaseRate <= 1.0):
            print("Decomp: O3 -> O2 + O [DiOxygen Case]")
            DiOxygenCount += 3
            MonoOxygenCount += 1
            TriOxygenCount += 1
            DiOxygenCountGraph = np.append(DiOxygenCountGraph,DiOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        print("DiOxygen Cases")
    elif (0.841 < photonHitRate <= 1.0):
        triCaseRate = random.random()
        if (triCaseRate <= 0.5):
            print("Hit Nothing [TriOxygen]")
            TriOxygenCount += 0
            MonoOxygenCount += 0
            DiOxygenCount += 0
            TriOxygenCountGraph = np.append(TriOxygenCountGraph,TriOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        elif (triCaseRate > 0.5):
            print("Photolysis Decomp Reaction: O3 -> O2 + O")
            TriOxygenCount += 2
            MonoOxygenCount += 1
            DiOxygenCount += 1
            TriOxygenCountGraph = np.append(TriOxygenCountGraph,TriOxygenCount)
            runCountGraph = np.append(runCountGraph,runCount)
        print("O3 Cases")
'''
        DiOxygenCount = (moleculeAmount*2 - ((MonoOxygenCount) + (TriOxygenCount*3)))/2
        MonoOxygenCount = moleculeAmount*2 - ((DiOxygenCount) + (TriOxygenCount*3))
        TriOxygenCount = moleculeAmount*2 - ((DiOxygenCount*2) + MonoOxygenCount)
'''
print("Simulation Finished")

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

'''
# Setting the domain of graph values
MonoAtomicDomainMax = int(MonoOxygenCount)
DiAtomicDomainMax = int(DiOxygenCount)
TriAtomicDomainMax = int(TriOxygenCount)
'''
'''
MonoAtomicDomainIntervals = np.linspace(0.0, )
DiAtomicDomainIntervals = np.linspace()
TriAtomicDomainIntervals = np.linspace()
'''
'''
# Plotting Values/ matplotlib
plt.hold(True)
plt.plot(MonoOxygenCount, MonoOxygenCountGraph, 'b--')
plt.plot(DiOxygenCount, DiOxygenCountGraph, 'g-.')
plt.plot(TriOxygenCount, TriOxygenCountGraph, 'r')
plt.title("Flucuations of Oxygen based on Atomic Values")
plt.ylabel("Oxygen Level")
plt.xlabel("Total Amount of Oxygen")
plt.show()
'''
