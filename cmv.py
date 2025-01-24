from GLOBAL_VARS import *
import math
# cmv functions go here
# 15 conditions to be met to create the 15 element CMV vector

# LIC 0
def lic_0(LENGTH1: float):
    return False

# LIC 1
def lic_1(RADIUS1: float):
    return False


def anglehelper(fst: Coordinate, snd: Coordinate, trd: Coordinate):
    assert fst != snd and trd != snd
    return math.asin( math.dist(snd, fst) / math.dist(snd, trd) )

# LIC 2
def lic_2(EPSILON: float):
    assert 0 <= EPSILON and EPSILON < PI
    min_angle = PI - EPSILON
    max_angle = PI + EPSILON
    for fst, snd, trd in zip(POINTS, POINTS[1:], POINTS[2:]):
        # If either the first point or the last point (or both) coincides with the vertex, the angle is undefined and the LIC is not satisfied by those three points
        if fst == snd or trd == snd:
            continue;

        angle = anglehelper(fst, snd, trd)
        if angle > min_angle or max_angle > angle:
            return True

    return False




    return False

# LIC 3
def lic_3(AREA1: float):
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
