import math
import numpy as np

# ant
ant_number = 20      # how many ants are simulated
ant_start_position = [1, 1598]       # starting position (possible values: ints between 1 and 1598)
global_vector_start = np.array([800, -800])      # global vector at the starting position
steps = 5000       # maximal steps the ant does

# random factors for the ant to be natural
sigma = math.pi / 2       # sigma for random angle distribution in desiredDirection
max_memory_error = math.pi / 1000       # maximal error per step of the global vector memory

# Map parameter
localWeight = 0.9
map_size = 1600
resolution = 25         # resolution for drawing

# channel
start_position = [1, 1598]     # where the channel starts
end_position = [400, 1200]     # where the channel ends

# nest
nest_position = math.floor(map_size/2)      # nest position in the middle of the map
nest_influence = 100        # distance from which the ant "sees" the nest
nest_pull_strength = 10

# channel exit
channel_exit_influence = 200
exit_direction = [0, -1]     # enter normed vector here # direction in which the ant leaves the channel
exit_push_strength = 5

# object
object_positions = []     # objects help the ant for orientation with local vector
object_influence = 100      # the size of influence circle
object_push_strength = 5        # influence how strong the local vector is in path direction
object_path_distance_influence = 0.1    # influence how strong the local vector directs to the path if left it

# familiar path
start_of_path = [1, 1]       # define a path direction but only influences the local vector if objects are near
end_of_path = [1, 1]