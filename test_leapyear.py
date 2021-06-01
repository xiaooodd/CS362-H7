import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.is_Leap(400),"Leap year")

    def test2(self):
        self.assertEqual(leapyear.is_Leap(100),"Not leap year")

    def test3(self):
        self.assertEqual(leapyear.is_Leap(4),"Leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)