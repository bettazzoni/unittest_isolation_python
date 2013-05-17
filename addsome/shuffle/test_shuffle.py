import unittest
from . shuffle import shuffle , same_key, hash_based_key, create_numeric_hash_based_key, Permutation

a = ["1", '2', '3', '4', '5', '6']
b = range(100) 

class Test_Shuffle(unittest.TestCase):

    def test_no_shuffle(self):
        self.assertEqual(a, shuffle(a, same_key))

    def test_shuffle_hash_based_key(self):
        r = shuffle(a, hash_based_key)
        self.assertNotEqual(a, r)
        self.assertEqual(r, shuffle(a, hash_based_key))

    def test_shuffle_simple_create_numeric_hash_based_key(self):
        kf = create_numeric_hash_based_key(3)
        r = shuffle(a, kf)
        self.assertNotEqual(a, r)
        self.assertNotEqual(r, shuffle(a, hash_based_key))
        self.assertEqual(r, shuffle(a, kf))

    def test_shuffle_multi_create_numeric_hash_based_key(self):
        ss = [ shuffle(b, create_numeric_hash_based_key(i)) for i in range (10) ]
        ss_ordered = sorted(ss, key=str)
        equals = [i for i in range(len(ss_ordered)-1) if ss_ordered[i] == ss_ordered[i+1] ] 
        self.assertEqual(len(equals), 0)

class Test_Permutation(unittest.TestCase):

    def test_first(self):
        p = Permutation(a)
        self.assertEqual(tuple(a), next(p) )
        self.assertNotEqual(tuple(a), next(p) )
