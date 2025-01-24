from GLOBAL_VARS import *
import cmv
# from the headerfile in the description
def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT

PARAMETERS = Parameters()
POINTS = [(0,1), (1,0)] # Array of the coordinates of data points
NUMPOINTS = 2  # Number of data points
LCM = [[None] * 15] * 15   # Logical Connector Matrix
PUM = [[None] * 15] * 15 # Preliminary Unlocking Matrix
CMV = [None] * 15    # Conditions Met Vector
FUV = [None] * 15    # Final Unlocking Vector
LAUNCH: bool = False          # Decision: Launch or No Launch

def decide():
    # call the cmv functions

    # calculate PUM

    # calculate FUV

    # calculate LAUNCH

    pass