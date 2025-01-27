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
def lic_6(N_PTS: int, DIST: float, POINTS: list, NUMPOINTS: int) -> bool:
    # Condition not meet when fewer then 3 points
    if NUMPOINTS < 3:
        return False
    # Iterate over every consecutive block of size N_PTS
    for start_idx in range(NUMPOINTS - N_PTS + 1):
        # First and last points of the block
        x1, y1 = POINTS[start_idx]
        x2, y2 = POINTS[start_idx + N_PTS - 1]
        # Check if the first and last points are the same
        same_endpoints = (abs(x1 - x2) < 1e-9 and abs(y1 - y2) < 1e-9)
        # Pre-calc line length if not coincident
        if not same_endpoints:
            line_len = distance(x1, y1, x2, y2)
        # Now examine every point in this block
        for j in range(start_idx, start_idx + N_PTS):
            px, py = POINTS[j]
            # If endpoints coincide, measure distance from that single point
            if same_endpoints:
                d = distance(x1, y1, px, py)
            else:
                # If line is extremely short, fallback to point-to-point distance
                if line_len < 1e-9:
                    d = distance(x1, y1, px, py)
                else:
                    # Standard perpendicular distance formula using cross product
                    cross = abs((x2 - x1)*(y1 - py) - (y2 - y1)*(x1 - px))
                    d = cross / line_len
            # If any point is too far, condition is satisfied => True
            if d > DIST:
                return True
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
