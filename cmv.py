
# cmv functions go here
# 15 conditions to be met to create the 15 element CMV vector
from typing import List
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
def lic_1(RADIUS1: float, POINTS: list, NUMPOINTS: int):
    # Return false if there are not enough points
    if NUMPOINTS < 3:
        return False
    # Iterating over our triplets of points
    for i in range(NUMPOINTS - 2):
        x1, y1 = POINTS[i]
        x2, y2 = POINTS[i + 1]
        x3, y3 = POINTS[i + 2]

        # Calculate triangle area
        area = triangle_area(x1, y1, x2, y2, x3, y3)
        # Check for collinearity
        if abs(area) < 1e-9:
            # calulate all pairwise distances
            d1 = distance(x1, y1, x2, y2)
            d2 = distance(x2, y2, x3, y3)
            d3 = distance(x1, y1, x3, y3)
            max_d = max(d1, d2, d3)
            # Diameter based radius 
            min_circle_radius = max_d / 2.0
        else:
            a = distance(x1, y1, x2, y2)
            b = distance(x2, y2, x3, y3)
            c = distance(x1, y1, x3, y3)
            # Circumcircle formula 
            min_circle_radius = (a * b * c) / (4.0 * area)

        if min_circle_radius > RADIUS1:
            return True

    return False

# LIC 2
def lic_2(POINTS: List[Coordinate], EPSILON: float, PI: float):
    assert 0 <= EPSILON and EPSILON < PI
    min_angle = PI - EPSILON
    max_angle = PI + EPSILON
    for fst, snd, trd in zip(POINTS, POINTS[1:], POINTS[2:]):
        # If either the first point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC is not satisfied by those three points
        if fst == snd or trd == snd:
            continue;

        angle = get_angle(fst, snd, trd)
        if angle < min_angle or max_angle < angle:
            return True

    return False

# LIC 3
def lic_3(AREA1: float, POINTS: list, NUMPOINTS: int):
    # There exists at least one set of three consecutive data points that are the vertices of 
    # a triangle with area greater than AREA1.

    # check if AREA1 is greater than 0 and NUMPOINTS >= 3, if not, throw an exception
    if AREA1 <= 0:
        return False
    if NUMPOINTS < 3:
        return False
    
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
def lic_5(POINTS: list, NUMPOINTS: int):
    # There exists at least one set of two consecutive data points where the second X coordinate 
    # is less than the first X coordinate.
    for point in range(NUMPOINTS-1):
        x1, _ = POINTS[point]
        x2, _ = POINTS[point+1]
        if x2 < x1:
            return True
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
        return False
    if A_PTS < 1:
        return False
    if B_PTS < 1:
        return False
    if A_PTS + B_PTS > NUMPOINTS - 3:
        return False
    
    for i in range(NUMPOINTS - 2 - A_PTS - B_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + A_PTS + 1]
        p3 = POINTS[i + A_PTS + B_PTS + 2]
        if not fit_in_circle(p1, p2, p3, RADIUS1):
            return True
    
    return False

# LIC 9
def lic_9(POINTS: list, NUMPOINTS: int, C_PTS: int, D_PTS: int, EPSILON: float):
    # There exists at least one set of three data points separated by exactly C_PTS and D_PTS
    # consecutive intervening points, respectively, that form an angle such that:
    # angle < (PI−EPSILON) or angle > (PI+EPSILON). The second point of the set of three points is always the vertex of the angle. 
    # If either the first point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC is not satisfied by those three points. 
    # When NUMPOINTS < 5, the condition is not met. 1 ≤ C_PTS, 1 ≤ D_PTS C_PTS + D_PTS ≤ NUMPOINTS−3

    if NUMPOINTS < 5:
        return False
    if C_PTS < 1:
        return False
    if D_PTS < 1:
        return False
    if C_PTS + D_PTS > NUMPOINTS - 3:
        return False
    
    for i in range(NUMPOINTS - 2 - C_PTS - D_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + C_PTS + 1]
        p3 = POINTS[i + C_PTS + D_PTS + 2]
        
    # Angle is undifined if any of the points coincide with the vertex
        if p1 == p2 or p1 == p3 or p2 == p3:
            continue
        else:
            angle = get_angle(p1,p2,p3)
            if angle < PI-EPSILON or angle > PI+EPSILON:
                return True
            else:
                continue
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
def lic_13(POINTS: list, NUMPOINTS: int, A_PTS: int, B_PTS: int, RADIUS1: float, RADIUS2: float):

    if NUMPOINTS < 5:
        return False
    if A_PTS < 1:
        return False
    if B_PTS < 1:
        return False
    if A_PTS + B_PTS > NUMPOINTS - 3:
        return False
    
    check = [False, False]

    # check there exists 3 pts that CAN be contained within a circle of radius2
    for i in range(NUMPOINTS - 2 - A_PTS - B_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + A_PTS + 1]
        p3 = POINTS[i + A_PTS + B_PTS + 2]
        
        # check if there exists 3 pts that CANNOT be contained within a circle of radius1
        if not fit_in_circle(p1, p2, p3, RADIUS1):
            check[0] = True
        
        # check if there exists 3 pts that CAN be contained within a circle of radius2
        if fit_in_circle(p1, p2, p3, RADIUS2):
            check[1] = True
        
    # check that both conditions were met
    if check[0] and check[1]:
        return True
    
    return False

# LIC 14
def lic_14(AREA2: float):
    return False
