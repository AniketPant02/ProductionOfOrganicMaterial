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

runCount = 0 # Iterates every simulation run
MonoOxygenCount = 0 # Calculated every run
DiOxygenCount = 0 # Calculated every run
TriOxygenCount = 0 # Calculated every run
totalMoleculeAmount = 0 # Iterates every simulation run

MonoOxygenProbability = 0.3 # Changed Recursively
DiOxygenProbability = 1.0
TriOxygenProbability = 0.7

# Change values, total probability always equals one.

while ((MonoOxygenProbability + DiOxygenProbability + TriOxygenProbability) = 1):
    while (moleculeAmount != totalMoleculeAmount): # Check if moleculeAmount == totalMoleculeAmount, if so, stop simulation, as we have run out of oxygen molecules to test
        photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation
        # Starting O molecule possibilities. As of 3:06 A.M., 5/1/17, using all random number intervals for probability.
        if (photonHitRate <= MonoOxygenProbability): #Less then OR Equal too
            monoCaseRate = random.random()
            if (monoCaseRate <= 0.241):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                runCount += 1
                MonoOxygenProbability += MonoOxygenCount/totalMoleculeAmount
            elif (0.242 < monoCaseRate < 0.841):
                print("Created O2 molecule (synthesis reaction: O + O -> O2)")
                MonoOxygenCount -= 2
                DiOxygenCount += 1
                TriOxygenCount += 0
                runCount += 1
                MonoOxygenProbability += MonoOxygenCount/totalMoleculeAmount
            elif (0.842 < monoCaseRate < 1.0):
                print("Created O3 molecule (synthesis reaction: O + O2 -> O3)")
                MonoOxygenCount -= 1
                DiOxygenCount -= 1
                TriOxygenCount += 1
                runCount += 1
                MonoOxygenProbability += MonoOxygenCount/totalMoleculeAmount
        elif (MonoOxygenProbability < photonHitRate < TriOxygenProbability): # Between intervals or equal to values
            diCaseRate = random.random()
            if (diCaseRate <= 0.241):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                runCount += 1
                DiOxygenProbability += DiOxygenCount/totalMoleculeAmount
            if (0.241 < diCaseRate <= 0.841):
                print("Photolysis Decomposition Reaction: O2 -> O + O")
                MonoOxygenCount += 2
                DiOxygenCount -= 1
                TriOxygenCount += 0
                runCount += 1
                DiOxygenProbability += DiOxygenCount/totalMoleculeAmount
            if (0.841 <= diCaseRate <= 1.0):
                print("Synthesis Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                runCount += 1
                DiOxygenProbability += DiOxygenCount/totalMoleculeAmount
        elif (TriOxygenProbability < photonHitRate < 1.0):
            triCaseRate = random.random()
            if (triCaseRate <= 0.500):
                print("Hit Nothing")
                MonoOxygenCount += 0
                DiOxygenCount += 0
                TriOxygenCount += 0
                runCount += 1
                TriOxygenProbability += TriOxygenCount/totalMoleculeAmount
            if (0.501 =< triCaseRate):
                print("Photolysis Decomposition Reaction: O3 -> O2 + O")
                MonoOxygenCount += 1
                DiOxygenCount -= 1
                TriOxygenCount -= 1
                runCount += 1
                TriOxygenProbability += TriOxygenCount/totalMoleculeAmount
    print("Simulation Complete")

MonoOxygenPercent = MonoOxygenCount/totalMoleculeAmount # runCount or totalMoleculeAmount/moleculeCount?
DiOxygenPercent = DiOxygenCount/totalMoleculeAmount
TriOxygenPercent = TriOxygenCount/totalMoleculeAmount

print("Following includes the Oxygen level counts per molecule type")
print(MonoOxygenCount)
print(DiOxygenCount)
print(TriOxygenCount)

print("Following includes the Oxygen percent levels repective to molecule type")
print(MonoOxygenPercent)
print(DiOxygenPercent)
print(TriOxygenPercent)

print(int(totalMoleculeAmount))
print(int(runCount))
