import argparse
import operator
from functools import reduce

def calculator(operation, numbers):
    # create a calculator that takes an operation and list of numbers.
    # perform the operation returning the result rounded to 2 decimals

    numbers=[float(n) for n in numbers]   
    if operation == 'add':
        return sum(numbers)

    if operation == 'sub':
        return reduce(operator.sub, numbers)
    
    if operation == 'mul':
        return round(reduce(lambda x, y: x*y, numbers), 2)
    
    if operation == 'div':
        return round(reduce(lambda x, y: x/y, numbers), 2)


def create_parser():
 
    # create an ArgumentParser object
    parser = argparse.ArgumentParser(description='A simple calculator') 
    parser.add_argument('-a', '--add', nargs='+', help="Sums numbers") 
    parser.add_argument('-s', '--sub', nargs='+', help="Subtracts numbers") 
    parser.add_argument('-m', '--mul', nargs='+', help="Multiplies numbers") 
    parser.add_argument('-d', '--div', nargs='+', help="Divides numbers") 
    # returns object
    return parser


def call_calculator(args=None, stdout=False):
    # calls calculator with provided args object.
    # if args are not provided get them via create_parser.
    # if stdout is True print the result.
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)