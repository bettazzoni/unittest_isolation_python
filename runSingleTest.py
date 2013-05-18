import sys, unittest

MAXTESTS = 1000000000

class TestGetter:
    def __init__ ( self, test_suite):
        self.test_suite = test_suite
        
    def get_num( self, num_to_get): 
        self.count = 0
        def _get_test_numbered(t_suite, count):
            tests = []
            for t in t_suite:
                try:
                    iter(t)
                except TypeError:
                    if self.count == num_to_get:
                        tests.append(t)
                        self.count = MAXTESTS
                        return unittest.TestSuite(tests)
                    else:
                        self.count += 1 
                else:
                    tests.append(_get_test_numbered(t, self.count))
            return unittest.TestSuite(tests)
        return unittest.TestSuite(_get_test_numbered( self.test_suite , 0) )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run Tests')
    parser.add_argument('--verbose', '-v', dest='verbose', type=int,  default=1,
                       help='unittest verbosity')
    known_args, other_args = parser.parse_known_args()
    
    runner = unittest.TextTestRunner(verbosity = known_args.verbose)
    complete_test_suite = unittest.loader.defaultTestLoader.discover('.', pattern='*.py')
    tg = TestGetter(complete_test_suite)
    result = runner.run( tg.get_num(num_to_get = 1) )

    for i in range(MAXTESTS):
        result = runner.run( tg.get_num(num_to_get = i) )
        if not result.wasSuccessful():
            print ("\n----------------\nError\nTest num. %d  fails" % i )
            sys.exit(-1) 
        if result.testsRun == 0:
            print ("\n----------------\nOK\nRan %d tests in single mode" % i )
            sys.exit(-1)

