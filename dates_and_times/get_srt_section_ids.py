from datetime import timedelta
from typing import List
import datetime
from collections import namedtuple
from operator import attrgetter

def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """


    info = []  
    subtitles = namedtuple('Subtitles', ['index', 'speed']) 
    d_sub = []
    
    for part in text.strip().split('\n\n'):
        for i, p in enumerate(part.splitlines()):
            if i == 0:
                info.append(p)
             
            if i == 1:
                start = datetime.datetime.strptime(p[:12], "%H:%M:%S,%f")
                stop = datetime.datetime.strptime(p[18:], "%H:%M:%S,%f")
                delta =(stop-start).total_seconds()
                
            if i == 2:
                len_text = len(p)
                info.append(len_text/delta)
                
                s =subtitles._make(info)
                info = []
                d_sub.append(s)
    sub_sorted = sorted(d_sub, key=attrgetter('speed'), reverse=True)
    return[int(subtitles.index) for subtitles in sub_sorted]