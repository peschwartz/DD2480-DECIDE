from GLOBAL_VARS import *

# The Conditions Met Vector (CMV) can now be used in conjunction with the Logical Connector
# Matrix (LCM) to form the Preliminary Unlocking Matrix (PUM). 
def calculate_pum(lcm, cmv):
    pum = [[None for _ in range(15)] for _ in range(15)]

    for i in range(15):
        for j in range(15): 
            
            # if LCM[i,j] is NOTUSED, then PUM[i,j] is True
            if lcm[i][j] == Connectors.NOTUSED:
                pum[i][j] = True

            # if LCM[i,j] is ANDD, then PUM[i,j] is True if CMV[i] and CMV[j] are True
            elif lcm[i][j] == Connectors.ANDD:
                pum[i][j] = cmv[i] and cmv[j]

            # if LCM[i,j] is ORR, then PUM[i,j] is True if CMV[i] or CMV[j] are True
            elif lcm[i][j] == Connectors.ORR:
                pum[i][j] = cmv[i] or cmv[j]
                
    return pum
