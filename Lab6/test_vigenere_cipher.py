from unittest import TestCase
from vigenere_cipher import *

class TestVigenere(TestCase):
    def test_combine_character(self):
        assert combine_character("E", "T") == "X"
        assert combine_character("N", "R") == "E"

    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    def test_separate_character(self):
        assert separate_character("X", "T") == "E"
        assert separate_character("E", "R") == "N"


    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"
