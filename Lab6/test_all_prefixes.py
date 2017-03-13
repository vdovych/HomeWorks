from unittest import TestCase
from all_prefixes import all_prefixes

class TestAll_prefixes(TestCase):
    def test_all_prefixes1(self):
        argument = 'land'
        expected = {'l', 'la', 'lan', 'land'}
        self.assertEqual(all_prefixes(argument), expected, "Simple word")
    def test_all_prefixes2(self):
        argument = 'lan'
        expected = {'l', 'la', 'lan'}
        self.assertEqual(all_prefixes(argument), expected, "Simple word")
    def test_all_prefixes3(self):
        argument = 'landl'
        expected = {'l', 'la', 'lan', 'land', 'landl'}
        self.assertEqual(all_prefixes(argument), expected, "Simple word")
    def test_all_prefixes4(self):
        argument = 'landlord'#Even though there are 2 'l' in a word, the second 'l' is not a first letter'
        expected = {'l', 'la', 'lan', 'land', 'landl'}
        self.assertEqual(all_prefixes(argument), expected, "Simple word")
