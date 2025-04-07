import unittest
from python_intermediate.string_utils import (
    reverse_strings,
    capitalize_strings,
    is_capitalized
)

class TestStringUtils(unittest.TestCase):

    def test_reverse_strings(self):
        self.assertEqual(reverse_strings('hello'), 'olleh')
        self.assertEqual(reverse_strings('Python'), 'nohtyP')
        self.assertEqual(reverse_strings(''), '')

    def test_capitalize_strings(self):
        self.assertEqual(capitalize_strings('hello'), 'Hello')
        self.assertEqual(capitalize_strings('python'), 'Python')
        self.assertEqual(capitalize_strings('123abc'), '123abc')   

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('Hello'))
        self.assertFalse(is_capitalized('hello'))
        self.assertFalse(is_capitalized(''))

if __name__ == '__main__':
    unittest.main()