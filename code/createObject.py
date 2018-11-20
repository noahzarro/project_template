import config as con
import numpy as np
import math

def create_object():

    object_number = len(con.object_positions)

    for i in range(1,object_number + 1):
        ix = con.object_positions[i,0]
        iy = con.object_positions[i,1]

        # draw object
        for x in range(-math.floor(con.resolution/2))
        # draw the channel
        for x in range(- math.floor(channel_width / 2) + 1, math.floor(channel_width / 2) + 1):
            for y in range(- math.floor(channel_width / 2) + 1, math.floor(channel_width / 2) + 1):
                point_to_draw = [drawing_position[0] + x, drawing_position[1] + y]
                # skip points out of map range
                if point_to_draw[0] <= 0 or point_to_draw[1] <= 0:
                    continue
                if point_to_draw[0] >= con.map_size - 1 or point_to_draw[1] >= con.map_size - 1:
                    continue
                con.map[point_to_draw[0], point_to_draw[1]] = 1
                # local vector points in the direction of the channel
                con.local_vector[point_to_draw[0], point_to_draw[1], 0] = max_cor_coordinates[0]
                con.local_vector[point_to_draw[0], point_to_draw[1], 1] = max_cor_coordinates[1]