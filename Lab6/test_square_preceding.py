from unittest import TestCase
import tet

class TestSquare_preceding(TestCase):
    def test_square_preceding(self):
        argument = [1, 2, 3]
        expected = [0, 1, 4]
        tet.square_preceding(argument)
        self.assertEqual(argument,expected,'Idiotic')
