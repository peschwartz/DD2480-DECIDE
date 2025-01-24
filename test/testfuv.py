import unittest
from fuv import *
from GLOBAL_VARS import *

class TestFUV(unittest.TestCase):
    def test_compute_fuv(self):
        self.assertEqual(compute_fuv([False] * 15, [False] * 15), [False] * 15)