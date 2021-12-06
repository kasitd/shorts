from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    # return row
    
    if N == 0:
        return []
    elif N == 1:
        return [1]
    else:
        new_row = [1]
        last_row = pascal(N-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row