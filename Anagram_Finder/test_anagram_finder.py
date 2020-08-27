import unittest
import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Anagram_Finder.anagram_finder import Anagram


class TestAnagrams(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setting up Anagram Instance and loading Dictionary for Test Cases')
        cls.__anagram = Anagram()
        cls.__anagram.process_input_dictionary('dictionary.txt')

    @classmethod
    def tearDownClass(cls):
        del cls.__anagram
        print()
        print('Tearing down Anagram Instance Completed')

    # Method to test given input word has correct matching anagrams from Dictionary
    def test_matching_anagrams(self):
        self.assertEqual(self.__anagram.match_anagrams('stop'), ['post', 'spot', 'stop', 'tops'])
        self.assertEqual(self.__anagram.match_anagrams('ernejfhrbhrefrei'), [])
        self.assertEqual(self.__anagram.match_anagrams('separ'), ['asper', 'parse', 'prase', 'spaer', 'spare', 'spear'])

    # Method to test encodings are correct for a given input word
    def test_encode_word(self):
        self.assertEqual(self.__anagram.encode_word('stop'), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1
, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 )
        # passing input which cannot be encoded should raise Error
        self.assertRaises(ValueError, self.__anagram.encode_word, 'Ã')

    #  Method to test function 'compare_encodings' which compares two input words encodings
    def test_compare_encodings(self):
        self.assertEqual(self.__anagram.compare_encodings(self.__anagram.encode_word('stop'),
                                                          self.__anagram.encode_word('care')), False)
        self.assertEqual(self.__anagram.compare_encodings(self.__anagram.encode_word('separ'),
                                                          self.__anagram.encode_word('pares')), True)

if __name__ == '__main__':
    unittest.main()

