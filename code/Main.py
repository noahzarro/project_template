import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desired_direction
from actualStep import actual_step
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from possibleDirection import possible_direction

# Define Ant
position = (0,0) #possible values: floats between 0 and 1600
globalVector = (10,10)
stepLength = 1
track = list()
track.append(position)

cycles = 100

# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)

map = np.zeros((1600,1600))
map[0, :] = 1        # Define border
map[1599, :] = 1
map[:, 0] = 1
map[:, 1599] = 1
map[1, 1:797] = 1  # Define channel of width 3
map[1, 798] = 2    # Define channel exit
map[799:800,799:800] = 3    # Define nest of size 2x2

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