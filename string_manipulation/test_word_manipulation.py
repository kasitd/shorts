import unittest
from word_manipulation import ScrabbleHelper

class TestScrabbleHelper(unittest.TestCase):
    def test_is_valid(self):
        
        self.assertTrue(ScrabbleHelper('zyg8mata').is_valid())

if __name__ == '__main__':
    unittest.main()