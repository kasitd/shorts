import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    temp = []
    
    if any(args):
        for x in args:
            if x != None and len(x)!=0:
                temp.append(set(x))
        return set.intersection(*temp)
    else:
        return set([])
    