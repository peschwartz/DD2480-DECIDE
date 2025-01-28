from GLOBAL_VARS import *
from decide_io import *
import cmv
import pum
import fuv
from launch import *

def final_values():
    
    print("Parameters: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, ".format(PARAMETERS.LENGTH1, PARAMETERS.RADIUS1, PARAMETERS.EPSILON, PARAMETERS.AREA1, PARAMETERS.Q_PTS, PARAMETERS.QUADS, PARAMETERS.DIST, PARAMETERS.N_PTS, PARAMETERS.K_PTS, PARAMETERS.A_PTS, PARAMETERS.B_PTS, PARAMETERS.C_PTS, PARAMETERS.D_PTS, PARAMETERS.E_PTS, PARAMETERS.F_PTS, PARAMETERS.G_PTS, PARAMETERS.LENGTH2, PARAMETERS.RADIUS2, PARAMETERS.AREA2))
    print("PUM {}".format(len(PUM)))
    for i in range(15):
        print("    ", len(PUM[i]))
        print("    ", PUM[i])
    
    print("Numpoints: {}".format(NUMPOINTS))
    print("Points ({}): {}".format(len(POINTS),POINTS))
    print("CMV ({}): {}".format(len(CMV), CMV))

    print("FUV ({}): {}".format(len(FUV), FUV))

    print("LAUNCH: {}".format(LAUNCH))

def test_values():

    
    print("LCM {}".format(len(LCM)))
    for i in range(15):
        print(len(LCM[i]))
        print(LCM[i])

    print("PUV ({}): {}".format(len(PUV), PUV))

# from the headerfile in the description
def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT

def decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV):
    # call the cmv functions, \
    # TODO: need to update the function calls to match the completed cmv file
    CMV = [False] * 15

    CMV[0] = cmv.lic_0(PARAMETERS.LENGTH1, POINTS, NUMPOINTS)
    CMV[1] = cmv.lic_1(PARAMETERS.RADIUS1, POINTS, NUMPOINTS)
    CMV[2] = cmv.lic_2(POINTS, PARAMETERS.EPSILON, PI)
    CMV[3] = cmv.lic_3(PARAMETERS.AREA1, POINTS, NUMPOINTS)
    CMV[4] = cmv.lic_4(PARAMETERS.Q_PTS, PARAMETERS.QUADS)
    CMV[5] = cmv.lic_5(POINTS, NUMPOINTS)
    CMV[6] = cmv.lic_6(PARAMETERS.N_PTS, PARAMETERS.DIST, POINTS, NUMPOINTS)
    CMV[7] = cmv.lic_7(POINTS, PARAMETERS.K_PTS, PARAMETERS.LENGTH1, NUMPOINTS)
    CMV[8] = cmv.lic_8(POINTS, NUMPOINTS, PARAMETERS.A_PTS, PARAMETERS.B_PTS, PARAMETERS.RADIUS1)
    CMV[9] = cmv.lic_9(POINTS, NUMPOINTS, PARAMETERS.C_PTS, PARAMETERS.D_PTS, PARAMETERS.EPSILON)
    CMV[10] = cmv.lic_10(PARAMETERS.E_PTS, PARAMETERS.F_PTS, PARAMETERS.AREA1, POINTS, NUMPOINTS)
    CMV[11] = cmv.lic_11(PARAMETERS.G_PTS, POINTS, NUMPOINTS)
    CMV[12] = cmv.lic_12(POINTS, PARAMETERS.K_PTS, PARAMETERS.LENGTH1, PARAMETERS.LENGTH2, NUMPOINTS)
    CMV[13] = cmv.lic_13(POINTS, NUMPOINTS, PARAMETERS.A_PTS, PARAMETERS.B_PTS, PARAMETERS.RADIUS1, PARAMETERS.RADIUS2)
    CMV[14] = cmv.lic_14(POINTS, NUMPOINTS, PARAMETERS.E_PTS, PARAMETERS.F_PTS, PARAMETERS.AREA1, PARAMETERS.AREA2)

    #calculate pum
    PUM = pum.calculate_pum(LCM, CMV)

    # calculate FUV
    FUV = fuv.compute_fuv_from_pum(PUV, PUM)

    # calculate LAUNCH
    LAUNCH = compute_launch(FUV)

    return CMV, PUM, FUV, LAUNCH

# make a main function to test the decide function
if __name__ == "__main__":
    # read input from file
    # test_values()
    read_input("test/test_decide.in")
    # test_values()
    # call the decide function
    CMV, PUM, FUV, LAUNCH = decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)
    
    # print the final values
    final_values()

    print(LAUNCH)