import unittest
from decide import *

class TestLaunch(unittest.TestCase):
    def test_compute_launch_true(self):
        self.assertEqual(compute_launch([True] * 15), "YES")
    
    def test_compute_launch_false(self):
        self.assertEqual(compute_launch([False] * 15), "NO")
    
    def test_compute_launch_mixed1(self):
        self.assertEqual(compute_launch([True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]), "NO")
    
    def test_compute_launch_mixed2(self):
        self.assertEqual(compute_launch([False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]), "NO")
