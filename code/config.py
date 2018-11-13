import numpy as np
from createChannel import create_channel



# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)

map_size = 1600
map = np.zeros([map_size, map_size], dtype=int, order='C')
map[0, :] = 4        # Define border
map[map_size - 1, :] = 4
map[:, 0] = 4
map[:, map_size -1] = 4

create_channel([1, 1], [1, 800])     # Define channel

map[799:800,799:800] = 3    # Define nest of size 2x2

local = np.zeros([map_size, map_size, 2])
