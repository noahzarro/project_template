import numpy as np
import math as m


def possible_direction(position):
    restriction = np.zeros(4)       # empty vector for return [x_min,x_max,y_min,y_max]
    square = np.array([m.floor(position[0]), m.floor(position[1])])      # descretise the position to a square
    if map(square) == 0:
        if map(square + np.array([-1, -1])) == (0 or 2):
            restriction[0] = -1     # x_min = -1
            restriction[2] = -1     # y_min = -1
        if map(square + np.array([-1, 1])) == (0 or 2):
            restriction[0] = -1     # x_min = -1
            restriction[3] = 1      # y_max = 1
        if map(square + np.array([1, -1])) == (0 or 2):
            restriction[1] = 1      # x_max = 1
            restriction[2] = -1     # y_min = -1
        if map(square + np.array([1, 1])) == (0 or 2):
            restriction[1] = 1      # x_max = 1
            restriction[3] = 1      # y_max = 1









