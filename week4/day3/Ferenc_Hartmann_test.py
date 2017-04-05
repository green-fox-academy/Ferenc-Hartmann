import unittest
from Ferenc_Hartmann_work import Needtest
from Ferenc_Hartmann_work import Summarize
from Ferenc_Hartmann_work import Anagram
from Ferenc_Hartmann_work import Letter_Counter
from Ferenc_Hartmann_work import Fibonacci


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

class Letters(unittest.TestCase):
    def test_null(self):
        string = Letter_Counter()
        self.assertEqual(string.lc(""), {})
    def test_one_letter(self):
        string = Letter_Counter()
        self.assertEqual(string.lc("a"), {'a': 1})
    def test_long_letter(self):
        string = Letter_Counter()
        self.assertEqual(string.lc("abcdefghijk"), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1})
    def test_double_long_letter(self):
        string = Letter_Counter()
        self.assertEqual(string.lc("aabbccdd"), {'a': 2, 'b': 2, 'c': 2, 'd': 2})

class Fibonacci_tester(unittest.TestCase):
    def test_negative(self):
        number = Fibonacci()
        self.assertEqual(number.fibonacci_m(-1), "Try with a natural number")

    def test_flow(self):
        number = Fibonacci()
        self.assertEqual(number.fibonacci_m(5.5), "Try with a natural number")

    def test_zero(self):
        number = Fibonacci()
        self.assertEqual(number.fibonacci_m(0), 0)

    def test_one(self):
        number = Fibonacci()
        self.assertEqual(number.fibonacci_m(1), 1)

    def test_six(self):
        number = Fibonacci()
        self.assertEqual(number.fibonacci_m(6), 8)

if __name__ == '__main__':
    unittest.main()
