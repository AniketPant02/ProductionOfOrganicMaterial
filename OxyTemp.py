import math
import numpy as np
import matplotlib.pyplot as plt
import random

runCount = 0
runCountGraph = []
totalMoleculeAmount = 0
totalMoleculeAmountGraph = []

while (runCount < 100):
    runCount += 1
    totalMoleculeAmount += 1
    runCountGraph.append(runCount)
    totalMoleculeAmountGraph.append(totalMoleculeAmount)

print("Sim done")
print(runCountGraph)
print(totalMoleculeAmountGraph)

plt.plot(totalMoleculeAmountGraph, runCountGraph)
plt.xlabel('Total Molecule Amount')
plt.ylabel('Simulation Run Count')
plt.title('Total Molecule Amount as Time Progresses')
plt.show
