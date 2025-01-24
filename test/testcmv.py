import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmv import *
from GLOBAL_VARS import *

class TestCMV(unittest.TestCase):

    def test_0(self):
        self.assertEqual(lic_0(PARAMETERS.LENGTH1), False)

    def test_1(self):
        self.assertEqual(lic_1(PARAMETERS.RADIUS1), False)

    # TESTS FOR LIC 2
    def test_20(self):
        # Point 1 and/or 2 coincides
        self.assertEqual(lic_2([(1,0), (0,2), (0,2)], 2, math.pi), False)

    def test_21(self):
        # A set of three points with an angle that should be valid
        self.assertEqual(lic_2([(2,0), (0,0), (1,1)], math.pi / 2, math.pi), True)

    def test_22(self):
        # A set of three points with an angle that should NOT be valid
        self.assertEqual(lic_2([(-1,1), (0,0), (2,1), ()], math.pi / 2, math.pi), False)

    def test_23(self):
        # A set which contain three point that have a valid angle but are not consecutive
        self.assertEqual(lic_2([(-1,1), (0,0), (2,1), (4,2)], math.pi / 2, math.pi), False)

    # TESTS FOR LIC 3, etc...
    def test_3(self):
        self.assertEqual(lic_3(PARAMETERS.AREA1), False)

    def test_4(self):
        self.assertEqual(lic_4(PARAMETERS.Q_PTS, PARAMETERS.QUADS), False)

    def test_5(self):
        self.assertEqual(lic_5(PARAMETERS.DIST), False)

    def test_6(self):
        self.assertEqual(lic_6(PARAMETERS.N_PTS, PARAMETERS.K_PTS), False)

    def test_7(self):
        self.assertEqual(lic_7(PARAMETERS.K_PTS), False)

    def test_8(self):
        self.assertEqual(lic_8(PARAMETERS.A_PTS, PARAMETERS.B_PTS), False)

    def test_9(self):
        self.assertEqual(lic_9(PARAMETERS.C_PTS, PARAMETERS.D_PTS), False)

    def test_10(self):
        self.assertEqual(lic_10(PARAMETERS.E_PTS, PARAMETERS.F_PTS), False)

    def test_11(self):
        self.assertEqual(lic_11(PARAMETERS.G_PTS), False)

    def test_12(self):
        self.assertEqual(lic_12(PARAMETERS.LENGTH2), False)

    def test_13(self):
        self.assertEqual(lic_13(PARAMETERS.RADIUS2), False)

    def test_14(self):
        self.assertEqual(lic_14(PARAMETERS.AREA2), False)
