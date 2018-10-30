import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desiredDirection

# Define Ant
position = np.array([0,0])
globalVector = np.array([10,10])
stepLength = 1
track = position

cycles = 100

# Define Map


# Main Loop

for i in range(cycles):
    desired = desiredDirection(globalVector, position)
    possible = possibleDirection(position)
    step = actualStep(desired,possible,stepLength)
    position = position + step
    track = np.append(track,position)

#plot