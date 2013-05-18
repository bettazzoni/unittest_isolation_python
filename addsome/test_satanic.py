import unittest


class TestIfSatanLovesYou(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.value = 10
        cls.cnt = 0

    def setUp(self):
        TestIfSatanLovesYou.cnt += 1

    def tearDown(self):
        self.value = 10

    def test_safe_01(self):
        pass

    def test_safe_02(self):
        pass

    def test_safe_03(self):
        pass

    def test_safe_04(self):
        pass

    def test_safe_05(self):
        assert self.value == 10

    def test_safe_06(self):
        assert self.cnt > 0

    def test_safe_07(self):
        pass

    def test_safe_08(self):
        pass

    def test_safe_09(self):
        pass
    
    @unittest.skip("introduce an orrible error for dependency")
    def test_Satan_Love(self):
        if TestIfSatanLovesYou.cnt == 4:
            from . import test_adder
            test_adder.setDEFAULT(666)
            assert False


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()