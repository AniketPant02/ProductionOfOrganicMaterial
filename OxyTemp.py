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

while (1==1):
    print("Photolysis Decomposition Reaction: O2 -> O + O")
    MonoOxygenCount += 2
    DiOxygenCount -= 1
    TriOxygenCount += 0
    oxygenCount = (MonoOxygenCount*1) + (DiOxygenCount*2) + (TriOxygenCount*3)
    newMonoOxygenCount = 2
    newDiOxygenCount = 0
    newTriOxygenCount = 0
    netGainedMoleculeAmount = newMonoOxygenCount + newDiOxygenCount + newTriOxygenCount
    lostMonoOxygenCount = 0
    lostDiOxygenCount = 1
    lostTriOxygenCount = 0
    netLostMoleculeAmount = lostMonoOxygenCount + lostDiOxygenCount + lostTriOxygenCount
    runCount += 1
    if (oxygenCount == 0):
       pass
    else:
       totalMoleculeAmount = oxygenCount + netGainedMoleculeAmount - netLostMoleculeAmount
    DiOxygenProbability = newDiOxygenCount/totalMoleculeAmount
    print(totalMoleculeAmount)
