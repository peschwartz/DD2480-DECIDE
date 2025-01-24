# cmv functions go here
# 15 conditions to be met to create the 15 element CMV vector
from lib.util import *


# LIC 0
def lic_0(LENGTH1: float):
    return False

# LIC 1
def lic_1(RADIUS1: float):
    return False

# LIC 2
def lic_2(EPSILON: float):
    return False

# LIC 3
def lic_3(AREA1: float, POINTS: list, NUMPOINTS: int):
    # There exists at least one set of three consecutive data points that are the vertices of 
    # a triangle with area greater than AREA1.

    # check if AREA1 is greater than 0 and NUMPOINTS >= 3, if not, throw an exception
    if AREA1 <= 0:
        raise ValueError("AREA1 must be greater than 0")
    if NUMPOINTS < 3:
        raise ValueError("NUMPOINTS must be greater than 3")
    
    for point in range(NUMPOINTS-2):
        x1, y1 = POINTS[point]
        x2, y2 = POINTS[point+1]
        x3, y3 = POINTS[point+2]
        area = triangle_area(x1, y1, x2, y2, x3, y3)
        if area > AREA1:
            # print(f"Area: {area} > {AREA1}")
            # print(f"Points: {x1, y1}, {x2, y2}, {x3, y3}")
            return True

    return False

# LIC 4
def lic_4(Q_PTS: int, QUADS: int):
    return False

# LIC 5
def lic_5(DIST: float):
    return False

# LIC 6
def lic_6(N_PTS: int, K_PTS: int):
    return False

# LIC 7
def lic_7(K_PTS: int):
    return False

# LIC 8
def lic_8(A_PTS: int, B_PTS: int):
    return False

# LIC 9
def lic_9(C_PTS: int, D_PTS: int):
    return False

# LIC 10
def lic_10(E_PTS: int, F_PTS: int, AREA1: float, POINTS: list, NUMPOINTS: int):
    if E_PTS < 1 or F_PTS < 1:
        return False
    if E_PTS + F_PTS > NUMPOINTS - 3:
        return False
    if NUMPOINTS < 5:
        return False

    # iterating through valid triplets
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        point1 = POINTS[i]
        point2 = POINTS[i + E_PTS + 1]
        point3 = POINTS[i + E_PTS + F_PTS + 2]
        area = triangle_area(point1[0], point1[1], point2[0], point2[1], point3[0], point3[1])
        if area > AREA1:
            return True
    return False

# LIC 11
def lic_11(G_PTS: int):
    return False

# LIC 12
def lic_12(LENGTH2: float):
    return False

# LIC 13
def lic_13(RADIUS2: float):
    return False

# LIC 14
def lic_14(AREA2: float):
    return False
