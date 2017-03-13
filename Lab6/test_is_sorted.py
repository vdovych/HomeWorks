from unittest import TestCase
from is_sorted import is_sorted

class TestIs_sorted(TestCase):
    def test_is_sorted1(self):
        argument = [1,2,3]
        expected = True
        self.assertEqual(is_sorted(argument), expected)
    def test_is_sorted2(self):
        argument = [1,3,2]
        expected = False
        self.assertEqual(is_sorted(argument), expected)
    def test_is_sorted3(self):
        argument = [1,2,2,3]
        expected = True
        self.assertEqual(is_sorted(argument), expected)
    def test_is_sorted4(self):
        argument = [1]
        expected = True
        self.assertEqual(is_sorted(argument), expected)
    def test_is_sorted5(self):
        argument = 'List of integers'
        expected = ValueError
        with self.assertRaises(expected):
            is_sorted(argument)
