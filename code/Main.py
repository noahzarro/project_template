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

ant_number = con.ant_number
tracks = list()     # save track of each ant

fig = plt.figure()
ax = fig.add_subplot(111)

cmap = ListedColormap(['w', 'b', 'y', 'r', 'k'])
ax.matshow(np.transpose(con.map), cmap=cmap)

ax.set_xlim([0, con.map_size])
ax.set_ylim([0, con.map_size])

max_error = con.max_memory_error

for j in range(ant_number):

    # Define Ant
    position = con.ant_start_position
    globalVector = con.global_vector_start
    tracks.append(list())
    tracks[j].append(position)

    cycles = con.steps

    # Main Loop

    for i in range(cycles):
        desired = desired_direction(globalVector, position)
        possible = possible_direction(position)
        step = actual_step(desired, possible)
        position = [position[0] + step[0], position[1] + step[1]]
        globalVector = globalVector - step

        # error in globalVector memory
        random_error = np.random.normal(0, max_error)
        rotation_global = [[math.cos(random_error), -math.sin(random_error)],
                           [math.sin(random_error), math.cos(random_error)]]
        globalVector = np.matmul(rotation_global, globalVector)

        tracks[j].append(position)
        if con.map[position[0], position[1]] == 3:
            break


    # Plot

    path = mpath.Path(tracks[j])
    patch = mpatches.PathPatch(path, facecolor='none', linewidth=0.25)
    ax.add_patch(patch)

print("git")
git = plt.figure()


ay = git.add_subplot(121)
az = git.add_subplot(122)

ay.set_xlim([0,1600])
ay.set_ylim([0,1600])

az.set_xlim([0,1600])
az.set_ylim([0,1600])

ay.matshow(np.transpose(con.local_vector[:,:,0]), cmap='bwr')
az.matshow(np.transpose(con.local_vector[:,:,1]), cmap='bwr')

plt.ioff()
plt.show()

print("fertig")
