import matplotlib.pyplot as plt
import numpy as np
from DesiredDirection import desired_direction
from actualStep import actual_step
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from possibleDirection import possible_direction

# Define Ant
position = [1600-2,1600-2] #possible values: ints between 0 and 1600
globalVector = np.array([-800,-800])
track = list()
track.append(position)

cycles = 10000

# Main Loop

for i in range(cycles):
    desired = desired_direction(globalVector, position)
    possible = possible_direction(position)
    step = actual_step(desired, possible)
    position = [position[0] + step[0], position[1] + step[1]]
    globalVector = globalVector - step
    track.append(position)

#plot



fig = plt.figure()
ax = fig.add_subplot(111)
path = mpath.Path(track)
patch = mpatches.PathPatch(path)
ax.add_patch(patch)

ax.set_xlim([0,1600])
ax.set_ylim([0,1600])

fig.show()

print("fertig")