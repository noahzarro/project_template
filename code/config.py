import numpy as np


# Define Map (0 desert, 1 channel, 2 channel entry/exit, 3 home, 4 object)

map = np.zeros([1600,1600])
map[0, :] = 4        # Define border
map[1599, :] = 4
map[:, 0] = 4
map[:, 1599] = 4
map[1, 1:797] = 1  # Define channel of width 3
map[1, 798] = 2    # Define channel exit
map[799:800,799:800] = 3    # Define nest of size 2x2

local = np.zeros([1600,1600,2])