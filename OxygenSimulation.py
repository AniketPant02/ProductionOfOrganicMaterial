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
cellAmount = int(input("Enter cell amount to be populated: "))

# Assigning photon amount to variable "photonAmount"
photonAmount = int(input("Enter photon amount: "))

runCount = 1
MonoOxygenCount = 0
DiOxygenCount = 0
TriOxygenCount = 0

while (runCount < 1000):
    photonHitRate = random.random() # photonHitRate decides which test-case is to be selected for simulation evaluation

    if (photonHitRate < 0.273):
        print("Hit O")
        runCount += 1
        MonoOxygenCount += 1
    elif (0.273 < photonHitRate < 0.841):
        print("Hit O2")
        runCount += 1
        DiOxygenCount += 1
    elif (0.841 < photonHitRate < 1.0):
        print("Hit O3")
        runCount += 1
        TriOxygenCount += 1

MonoOxygenPercent = MonoOxygenCount/runCount
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
