import re

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5



def filter_names(names):
    lista = []
    for name in names:

        pattern = re.compile(IGNORE_CHAR)
        if pattern.search(name,0, 1):
            continue
        s3 = re.search('[0-9]', name)
        if s3:
            continue
        pattern2 = re.compile(QUIT_CHAR)
        if pattern2.search(name):
            break

        else:
            lista.append(name)

        if len(lista) == MAX_NAMES:
            break
    return lista