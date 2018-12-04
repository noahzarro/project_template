import config as con
import numpy as np
import math


def define_familiar_path(start_of_path, end_of_path):
    path_direction = [end_of_path[0] - start_of_path[0],        # creates a not normalized path vector
                      end_of_path[1] - start_of_path[1]]
    p_vec_norm = math.sqrt(path_direction[0] ** 2 + path_direction[1] ** 2)     # calculate norm
    path_vector = [path_direction[0] / p_vec_norm, path_direction[1] / p_vec_norm]      # normalize
    path_slope = path_vector[1] / path_vector[0]        # calculate the slope of the path straight
    vertical_slope = -1 / path_slope        # slope product of two verticals is -1
    vertical_direction = [1, vertical_slope]      # creates the vertical vector
    v_vec_norm = math.sqrt(vertical_direction[0]**2 + vertical_direction[1]**2)     # calculate norm
    vertical_vector = [vertical_direction[0] / v_vec_norm, vertical_direction[1]/ v_vec_norm]       # normalize

    object_number = len(con.object_positions)       # count objects

    for i in range(0,object_number):
        ix = con.object_positions[i][0]     # get the object position
        iy = con.object_positions[i][1]

        # edit local vector around the object
        for x in range(-math.floor(con.object_influence / 2), math.floor(con.object_influence / 2)):   # influence range
            y_border = math.floor(math.sqrt(math.floor(con.object_influence / 2) ** 2 - x ** 2))        # circle
            for y in range(- y_border, y_border):
                local_point = [ix + x, iy + y]      # cell which local vector is edited
                # skip points out of map range
                if local_point[0] <= 0 or local_point[1] <= 0:
                    continue
                if local_point[0] >= con.map_size - 1 or local_point[1] >= con.map_size - 1:
                    continue
                subtraction = [local_point[0] - start_of_path[0],       # calculate the distance between path and ant
                               local_point[1] - start_of_path[1]]
                ant_path_distance = np.cross(path_vector, subtraction)
                ant_path_vec = [vertical_vector[0] * ant_path_distance,     # create vertical vector from ant to path
                                vertical_vector[1] * ant_path_distance]
                stretched_path_vec = [con.object_push_strength * path_vector[0],        # stretch path component
                                      con.object_push_strength * path_vector[1]]
                stretched_ant_path_vec = [con.object_path_distance_influence *      # stretch distance component
                                          ant_path_vec[0], con.object_path_distance_influence * ant_path_vec[1]]
                local_vec = [stretched_ant_path_vec[0] + stretched_path_vec[0],     # combine path and distance comp.
                             stretched_ant_path_vec[1] + stretched_path_vec[1]]
                con.local_vector[local_point[0], local_point[1], 0] = local_vec[0]      # write local vector
                con.local_vector[local_point[0], local_point[1], 1] = local_vec[1]

    return
