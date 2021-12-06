from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError(type(data_type), ' is an Unsupported type')
    
@count_down.register(str)
def _(s):
    while s:
        print(s)
        s = s[:-1]
        
@count_down.register(int)
@count_down.register(float)
def _(x):
    count_down(str(x))

@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(l):
    count_down(''.join(str(c) for c in l))

@count_down.register(dict)
def _(d):
    count_down(list(d.keys()))