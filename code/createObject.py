import config as con
import numpy as np
import math


def create_object():

    object_number = len(con.object_positions)

    for i in range(0, object_number):
        ix = con.object_positions[i][0]
        iy = con.object_positions[i][1]

        # draw object
        for x in range(-math.floor(con.resolution/2) + 1, math.floor(con.resolution/2) + 1):
            for y in range(-math.floor(con.resolution / 2) + 1, math.floor(con.resolution / 2) + 1):
                point_to_draw = [ix + x, iy + y]
                # skip points out of map range
                if point_to_draw[0] <= 0 or point_to_draw[1] <= 0:
                    continue
                if point_to_draw[0] >= con.map_size - 1 or point_to_draw[1] >= con.map_size - 1:
                    continue
                con.map[point_to_draw[0], point_to_draw[1]] = 4

