from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    
    for section_start in range(0, len(names), cols):
        ind = [f'| {names[i]:<10}' for i in range(section_start, section_start+cols) if i <len(names)]
        print(''.join(ind))
                