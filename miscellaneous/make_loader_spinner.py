from itertools import cycle
import sys
from time import struct_time, time, sleep
import datetime

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def make_loader_spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    
    symbols = cycle(SPINNER_STATES)
    end = time()+seconds
    while time()<end:
        sys.stdout.write("\r" + next(symbols))
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
    


if __name__ == '__main__':
    spinner(2)
