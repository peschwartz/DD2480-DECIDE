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
    
    print("Numpoints: {}".format(gv.NUMPOINTS))
    print("Points ({}): {}".format(len(gv.POINTS), gv.POINTS))
    print("CMV ({}): {}".format(len(CMV), CMV))

    print("FUV ({}): {}".format(len(FUV), FUV))

    print("LAUNCH: {}".format(LAUNCH))

def test_values():

    
    print("LCM {}".format(len(LCM)))
    for i in range(15):
        print(len(LCM[i]))
        print(LCM[i])

    print("PUV ({}): {}".format(len(PUV), PUV))

def decide():
    # call the cmv functions
    CMV = [False] * 15

    CMV[0] = cmv.lic_0(gv.PARAMETERS.LENGTH1, gv.POINTS, gv.NUMPOINTS)
    CMV[1] = cmv.lic_1(gv.PARAMETERS.RADIUS1, gv.POINTS, gv.NUMPOINTS)
    CMV[2] = cmv.lic_2(gv.POINTS, gv.PARAMETERS.EPSILON, PI)
    CMV[3] = cmv.lic_3(gv.PARAMETERS.AREA1, gv.POINTS, gv.NUMPOINTS)
    CMV[4] = cmv.lic_4(gv.POINTS, gv.NUMPOINTS, gv.PARAMETERS.Q_PTS, gv.PARAMETERS.QUADS)
    CMV[5] = cmv.lic_5(gv.POINTS, gv.NUMPOINTS)
    CMV[6] = cmv.lic_6(gv.PARAMETERS.N_PTS, gv.PARAMETERS.DIST, gv.POINTS, gv.NUMPOINTS)
    CMV[7] = cmv.lic_7(gv.POINTS, gv.PARAMETERS.K_PTS, gv.PARAMETERS.LENGTH1, gv.NUMPOINTS)
    CMV[8] = cmv.lic_8(gv.POINTS, gv.NUMPOINTS, gv.PARAMETERS.A_PTS, gv.PARAMETERS.B_PTS, gv.PARAMETERS.RADIUS1)
    CMV[9] = cmv.lic_9(gv.POINTS, gv.NUMPOINTS, gv.PARAMETERS.C_PTS, gv.PARAMETERS.D_PTS, gv.PARAMETERS.EPSILON)
    CMV[10] = cmv.lic_10(gv.PARAMETERS.E_PTS, gv.PARAMETERS.F_PTS, gv.PARAMETERS.AREA1, gv.POINTS, gv.NUMPOINTS)
    CMV[11] = cmv.lic_11(gv.PARAMETERS.G_PTS, gv.POINTS, gv.NUMPOINTS)
    CMV[12] = cmv.lic_12(gv.POINTS, gv.PARAMETERS.K_PTS, gv.PARAMETERS.LENGTH1, gv.PARAMETERS.LENGTH2, gv.NUMPOINTS)
    CMV[13] = cmv.lic_13(gv.POINTS, gv.NUMPOINTS, gv.PARAMETERS.A_PTS, gv.PARAMETERS.B_PTS, gv.PARAMETERS.RADIUS1, gv.PARAMETERS.RADIUS2)
    CMV[14] = cmv.lic_14(gv.POINTS, gv.NUMPOINTS, gv.PARAMETERS.E_PTS, gv.PARAMETERS.F_PTS, gv.PARAMETERS.AREA1, gv.PARAMETERS.AREA2)

    #calculate pum
    PUM = pum.calculate_pum(gv.LCM, CMV)

    # calculate FUV
    FUV = fuv.compute_fuv_from_pum(gv.PUV, PUM)

    # calculate LAUNCH
    LAUNCH = compute_launch(FUV)

    return CMV, PUM, FUV, LAUNCH

# make a main function to test the decide function
if __name__ == "__main__":
    # read input from file
    read_input("test/test_decide.in")
    
    # call the decide function
    CMV, PUM, FUV, LAUNCH = decide()
    
    # print the final values
    # final_values()

    print(LAUNCH)