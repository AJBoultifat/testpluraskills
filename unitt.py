from typing import List
import unittest
from calculation import calculate

class TestStringMethods(unittest.TestCase):
    def test_calculation(self):
        List = [3]
        self.assertEqual('Buzz', calculate.functionTest(List))
    def test_calculation1(self):
        List = [5]
        self.assertEqual('Fizz', calculate.functionTest(List))
    def test_calculation2(self):
        List = [15]
        self.assertEqual('FizzBuzz', calculate.functionTest(List))

if __name__ == '__main__':
    unittest.main()
