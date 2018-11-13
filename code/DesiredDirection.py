import math;
import numpy as np
import config as con


def desired_direction(globalVector, position):
    # returns vector pointing in desired direction

    # calculate desired Vector depending on globalVector and localVector
    localVector = con.local_vector[position[0],position[1]]

    norm = np.linalg.norm(globalVector)
    if norm != 0:
        globalVector = globalVector/norm
    else:
        globalVector = globalVector

    desired = globalVector*(1-con.localWeight) + localVector*con.localWeight

    norm = np.linalg.norm(desired)
    if norm != 0:
        desired = desired / norm
    else:
        desired = desired

    # choose a random angle
    sigma = math.pi/8;
    randomAngle = np.random.normal(0, sigma);

    # construct rotation matrix
    rotationMatrix = [[math.cos(randomAngle), -math.sin(randomAngle)], [math.sin(randomAngle), math.cos(randomAngle)]]

    # rotate vector
    rotated = np.matmul(rotationMatrix, desired);

    return rotated;