# PARAMETERS CLASS needs all of these
# double LENGTH1; // Length in LICs 0 , 7 , 12
# double RADIUS1 ; // Radius in LICs 1 , 8 , 13
# double EPSILON ; // Deviation from PI in LICs 2 , 9
# double AREA1; // Area in LICs 3 , 1 0 , 14
# int Q_PTS ; // No. of consecutive points in LIC 4
# int QUADS; // No. of quadrants in LIC 4
# double DIST ; // Distance in LIC 6
# int N_PTS ; // No .of consecutive pts. in LIC 6
# int K_PTS ; // No. of int. pts. in LICs 7 , 12
# int A_PTS ; // No. of int. pts. in LICs 8 , 13
# int B_PTS ; // No. of int. pts. in LICs 8 , 13
# int C_PTS ; // No. of int. pts. in LIC 9
# int D_PTS ; // No. of int. pts. in LIC 9
# int E_PTS ; // No. of int. pts. in LICs 10 , 14
# int F_PTS ; // No. of int. pts. in LICs 10 , 14
# int G_PTS ; // No. of int. pts. in LIC 11
# double LENGTH2; // Maximum length in LIC 12
# double RADIUS2 ; // Maximum radius in LIC 13
# double AREA2; // Maximum area in LIC 14

# decide function goes here, takes in all parameters from PARAMETERS CLASS
# global variables available
# NUMPOINTS - number of planar data points
# POINTS - array of the coordinates of data points
# PARAMETERS - object with parameters, struct holding parameters for LICs
# LCM - Logical connector Matrix
# PUV - preliminary unlocking vector

# launch decision function returns YES OR NO
# launch based on every element of FUV = TRUE