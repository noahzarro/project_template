import math;
import numpy as np

def desired_direction(globalVector,position):
    #returns vector pointing in desired direction

    #calculate desired Vector depending on globalVector and localVector
    desired = globalVector

    #choose a random angle
    sigma = math.pi/2;
    randomAngle = np.random.normal(0,sigma);

    #construct rotation matrix
    rotationMatrix = [[math.cos(randomAngle), -math.sin(randomAngle)],[math.sin(randomAngle), math.cos(randomAngle)]]

    #rotate vector
    rotated = np.matmul(rotationMatrix,desired);


    return rotated;