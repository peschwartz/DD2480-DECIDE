import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmv import *
from GLOBAL_VARS import *
from lib.util import *

class Test0(unittest.TestCase):

    def test_0(self):
        self.assertEqual(lic_0(PARAMETERS.LENGTH1), False)

class Test1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lic_1(PARAMETERS.RADIUS1), False)

class Test2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(lic_2(PARAMETERS.EPSILON), False)

class Test3(unittest.TestCase):
    # test the lic_3 function

    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(4,0), (5,0), (0,5), (0,0)]
        self.num_points = 4
    
    def test_area(self):
        # test the triangle area function
        self.assertEqual(triangle_area(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.points[2][0], self.points[2][1]), 2.5)

    def test_correct(self):
        # should be true since the triangle area is larger than 10
        self.assertEqual(lic_3(self.area, self.points, self.num_points), True) 
    
    def test_false(self):
        # should be false since there are 3 points that do not have an area large enough
        self.assertFalse(lic_3(self.area, self.points, 3)) 
    
    def test_error(self):
        # should raise a ValueError since the area is 0
        try:
            lic_3(0, self.points, self.num_points) 
        except ValueError as e:
            self.assertEqual(str(e), "AREA1 must be greater than 0")
    
    def test_num_error(self):
        # should raise a ValueError there are less than 3 points
        try:
            lic_3(self.area, self.points, 2)
        except ValueError as e:
            self.assertEqual(str(e), "NUMPOINTS must be greater than 3")


class Test4(unittest.TestCase):
    def test_4(self):
        self.assertEqual(lic_4(PARAMETERS.Q_PTS, PARAMETERS.QUADS), False)

class Test5(unittest.TestCase):
    def test_5(self):
        self.assertEqual(lic_5(PARAMETERS.DIST), False)

class Test6(unittest.TestCase):
    def test_6(self):
        self.assertEqual(lic_6(PARAMETERS.N_PTS, PARAMETERS.K_PTS), False)

class Test7(unittest.TestCase):
    def test_7(self):
        self.assertEqual(lic_7(PARAMETERS.K_PTS), False)

class Test8(unittest.TestCase):
    # test the LIC8 function

    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(1,2), (1,4), (2,2), (2,4), (6,3)]
        self.num_points = 5
        self.a_pts = 1
        self.b_pts = 1
        self.radius = 2.0

    def test_correct(self):
        # should be true since there are 3 points that do not fit in the circle
        self.assertEqual(lic_8(self.points, self.num_points, self.a_pts, self.b_pts, self.radius), True) 
    
    def test_false(self):
        # should be false since all points fit in the radius circle
        self.assertFalse(lic_8(self.points, self.num_points, self.a_pts, self.b_pts, 5.0))

    def test_a_error(self):
        # should raise a ValueError since the a_pts is 0
        try:
            lic_8(self.points, self.num_points, 0, self.b_pts, self.radius)
        except ValueError as e:
            self.assertEqual(str(e), "A_PTS must be greater than 0")

    def test_b_error(self):
        # should raise a ValueError since the b_pts is 0
        try:
            lic_8(self.points, self.num_points, self.a_pts, 0, self.radius)
        except ValueError as e:
            self.assertEqual(str(e), "B_PTS must be greater than 0")
    
    def test_num_error(self):
        # should raise a ValueError since a_pts + b_pts is greater than num_points (5) - 3
        try:
            lic_8(self.points, self.num_points, 2, 2, self.radius)
        except ValueError as e:
            self.assertEqual(str(e), "A_PTS + B_PTS must be less than NUMPOINTS - 3")
    
    def test_total_num_error(self):
        # should raise a ValueError since a_pts + b_pts is greater than num_points (5) - 3
        try:
            lic_8(self.points, 4, self.a_pts, self.b_pts, self.radius)
        except ValueError as e:
            self.assertEqual(str(e), "NUMPOINTS must be greater than 5")

class Test9(unittest.TestCase):
    def test_9(self):
        self.assertEqual(lic_9(PARAMETERS.C_PTS, PARAMETERS.D_PTS), False)

class Test10(unittest.TestCase):
    def test_10(self):
        self.assertEqual(lic_10(PARAMETERS.E_PTS, PARAMETERS.F_PTS), False)

class Test11(unittest.TestCase):
    def test_11(self):
        self.assertEqual(lic_11(PARAMETERS.G_PTS), False)

class Test12(unittest.TestCase):
    def test_12(self):
        self.assertEqual(lic_12(PARAMETERS.LENGTH2), False)

class Test13(unittest.TestCase):
    def test_13(self):
        self.assertEqual(lic_13(PARAMETERS.RADIUS2), False)

class Test14(unittest.TestCase):
    def test_14(self):
        self.assertEqual(lic_14(PARAMETERS.AREA2), False)