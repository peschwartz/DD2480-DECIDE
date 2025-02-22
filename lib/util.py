# File for storing utility function for the rest of the decide program
import math
import GLOBAL_VARS as gv
# util functions go here

# Function to calculate the distance between two points given their x,y coordinates
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Function to calculate the area of a triangle given 3 x,y coordinates
def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# Calculate shortest angle between the three coordinate points fst,snd,trd
# Angle is measured clockwise between fst and trd where snd is the vertex of the angle.
# Throws an error if either fst or trd coincides with snd
def get_angle(fst: gv.Coordinate, snd: gv.Coordinate, trd: gv.Coordinate):
    assert fst != snd and trd != snd
    f = lambda x, y : math.atan2(x[1] - y[1], x[0] - y[0])
    angle = f(fst,snd) - f(trd,snd)
    return angle if angle > 0 else 2 * math.pi + angle

# Function to calculate if the 3 points (tuples) fit in a circle given the radius
def fit_in_circle(p1, p2, p3, radius):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # calculate the center of the circle
    x_center = (x1 + x2 + x3) / 3
    y_center = (y1 + y2 + y3) / 3

    dist = []
    # calculate the distance between the center and each of the points
    dist.append(distance(x_center, y_center, x1, y1))
    dist.append(distance(x_center, y_center, x2, y2))
    dist.append(distance(x_center, y_center, x3, y3))

    for i in dist:
        # if one of the distances between the center and each of the points is greater than the radius
        # then the points do not fit in the circle and return false
        if i > radius:
            return False
    
    return True

# determine what quadrant that the point lies in
def quadrants(x,y):
    # assigning the quadrant number to a variable q
    if x >= 0 and y >= 0:
        q = 1
    elif x < 0 and y >= 0:
        q = 2
    elif x >= 0 and y < 0:
        q = 3
    else:
        q = 4
    
    return q

# from the headerfile in the description, compares two floats
def DOUBLECOMPARE(a: float, b: float) -> gv.CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return gv.CompType.EQ
    return gv.CompType.LT if a < b else gv.CompType.GT

# reset the global definitions for the input parameters to null
def reset_globals():
    gv.NUMPOINTS = 0
    gv.POINTS = []
    gv.PARAMETERS = gv.Parameters()
    gv.LCM = []
    gv.PUV = []