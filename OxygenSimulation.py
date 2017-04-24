# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:06:42 2017

@author: Aniket Pant
"""
# Code must be able to return percentage abundance of O, O2, and O3 after recieving informaiton on cell numbers and molecule amount
# Needs: Molecule Amount Checker

import math
import numpy as np
import matplotlib.pyplot as plt
import random

# Assigning molecule amount to variable "moleculeAmount"
moleculeAmount = int(input("Enter molecule amount here: "))

# Assigning cell amount to variable "cellAmount"
cellAmount = int(input("Enter cell amount to be populated: ")) # Not relevant as of now

# Assigning photon amount to variable "photonAmount"
photonAmount = int(input("Enter photon amount: ")) # Not relevant as of now

runCount = 0 # Iterates every simulation run
MonoOxygenCount = 0 # Calculated every run
DiOxygenCount = 0 # Calculated every run
TriOxygenCount = 0 # Calculated every run
totalMoleculeAmount = 0 # Iterates every simulation run

while (moleculeAmount != totalMoleculeAmount): # Check if moleculeAmount == totalMoleculeAmount, if so, stop simulation, as we have run out of oxygen molecules to test
    photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation
    if (photonHitRate < 0.273):
        print("Hit O")
        runCount += 1
        MonoOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (MonoOxygenCount*1)
    elif (0.273 < photonHitRate < 0.841):
        print("Hit O2")
        runCount += 1
        DiOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (DiOxygenCount*2)
    elif (0.841 < photonHitRate < 1.0):
        print("Hit O3")
        runCount += 1
        TriOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (TriOxygenCount*3)
print("Simulation Complete")

MonoOxygenPercent = MonoOxygenCount/runCount # runCount or totalMoleculeCount/moleculeCount?
DiOxygenPercent = DiOxygenCount/runCount
TriOxygenPercent = TriOxygenCount/runCount

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
