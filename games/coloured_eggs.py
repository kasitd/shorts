from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    
    def __init__(self, limit):
        self.start = 0
        self.limit =  limit
        self.colors = COLORS

    def __iter__(self):
        return self

    def __next__(self):
        self.start+=1
        if self.start > self.limit:
            raise StopIteration
        return f'{choice(self.colors)} egg'