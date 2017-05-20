# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:06:42 2017

@author: Aniket Pant
"""
# Code must be able to return percentage abundance of O, O2, and O3 after recieving informaiton on cell numbers and molecule amount
# Needs: Molecule Amount Checker
# Issue: totalMoleculeAmount does not count molecule amount correctly. Generally, totalMoleculeAmount > moleculeAmount

import math
import numpy as np
import matplotlib.pyplot as plt
import random

# Assigning molecule amount to variable "moleculeAmount"
moleculeAmount = int(input("Enter diatomic oxygen molecule amount here: ")) # moleculeAmount divided by two because we begin with all DiAtomic Oxygen molecules, but we want to count monoAtomic because it is easier to keep track off.

# Assigning cell amount to variable "cellAmount"
cellAmount = int(input("Enter cell amount to be populated: ")) # Not relevant as of now

# Assigning photon amount to variable "photonAmount"
photonAmount = int(input("Enter photon amount: ")) # Not relevant as of now

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
# Change values, total probability always equals one.
# Intervals are incorrect, fix interval selection method to be inclusive

totalMoleculeAmountGraph = []
runCountGraph = []

while (MonoOxygenProbability + DiOxygenProbability + TriOxygenProbability == 1.0):
    while (totalMoleculeAmount != moleculeAmount*2): # Check if moleculeAmount == totalMoleculeAmount, if so, stop simulation, as we have run out of oxygen molecules to test
        photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation
        # Starting O molecule possibilities. As of 3:06 A.M., 5/1/17, using all random number intervals for probability.
        if (photonHitRate <= 0.241): #Less then OR Equal too
            monoCaseRate = random.random()
            if (0.0 <= monoCaseRate <= 0.241):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                netLostMoleculeAmount = 0
                netGainedMoleculeAmount = 0
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.241 < monoCaseRate <= 0.841):
                print("Created O2 molecule (synthesis reaction: O + O -> O2)")
                MonoOxygenCount -= 2
                DiOxygenCount += 1
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 0
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 2
                lostDiOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.841 < monoCaseRate <= 1.0):
                print("Created O3 molecule (synthesis reaction: O + O2 -> O3)")
                MonoOxygenCount -= 1
                DiOxygenCount -= 1
                TriOxygenCount += 1
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 1
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 1
                lostDiOxygenCount = 1
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
        elif (0.241 < photonHitRate <= 0.841): # Between intervals or equal to values
            diCaseRate = random.random()
            if (diCaseRate <= 0.241):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.241 < diCaseRate <= 0.841):
                print("Photolysis Decomposition Reaction: O2 -> O + O")
                MonoOxygenCount += 2
                DiOxygenCount -= 1
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 2
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 1
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.841 < diCaseRate <= 1.0):
                print("Synthesis Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 1
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 1
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
        elif (0.841 < photonHitRate <= 1.0):
            triCaseRate = random.random()
            if (triCaseRate <= 0.500):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
            elif (0.501 <= triCaseRate):
                print("Photolysis Decomposition Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
                newMonoOxygenCount = 1
                newDiOxygenCount = 1
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 1
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                runCount += 1
                if (oxygenCount == 0):
                    pass
                else:
                    totalMoleculeAmount += (oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount)
                MonoOxygenProbability += ((MonoOxygenCount + newMonoOxygenCount - lostMonoOxygenCount)/totalMoleculeAmount)
                DiOxygenProbability += ((DiOxygenCount + newDiOxygenCount - lostDiOxygenCount)/totalMoleculeAmount)
                TriOxygenProbability += ((TriOxygenCount + newTriOxygenCount - lostTriOxygenCount)/totalMoleculeAmount)
                print(totalMoleculeAmount)
                totalMoleculeAmountGraph.append(totalMoleculeAmount)
                runCountGraph.append(runCount)
    print("Simulation Complete")

MonoOxygenPercent = MonoOxygenCount/totalMoleculeAmount # runCount or totalMoleculeAmount/moleculeCount?
DiOxygenPercent = DiOxygenCount/totalMoleculeAmount
TriOxygenPercent = TriOxygenCount/totalMoleculeAmount

print("Following includes the Oxygen level counts per molecule type")
print(MonoOxygenCount)
print(DiOxygenCount)
print(TriOxygenCount)

print("Following includes the Oxygen percent levels respective to molecule type")
print(MonoOxygenPercent)
print(DiOxygenPercent)
print(TriOxygenPercent)
print("Following includes the totalMoleculeAmount and runCount")
print(totalMoleculeAmount)
print(runCount)
print(MonoOxygenCount + DiOxygenCount + TriOxygenCount)


plt.plot(totalMoleculeAmountGraph, runCountGraph)
plt.xlabel('Total Molecule Amount')
plt.ylabel('Simulation Run Count')
plt.title('Total Molecule Amount as Time Progresses')
plt.show
