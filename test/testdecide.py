import unittest
from decide import *
from GLOBAL_VARS import *
from decide_io import *


class TestDecide(unittest.TestCase):
    
    # test the decide_io.py file
    def test_read_input(self):
        read_input("./test/test_decide.in")
        print(NUMPOINTS)

        self.assertEqual(NUMPOINTS, 9)

        self.assertEqual(PARAMETERS.E_PTS, 1)

    # def test_compute_launch(self):
        # self.assertEqual(compute_launch([True] * 15), "YES")
