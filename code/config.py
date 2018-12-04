import numpy as np
from createChannel import create_channel
import math
from editLocalVector import edit_local_vector
from createObject import create_object
from defineFamiliarPath import define_familiar_path


'''
# Here all parameters can be changed for different simulations
'''

# ant
ant_number = 1      # how many ants are simulated
ant_start_position = [1, 1]       # starting position (possible values: ints between 1 and 1598)
global_vector_start = np.array([800, 800])      # global vector at the starting position
steps = 10000       # maximal steps the ant does
sigma = math.pi/8       # sigma for random angle distribution in desiredDirection
max_memory_error = math.pi / 1000       # maximal error per step of the global vector memory

# Map parameter
localWeight = 0.9
map_size = 1600
resolution = 20         # resolution for drawing

# channel
start_position = [1, 1]     # where the channel starts
end_position = [1, 799]     # where the channel ends

# nest
nest_position = math.floor(map_size/2)      # nest position in the middle of the map
nest_influence = 100        # distance from which the ant "sees" the nest
nest_pull_strength = 10

# channel exit
channel_exit_influence = 300
exit_direction = [1, 0]     # enter normed vector here # direction in which the ant leaves the channel
exit_push_strength = 5

# object
object_positions = [[100, 800], [150, 850], [200, 900]]     # objects help the ant for orientation with local vector
object_influence = 100
object_push_strength = 5        # influence how strong the local vector is in path direction
object_path_distance_influence = 0.1    # influence how strong the local vector directs to the path if left it

# familiar path
start_of_path = [10, 800]       # define a path direction but has only influences the local vector if objects are near
end_of_path = [300, 1000]

'''
# The following code should not be changed
'''

# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)
map = np.zeros([map_size, map_size], dtype=int, order='C')
local_vector = np.zeros([map_size, map_size, 2])

# Define border
map[0, :] = 4
map[map_size - 1, :] = 4
map[:, 0] = 4
map[:, map_size -1] = 4

# Define channel (start_position, end_position, channel_width)
channel_length = math.sqrt((start_position[0] - end_position[0])**2 + (start_position[1] - end_position[1])**2)
create_channel(start_position, end_position, resolution)

# Define nest
for x in range(- math.floor(resolution / 2) + 1, math.floor(resolution/2) + 1):
    for y in range(- math.floor(resolution / 2) + 1, math.floor(resolution/2) + 1):
        map[nest_position + x, nest_position + y] = 3

# define familiar path with objects and edit local vector
create_object()
define_familiar_path(start_of_path, end_of_path)
edit_local_vector()

