import config as con
import math
import numpy as np

def edit_local_vector():

    # add local vector at channel exit
    for x in range(- math.floor(con.channel_exit_influence / 2) + 1,
                   math.floor(con.channel_exit_influence / 2) + 1):
        for y in range(-math.floor(math.sqrt(abs(math.floor(con.channel_exit_influence/2)**2-x**2))),
                       math.floor(math.sqrt(abs(math.floor(con.channel_exit_influence/2)**2-x**2)))+1):
            if (x+con.end_position[0]>=0 and y+con.end_position[1]>=0 and
                    x+con.end_position[0]<=con.map_size-1 and y+con.end_position[1]<=con.map_size-1):
                # x direction
                con.local_vector[con.end_position[0] + x, con.end_position[1] + y, 0] += \
                    con.exit_direction[0]/max(1,abs(x**0.5)) * con.exit_push_strength *(con.channel_length/800)
                # y direction
                con.local_vector[con.end_position[0] + x, con.end_position[1] + y, 1] += \
                    con.exit_direction[1]/max(1,abs(y**0.5)) * con.exit_push_strength * (con.channel_length/800)

    # add local vector at nest
    for x in range(- math.floor(con.nest_influence / 2) + 1, math.floor(con.nest_influence / 2) + 1):
        for y in range(- math.floor(math.sqrt(abs(math.floor(con.nest_influence/2)**2-x**2))),
                       math.floor(math.sqrt(abs(math.floor(con.nest_influence/2)**2-x**2)))+1):
            home_vector = [-x/max(np.linalg.norm([x,y]),1),-y/max(np.linalg.norm([x,y]),1)]

            con.local_vector[con.nest_position + x, con.nest_position + y, 0] = \
                home_vector[0] /max(1,abs(x**0.5)) * con.nest_pull_strength     # x direction
            con.local_vector[con.nest_position + x, con.nest_position + y, 1] = \
                home_vector[1] /max(1,abs(y**0.5)) * con.nest_pull_strength     # y direction
