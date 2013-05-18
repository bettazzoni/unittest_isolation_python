#!/usr/bin/env python3

import unittest
from order import echo


class Test_2(unittest.TestCase):

    def test_2(self):
        self.assertTrue(echo( 1 ) == 1)
    
    def test_3(self):
        self.assertTrue(echo( 1 ) == 1)
        
    def test_5(self):
        self.assertTrue(echo( 1 ) == 1)

    def test_1(self):
        self.assertTrue(echo( 1 ) == 1)

    def test_4(self):
        self.assertTrue(echo( 1 ) == 1)

 
class Test_1(Test_2):
    pass

class Test_4 (Test_1):
    def test_6(self):
        pass

class Test_3 (Test_1):
    def test_8(self):
        pass
    def test_6(self):
        pass
    def test_7(self):
        pass


if __name__ == '__main__':
    def compare(a,b):
        return -1 if a < b else 1 if a > b else 0
    def hash_compare(a,b):
        return compare(hash(a), hash(b))
    def id_compare(a,b):
        return compare(id(a), id(b))
    
    unittest.loader.defaultTestLoader.sortTestMethodsUsing = hash_compare
    unittest.main(exit=False)
    print('\n---------------------------------------------------------\n')
    unittest.loader.defaultTestLoader.sortTestMethodsUsing = id_compare
    unittest.main()
