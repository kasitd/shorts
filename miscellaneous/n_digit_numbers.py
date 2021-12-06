from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    n_digit_list = []
    for num in numbers:
        
        clean = ([n for n in str(num) if n.isdigit()])
        #print(len(clean))
        if len(clean)>= n:
            n_digit = (''.join(clean)[:n])
        else:
            add = '0'*(n-len(clean))
            n_digit = (''.join(clean)+add)
        if str(num)[0]=='-':
            n_digit='-'+n_digit
        n_digit_list.append(int(n_digit))
    return n_digit_list