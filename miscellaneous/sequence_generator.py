from string import ascii_lowercase
import itertools




def sequence_generator():
    new = []
    saved = []
    letters = [x for x in ascii_lowercase.upper()]
    numbers = list(range(1,27))
    for l, n in zip(itertools.cycle(numbers), itertools.cycle(letters)):
        yield l
        yield n
       