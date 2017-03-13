from unittest import TestCase
from line_intersect import line_intersect


class TestLine_intersect(TestCase):
    def test_line_intersect1(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(0.0, 0.0), (1.0, 3.0)])
        expected = [(0.0, 0.0), (1.0, 3.0)]
        self.assertEqual(line_intersect(argument[0], argument[1]), expected,
                         'Similar lines')

    def test_line_intersect2(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(0.0, 0.0), (1.0, 4.0)])
        expected = (0.0, 0.0)
        self.assertEqual(line_intersect(argument[0], argument[1]), expected,
                         'Simple intersection')

    def test_line_intersect3(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(0.0, 1.0), (1.0, 4.0)])
        expected = None
        self.assertEqual(line_intersect(argument[0], argument[1]), expected,
                         'No intersection')

    def test_line_intersect4(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(-1.0, -4.0), (1.0, 4.0)])
        expected = (0.0, 0.0)
        self.assertEqual(line_intersect(argument[0], argument[1]), expected,
                         'Simple intersection')

    def test_line_intersect5(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(0.0, 0.0), (0.0, 0.0)])
        expected = ZeroDivisionError
        with self.assertRaises(expected):
            line_intersect(argument[0], argument[1]),

    def test_line_intersect6(self):
        argument = ([(0.0, 0.0), (1.0, 3.0)], [(1.0, 0.0), (1.0, 4.0)])
        expected = (1.0, 3.0)
        self.assertEqual(line_intersect(argument[0], argument[1]), expected,
                         'Simple intersection')
