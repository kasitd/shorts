class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        pass
        

    def __call__(self, score, memory=[]):
        memory.append(score)
        print(f'to memory {memory}')
        if score<0:
           memory = [n for n in memory if n < 0]

        return sorted(memory, reverse=True)[0]