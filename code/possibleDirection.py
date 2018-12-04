import numpy as np
import math as m
import config

'''
 returns 3x3 matrix with each number representing a square. The middle one is the current position the others 
 are filled with 1 for possible direction and 0 for not possible direction.
'''


def possible_direction(position):
    possible_move = np.zeros([3, 3], order='C')      # empty matrix with possible direction
    square = np.array([position[0], position[1]])
    if config.map[square[0], square[1]] == 0:
        for x in range(0, 3):
            for y in range(0, 3):
                square_to_check = config.map[square[0] + (x - 1), square[1] + (y - 1)]
                # possible if desert, channel exit or nest
                if (square_to_check == 0) or (square_to_check == 2) or (square_to_check == 3):
                    possible_move[x, y] = 1      # move is possible

    if config.map[square[0], square[1]] == 1:
        for x in range(0, 3):
            for y in range(0, 3):
                square_to_check = config.map[square[0] + (x - 1), square[1] + (y - 1)]
                # possible if channel, channel exit or nest
                if (square_to_check == 1) or (square_to_check == 2) or (square_to_check == 3):
                    possible_move[x, y] = 1      # move is possible

    if config.map[square[0], square[1]] == 2:
        for x in range(0, 3):
            for y in range(0, 3):
                square_to_check = config.map[square[0] + (x - 1), square[1] + (y - 1)]
                # possible if desert, channel, channel exit or nest
                if (square_to_check == 0) or (square_to_check == 1) or (square_to_check == 2) or (square_to_check == 3):
                    possible_move[x, y] = 1      # move is possible

    possible_move[1, 1] = 0  # the ant is not allowed to stay on the same place
    return possible_move







