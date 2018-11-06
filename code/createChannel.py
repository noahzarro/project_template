import config as con
import numpy as np


def create_channel(start_position, end_position):
    con.map[start_position] = 2
    con.map[end_position] = 2
    channel_direction = np.array([end_position[0] - start_position[0], end_position[1] - start_position[1]])

    drawing_position = start_position

    while drawing_position != end_position:
        correlation = np.zeros(3,3)-2
        max_correlation = -2
        max_cor_coordinates = [0,0]

        for x in range(-1,2):
            for y in range(-1,2):
                correlationrelation[x+1, y+1] = np.inner([x,y],channel_direction)
                if correlation[x+1, y+1] > max_correlation:
                    max_correlation = correlation[x+1, y+1]
                    max_cor_coordinates = [x,y]

        drawing_position = [drawing_position[0] + max_cor_coordinates[0], drawing_position[1] + max_cor_coordinates[1]]
        channel_direction = [channel_direction[0] - max_cor_coordinates[0], channel_direction[1] - max_cor_coordinates[1]]





