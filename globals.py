from enum import Enum
from typing import List, Optional

# Constants
PI = 3.141592653589793

# Enums
class Connectors(Enum):
    NOTUSED = 777
    ORR = 778
    ANDD = 779

class CompType(Enum):
    LT = 1111
    EQ = 1112
    GT = 1113

# Type aliases
Coordinate = List[float]  # Array of doubles
CMatrix = List[List[Connectors]]  # 2D array of Connectors [15][15]
BMatrix = List[List[bool]]  # 2D array of booleans [15][15]
Vector = List[bool]  # Array of 15 booleans

# Parameters structure
class Parameters:
    def __init__(self):
        self.LENGTH1: float = 0  # Length in LICs 0, 7, 12
        self.RADIUS1: float = 0  # Radius in LICs 1, 8, 13
        self.EPSILON: float = 0  # Deviation from PI in LICs 2, 9
        self.AREA1: float = 0    # Area in LICs 3, 10, 14
        self.Q_PTS: int = 0      # No. of consecutive points in LIC 4
        self.QUADS: int = 0      # No. of quadrants in LIC 4
        self.DIST: float = 0     # Distance in LIC 6
        self.N_PTS: int = 0      # No. of consecutive pts. in LIC 6
        self.K_PTS: int = 0      # No. of int. pts. in LICs 7, 12
        self.A_PTS: int = 0      # No. of int. pts. in LICs 8, 13
        self.B_PTS: int = 0      # No. of int. pts. in LICs 8, 13
        self.C_PTS: int = 0      # No. of int. pts. in LIC 9
        self.D_PTS: int = 0      # No. of int. pts. in LIC 9
        self.E_PTS: int = 0      # No. of int. pts. in LICs 10, 14
        self.F_PTS: int = 0      # No. of int. pts. in LICs 10, 14
        self.G_PTS: int = 0      # No. of int. pts. in LIC 11
        self.LENGTH2: float = 0  # Maximum length in LIC 12
        self.RADIUS2: float = 0  # Maximum radius in LIC 13
        self.AREA2: float = 0    # Maximum area in LIC 14

# Global variables
PARAMETERS: Parameters = Parameters()
X: Coordinate = []  # X coordinates of data points
Y: Coordinate = []  # Y coordinates of data points
NUMPOINTS: int = 0  # Number of data points
LCM: CMatrix = []   # Logical Connector Matrix
PUM: BMatrix = []   # Preliminary Unlocking Matrix
CMV: Vector = [None] * 15    # Conditions Met Vector
FUV: Vector = [None] * 15    # Final Unlocking Vector
LAUNCH: bool = False          # Decision: Launch or No Launch

def DOUBLECOMPARE(a: float, b: float) -> CompType:
    """Compares floating point numbers"""
    if abs(a - b) < 0.000001:
        return CompType.EQ
    return CompType.LT if a < b else CompType.GT