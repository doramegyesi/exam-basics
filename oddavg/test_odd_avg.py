import unittest
from odd_avg import *

class TestAverageOfOddNumbers(unittest.TestCase):
    def test_odd_average(numbers = [1, 2, 3, 4, 5]):
        what_i_should_get = average
        self.assertEqual(what_i_should_get.odd_average, "3")

if __name__ == '__main__':
    unittest.main()
