import numpy as np
from createChannel import create_channel
import math
from editLocalVector import edit_local_vector

# Map parameter
localWeight = 0.9
map_size = 1600
resolution = 20

# channel
start_position = [1, 1]
end_position = [1, 200]

# nest
nest_position = math.floor(map_size/2)
nest_influence = 300
nest_pull_strength = 5

# channel exit
channel_exit_influence = 300
exit_direction = [1, 0]     # enter normed vector here
exit_push_strength = 5

# object
object_positions = [[50, 50], [100, 50], [150, 50]]
object_influence = 50
object_push_strength = 5

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


edit_local_vector()

