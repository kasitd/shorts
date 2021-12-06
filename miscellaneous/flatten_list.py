def flatten(list_of_lists):
    for l in list_of_lists:
        if isinstance(l, (list,tuple)):
            yield from flatten(l)
        else:
            yield(l)