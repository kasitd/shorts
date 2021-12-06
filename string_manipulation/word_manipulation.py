import os
import urllib.request
import collections
import re
import shutil
import tempfile
from itertools import permutations, product

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}
class ScrabbleHelper:
    # creates one word, takes one argument

    def __init__(self, word):
        self.word = word

    def get_word(self) -> str:
        return self.word
    
    def __str__(self) -> str:
        pass

    def load_dictionary(self) -> str:

    # load dictionary and return as generator

        req = urllib.request.Request('https://www.scrapmaker.com/data/wordlists/dictionaries/dictionary.txt',
                                headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
            
        with urllib.request.urlopen(req) as response:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                shutil.copyfileobj(response, tmp_file)

        with open(tmp_file.name) as html:
            dictionary = html.read()
            return dictionary

    def is_valid(self) -> bool:
        if self.word==None or len(self.word)==0 or not self.word.isalnum() or not self.word.isalpha():
            return False
        return True
            

    def check_dictionary(self):
        dictionary = self.load_dictionary()
        if self.word.lower() in dictionary:
            return True
        return False
        
    def prepare_letter_list(self):
        return [letter.upper() for letter in self.word if letter.isalnum() or letter.isalpha()]

    def get_word_value(self):
        word_list = self.prepare_letter_list()
        sum = 0
        for letter in word_list:
            if letter not in LETTER_VALUES.keys():
                continue
            else:
                sum+=int(LETTER_VALUES[letter])
        return sum

    def get_permutations(self, r=None):
        pool = tuple(self.word)
        n = len(pool)
        r = n if r is None else r
        for indices in product(range(n), repeat=r):
            if len(set(indices)) == r:
                yield ''.join(tuple(pool[i] for i in indices))
        

    def is_palindrome(self):
        # return if word is palindrome.
        # case insensitive.

        if self.word == self.word[::-1]:
            return True
        return False


    def get_longest_palindrome(self, words=None):
        # given a list of words return the longest palindrome
        # if called without argument use the load_dictionary helper
        # to populate the words list
        
        if words==None:
            words = self.load_dictionary()
        
        list_of_palidromes = [word for word in words if self.is_palindrome(word)]
        
        return max(list_of_palidromes, key=len)

w = ScrabbleHelper('zygomata')
print(w.is_palindrome())
