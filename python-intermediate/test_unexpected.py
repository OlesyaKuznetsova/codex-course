import unittest
from python_intermediate.unexpected import get_sqrt, divide

class TestUnexpected(unittest.TestCase):

    def test_get_sqrt_valid(self):
        self.assertEqual(get_sqrt(144), 12)

    def test_get_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-4)

    def test_divide_valid(self):
        self.assertEqual(divide(144, 12), 12)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()