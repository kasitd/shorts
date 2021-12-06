from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*numbers):
        for number in numbers:
            for n in numbers:
                if type(n)==str or type(n)==float:
                    raise TypeError  
                if n<0:
                    raise ValueError
                
            return func(*numbers)
    return wrapped