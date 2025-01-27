import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmv import *
from GLOBAL_VARS import *
from lib.util import *

class Test0(unittest.TestCase):

    def setUp(self):
        self.parameters = PARAMETERS
        self.points = []
        self.num_points = 0
    def test_basic_false(self):
        # test when points are closer than LENGTH1
        self.points = [(0, 0), (1, 0)]
        self.num_points = 2
        self.parameters.LENGTH1 = 2
        self.assertFalse(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

    def test_basic_true(self):
        # test when points are further than LENGTH1
        self.points = [(0, 0), (3, 0)]
        self.num_points = 2
        self.parameters.LENGTH1 = 2
        self.assertTrue(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

    def test_exact_length(self):
        # test when points are exactly LENGTH1 apart
        self.points = [(0, 0), (2, 0)]
        self.num_points = 2
        self.parameters.LENGTH1 = 2
        self.assertFalse(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

    def test_diagonal_distance(self):
        # test with points at diagonal distance
        self.points = [(0, 0), (2, 2)]
        self.num_points = 2
        self.parameters.LENGTH1 = 2
        self.assertTrue(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

    def test_insufficient_points(self):
        # test with less than 2 points
        self.points = [(0, 0)]
        self.num_points = 1
        self.parameters.LENGTH1 = 2
        self.assertFalse(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

    def test_multiple_points(self):
        # test with multiple points where only one pair satisfies the condition
        self.points = [(0, 0), (1, 0), (4, 0), (5, 0)]
        self.num_points = 4
        self.parameters.LENGTH1 = 2
        self.assertTrue(lic_0(self.parameters.LENGTH1, self.points, self.num_points))

class Test1(unittest.TestCase):
    # test the lic_1 function

    def setUp(self):
        # Set up the variables
        self.parameters = PARAMETERS
        self.parameters.RADIUS1 = 1.0
        self.points = []
        self.num_points = 0

    def test_1_true(self):
        # Expect True when any triple of consecutive points doesn't fit in RADIUS1
        self.points = [(0,0), (1,0), (2,2), (3,2)]
        self.num_points = 4
        self.parameters.RADIUS1 = 0.5
        self.assertTrue(lic_1(self.parameters.RADIUS1, self.points, self.num_points))

    def test_1_false(self):
        # Expect False when all triples of consecutive points fit in RADIUS1
        self.points = [(0,0), (1,0), (2,0)]
        self.num_points = 3
        self.parameters.RADIUS1 = 2.0
        self.assertFalse(lic_1(self.parameters.RADIUS1, self.points, self.num_points))

    def test_1_insufficient_points(self):
        # Expect False when fewer than 3 points (no triple possible)
        self.points = [(0,0), (1,1)]
        self.num_points = 2
        self.parameters.RADIUS1 = 5.0
        self.assertFalse(lic_1(self.parameters.RADIUS1, self.points, self.num_points))

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
    def setUp(self):
        self.points = [(1,0),(2,1),(3,3),(4,4),(6,5)]
        self.num_points = 5
        self.c_pts = 1
        self.d_pts = 1

    def test_correct(self):
        self.assertEqual(lic_9(self.points, self.num_points,self.c_pts,self.d_pts,PARAMETERS.EPSILON), True)

    def test_incorrect_c_pts(self):
        self.assertEqual(lic_9(self.points,self.num_points,0,1,PARAMETERS.EPSILON),False)
    
    def test_incorrect_d_pts(self):
        self.assertEqual(lic_9(self.points,self.num_points,1,0,PARAMETERS.EPSILON),False)
       
    def test_incorrect_num_points(self):
        self.assertEqual(lic_9(self.points,4,self.c_pts,self.d_pts,PARAMETERS.EPSILON),False)
        
    def test_incorrect_sum(self):
        self.assertEqual(lic_9(self.points,self.num_points,4,7,PARAMETERS.EPSILON),False)
    
    def test_coincident(self):
        self.points = [(1,0),(2,1),(2,0),(4,4),(1,0)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,PARAMETERS.EPSILON),False)
    
    def test_less_than_min_angle(self):
        self.points = [(1,0),(2,1),(3,3),(4,4),(2,-6)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)

    def test_greater_than_max_angle(self):
        self.points = [(100,10),(2,1),(0,0),(4,4),(-8,-9)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)

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