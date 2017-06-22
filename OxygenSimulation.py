# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:06:42 2017

@author: Aniket Pant
"""
# Code must be able to return percentage abundance of O, O2, and O3 after recieving informaiton on cell numbers and molecule amount
# Needs: Molecule Amount Checker
# Issue: totalMoleculeAmount does not count molecule amount correctly. Generally, totalMoleculeAmount > moleculeAmount
# Need to recursively generate probabilities.

import math
import numpy as np
import matplotlib.pyplot as plt
import random

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
'''

# Assigning molecule amount to variable "moleculeAmount". Amount already set. 10,000 O2 Molecules
moleculeAmount = 10000 # moleculeAmount divided by two because we begin with all DiAtomic Oxygen molecules, but we want to count monoAtomic because it is easier to keep track off.

# Assigning cell amount to variable "cellAmount"
# cellAmount = int(input("Enter cell amount to be populated: ")) # Not relevant as of now

# Assigning photon amount to variable "photonAmount"
# photonAmount = int(input("Enter photon amount: ")) # Not relevant as of now

totalMoleculeAmountGraph = []
runCountGraph = []

runCount = 0 # Iterates every simulation run
lostTriOxygenCount = 0
MonoOxygenCount = 0 # Calculated every run
DiOxygenCount = moleculeAmount # Calculated every run
TriOxygenCount = 0 # Calculated every run
totalMoleculeAmount = 0 # Iterates every simulation run
newMonoOxygenCount = 0 # Amount of molecule gained per simulation, repestively calculated recursively
newDiOxygenCount = 0
newTriOxygenCount = 0
lostMonoOxygenCount = 0 # Amount of molecule lost per simulation, respectively calculated recursively
lostDiOxygenCount = 0
lostTriOxygenCount = 0
MonoOxygenProbability = 0.0 # Changed Recursively
DiOxygenProbability = 1.0 # 1.0 because all molecules are diatomic to begin with!
TriOxygenProbability = 0.0
TotalPercent = MonoOxygenProbability + DiOxygenProbability + TriOxygenProbability
# Change values, total probability always equals one.
# Intervals are incorrect, fix interval selection method to be inclusive

totalMoleculeAmountGraph = []
runCountGraph = []

while (TotalPercent == 1.0):
    while ((MonoOxygenProbability > 0.0) and (DiOxygenProbability > 0.0) and (TriOxygenProbability > 0.0)):
        photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation
        # Starting O molecule possibilities. As of 3:06 A.M., 5/1/17, using all random number intervals for probability.
        if (photonHitRate <= 0.241): #Less then OR Equal too
            monoCaseRate = random.random()
            if (0.0 <= monoCaseRate <= 0.241):
                print("Hit Nothing [1]")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.241 < monoCaseRate <= 0.841):
                print("Created O2 molecule (synthesis reaction: O + O -> O2)")
                MonoOxygenCount -= 2
                DiOxygenCount += 1
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 0
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 2
                lostDiOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.841 < monoCaseRate <= 1.0):
                print("Created O3 molecule (synthesis reaction: O + O2 -> O3)")
                MonoOxygenCount -= 1
                DiOxygenCount -= 1
                TriOxygenCount += 1
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 1
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 1
                lostDiOxygenCount = 1
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
        elif (0.241 < photonHitRate <= 0.841): # Between intervals or equal to values
            diCaseRate = random.random()
            if (diCaseRate <= 0.241):
                print("Hit Nothing [2]")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.241 < diCaseRate <= 0.841):
                print("Photolysis Decomposition Reaction: O2 -> O + O")
                MonoOxygenCount += 2
                DiOxygenCount -= 1
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 2
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 1
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.841 < diCaseRate <= 1.0):
                print("Decomposition Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 1
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 1
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
        elif (0.841 < photonHitRate <= 1.0):
            triCaseRate = random.random()
            if (triCaseRate <= 0.500):
                print("Hit Nothing [3]")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.501 <= triCaseRate):
                print("Photolysis Decomposition Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                oxygenCount = (MonoOxygenCount) + (DiOxygenCount) + (TriOxygenCount)
                newMonoOxygenCount = 1
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount) + (newDiOxygenCount) + (newTriOxygenCount)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 1
                netLostMoleculeAmount = (lostMonoOxygenCount) + (lostDiOxygenCount) + (lostTriOxygenCount)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability = ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability = ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability = ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
print("Simulation Complete")

MonoOxygenPercent = MonoOxygenCount/totalMoleculeAmount # runCount or totalMoleculeAmount/moleculeCount?
DiOxygenPercent = DiOxygenCount/totalMoleculeAmount
TriOxygenPercent = TriOxygenCount/totalMoleculeAmount

# To Do: Make code open a new command prompt window to print results in a more readable format.

print("Following includes the Oxygen level counts per molecule type")
print(MonoOxygenCount)
print(DiOxygenCount)
print(TriOxygenCount)

print("Following includes the Oxygen percent levels respective to molecule type")
print(MonoOxygenPercent)
print(DiOxygenPercent)
print(TriOxygenPercent)
print("Following includes the totalMoleculeAmount and runCount")
print((totalMoleculeAmount))
print(runCount)
print(MonoOxygenCount + DiOxygenCount + TriOxygenCount)


plt.plot(totalMoleculeAmountGraph, runCountGraph)
plt.xlabel('Total Molecule Amount')
plt.ylabel('Simulation Run Count')
plt.title('Total Molecule Amount as Time Progresses')
plt.show
