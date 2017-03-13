from unittest import TestCase
import square_preceding

class TestSquare_preceding(TestCase):
    def test_square_preceding(self):
        argument = [1, 2, 3]
        expected = [0, 1, 4]
        square_preceding.square_preceding(argument)
        self.assertEqual(argument,expected,'Alalalalalal')
