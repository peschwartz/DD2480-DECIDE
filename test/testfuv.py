import unittest
from fuv import *
from GLOBAL_VARS import *

class TestFUV(unittest.TestCase):
    def test_false(self):
        # tests the case where the PUV and PUM are all false
        # should be all true since the PUV is false
        puv = [False] * 15
        pum = [[False] * 15] * 15
        self.assertEqual(compute_fuv_from_pum(puv, pum), [True] * 15)

    def test_true(self):
        # tests the case where the PUV is all true
        # should be all true since the PUM is all true
        puv = [True] * 15
        pum = [[True] * 15] * 15
        self.assertEqual(compute_fuv_from_pum(puv, pum), [True] * 15)

    def test_true_puv_true_true_pum_but_one_false(self):
        # tests the case where the PUM is all true but one entry is false
        puv = [True] * 15
        # create a proper 2D list where each row is a new list
        pum = [[True for _ in range(15)] for _ in range(15)]
        pum[0][0] = False
        expected_fuv = [True] * 15
        expected_fuv[0] = False
        self.assertEqual(compute_fuv_from_pum(puv, pum), expected_fuv)

    def test_mixed(self):
        # tests the case where PUV and PUM are mixed
        pum = [[False for _ in range(15)] for _ in range(15)]
        puv = [False] * 15
        expected_fuv = [True] * 15
        
        # set alternating values in PUV
        for i in range(15):
            puv[i] = (i % 2 == 0) 
            
            # for indices where PUV is True, set corresponding PUM row
            # to ensure FUV will be True (all True values)
            if puv[i]:
                pum[i] = [True] * 15
                expected_fuv[i] = True
            else:
                # for indices where PUV is False, FUV should be True
                # regardless of PUM values
                pum[i] = [False] * 15
                expected_fuv[i] = True
                
        self.assertEqual(compute_fuv_from_pum(puv, pum), expected_fuv)

        
    def test_mixed_2(self):
        # tests the case where the PUM is mixed but should be all false
        # create a proper 2D list where each row is a new list
        pum = [[False for _ in range(15)] for _ in range(15)]
        puv = [False] * 15
        expected_fuv = [False] * 15
        for i in range(15):
            val = i % 2
            pum[i] = [val] * 15
            puv[i] = not val
            expected_fuv[i] = val
        self.assertEqual(compute_fuv_from_pum(puv, pum), expected_fuv)
        self.assertEqual(compute_fuv_from_pum(puv, pum), expected_fuv)
