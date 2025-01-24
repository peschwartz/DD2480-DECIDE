import unittest
from cmv import *
from VARIABLES import *

class TestCMV(unittest.TestCase):

    def test_0(self):
        self.assertEqual(cmv_0(.LENGTH1), False)

    def test_1(self, RADIUS1: float):
        self.assertEqual(cmv_1(RADIUS1), False)

    def test_2(self, EPSILON: float):
        self.assertEqual(cmv_2(EPSILON), False)

    def test_3(self, AREA1: float):
        self.assertEqual(cmv_3(AREA1), False)

    def test_4(self, Q_PTS: int, QUADS: int):
        self.assertEqual(cmv_4(Q_PTS, QUADS), False)

    def test_5(self, DIST: float):
        self.assertEqual(cmv_5(DIST), False)

    def test_6(self, N_PTS: int, K_PTS: int):
        self.assertEqual(cmv_6(N_PTS, K_PTS), False)

    def test_7(self, K_PTS: int):
        self.assertEqual(cmv_7(K_PTS), False)

    