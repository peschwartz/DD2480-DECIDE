import unittest
from decide import *

class TestLaunch(unittest.TestCase):
    def test_compute_launch(self):
        self.assertEqual(compute_launch([True] * 15), "YES")
        self.assertEqual(compute_launch([False] * 15), "NO")
