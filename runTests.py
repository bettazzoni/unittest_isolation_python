import sys, unittest

same_key = echo_key = lambda x: str(x)

def safe_calc_hash(x):
        try:
            h=hash(x)
        except TypeError:
            h = hash(repr(x)) 
            try:
                s= sum([ safe_calc_hash(e) for e in x])
            except TypeError:
                s = 0
            h += s
        return h

def create_numeric_hash_based_key(generator):
    return lambda x: (0x5A5A5A * safe_calc_hash(x) * generator) % 100000

def my_discover( start_dir, pattern='test*.py', top_level_dir=None, key_function = same_key): 
    def _swap_tests(tests_suite):
        tests = []
        for t in tests_suite:
            try:
                iter(t)
            except TypeError:
                tests.append(t) 
            else:
                tests.append(_swap_tests(t))
        return unittest.TestSuite(sorted(tests, key=key_function))

    all_tests = unittest.loader.defaultTestLoader.discover(start_dir,pattern=pattern, top_level_dir=top_level_dir)
    return unittest.TestSuite(_swap_tests( all_tests ) )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run Tests')
    parser.add_argument('--verbose', '-v', dest='verbose', type=int,  default=1,
                       help='unittest verbosity')
    parser.add_argument('--repeat', '-r', dest='repeat', type=int, default=0,
                       help='number of repetition with shuffle')
    parser.add_argument('--shuffle_with_key', '-s', dest='shuffle_with_key', type=int,
                       help='runs only the N shuffle')
    known_args, other_args = parser.parse_known_args()
    
    runner = unittest.TextTestRunner(verbosity = known_args.verbose)
    
    if known_args.shuffle_with_key is not None:
        runner.run( my_discover('.', pattern='*.py', 
                                key_function = create_numeric_hash_based_key(known_args.shuffle_with_key)) )
        
    else:
        runner.run( my_discover('.', pattern='*.py'))
        for i in range(known_args.repeat):
            print ("\nrepeat num. %d" % i)
            result = runner.run( my_discover('.', pattern='*.py', 
                                key_function = create_numeric_hash_based_key(i)) )  
            if not result.wasSuccessful():
                sys.exit(-1)


