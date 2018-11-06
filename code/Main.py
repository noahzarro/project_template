import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desired_direction
from actualStep import actual_step
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from possibleDirection import possible_direction

# Define Ant
position = [0,0] #possible values: ints between 0 and 1600
globalVector = (10,10)
track = list()
track.append(position)

cycles = 100

# Main Loop

for i in range(cycles):
    desired = desired_direction(globalVector, position)
    possible = possible_direction(position)
    step = actual_step(desired, possible)
    position = position + step
    globalVector = globalVector - step
    track.append(position)

#plot

fig = plt.figure()
ax = fig.add_subplot(111)
path = mpath.Path(track)
patch = mpatches.PathPatch(path)
ax.add_patch(patch)