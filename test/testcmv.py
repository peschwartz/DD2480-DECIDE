import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmv import *
from GLOBAL_VARS import *
from lib.util import *

class Test0(unittest.TestCase):
    # test the LIC 0 function
    def setUp(self):
        self.parameters = PARAMETERS
        self.points = []
        self.num_points = 0

    def test_negative_length(self):
        # test that negative LENGTH1 raises assertion
        with self.assertRaises(AssertionError):
            lic_0(-1, [(0,0), (1,0)], 2)

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
    # test the LIC 1 function

    def setUp(self):
        # Set up the variables
        self.parameters = PARAMETERS
        self.parameters.RADIUS1 = 1.0
        self.points = []
        self.num_points = 0

    def test_negative_radius(self):
        # test that negative RADIUS1 raises assertion
        with self.assertRaises(AssertionError):
            lic_1(-1.0, [(0,0), (1,1), (2,2)], 3)

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
    # test the LIC 3 function
    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(4,0), (5,0), (0,5), (0,0)]
        self.num_points = 4
    
    def test_negative_area(self):
        # test that negative AREA1 raises assertion
        with self.assertRaises(AssertionError):
            lic_3(-1.0, self.points, self.num_points)

    def test_area(self):
        # test the triangle area function
        self.assertEqual(triangle_area(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.points[2][0], self.points[2][1]), 2.5)

    def test_correct(self):
        # should be true since the triangle area is larger than 10
        self.assertEqual(lic_3(self.area, self.points, self.num_points), True) 
    
    def test_false(self):
        # should be false since there are 3 points that do not have an area large enough
        self.assertFalse(lic_3(self.area, self.points, 3)) 
    
    def test_num_error(self):
        # should be false since there are less than 3 points
        self.assertFalse(lic_3(self.area, self.points, 2))

class Test4(unittest.TestCase):
    # test the LIC 4 function
    def setUp(self):
        self.points = [(-1,-1),(0,0),(1,1)]
        self.num_points = 3
        self.q_pts = 2
        self.quads = 3
    
    def test_invalid_q_pts(self):
        # test that invalid Q_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_4(self.points, self.num_points, 1, self.quads)
        with self.assertRaises(AssertionError):
            lic_4(self.points, self.num_points, self.num_points + 1, self.quads)

    def test_invalid_quads(self):
        # test that invalid QUADS raises assertion
        with self.assertRaises(AssertionError):
            lic_4(self.points, self.num_points, self.q_pts, 0)
        with self.assertRaises(AssertionError):
            lic_4(self.points, self.num_points, self.q_pts, 4)

    def test_false(self):
        # should be false since the points are distributed over the same amount of quadrants as QUADS
        self.q_pts = 3
        self.quads = 2
        self.assertFalse(lic_4(self.points,self.num_points, self.q_pts, self.quads))
    
    def test_correct(self):
        # should be true since the points lie in more quadrants than QUADS
        self.points = [(-1,1),(1,1),(1,-1)]
        self.q_pts = 3
        self.quads = 2
        self.assertTrue(lic_4(self.points,self.num_points, self.q_pts, self.quads))

    def test_extended_point_vec(self):
        # should be true since the set contains Q_PTS consecutive points distributed over more than QUADS
        self.points = [(-1,1),(1,1),(1,-1),(-2,-1),(2,2)]
        self.q_pts = 4
        self.num_points = 5
        self.assertTrue(lic_4(self.points,self.num_points, self.q_pts, self.quads))


class Test5(unittest.TestCase):
    # test the LIC 5 function
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
    # test the LIC 6 function
    def setUp(self):
        self.parameters = PARAMETERS
        self.parameters.N_PTS = 3
        self.parameters.DIST = 1.0
        self.points = [(0,0), (1,0), (2,0), (2,2), (3,2)]
        self.num_points = len(self.points)

    def test_invalid_n_pts(self):
        # test that invalid N_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_6(2, self.parameters.DIST, self.points, self.num_points)
        with self.assertRaises(AssertionError):
            lic_6(self.num_points + 1, self.parameters.DIST, self.points, self.num_points)

    def test_negative_dist(self):
        # test that negative DIST raises assertion
        with self.assertRaises(AssertionError):
            lic_6(self.parameters.N_PTS, -1.0, self.points, self.num_points)

    def test_6_true(self):
        # A point (2,6) is farther than DIST=1 from the line joining (0,0) to (2,0), so returns True.
        self.points = [(0,0), (1,0), (2,0), (2,6), (3,5)]
        self.num_points = len(self.points)
        self.assertTrue(
            lic_6(self.parameters.N_PTS, 
                  self.parameters.DIST, 
                  self.points, 
                  self.num_points)
        )

    def test_6_false(self):
        # DIST is set to 5, and no point is farther than this from the relevant line, so returns False.
        self.parameters.DIST = 5.0
        self.parameters.DIST = 5.0
        self.assertFalse(
            lic_6(self.parameters.N_PTS, 
                  self.parameters.DIST, 
                  self.points, 
                  self.num_points)
        )

    def test_6_too_few_points(self):
        # test that too few points raises assertion
        fewer_points = [(0,0), (1,1)]
        with self.assertRaises(AssertionError):
            lic_6(3, self.parameters.DIST, fewer_points, len(fewer_points))

    def test_6_identical_endpoints_true(self):
        # First and last points are identical, and (1,1) is farther than DIST=0.5, so returns True.
        pts = [(0,0), (1,1), (0,0)]
        self.assertTrue(
            lic_6(3, 0.5, pts, len(pts))
        )

    def test_6_identical_endpoints_false(self):
        # All points are identical, meaning all distances are zero, so returns False.
        pts = [(1,1), (1,1), (1,1)]
        self.assertFalse(
            lic_6(3, 0.5, pts, len(pts))
        )


class Test7(unittest.TestCase):
    # test the LIC 7 function
    def test_invalid_k_pts(self):
        # test that invalid K_PTS raises assertion
        points = [(0,0),(1,0),(2,0),(3,0)]
        with self.assertRaises(AssertionError):
            lic_7(points, 0, 2, 4)
        with self.assertRaises(AssertionError):
            lic_7(points, 3, 2, 4)

    def test_negative_length(self):
        # test that negative LENGTH1 raises assertion
        points = [(0,0),(1,0),(2,0),(3,0)]
        with self.assertRaises(AssertionError):
            lic_7(points, 1, -1, 4)

    def test_valid_minimum_sequence(self):
        # should be true since distance is 3 is greater than LENGTH1
        self.assertTrue(lic_7([(0,0),(1,0),(2,0),(3,0)],2,2,4))

    def test_invalid_sequence_length1_to_short(self):
        # should be false since the distance between both (-1,-1) and (-1,0), respectively (-3,4) and (-4,3) is less than 2
        self.assertFalse(lic_7([(-3,4), (-1,-1), (0,0), (-4,3), (-1,0)], 2, 2, 5))

    def test_valid_sequence(self):
        # should be true since the distance between (-3,4) and (1,0) is greater than 3
        self.assertTrue(lic_7([(-3,4), (-1,-1), (0,0), (1,0), (1,1)], 2, 3, 5))

class Test8(unittest.TestCase):
    # test the LIC 8 function
    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(1,2), (1,4), (2,2), (2,4), (6,3)]
        self.num_points = 5
        self.a_pts = 1
        self.b_pts = 1
        self.radius = 2.0

    def test_invalid_a_pts(self):
        # test that invalid A_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, self.num_points, 0, self.b_pts, self.radius)

    def test_invalid_b_pts(self):
        # test that invalid B_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, self.num_points, self.a_pts, 0, self.radius)

    def test_invalid_points_constraint(self):
        # test that invalid A_PTS + B_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, self.num_points, 2, 2, self.radius)

    def test_negative_radius(self):
        # test that negative RADIUS1 raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, self.num_points, self.a_pts, self.b_pts, -1.0)

    def test_correct(self):
        # should be true since there are 3 points that do not fit in the circle
        self.assertEqual(lic_8(self.points, self.num_points, self.a_pts, self.b_pts, self.radius), True) 
    
    def test_false(self):
        # should be false since all points fit in the radius circle
        self.assertFalse(lic_8(self.points, self.num_points, self.a_pts, self.b_pts, 5.0))

    def test_num_error(self):
        # test that invalid number of points raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, self.num_points, 2, 2, self.radius)

    def test_total_num_error(self):
        # test that invalid total number of points raises assertion
        with self.assertRaises(AssertionError):
            lic_8(self.points, 4, self.a_pts, self.b_pts, self.radius)

class Test9(unittest.TestCase):
    # test the LIC 9 function
    def setUp(self):
        # set up the variables
        self.points = [(1,0),(1,2),(3,3),(1,4),(6,5)]
        self.num_points = 5
        self.c_pts = 1
        self.d_pts = 1

    def test_correct(self):
        # should be false since the angle is within the range [PI-EPSILON, PI+EPSILON]
        self.assertEqual(lic_9(self.points, self.num_points,self.c_pts,self.d_pts,1), False)

    def test_invalid_c_pts(self):
        # test that invalid C_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_9(self.points, self.num_points, 0, self.d_pts, 1)

    def test_invalid_d_pts(self):
        # test that invalid D_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_9(self.points, self.num_points, self.c_pts, 0, 1)
       
    def test_invalid_points_constraint(self):
        # test that invalid C_PTS + D_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_9(self.points, self.num_points, 2, 2, 1)
        
    def test_incorrect_num_points(self):
        # test that incorrect number of points raises assertion
        with self.assertRaises(AssertionError):
            lic_9(self.points, 4, self.c_pts, self.d_pts, 1)
        
    def test_incorrect_sum(self):
        # test that incorrect sum of points raises assertion
        with self.assertRaises(AssertionError):
            lic_9(self.points, self.num_points, 4, 7, 1)
    
    def test_coincident(self):
        # should be false since a triangle only can be created with 3 non-coincident points
        self.points = [(1,0),(1,1),(2,0),(2,2),(1,0)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1),False)
    
    def test_less_than_min_angle(self):
        # should be true since the angle is less than the min angle
        self.points = [(1,0),(2,1),(0,0),(4,4),(-1,-6)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)

    def test_greater_than_max_angle(self):
        # should be true since the angle is greater than the max angle
        self.points = [(10,0),(2,1),(0,0),(4,4),(0,10)]
        self.assertEqual(lic_9(self.points,self.num_points,self.c_pts,self.d_pts,1.0),True)
    
    def test_wrong_c_pts(self):
        # test that wrong C_PTS raises assertion
        self.c_pts = 2
        with self.assertRaises(AssertionError):
            lic_9(self.points, self.num_points, self.c_pts, self.d_pts, 1.0) 

class Test10(unittest.TestCase):
    # test the LIC 10 function
    def setUp(self):
        self.points = [(0,0), (1,1), (10,10), (5,0), (0,10)]
        self.num_points = 5
        self.e_pts = 1
        self.f_pts = 1
        self.area = 10

    def test_invalid_e_pts(self):
        # test that invalid E_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_10(0, 1, 10, self.points, 5)

    def test_invalid_f_pts(self):
        # test that invalid F_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_10(1, 0, 10, self.points, 5)

    def test_invalid_points_constraint(self):
        # test that invalid E_PTS + F_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_10(2, 2, 10, self.points, 5)

    def test_negative_area(self):
        # test that negative AREA1 raises assertion
        with self.assertRaises(AssertionError):
            lic_10(1, 1, -1, self.points, 5)

    def test_valid_triangle(self):
        # points at indices 0, 2, 4 form a triangle with area > 10
        self.points = [(0,0), (1,1), (10,10), (5,0), (0,10)]
        self.num_points = 6
        self.area = 10
        self.e_pts = 1
        self.f_pts = 1
        self.assertTrue(lic_10(self.e_pts, self.f_pts, self.area, self.points, self.num_points))
    
    def test_insufficient_points(self):
        # test that insufficient points raises assertion
        small_points = [(0,0), (1,1), (2,2), (3,3)]
        with self.assertRaises(AssertionError):
            lic_10(self.e_pts, self.f_pts, self.area, small_points, 4)
    
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
    # test the LIC 11 function
    def setUp(self):
        self.parameters = PARAMETERS
        self.parameters.G_PTS = 1
        self.points = [(0,0), (1,0), (2,0), (1,0)]
        self.num_points = len(self.points)

    def test_invalid_g_pts(self):
        # test that invalid G_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_11(0, self.points, 4)
        with self.assertRaises(AssertionError):
            lic_11(3, self.points, 4)

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
        # test that too few points raises assertion
        few_points = [(1,0), (2,0)]
        with self.assertRaises(AssertionError):
            lic_11(self.parameters.G_PTS, few_points, len(few_points))

class Test12(unittest.TestCase):
    # test the LIC 12 function
    def test_invalid_k_pts(self):
        # test that invalid K_PTS raises assertion
        points = [(0,0), (1,0), (2,0)]
        with self.assertRaises(AssertionError):
            lic_12(points, 0, 1, 3, 3)
        with self.assertRaises(AssertionError):
            lic_12(points, 2, 1, 3, 3)

    def test_negative_length1(self):
        # test that negative LENGTH1 raises assertion
        points = [(0,0), (1,0), (2,0)]
        with self.assertRaises(AssertionError):
            lic_12(points, 1, -1, 3, 3)

    def test_negative_length2(self):
        # test that negative LENGTH2 raises assertion
        points = [(0,0), (1,0), (2,0)]
        with self.assertRaises(AssertionError):
            lic_12(points, 1, 1, -1, 3)

    def test_valid_min_sequence(self):
        # should be true since the distance between (0,0) and (2,0) is greater than 1 but less than 2
        self.assertTrue(lic_12([(0,0), (1,0), (2,0)],1,1,3,3))

    def test_invalid_sequence_length1_to_long(self):
        # should be false since the distance between the two pairs of points are greater than LENGTH1
        self.assertFalse(lic_12([(-3,4), (-1,-1), (0,0), (1,0), (1,1)], 2, 6, 3, 5))

    def test_invalid_sequence_length2_to_short(self):
        # should be false since both of the two pairs of points are separated by a distance greater than LENGTH2
        self.assertFalse(lic_12([(-3,4), (-1,-1), (0,0), (1,0), (1,1)], 2, 5, 2, 5))

    def test_valid_sequence(self):
        # should be true since since the second pair of points are separated by a distance less than LENGTH2
        self.assertTrue(lic_12([(-3,4), (-1,-1), (0,0), (1,0), (1,1)], 2, 5, 3, 5))

class Test13(unittest.TestCase):
    # test the LIC 13 function
    def setUp(self):
        # set up the variables 
        self.area = 10
        self.points = [(1,2), (1,4), (2,2), (2,4), (6,3), (5,5)]
        self.num_points = 5
        self.a_pts = 1
        self.b_pts = 1
        self.radius1 = 2.0
        self.radius2 = 4.0

    def test_invalid_a_pts(self):
        # test that invalid A_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, 0, self.b_pts, self.radius1, self.radius2)

    def test_invalid_b_pts(self):
        # test that invalid B_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, self.a_pts, 0, self.radius1, self.radius2)

    def test_invalid_points_constraint(self):
        # test that invalid A_PTS + B_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, 2, 2, self.radius1, self.radius2)

    def test_negative_radius1(self):
        # test that negative RADIUS1 raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, self.a_pts, self.b_pts, -1.0, self.radius2)

    def test_negative_radius2(self):
        # test that negative RADIUS2 raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, self.a_pts, self.b_pts, self.radius1, -1.0)

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

    def test_num_error(self):
        # test that insufficient points raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, 4, self.a_pts, self.b_pts, self.radius1, self.radius2)

    def test_total_num_error(self):
        # test that invalid point separation raises assertion
        with self.assertRaises(AssertionError):
            lic_13(self.points, self.num_points, 2, 2, self.radius1, self.radius2)
    

class Test14(unittest.TestCase):
    # test the LIC 14 function
    def setUp(self):
        # setup initial variables
        self.points = [(1,1),(2,2),(3,3),(4,4),(5,5)]
        self.num_points = 5
        self.e_pts = 1
        self.f_pts = 1
        self.area1 = 1.0
        self.area2 = 2.0
    
    def test_invalid_e_pts(self):
        # test that invalid E_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_14(self.points, self.num_points, 0, self.f_pts, self.area1, self.area2)

    def test_invalid_f_pts(self):
        # test that invalid F_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_14(self.points, self.num_points, self.e_pts, 0, self.area1, self.area2)

    def test_invalid_points_constraint(self):
        # test that invalid E_PTS + F_PTS raises assertion
        with self.assertRaises(AssertionError):
            lic_14(self.points, self.num_points, 2, 2, self.area1, self.area2)

    def test_negative_area1(self):
        # test that negative AREA1 raises assertion
        with self.assertRaises(AssertionError):
            lic_14(self.points, self.num_points, self.e_pts, self.f_pts, -1.0, self.area2)

    def test_negative_area2(self):
        # test that negative AREA2 raises assertion
        with self.assertRaises(AssertionError):
            lic_14(self.points, self.num_points, self.e_pts, self.f_pts, self.area1, -1.0)

    def test_correct(self):
        # should return true since these points generate a triangle with an area of 1.5 area units
        self.points = [(1,2),(2,2),(3,5),(4,4),(4,8)]
        self.assertTrue(lic_14(self.points,self.num_points,self.e_pts,self.f_pts,self.area1, self.area2))
    
    def test_correct_area1_false_area2(self):
        # testing if the function returns False for an area greater than both AREA1 and AREA2
        self.points = [(1,2),(2,2),(3,5),(4,4),(4,9)]
        self.assertFalse(lic_14(self.points,self.num_points,self.e_pts,self.f_pts,self.area1, self.area2))

    def test_larger_points_vec(self):
        # should return True since the second three points generates a triangle with an area less than AREA2
        self.points = [(1,2),(2,2),(3,5),(4,4),(4,9),(8,7)]
        self.num_points = 6
        self.assertTrue(lic_14(self.points,self.num_points,self.e_pts,self.f_pts,self.area1,self.area2))

    def test_larger_points_vec_first_points(self):
        # should return true since the condition is met for the first set of points
        self.points = [(1,2),(2,2),(3,5),(4,4),(4,8),(11,8)]
        self.num_points = 6
        self.assertTrue(lic_14(self.points,self.num_points,self.e_pts,self.f_pts,self.area1,self.area2))
