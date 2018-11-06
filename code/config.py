import numpy as np
from createChannel import create_channel



# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)

map = np.zeros([1600, 1600], dtype=int, order='C')
map[0, :] = 4        # Define border
map[1599, :] = 4
map[:, 0] = 4
map[:, 1599] = 4

create_channel([1, 1], [1, 800])     # Define channel

map[799:800,799:800] = 3    # Define nest of size 2x2

local = np.zeros([1600,1600,2])