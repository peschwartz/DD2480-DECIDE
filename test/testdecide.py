import unittest
from decide import *
from GLOBAL_VARS import *
from decide_io import *


class TestDecide(unittest.TestCase):

    def setUp(self):
        # Reset global variables before each test
        gv.reset_globals()
    
    def test_decide(self):
        # test the decide.py file correctly computes the variables and returns YES
        read_input("./test/test_decide.in")
        
        self.cmv, self.pum, self.fuv, self.launch = decide()
        self.assertEqual(self.launch, "YES")
        self.assertEqual(self.fuv, [True]*15)

    # test the decide.py file correctly computes CMV, PUM, FUV, and LAUNCH
    def test_decide2(self):
        # all PUV are false, so the FUV should all be true, and LAUNCH should be YES
        read_input("./test/test_decide2.in")
        self.cmv, self.pum, self.fuv, self.launch = decide()

        self.assertEqual(self.fuv, [True]*15)
        self.assertEqual(self.launch, "YES")
    
    def test_decide3(self):
        # test decide.py for input that will not pass the CMV, PUM, FUV, or LAUNCH
        read_input("./test/test_decide3.in")

        self.cmv, self.pum, self.fuv, self.launch = decide()
        
        self.assertNotEqual(self.cmv, [True]*15)
        self.assertNotEqual(self.pum[0], [True]*15)
        self.assertEqual(self.fuv, [True]*15)
        self.assertEqual(self.launch, "YES")