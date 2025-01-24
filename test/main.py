import unittest
from testcmv import TestCMV

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCMV)
    
    unittest.TextTestRunner(verbosity=2).run(test_suite)
