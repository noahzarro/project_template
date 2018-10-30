import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desired_direction
from actualStep import actual_step
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

# Define Ant
position = (0,0)
globalVector = (10,10)
stepLength = 1
track = list()
track.append(position)

cycles = 100

# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)


# Main Loop

for i in range(cycles):
    desired = desired_direction(globalVector, position)
    possible = possible_direction(position)
    step = actual_step(desired, possible, stepLength)
    position = position + step
    globalVector = globalVector - step
    track.append(position)

#plot

fig = plt.figure()
ax = fig.add_subplot(111)
path = mpath.Path(track)
patch = mpatches.PathPatch(path)
ax.add_patch(patch)