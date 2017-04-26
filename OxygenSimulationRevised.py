import math
import random

# Code must be able to return percentage abundance of O, O2, and O3 after recieving informaiton on cell numbers and molecule amount
# Needs: Molecule Amount Checker
# Issue: totalMoleculeAmount does not count molecule amount correctly. Generally, totalMoleculeAmount > moleculeAmount
# runCount = photonAmount?
# Need to subtract old values and add new values based on simulation results

# Assigning molecule amount to variable "moleculeAmount"
 moleculeAmount = int(input("Molecule Amount: "))

# Assinging cell amount to variable amount to variable "cellAmount"
cellAmount = int(input("Cell Amount:"))

# Assigning photon amount to variable "photonAmount"
photonAmount = int(input("Photon Amount:"))

# Assigning intitial pre-simulation variable values for Mono/Di/TriAtomic Molecule #
MonoOxygenCount = 0
DiOxygenCount = 0
TriOxygenCount = 0

# runCount counts all runs of while loop (simulation)
runCount = 0

# totalMoleculeAmount counts total molecules found in system.
# Calculated by multiplying "subscripts" based on simulation test case.
totalMoleculeAmount = 0

# While loop runs until moleculeAmount = totalMoleculeAmount, becasue as we reach that point, we have run out of molecule values to assign.
while (moleculeAmount != totalMoleculeAmount): # Line checks for equivalance
    photonHitRate = random.random() # photonHitRate = assigning probability. Random from range photonHitRate = (0.0, 1.0]
    if (photonHitRate < 0.273): # Starting MonoAtomic initial probability test case
        print ("Hit O (MonoAtomic Oxygen)")
        runCount += 1 # Add one to runCount to account for new simulation test-case run
        MonoOxygenCount += 1 # Adding +1 because we have a new amount of Mono Atomic Oxygen
        totalMoleculeAmount += 1 # Adding only (1) because MonoAtomic adds one molecule per runCount
        # Subtract values here to compensate for loss of initial DiAtomic states?
    elif (0.273 < photonHitRate < 0.841):
        print ("Hit O2 (DiAtomic Oxygen)")
        runCount += 1 # Add one to runCount to account for new simulation test-case run
        DiOxygenCount +=  #Plus two or plus one??
        totalMoleculeAmount += 2 # Adding two new molcules to account for new DiAtomic Molecules (??)
        # Subtract values here to compensate for loss of other states.
    elif (0.841 < photonHitRate < 1.0):
        print("Hit O3")
        runCount += 1 # Add one to runCount to account for
        TriOxygenCount += 3 # Add three for TriAtomic
        totalMoleculeAmount += 3 # Adding three new molecules to account for new TriAtomic Molecule addition (??)
        # Subtract values here to compensate for variable shift
    else:
        print("Error") # Last Case Scenario
print("Simulation Complete") # First Line outside of loop, non-recursive

# Defining variable percent based on Mono/Di/TriAtomic states
MonoOxygenPercent = MonoOxygenCount/totalMoleculeAmount
DiOxygenCount = DiOxygenCount/totalMoleculeAmount
TriOxygenCount = TriOxygenCount/totalMoleculeAmount

# Print values found in simulation
print("Following includes the Oxygen level counts per molecule type")
print(MonoOxygenCount)
print(DiOxygenCount)
print(TriOxygenCount)

# Print observed percentages
print("Following includes the Oxygen percent levels repective to molecule type")
print(MonoOxygenPercent)
print(DiOxygenPercent)
print(TriOxygenPercent)

# Print total counts post-sim
print(int(totalMoleculeAmount))
print(int(runCount))
