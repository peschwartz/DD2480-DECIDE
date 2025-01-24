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

    def test_2(self):
        self.assertEqual(lic_2(PARAMETERS.EPSILON), False)

    def test_3(self):
        PARAMETERS.AREA1 = 10
        POINTS = [(4,0), (5,0), (0,5), (0,0)]
        NUMPOINTS = 4
        self.assertEqual(lic_3(PARAMETERS.AREA1, POINTS, NUMPOINTS), True)

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