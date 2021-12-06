from typing import List, Union
from itertools import chain


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    with_separator = []
    if lst_of_lst == []:
        return None
    else:
        for n, elem in enumerate(lst_of_lst):
            if n < len(lst_of_lst)-1:
                with_separator.append(elem)
                with_separator.append(sep)
            else:
                with_separator.append(elem)
        return list(chain.from_iterable(with_separator))