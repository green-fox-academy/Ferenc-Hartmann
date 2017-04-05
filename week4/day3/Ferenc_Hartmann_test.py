import unittest
from Ferenc_Hartmann_work import Needtest
from Ferenc_Hartmann_work import Summarize

class Testalma(unittest.TestCase):
    def test_get_apple(self):
        apple = Needtest()
        self.assertEqual(apple.get_apple(), "apple")

class Summar(unittest.TestCase):
    def test_sum_zero(self):
        numbers = Summarize()
        self.assertEqual(numbers.sum([]), 0)

    def test_sum_of_one(self):
        numbers = Summarize()
        self.assertEqual(numbers.sum([1]), 1)

    def test_sum_of_three(self):
        numbers = Summarize()
        self.assertEqual(numbers.sum([1,2,2]), 5)

    def test_sum_null(self):
        numbers = Summarize()
        self.assertEqual(numbers.sum([0]), 0)

if __name__ == '__main__':
    unittest.main()
