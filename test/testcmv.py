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

    # TESTS FOR LIC 2
    def test_20(self):
        # Point 1 and/or 2 coincides
        self.assertEqual(lic_2([(1,0), (0,2), (0,2)], 2, math.pi), False)

    def test_21(self):
        # A set of three points with an angle that should be valid
        self.assertEqual(lic_2([(2,0), (0,0), (1,1)], math.pi / 2, math.pi), True)

    def test_22(self):
        # A set of three points with an angle that should NOT be valid
        self.assertEqual(lic_2([(-1,1), (0,0), (2,1)], math.pi / 2, math.pi), False)

    def test_23(self):
        # A set which contain three point that have a valid angle but are not consecutive
        self.assertEqual(lic_2([(-1,1), (0,0), (2,1), (4,2)], math.pi / 2, math.pi), False)

    def test_get_angle_1(self):
        # Two linearly dependent points
        self.assertEqual(get_angle((2,1), (0,0), (4,2)), 2 * math.pi)

    def test_get_angle_2(self):
        # Two linearly dependent points on opposite side of the origin
        self.assertEqual(get_angle((2,1), (0,0), (-2,-1)), math.pi)

    def test_get_angle_3(self):
        # Correct angle between two points in the first quadrant
        angle = get_angle((1/2, math.sqrt(3) / 2), (0,0), (math.sqrt(3) / 2, 1/2))
        self.assertTrue(0.5 < angle and angle < 0.55)

    def test_get_angle_4(self):
        # Correct angle when vertex is not at origin
        angle = get_angle((1/2 + 1, math.sqrt(3) / 2 + 2), (1, 2), (math.sqrt(3) / 2 + 1, 1/2 + 2))
        self.assertTrue(0.5 < angle and angle < 0.55)

    def test_get_angle_5(self):
        # Correct angle when vertex is not at origin
        angle = get_angle((math.sqrt(3) / 2, 1/2), (0,0), (1/2, math.sqrt(3) / 2))
        self.assertTrue(5.7 < angle and angle < 5.8)

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
        # should be false since the area is 0
        self.assertFalse(lic_3(0, self.points, self.num_points))
    
    def test_num_error(self):
        # should be false since there are less than 3 points
        self.assertFalse(lic_3(self.area, self.points, 2))


class Test4(unittest.TestCase):
    def test_4(self):
        self.assertEqual(lic_4(PARAMETERS.Q_PTS, PARAMETERS.QUADS), False)

class Test5(unittest.TestCase):
    def setUp(self):
        # reset points before each test
        self.points = []
        self.num_points = 0

    def test_basic_true(self):
        # test when there are two consecutive points where second X is less than first X
        self.points = [(1, 0), (0, 0)]  # second X less than first X
        self.num_points = 2
        self.assertTrue(lic_5(self.points, self.num_points))

    def test_basic_false(self):
        # test when points are in increasing X order
        self.points = [(0, 0), (1, 0), (2, 0)]
        self.num_points = 3
        self.assertFalse(lic_5(self.points, self.num_points))

    def test_equal_x(self):
        # test when consecutive points have equal X coordinates
        self.points = [(1, 0), (1, 0)]
        self.num_points = 2
        self.assertFalse(lic_5(self.points, self.num_points))

    def test_multiple_points_true(self):
        # test with multiple points where one pair satisfies the condition
        self.points = [(0, 0), (1, 0), (2, 0), (1, 0)]  # last pair satisfies X[j] - X[i] < 0
        self.num_points = 4
        self.assertTrue(lic_5(self.points, self.num_points))

    def test_insufficient_points(self):
        # test with less than 2 points
        self.points = [(1, 0)]
        self.num_points = 1
        self.assertFalse(lic_5(self.points, self.num_points))

class Test6(unittest.TestCase):
    def setUp(self):
        self.parameters = PARAMETERS
        self.parameters.N_PTS = 3
        self.parameters.DIST = 1.0
        self.points = [(0,0), (1,0), (2,0), (2,2), (3,2)]
        self.num_points = len(self.points)

    def test_6_true(self):
        self.points = [(0,0), (1,0), (2,0), (2,6), (3,5)]
        self.num_points = len(self.points)
        self.assertTrue(
            lic_6(self.parameters.N_PTS, 
                  self.parameters.DIST, 
                  self.points, 
                  self.num_points)
        )

    def test_6_false(self):
        self.parameters.DIST = 5.0
        self.assertFalse(
            lic_6(self.parameters.N_PTS, 
                  self.parameters.DIST, 
                  self.points, 
                  self.num_points)
        )

    def test_6_too_few_points(self):
        fewer_points = [(0,0), (1,1)]
        self.assertFalse(
            lic_6(self.parameters.N_PTS, 
                  self.parameters.DIST, 
                  fewer_points, 
                  len(fewer_points))
        )

    def test_6_identical_endpoints_true(self):
        pts = [(0,0), (1,1), (0,0)]
        self.assertTrue(
            lic_6(3, 0.5, pts, len(pts))
        )

    def test_6_identical_endpoints_false(self):
        pts = [(1,1), (1,1), (1,1)]
        self.assertFalse(
            lic_6(3, 0.5, pts, len(pts))
        )


class Test7(unittest.TestCase):
    def test_negative_length2_raise_error(self):
        with self.assertRaises(AssertionError):
            lic_7([(3,3),(0,0)], 0, 3, 2)

    def test_invalid_sequence_length1_to_short(self):
        self.assertFalse(lic_7([(-3,4), (-1,-1), (0,0), (-4,3), (-1,0)], 2, 2, 5))

    def test_valid_sequence(self):
        self.assertTrue(lic_7([(-3,4), (-1,-1), (0,0), (1,0), (1,1)], 2, 3, 5))

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
        # should be false since the a_pts is 0
        self.assertFalse(lic_8(self.points, self.num_points, 0, self.b_pts, self.radius))

    def test_b_error(self):
        # should be false since the b_pts is 0
        self.assertFalse(lic_8(self.points, self.num_points, self.a_pts, 0, self.radius))
    
    def test_num_error(self):
        # should be false since a_pts + b_pts is greater than num_points (5) - 3
        self.assertFalse(lic_8(self.points, self.num_points, 2, 2, self.radius))
    
    def test_total_num_error(self):
        # should be false since a_pts + b_pts is greater than num_points (5) - 3
        self.assertFalse(lic_8(self.points, 4, self.a_pts, self.b_pts, self.radius))

class Test9(unittest.TestCase):
    # test the LIC 9 function
    def setUp(self):
        # set up the variables
        self.points = [(1,0),(1,2),(3,3),(1,4),(6,5)]
        self.num_points = 5
        self.c_pts = 1
        self.d_pts = 1

    def test_correct(self):
        self.assertEqual(lic_9(self.points, self.num_points,self.c_pts,self.d_pts,PARAMETERS.EPSILON), True)

    def test_incorrect_c_pts(self):
        # should be false since C_PTS < 1
        self.assertEqual(lic_9(self.points,self.num_points,0,1,PARAMETERS.EPSILON),False)
    
    def test_incorrect_d_pts(self):
        # should be false since D_PTS < 1
        self.assertEqual(lic_9(self.points,self.num_points,1,0,PARAMETERS.EPSILON),False)
       
    def test_incorrect_num_points(self):
        # should be false since NUMPOINTS < 5
        self.assertEqual(lic_9(self.points,4,self.c_pts,self.d_pts,PARAMETERS.EPSILON),False)
        
    def test_incorrect_sum(self):
        # should be false since C_PTS + D_PTS > NUMPOINTS - 3
        self.assertEqual(lic_9(self.points,self.num_points,4,7,PARAMETERS.EPSILON),False)
    
    def test_coincident(self):
        # should be false since a triangle only can be created with 3 non-coincident points
        self.points = [(1,0),(1,1),(2,0),(2,2),(1,0)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,PARAMETERS.EPSILON),False)
    
    def test_less_than_min_angle(self):
        # should be true since the angle is less than the min angle
        self.points = [(1,0),(2,1),(0,0),(4,4),(-1,-6)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)

    def test_greater_than_max_angle(self):
        # should be true since the angle is greater than the max angle
        self.points = [(10,0),(2,1),(0,0),(4,4),(0,10)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)
    
    def test_wrong_c_pts(self):
        # should be false since there are not 2 consecutive intervening points between p1 and p2
        self.c_pts = 2
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),False) 

class Test10(unittest.TestCase):
    def test_valid_triangle(self):
        # points at indices 0, 2, 4 form a triangle with area > 10
        self.points = [(0,0), (1,1), (10,10), (5,0), (0,10)]
        self.num_points = 6
        self.area = 10
        self.e_pts = 1
        self.f_pts = 1
        self.assertTrue(lic_10(self.e_pts, self.f_pts, self.area, self.points, self.num_points))
    
    def test_insufficient_points(self):
        # test with less than 5 points
        small_points = [(0,0), (1,1), (2,2), (3,3)]
        self.points = small_points
        self.num_points = 4
        self.area = 1
        self.e_pts = 1
        self.f_pts = 1
        self.assertFalse(lic_10(self.e_pts, self.f_pts, self.area, self.points, self.num_points))
    
    def test_no_valid_triangle(self):
        # points that don't form a triangle with area > 10
        small_triangle = [(0,0), (1,0), (2,0), (1,1), (0,1)]
        self.points = small_triangle
        self.num_points = 5
        self.area = 10
        self.e_pts = 1
        self.f_pts = 1
        self.assertFalse(lic_10(self.e_pts, self.f_pts, self.area, self.points, self.num_points))

class Test11(unittest.TestCase):
    def setUp(self):
        self.parameters = PARAMETERS
        self.parameters.G_PTS = 1
        self.points = [(0,0), (1,0), (2,0), (1,0)]
        self.num_points = len(self.points)

    def test_11_true(self):
        # let's modify points so we do get a negative
        self.points = [(2,0), (3,0), (1,0)]
        self.num_points = 3
        self.assertTrue(
            lic_11(self.parameters.G_PTS, self.points, self.num_points)
        )

    def test_11_false(self):
        # test when no pair has X[j]<X[i]
        self.points = [(0,0), (1,1), (2,2), (5,0)]
        self.num_points = 4
        # All x-coords are increasing or same, so should be False
        self.assertFalse(
            lic_11(self.parameters.G_PTS, self.points, self.num_points)
        )

    def test_11_too_few_points(self):
        # test with fewer than 3 points
        few_points = [(1,0), (2,0)]
        self.assertFalse(
            lic_11(self.parameters.G_PTS, few_points, len(few_points))
        )

class Test12(unittest.TestCase):
    def test_12(self):
        self.assertEqual(lic_12(PARAMETERS.LENGTH2), False)

class Test13(unittest.TestCase):
    # test the LIC13 function
    
    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(1,2), (1,4), (2,2), (2,4), (6,3), (5,5)]
        self.num_points = 5
        self.a_pts = 1
        self.b_pts = 1
        self.radius1 = 2.0
        self.radius2 = 4.0

    def test_true(self):
        # should be true since there are 3 pts that do not fit in radius1 and 3 pts that fit in radius2
        self.assertTrue(lic_13(self.points, self.num_points, self.a_pts, self.b_pts, self.radius1, self.radius2))
    
    def test_more_true(self):
        # should be true since there are 3 pts that do not fit in radius1 and 3 pts that fit in radius2 from more points
        self.num_points = 6
        self.assertTrue(lic_13(self.points, self.num_points, self.a_pts, self.b_pts, self.radius1, self.radius2))
    
    def test_false(self):
        # should be false since all points fit in the radius1 circle
        self.radius1 = 4.0
        self.assertFalse(lic_13(self.points, self.num_points, self.a_pts, self.b_pts, self.radius1, self.radius2))

    def test_false2(self):
        # should be false since all points do not fit in the radius2 circle
        self.radius2 = 2.0
        self.assertFalse(lic_13(self.points, self.num_points, self.a_pts, self.b_pts, self.radius1, self.radius2))

    def test_a_error(self):
        # should be false since the a_pts is 0
        self.assertFalse(lic_13(self.points, self.num_points, 0, self.b_pts, self.radius1, self.radius2))

    def test_b_error(self):
        # should be false since the b_pts is 0
        self.assertFalse(lic_13(self.points, self.num_points, self.a_pts, 0, self.radius1, self.radius2))

    def test_num_error(self):
        # should be false since the number of points is less than 5
        self.assertFalse(lic_13(self.points, 4, self.a_pts, self.b_pts, self.radius1, self.radius2))

    def test_total_num_error(self):
        # should be false since a_pts + b_pts is greater than num_points (5) - 3
        self.assertFalse(lic_13(self.points, self.num_points, 2, 2, self.radius1, self.radius2))
    

class Test14(unittest.TestCase):
    def test_14(self):
        self.assertEqual(lic_14(PARAMETERS.AREA2), False)
