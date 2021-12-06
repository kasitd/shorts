from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as C:
        x = []
        for el in C:
            pattern = re.findall(r'(\d{1,2}:\d\d)', el)
            if pattern !=[]:
                x.append(pattern[0])
    return x


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    min = 0
    sec = 0
    for el in timestamps:
        (minutes, seconds) = (el.split(':')[0], el.split(':')[1])
        min+=int(minutes)
        sec += int(seconds)
    return str(timedelta(minutes=min, seconds=sec))