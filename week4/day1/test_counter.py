import unittest
from counter import Counter

class TestCounter(unittest.TestCase):

    def setUp(self):
        self.c = Counter()

    def test_addMore(self):
        self.c.add(5)
        self.assertEqual(self.c.get(), 5)

    def test_addOne(self):
        self.c.add()
        self.assertEqual(self.c.get(), 1)

    def test_getZero(self):
        self.assertEqual(self.c.get(), 0)

    def test_getInit(self):
        c = Counter(7)
        self.assertEqual(c.get(), 7)

    def test_resetToZero(self):
        self.c.add()
        self.c.reset()
        self.assertEqual(self.c.get(), 0)

    def test_resetToInit(self):
        c = Counter(7)
        self.c.add(5)
        self.c.reset()
        self.assertEqual(c.get(), 7)

if __name__ == '__main__':
    unittest.main()
