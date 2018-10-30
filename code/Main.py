import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desiredDirection
from possibleDirection import possible_direction

# Define Ant
position = np.array([0,0])      #possible values: floats between 0 and 1600
globalVector = np.array([10,10])
stepLength = 1
track = position

cycles = 100

# Define Map
map = np.zeros((1600,1600))
map[0,:] = 1        #Define border
map[1599,:] = 1
map[:,0] = 1
map[:,1599] = 1
map[1:4,1:797] = 1  #Define channel of width 3
map[1:4,798] = 2    #Define channelexit
map[799:800,799:800] = 3    #Define nest of size 2x2

# Main Loop

for i in range(cycles):
    desired = desiredDirection(globalVector, position)
    possible = possible_direction(position)
    step = actualStep(desired,possible,stepLength)
    position = position + step
    track = np.append(track,position)

#plot