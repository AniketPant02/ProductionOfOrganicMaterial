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

MonoOxygenProbability = 0.0 # Changed Recursively
DiOxygenProbability = 1.0
TriOxygenProbability = 0.0

# Change values, total probability always equals one.

while (moleculeAmount != totalMoleculeAmount): # Check if moleculeAmount == totalMoleculeAmount, if so, stop simulation, as we have run out of oxygen molecules to test
    photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation
    if (photonHitRate < MonoOxygenProbability): #Less then OR Equal too
        print("Hit O")
        runCount += 1
        MonoOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (1) # Adding one because one Oxygen molecule
    elif (MonoOxygenProbability < photonHitRate < TriOxygenProbability): # Between intervals or equal to values
        print("Hit O2") # May do nothing
        # if # Hits something else
        runCount += 1
        DiOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (2) # Adding one because two Oxygen molecules / Do NOT caluculate as of now. Run other test cases for O2 photo first!
    elif (0.841 < photonHitRate < 1.0):
        print("Hit O3")
        runCount += 1
        TriOxygenCount += 1
        totalMoleculeAmount = totalMoleculeAmount + (3) # Adding one because three Oxygen molecules
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
