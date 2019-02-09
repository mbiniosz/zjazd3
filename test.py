import unittest
import modul

class TestStringMethods(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)
    def test_f1(self):
        w1=modul.f1(0)
        self.assertEqual(w1,0)
    def test_f1_1(self):
        w1=modul.f1(1)
        self.assertEqual(w1,1)
    def test_f1_2(self):
        w1=modul.f1(2)
        self.assertEqual(w1,4)
    def test_f1_3(self):
        w1=modul.f1(2,1)
        self.assertEqual(w1,5)
    def test_f1_4(self):
        w1=modul.f1(2,3)
        self.assertEqual(w1,7)
    def test_f2_1(self):
        w1=modul.f2('ala')
        self.assertEqual(w1,'a')
    def test_f2_2(self):
        w1=modul.f2('')
        self.assertEqual(w1, 'BUUUM')
    def test_f2_3(self):
        w1=modul.f2('1,2,3')
        self.assertEqual(w1,'1')
    def test_f3_1(self):
        w1=modul.f3(1)
        self.assertEqual(w1,'jeden')
    def test_f3_2(self):
        w1=modul.f3(2)
        self.assertEqual(w1,'dwa')


if __name__ == '__main__':
    unittest.main()
