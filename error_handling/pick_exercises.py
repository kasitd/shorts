import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self):
        # updated Bite to make local copies (avoid globals!)
        self.all_bites = BITES.copy()
        self.bites_done = BITES_DONE.copy()

    def _pick_random_bite(self):
        """Pick a random Bite that is not done yet, if all
           Bites are done, raise a NoBitesAvailable exception"""
        all_keys = self.all_bites.keys()
        if sorted(self.bites_done) == sorted(all_keys):
            raise NoBitesAvailable
        else:
            available_keys = [k for k in list(all_keys) if k not in self.bites_done]
            return random.choice(list(available_keys))
        

    def new_bite(self):
        """Get  a random Bite using _pick_random_bite,
           add it to self.bites_done, then return it"""
        not_available = self._pick_random_bite()
        self.bites_done.add(not_available)
        return not_available
    
    def filter_bites(bites=BITES, bites_done=BITES_DONE):
        """return the bites dict with the exclude_bites filtered out"""
        bites_copy = {}
        for (key, value) in bites.items():
            if key not in bites_done:
                bites_copy[key] = value
        return bites_copy