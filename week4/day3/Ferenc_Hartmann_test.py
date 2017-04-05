import unittest
from Ferenc_Hartmann_work import Needtest
from Ferenc_Hartmann_work import Summarize
from Ferenc_Hartmann_work import Anagram

class Alma_tester(unittest.TestCase):
    def test_get_apple(self):
        apple = Needtest()
        self.assertEqual(apple.get_apple(), "apple")

class Sum_tester(unittest.TestCase):
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

class Anagramtester(unittest.TestCase):
    def test_true(self):
        string = Anagram()
        self.assertEqual(string.anag("caaaica", "acicaaa"), True)
    def test_false(self):
        string = Anagram()
        self.assertEqual(string.anag("cica", "acitaaaa"), False)

if __name__ == '__main__':
    unittest.main()
