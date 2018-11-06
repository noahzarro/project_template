import numpy as np;

def actual_step(desired, possible):
    #returns actual step Vector

    values = np.zeros([3,3])-1
    max = -1;
    maxCoord = [0,0]


    for x in range(-1,2):
        for y in range(-1,2):
            if possible[x+1, y+1]: #if field acessible calculate inner product
                values[x+1, y+1] = np.inner([x,y],desired)
            if values[x+1, y+1] > max: #if we have maximum correlation choose this direction
                max = values[x+1, y+1]
                maxCoord = [x, y]

    return maxCoord;
