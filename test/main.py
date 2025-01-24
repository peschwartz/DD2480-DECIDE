import unittest
from testcmv import TestCMV
from testfuv import TestFUV

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCMV)
    
    unittest.TextTestRunner(verbosity=2).run(test_suite)

    test_suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFUV)
    
    unittest.TextTestRunner(verbosity=2).run(test_suite2)

    