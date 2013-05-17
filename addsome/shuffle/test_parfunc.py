import unittest

from . parfunc import cy, cs

class TestModule(unittest.TestCase):

    def test01(self):
        f= [ cy(i) for i in range(10)]
        self.assertEqual(f[0](0) , 0)
        self.assertEqual(f[0](1) , 1)
        self.assertEqual(f[3](4) , 7)

    def test02(self):
        f= [ cy(i) for i in range(100)]
        for i in range(100):
            self.assertEqual(f[i](i-1) , i*2-1)

    def test03(self):
        f= [ cs(i) for i in range(1000)]
        dist = sorted([ f[i](self) for i in range(100)])
        equals = [i for i in range(len(dist)-1) if dist[i] == dist[i+1] ] 
        self.assertEqual(len(equals), 0)
