import unittest
from Ferenc_Hartmann_work import Alma

class Testalma(unittest.TestCase):
    def test_get_apple(self):
        apple = Alma()
        apple.get_apple()
        self.assertEqual(apple.get_apple(), "apple")



if __name__ == '__main__':
    unittest.main()
