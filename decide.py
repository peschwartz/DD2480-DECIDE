from GLOBAL_VARS import *
import cmv
import pum
import fuv

# from the headerfile in the description
def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT

def decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV):
    # call the cmv functions, \
    # TODO: need to update the function calls to match the completed cmv file

    CMV[0] = cmv.lic_0(PARAMETERS.LENGTH1, POINTS, NUMPOINTS)
    CMV[1] = cmv.lic_1(PARAMETERS.RADIUS1, POINTS, NUMPOINTS)
    CMV[2] = cmv.lic_2(PARAMETERS.EPSILON)
    CMV[3] = cmv.lic_3(PARAMETERS.AREA1, POINTS, NUMPOINTS)
    CMV[4] = cmv.lic_4(PARAMETERS.Q_PTS, PARAMETERS.QUADS)
    CMV[5] = cmv.lic_5(POINTS, NUMPOINTS)
    CMV[6] = cmv.lic_6(PARAMETERS.N_PTS, PARAMETERS.K_PTS)
    CMV[7] = cmv.lic_7(PARAMETERS.K_PTS)
    CMV[8] = cmv.lic_8(POINTS, NUMPOINTS, PARAMETERS.A_PTS, PARAMETERS.B_PTS, PARAMETERS.RADIUS1)
    CMV[9] = cmv.lic_9(PARAMETERS.C_PTS, PARAMETERS.D_PTS)
    CMV[10] = cmv.lic_10(PARAMETERS.E_PTS, PARAMETERS.F_PTS, PARAMETERS.AREA1, POINTS, NUMPOINTS)
    CMV[11] = cmv.lic_11(PARAMETERS.G_PTS)
    CMV[12] = cmv.lic_12(PARAMETERS.LENGTH2)
    CMV[13] = cmv.lic_13(POINTS, NUMPOINTS, PARAMETERS.A_PTS, PARAMETERS.B_PTS, PARAMETERS.RADIUS1, PARAMETERS.RADIUS2)
    CMV[14] = cmv.lic_14(PARAMETERS.AREA2)

    #calculate pum
    PUM = pum.calculate_pum(LCM, CMV)

    # calculate FUV
    FUV = fuv.compute_fuv_from_pum(PUV, PUM)

    # calculate LAUNCH

    return "NO"

decide(NUMPOINTS, POINTS, PARAMETERS, LCM, PUV)