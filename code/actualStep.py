import numpy as np;
import math;

def actual_step(desired, possible):
    #returns actual step Vector

    values = np.zeros([3,3])-1 # initialize 3x3 matrix, where the correlation the desired step vector and the unit vectors pointing in all directions (cells of the matrix) are saved
    max = -1; # current best result
    maxCoord = [0,0] # coordinates with currently best result

    # iterate through all unit vectors (horizontal, diagonal and vertical (and zero, but it will never be chosen))

    for x in range(-1,2):
        for y in range(-1,2):
            if possible[x+1,y+1]: # if field accessible calculate correlation between direction vector for that field and desired vector
                values[x+1,y+1] = np.inner([x,y],desired)
                if (abs(x) == 1 and abs(y) == 1): # if diagonal, divide by sqrt(2) (because [+/-1,+/-1] is not normalized)
                    values[x + 1, y + 1] =  values[x+1,y+1]/math.sqrt(2);
            if values[x+1,y+1]>max: # if we have maximum correlation choose this direction
                max = values[x+1,y+1]
                maxCoord = [x,y]

    return maxCoord;
