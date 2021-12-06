import os
from pathlib import Path

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    bigger= []
    """Return files in dirname that are >= size_in_kb"""
    entries = os.listdir(dirname)
    for entry in entries:
        
        #use join to concatenate all the components of path
        f = os.path.join(dirname, entry)
        
    
        if os.path.getsize(f)>=(size_in_kb*ONE_KB):
            bigger.append(entry)
    return bigger