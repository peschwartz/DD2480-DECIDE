from GLOBAL_VARS import *
import cmv
import pum

# from the headerfile in the description
def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT

def decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV):
    # call the cmv functions

    #calculate pum
    PUM = pum.calculate_pum(LCM, CMV)

    # calculate FUV

    # calculate LAUNCH

    pass

decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)
