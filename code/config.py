import numpy as np
from createChannel import create_channel
import math
from editLocalVector import edit_local_vector
from createObject import create_object
from defineFamiliarPath import define_familiar_path


# Map parameter
localWeight = 0.9
map_size = 1600
resolution = 20

# channel
start_position = [1, 1]
end_position = [1, 799]
channel_length = math.sqrt((start_position[0] - end_position[0])**2 + (start_position[1] - end_position[1])**2)

# nest
nest_position = math.floor(map_size/2)
nest_influence = 100
nest_pull_strength = 10

# channel exit
channel_exit_influence = 300
exit_direction = [1, 0]     # enter normed vector here
exit_push_strength = 5

# object
object_positions = [[100, 800], [150, 850], [200, 900]]
object_influence = 100
object_push_strength = 5
object_path_distance_influence = 0.1

# familiar path
start_of_path = [10, 800]
end_of_path = [300, 1000]

# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)
map = np.zeros([map_size, map_size], dtype=int, order='C')
local_vector = np.zeros([map_size, map_size, 2])

# Define border
map[0, :] = 4
map[map_size - 1, :] = 4
map[:, 0] = 4
map[:, map_size -1] = 4

# Define channel (start_position, end_position, channel_width)
create_channel(start_position, end_position, resolution)

# Define nest
for x in range(- math.floor(resolution / 2) + 1, math.floor(resolution/2) + 1):
    for y in range(- math.floor(resolution / 2) + 1, math.floor(resolution/2) + 1):
        map[nest_position + x, nest_position + y] = 3

# define familiar path with objects and edit local vector
create_object()
define_familiar_path(start_of_path, end_of_path)

edit_local_vector()

