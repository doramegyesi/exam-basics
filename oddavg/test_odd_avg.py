import unittest
from odd_avg import *

class TestAverageOfOddNumbers(unittest.TestCase):
    def test_odd_average(self, numbers = [1, 2, 3, 4, 5]):
        result = "3"
        self.assertEqual(odd_average(numbers), "3")

if __name__ == '__main__':
    unittest.main()
