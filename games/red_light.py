from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    state = []
    Command = 'Stop Go Caution'.split()
    Timeout = '2 2 0.5'.split()
    Color = 'red green amber'.split()
    for color, command, time in zip(Color, Command, Timeout):
        state.append(State(color=color, command=command, timeout= float(time)))
    return cycle(state)

if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)