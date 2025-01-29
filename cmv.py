# Functions for calculating contents of CMV vector
import math

from typing import List
from lib.util import *
from GLOBAL_VARS import *

''' 
Check that there exists at least one set of two consecutive data points that 
are a distance greater than the length, LENGTH1, apart, otherwise False. 
'''
def lic_0(LENGTH1: float, POINTS: list, NUMPOINTS: int):
    assert LENGTH1 >= 0, "LENGTH1 must be non-negative"
    # There must exist 2 point
    if NUMPOINTS < 2:
        return False
    for i in range(NUMPOINTS-1):
        x1, y1 = POINTS[i]
        x2, y2 = POINTS[i+1]
        if distance(x1, y1, x2, y2) > LENGTH1:
            return True
    return False

''' 
There exists at least one set of three consecutive data points that 
cannot all be contained, within or on a circle of radius RADIUS1. 
'''
def lic_1(RADIUS1: float, POINTS: list, NUMPOINTS: int):
    assert RADIUS1 >= 0, "RADIUS1 must be non-negative"
    # There must exist 3 point
    if NUMPOINTS < 3:
        return False
    for i in range(NUMPOINTS - 2):
        x1, y1 = POINTS[i]
        x2, y2 = POINTS[i + 1]
        x3, y3 = POINTS[i + 2]

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

''' 
Check that there exists at least one set of three consecutive data points which form 
an angle such that: angle < PI−EPSILON or angle > PI+EPSILON. The second of the three 
consecutive points is always the vertex of the angle. 
'''
def lic_2(POINTS: list, EPSILON: float, PI: float):
    assert 0 <= EPSILON and EPSILON < PI, "EPSILON must be in [0,PI)"
    min_angle = PI - EPSILON
    max_angle = PI + EPSILON
    for fst, snd, trd in zip(POINTS, POINTS[1:], POINTS[2:]):
        # If either the first point or the last point (or both) coincides with the vertex, 
        # the angle is undefined and the LIC is not satisfied by those three points
        if fst == snd or trd == snd:
            continue

        angle = get_angle(fst, snd, trd)
        if angle < min_angle or max_angle < angle:
            return True

    return False

''' 
Check that There exists at least one set of three consecutive data points that are the 
vertices of a triangle with area greater than AREA1. 
'''
def lic_3(AREA1: float, POINTS: list, NUMPOINTS: int):
    assert AREA1 >= 0, "AREA1 must be non-negative"

    # There must exist 3 point
    if NUMPOINTS < 3:
        return False
    
    for point in range(NUMPOINTS-2):
        x1, y1 = POINTS[point]
        x2, y2 = POINTS[point+1]
        x3, y3 = POINTS[point+2]
        area = triangle_area(x1, y1, x2, y2, x3, y3)
        if area > AREA1:
            return True

    return False

''' 
Check that there exists at least one set of Q_PTS consecutive data points that lie in 
more than QUADS quadrants. Where there is ambiguity as to which quadrant contains a given 
point, priority of decision will be by quadrant number, i.e., I, II, III, IV. For example, 
the data point (0,0) is in quadrant I, the point (-l,0) is in quadrant II, the point (0,-l) 
is in quadrant III, the point (0,1) is in quadrant I and the point (1,0) is in quadrant I. 
'''
def lic_4(POINTS: list, NUMPOINTS: int, Q_PTS: int, QUADS: int):
    assert 2 <= Q_PTS <= NUMPOINTS, "Q_PTS must be between 2 and NUMPOINTS"
    assert 1 <= QUADS <= 3, "QUADS must be between 1 and 3"

    # mapping coordinates to quadrant
    quads = [quadrants(x,y) for x,y in POINTS]
    for i in range(NUMPOINTS-Q_PTS+1):
        # Extracta subset of quads for Q_PTS consecutive points
        subset_quads = quads[i:i+Q_PTS]

        # Extracting the unique quadrants
        common_quads = set(subset_quads)
        if len(common_quads) > QUADS:
            return True
    return False

''' 
Check that there exists at least one set of two consecutive data points where the 
second X coordinate is less than the first X coordinate. 
'''
def lic_5(POINTS: list, NUMPOINTS: int):
    for point in range(NUMPOINTS-1):
        x1, _ = POINTS[point]
        x2, _ = POINTS[point+1]
        if x2 < x1:
            return True
    return False

''' 
Check that there exists at least one set of N PTS consecutive data points such that 
at least one of the points lies a distance greater than DIST from the line joining the 
first and last of these N PTS points. If the first and last points of these N PTS are 
identical, then the calculated distance to compare with DIST will be the distance from 
the coincident point to all other points of the N PTS consecutive points. 
'''
def lic_6(N_PTS: int, DIST: float, POINTS: list, NUMPOINTS: int) -> bool:
    assert N_PTS >= 3 and N_PTS <= NUMPOINTS, "N_PTS must be between 3 and NUMPOINTS"
    assert DIST >= 0, "DIST must be non-negative"
    # Condition is not met when NUMPOINTS < 3.
    if NUMPOINTS < 3:
        return False

    for start_idx in range(NUMPOINTS - N_PTS + 1):
        x1, y1 = POINTS[start_idx]
        x2, y2 = POINTS[start_idx + N_PTS - 1]
        # Check if the first and last points are the same
        same_endpoints = (abs(x1 - x2) < 1e-9 and abs(y1 - y2) < 1e-9)
        # Pre-calc line length if not coincident
        if not same_endpoints:
            line_len = distance(x1, y1, x2, y2)

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

''' 
Check that there exists at least one set of two data points separated by exactly K_PTS 
consecutive intervening points that are a distance greater than the length, LENGTH1, apart. 
'''
def lic_7(POINTS: list, K_PTS: int, LENGTH1: float, NUMPOINTS: int):
    assert K_PTS >= 1 and K_PTS <= NUMPOINTS - 2, "K_PTS must be between 1 and NUMPOINTS-2"
    assert LENGTH1 >= 0, "LENGTH1 must be non-negative"
    # Condition is not met when NUMPOINTS < 3.
    if NUMPOINTS < 3:
        return False

# Iterate through all pairs K_PTS apart
    for s in range(NUMPOINTS - K_PTS - 1):
        distance = math.dist(POINTS[s], POINTS[s + K_PTS + 1]) 
        if distance > LENGTH1:
            return True

    return False


'''
Check that here exists at least one set of 3 data points separated by exactly A_PTS and B_PTS 
consecutive intervening points, respectively, that cannot be contained within or on a circle 
of radius RADIUS1. 
'''
def lic_8(POINTS: list, NUMPOINTS: int, A_PTS: int, B_PTS: int, RADIUS1: float):
    assert A_PTS >= 1, "A_PTS must be at least 1"
    assert B_PTS >= 1, "B_PTS must be at least 1"
    assert A_PTS + B_PTS <= NUMPOINTS - 3, "A_PTS + B_PTS must be at most NUMPOINTS-3"
    assert RADIUS1 >= 0, "RADIUS1 must be non-negative"

    # The condition is not met when NUMPOINTS < 5. 
    if NUMPOINTS < 5:
        return False
    
    for i in range(NUMPOINTS - 2 - A_PTS - B_PTS):
        p1 = POINTS[i]
        p2 = POINTS[i + A_PTS + 1]
        p3 = POINTS[i + A_PTS + B_PTS + 2]
        if not fit_in_circle(p1, p2, p3, RADIUS1):
            return True
    
    return False

''' 
Check that there exists at least one set of three data points separated by exactly C_PTS
and D_PTS consecutive intervening points, respectively, that form an angle such that:
angle < (PI−EPSILON) or angle > (PI+EPSILON). The second point of the set of three points is 
always the vertex of the angle. If either the first point or the last point (or both) coincide 
with the vertex, the angle is undefined and the LIC is not satisfied by those three points. 
'''
def lic_9(POINTS: list, NUMPOINTS: int, C_PTS: int, D_PTS: int, EPSILON: float):
    assert C_PTS >= 1, "C_PTS must be at least 1"
    assert D_PTS >= 1, "D_PTS must be at least 1"
    assert C_PTS + D_PTS <= NUMPOINTS - 3, "C_PTS + D_PTS must be at most NUMPOINTS-3"
    assert EPSILON >= 0 and EPSILON < PI, "EPSILON must be in [0,PI)"

    # The condition is not met when NUMPOINTS < 5. 
    if NUMPOINTS < 5:
        return False
    if C_PTS < 1:
        return False
    if D_PTS < 1:
        return False
    if C_PTS + D_PTS > NUMPOINTS - 3:
        return False
    
    # iterating through valid triplets
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

''' 
Check that there exists at least one set of three data points separated by exactly E_PTS 
and F_PTS consecutive intervening points, respectively, that are the vertices of a triangle 
with area greater than AREA1 
'''
def lic_10(E_PTS: int, F_PTS: int, AREA1: float, POINTS: list, NUMPOINTS: int):
    assert E_PTS >= 1, "E_PTS must be at least 1"
    assert F_PTS >= 1, "F_PTS must be at least 1"
    assert E_PTS + F_PTS <= NUMPOINTS - 3, "E_PTS + F_PTS must be at most NUMPOINTS-3"
    assert AREA1 >= 0, "AREA1 must be non-negative"

    # iterating through valid triplets
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        point1 = POINTS[i]
        point2 = POINTS[i + E_PTS + 1]
        point3 = POINTS[i + E_PTS + F_PTS + 2]
        area = triangle_area(point1[0], point1[1], point2[0], point2[1], point3[0], point3[1])
        if area > AREA1:
            return True

    return False

''' 
Check that there exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), 
separated by exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j) 
'''
def lic_11(G_PTS: int, POINTS: list, NUMPOINTS: int) -> bool:
    assert G_PTS >= 1 and G_PTS <= NUMPOINTS - 2, "G_PTS must be between 1 and NUMPOINTS-2"

    # The condition is not met when NUMPOINTS < 3.
    if NUMPOINTS < 3:
        return False
    for i in range(NUMPOINTS - G_PTS - 1):
        j = i + G_PTS + 1
        if POINTS[j][0] - POINTS[i][0] < 0:
            return True

    return False

''' 
Check that there exists at least one set of two data points, separated by exactly K PTS 
consecutive intervening points, which are a distance greater than the length, LENGTH1, 
apart. In addition, there exists at least one set of two data points (which can be the 
same or different from the two data points just mentioned), separated by exactly K PTS 
consecutive intervening points, that are a distance less than the length, LENGTH2, apart. 
Both parts must be true for the LIC to be true 
'''
def lic_12(POINTS: list, K_PTS: int, LENGTH1: float, LENGTH2: float, NUMPOINTS: int):
    assert K_PTS >= 1 and K_PTS <= NUMPOINTS - 2, "K_PTS must be between 1 and NUMPOINTS-2"
    assert LENGTH1 >= 0, "LENGTH1 must be non-negative"
    assert LENGTH2 >= 0, "LENGTH2 must be non-negative"

    # The condition is not met when NUMPOINTS < 3.
    if NUMPOINTS < 3:
        return False

    length1_condition = False
    length2_condition = False
    for s in range(NUMPOINTS - K_PTS - 1):
        distance = math.dist(POINTS[s], POINTS[s + K_PTS + 1]) 
        if distance > LENGTH1:
            length1_condition = True

        if distance < LENGTH2:
            length2_condition = True

    return length1_condition and length2_condition

''' 
Check that there exists at least one set of three data points, separated by exactly A_PTS 
and B_PTS consecutive intervening points, respectively, that cannot be contained within or 
on a circle of radius RADIUS1. In addition, there exists at least one set of three data points 
(which can be the same or different from the three data points just mentioned) separated by 
exactly A_PTS and B_PTS consecutive intervening points, respectively, that can be contained 
in or on a circle of radius RADIUS2. Both parts must be true for the LIC to be true. 
'''
def lic_13(POINTS: list, NUMPOINTS: int, A_PTS: int, B_PTS: int, RADIUS1: float, RADIUS2: float):
    assert A_PTS >= 1, "A_PTS must be at least 1"
    assert B_PTS >= 1, "B_PTS must be at least 1"
    assert A_PTS + B_PTS <= NUMPOINTS - 3, "A_PTS + B_PTS must be at most NUMPOINTS-3"
    assert RADIUS1 >= 0, "RADIUS1 must be non-negative"
    assert RADIUS2 >= 0, "RADIUS2 must be non-negative"

    # The condition is not met when NUMPOINTS < 5.
    if NUMPOINTS < 5:
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

''' 
Check that there exists at least one set of three data points, separated by exactly E_PTS 
and F_PTS consecutive intervening points, respectively, that are the vertices of a triangle 
with area greater than AREA1. In addition, there exist three data points (which can be the 
same or different from the three data points just mentioned) separated by exactly E_PTS and 
F_PTS consecutive intervening points, respectively, that are the vertices of a triangle with 
area less than AREA2. Both parts must be true for the LIC to be true. 
'''
def lic_14(POINTS: list, NUMPOINTS: int, E_PTS: int, F_PTS: int, AREA1: float, AREA2: float):
    assert E_PTS >= 1, "E_PTS must be at least 1"
    assert F_PTS >= 1, "F_PTS must be at least 1"
    assert E_PTS + F_PTS <= NUMPOINTS - 3, "E_PTS + F_PTS must be at most NUMPOINTS-3"
    assert AREA1 >= 0, "AREA1 must be non-negative"
    assert AREA2 >= 0, "AREA2 must be non-negative"

    # Condition is not met when NUMPOINTS < 5
    if NUMPOINTS < 5:
        return False
    
    # check condition
    check = [False, False]
    
    # iterating through valid triplets
    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        p1 = POINTS[i]
        p2 = POINTS[i + E_PTS + 1]
        p3 = POINTS[i + E_PTS + F_PTS + 2]

        # check if there exists a triangle formed by 3 points with greater area than AREA1
        if triangle_area(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1]) > AREA1:
            check[0] = True
        
        # check if there exists a triangle formed by 3 points with a smaller area than AREA2
        if triangle_area(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1]) < AREA2:
            check[1] = True

    # both parts must be true for the LIC to be true
    if check[0] and check[1]:
        return True
    
    return False
