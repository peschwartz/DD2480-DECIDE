from GLOBAL_VARS import *
import cmv
import pum
import fuv
from launch import *
from decide_io import *
from launch import *

# from the headerfile in the description
def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT

PARAMETERS = Parameters()
POINTS = [(0,1), (1,0)] # Array of the coordinates of data points
NUMPOINTS = 2  # Number of data points, between 2 and 100
LCM = [[None] * 15] * 15   # Logical Connector Matrix
PUM = [[None] * 15] * 15 # Preliminary Unlocking Matrix
CMV = [None] * 15    # Conditions Met Vector
FUV = [None] * 15    # Final Unlocking Vector
LAUNCH: str = "NO"          # Decision: Launch or No Launch

def decide():
    # call the cmv functions
    CMV = cmv.calculate_cmv()
    # calculate PUM

    # calculate FUV
    FUV = fuv.compute_fuv_from_pum(PUV, PUM)

    # calculate LAUNCH
    LAUNCH = compute_launch(FUV)

    return LAUNCH