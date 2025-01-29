import unittest
from decide import *
from decide_io import *
from lib.util import *

class TestInputParse(unittest.TestCase):

    def setUp(self):
        # Reset global variables before each test
        reset_globals()
        read_input("./test/test_decide.in")
    
    def test_basic_parameters(self):
        self.assertEqual(gv.NUMPOINTS, 9)
        self.assertEqual(len(gv.POINTS), 9)
        self.assertEqual(gv.POINTS, [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1)])

    def test_lcm_matrix(self):
        self.assertEqual(len(gv.LCM), 15)
        self.assertEqual(len(gv.LCM[0]), 15)
        
        # Test specific LCM values
        self.assertEqual(gv.LCM[0][0], gv.Connectors.ANDD)
        self.assertEqual(gv.LCM[0][1], gv.Connectors.ANDD)
        self.assertEqual(gv.LCM[0][2], gv.Connectors.ORR)
        self.assertEqual(gv.LCM[2][0], gv.Connectors.ORR)
        self.assertEqual(gv.LCM[2][1], gv.Connectors.ORR)
        self.assertEqual(gv.LCM[2][2], gv.Connectors.ANDD)
        self.assertEqual(gv.LCM[2][3], gv.Connectors.ANDD)

    def test_puv_vector(self):
        self.assertEqual(len(gv.PUV), 15)
        self.assertEqual(gv.PUV[0], True)
        self.assertEqual(gv.PUV[1], True)
        self.assertEqual(gv.PUV[2], True)
        self.assertEqual(gv.PUV[3], False)
        self.assertEqual(gv.PUV[4], False)
        self.assertEqual(gv.PUV[5], False)

    def test_distance_parameters(self):
        self.assertEqual(gv.PARAMETERS.LENGTH1, 1)
        self.assertEqual(gv.PARAMETERS.RADIUS1, 1)
        self.assertEqual(gv.PARAMETERS.DIST, 1)
        self.assertEqual(gv.PARAMETERS.AREA1, 1)

    def test_point_count_parameters(self):
        self.assertEqual(gv.PARAMETERS.N_PTS, 3)
        self.assertEqual(gv.PARAMETERS.E_PTS, 1)
        self.assertEqual(gv.PARAMETERS.F_PTS, 1)
        self.assertEqual(gv.PARAMETERS.K_PTS, 1)

    def test_separation_parameters(self):
        self.assertEqual(gv.PARAMETERS.A_PTS, 1)
        self.assertEqual(gv.PARAMETERS.B_PTS, 1)
        self.assertEqual(gv.PARAMETERS.C_PTS, 1)
        self.assertEqual(gv.PARAMETERS.D_PTS, 1)

    def test_angle_parameters(self):
        self.assertEqual(gv.PARAMETERS.EPSILON, 1)
