# cmv functions go here
# 15 conditions to be met to create the 15 element CMV vector
from lib.util import *
from GLOBAL_VARS import *


# LIC 0
def lic_0(LENGTH1: float, POINTS: list, NUMPOINTS: int):
    if NUMPOINTS < 2:
        return False
    for i in range(NUMPOINTS-1):
        x1, y1 = POINTS[i]
        x2, y2 = POINTS[i+1]
        if distance(x1, y1, x2, y2) > LENGTH1:
            return True
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
def lic_8(POINTS: list, NUMPOINTS: int, A_PTS: int, B_PTS: int, RADIUS1: float):
    # there exists at least one set of 3 data points separated by exactly 
    # A_PTS and B_PTS consecutive intervening points, respectively, that cannot 
    # be contained within or on a circle of radius RADIUS1. 
    # 
    # The condition is not met when NUMPOINTS < 5. 
    # 1 <= A_PTS, 1 <=B_PTS
    # A_PTS + B_PTS <= NUMPOINTS - 3

    if NUMPOINTS < 5:
        raise ValueError("NUMPOINTS must be greater than 5")
    if A_PTS < 1:
        raise ValueError("A_PTS must be greater than 0")
    if B_PTS < 1:
        raise ValueError("B_PTS must be greater than 0")
    if A_PTS + B_PTS > NUMPOINTS - 3:
        raise ValueError("A_PTS + B_PTS must be less than NUMPOINTS - 3")
    
    for i in range(NUMPOINTS - 2 - A_PTS - B_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + A_PTS + 1]
        p3 = POINTS[i + A_PTS + B_PTS + 2]
        if not fit_in_circle(p1, p2, p3, RADIUS1):
            return True
    
    return False

# LIC 9
def lic_9(C_PTS: int, D_PTS: int):
    return False

# LIC 10
def lic_10(E_PTS: int, F_PTS: int):
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
