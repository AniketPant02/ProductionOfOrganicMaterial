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

# Assigning molecule amount to variable "moleculeAmount"
moleculeAmount = 10000 # moleculeAmount divided by two because we begin with all DiAtomic Oxygen molecules, but we want to count monoAtomic because it is easier to keep track off.

# Add cellAmount and photonAmount rates later

# Introduce Graph variables here
totalMoleculeAmountGraph = []
runCountGraph = []

# Introduce Oxygen Variables here (Compound specific vriables)
runCount = 0

# Base Oxygen count
MonoOxygenCount = 0
DiOxygenCount = moleculeAmount*2
TriOxygenCount = 0
totalMoleculeAmount = 0
StartDiOxygenCount = moleculeAmount*2

# Counting new additions
newMonoOxygenCount = 0
newDiOxygenCount = 0
newTriOxygenCount = 0

# Counting lost molecules
lostMonoOxygenCount = 0
lostDiOxygenCount = 0
lostTriOxygenCount = 0

# Counting probabilities, to be calculated iteratively. Should always be equal to 1.0
MonoOxygenProbability = 0.0
DiOxygenProbability = 1.0
TriOxygenProbability = 0.0
TotalProbability = MonoOxygenProbability + DiOxygenProbability + TriOxygenProbability

while (MonoOxygenProbability + DiOxygenProbability + TriOxygenProbability == 1.0): # Checking for 1.0 sum of probability
    while (totalMoleculeAmount <= StartDiOxygenCount): # Checks to make sure we have not broken Conservation of Mass law (broke Physics :P)
        photonHitRate = random.random() # Chooses with one of three cases to be considered. (0.0, 1.0]
        if (photonHitRate <= 0.241):  # Nothing, O2 Synthesis, O3 Synthesis (with O2)
            monoCaseRate = random.random()
            if (monoCaseRate <= 0.241): # Hit Nothing
                print("Hit Nothing")
                newMonoOxygenCount = 0
                newDiOxygenCount = 0
                newTriOxygenCount = 0
                netGainedMoleculeAmount = (newMonoOxygenCount*1) + (newDiOxygenCount*2) + (newTriOxygenCount*3)
                lostMonoOxygenCount = 0
                lostDiOxygenCount = 0
                lostTriOxygenCount = 0
                netLostMoleculeAmount = (lostMonoOxygenCount*1) + (lostDiOxygenCount*2) + (lostTriOxygenCount*3)
                MonoOxygenCount = (MonoOxygenCount*1) + (newMonoOxygenCount*1) - (lostMonoOxygenCount*1)
                DiOxygenCount = (DiOxygenCount*2) + (newDiOxygenCount*2) - (lostDiOxygenCount*2)
                TriOxygenCount = (TriOxygenCount*3) + (newTriOxygenCount*3) - (lostTriOxygenCount*3)
                totalMoleculeAmount = MonoOxygenCount + DiOxygenCount + TriOxygenCount
                MonoOxygenProbability += ((MonoOxygenCount*1) + (newMonoOxygenCount*1) - (lostMonoOxygenCount*1))/totalMoleculeAmount
                DiOxygenProbability += ((DiOxygenCount*2) + (newDiOxygenCount*2) - (lostDiOxygenCount*2))/totalMoleculeAmount
                TriOxygenProbability += ((TriOxygenCount*3) + (newTriOxygenCount*3) - (lostTriOxygenCount*3))/totalMoleculeAmount
            else:
                print("Test Subject 1")
        else:
            print("Test Subject 2")
print("Broke Physics")
print(totalMoleculeAmount)
