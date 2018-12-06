import numpy as np
from createChannel import create_channel
import math
from editLocalVector import edit_local_vector
from createObject import create_object
from defineFamiliarPath import define_familiar_path


'''
# Insert here testfile to run test
from <testfile> import *
'''
from Test_1a import *

'''
The following code should not be changed
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

