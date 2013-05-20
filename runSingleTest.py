import sys, unittest, coverage, io

from coverageutilities import called_coverage_data

MAXTESTS = 1000000000

class TestGetter:
    def __init__ ( self, test_suite):
        self.test_suite = test_suite
        
    def get_num( self, num_to_get): 
        self.count = 0
        self.result = None
        def _get_test_numbered(t_suite, count):
            tests = []
            for t in t_suite:
                try:
                    iter(t)
                except TypeError:
                    if self.count == num_to_get:
                        tests.append(t)
                        self.count = MAXTESTS
                        self.result = unittest.TestSuite(tests)
                        return self.result
                    else:
                        self.count += 1 
                else:
                    tests.append(_get_test_numbered(t, self.count))
            return unittest.TestSuite(tests)
        _get_test_numbered( self.test_suite , 0) 
        return self.result

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run Tests')
    parser.add_argument('--verbose', '-v', dest='verbose', type=int,  default=1,
                       help='unittest verbosity')
    known_args, other_args = parser.parse_known_args()
    
    test_runner_output = io.StringIO()
    runner = unittest.TextTestRunner(stream=test_runner_output, verbosity = known_args.verbose)
    complete_test_suite = unittest.loader.defaultTestLoader.discover('.', pattern='*.py')
    tg = TestGetter(complete_test_suite)
    result = runner.run( tg.get_num(num_to_get = 1) )
    
    i = 0
    test_suite_with_a_single_test = tg.get_num(num_to_get = 0)
    while test_suite_with_a_single_test is not None:
        cov = coverage.coverage()
        cov.start()
        result = runner.run( test_suite_with_a_single_test )
        cov.stop ()
        cov_data = called_coverage_data(cov)
        #print (cov_data) 
        if not result.wasSuccessful():
            print(test_runner_output.getvalue())
            print ("\n----------------\nError\nTest num. %d  fails" % i )
            sys.exit(-1) 
        i += 1
        test_suite_with_a_single_test = tg.get_num(num_to_get = i)
    
    print ("\n----------------\nOK\nRan %d tests in single mode" % i )
    sys.exit(-1)

