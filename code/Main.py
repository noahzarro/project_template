import math
import numpy as np
from DesiredDirection import desired_direction
from actualStep import actual_step
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from possibleDirection import possible_direction
import config as con
from matplotlib.colors import ListedColormap


# Define Ant
position = [1, 1] # possible values: ints between 0 and 1599
globalVector = np.array([800, 800])
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

    # error in globalVector memory
    max_error = math.pi / 1000
    random_error = np.random.normal(0, max_error)
    rotation_global = [[math.cos(random_error), -math.sin(random_error)],[math.sin(random_error), math.cos(random_error)]]
    globalVector = np.matmul(rotation_global, globalVector)

    track.append(position)

# Plot

fig = plt.figure()
ax = fig.add_subplot(111)
path = mpath.Path(track)
patch = mpatches.PathPatch(path, facecolor='none')
ax.add_patch(patch)

ax.set_xlim([0,1600])
ax.set_ylim([0,1600])

cmap = ListedColormap(['w', 'b', 'r', 'y', 'k'])
ax.matshow(np.transpose(con.map), cmap = cmap)



print("git")
git = plt.figure()


ay = git.add_subplot(121)
az = git.add_subplot(122)
ay.matshow(con.local_vector[:,:,0])
az.matshow(con.local_vector[:,:,1])
plt.ioff()
plt.show()

print("fertig")