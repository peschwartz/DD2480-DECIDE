import unittest

if __name__ == '__main__':
    # make sure all test files start with test
    test_suite = unittest.TestLoader().discover('test', pattern='test*.py')
    
    unittest.TextTestRunner(verbosity=2).run(test_suite)

