import argparse


def calc_bmi(weight, length):
    # calcutale BMI give a weight in kg and length in cm, return the BMI
    # rounded on 2 decimals
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    # create an ArgumentParser adding the right arguments to pass the tests
   
    parser = argparse.ArgumentParser(description='Calculate your BMI.')
    parser.add_argument("-w", "--weight", type=int,
                        help='Your weight in kg')
    parser.add_argument("-l", "--length", type=int,
                        help='Your length in cm')
    return parser


def handle_args(args=None):
    # Call calc_bmi with provided args object.

    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        raise SystemExit


if __name__ == '__main__':
    handle_args()