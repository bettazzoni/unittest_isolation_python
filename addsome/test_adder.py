import unittest
from . import adder 


DEFAULT  = 10
def setDEFAULT(d):
    global DEFAULT
    DEFAULT = d

orrible = adder.Adder(DEFAULT)

def setUpOrribleWay(value = DEFAULT):
    global orrible
    orrible = adder.Adder(value)
    
def testingSomethingInOrribleWay():
    assert orrible.add(10) == 20
    assert orrible.add(1) == 21


class OrribleFunctionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        setUpOrribleWay(DEFAULT)

    def tearDown(self):
        setUpOrribleWay(10)
          
    def test(self):
        testingSomethingInOrribleWay()
 
    def test_again(self):
        testingSomethingInOrribleWay()
    


class TestModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.init_value = 0

    @classmethod
    def tearDownClass(cls):
        cls.init_value = None

    def setUp(self):
        self.a = adder.Adder(TestModule.init_value)
        
    def test_01(self):
        self.assertEqual(self.a.add(1), 1)

    def test_02(self):
        self.a.add(1)
        self.assertEqual(self.a.add(1), 2)
 
    def test_03(self):
        self.a.add(2)
        self.assertEqual(self.a.add(1), 3)

    def test_05(self):
        self.assertEqual(adder.Adder(10).add(-1), 9)

    @unittest.skip("introduce error for dependency")
    def test_69(self):
        self.assertEqual(adder.Adder(1).add(-1), 0)
        TestModule.init_value += 1

    def test_04(self):
        self.assertEqual(adder.Adder(1).add(-1), 0)
    
    @unittest.skip("introduce an orrible error for dependency")
    def test_666(self):
        setDEFAULT(666)
 
 
    
