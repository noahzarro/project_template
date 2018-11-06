import numpy as np
import math as m

'''
 returns 3x3 matrix with each number representing a square. The middle one is the current position the others 
 are filled with 1 for possible direction and 0 for not possible direction.
'''

def possible_direction(position):
    possible_move = np.zeros(3,3)      # empty matrix with possible direction
    square = np.array(position[0], position[1])
    if map(square) == 0:
        for x in range(0, 3):
            for y in range(0, 3):
                if map(square + np.array([x - 1, y - 1])) == (0 or 2):
                    possible_move[x, y] = 1      # move is possible

    if map(square) == 1:
        for x in range(0, 3):
            for y in range(0, 3):
                if map(square + np.array([x - 1, y - 1])) == (1 or 2):
                    possible_move[x, y] = 1      # move is possible

    if map(square) == 2:
        for x in range(0, 3):
            for y in range(0, 3):
                if map(square + np.array([x - 1, y - 1])) == (0 or 1 or 2):
                    possible_move[x, y] = 1      # move is possible

    possible_move[1, 1] = 0  # the ant is not allowed to stay on the same place
    return possible_move






