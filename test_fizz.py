import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fizz(3),"Fizz")
    
    def test2(self):
        self.assertEqual(fizzbuzz.fizz(5),"Buzz")

if __name__ == '__main__':
    unittest.main(verbosity=2)