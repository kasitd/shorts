from itertools import accumulate

def running_mean(sequence):
    list1 = []
    divider = 0
    for number in accumulate(sequence):
        divider +=1
        n = number/divider
        list1.append(round(n,2))
    return list1