def positive_divide(numerator, denominator):
    while True:
        try:
            numerator/denominator
        except ZeroDivisionError:
            return 0
        except TypeError:
            raise TypeError
        if numerator/denominator <0:
            raise ValueError
        return numerator/denominator