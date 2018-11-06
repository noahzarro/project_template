import math

def actual_step(desired, possible, stepLength):
    #returns actual step Vector normalized to stepLength
    xmin = possible(0)
    xmax = possible(1)
    ymin = possible(2)
    ymax = possible(3)
    actual = desired

    if (desired[0]<0 and xmin > -1): #if desired.x < 0 and xmin not -1 (xmin == 0) set actual.x to 0
        actual[0] = 0

    if (desired[0]>0 and xmax < 1): #if x positive but not possible, set x to 0
        actual[0] = 0

    if (desired[1]<0 and ymin > -1): #if desired.y < 0 and ymin not -1 (xmin == 0) set actual.y to 0
        actual[1] = 0

    if (desired[1]>0 and ymax < 1): #if y positive but not possible, set y to 0
        actual[1] = 0

    return actual/math.sqrt((actual[0])^2+(actual[1])^2)