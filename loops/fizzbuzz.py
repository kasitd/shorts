def fizzbuzz(num):
    for number in range(1, num+1):
        if number % 3 == 0 and number % 5 == 0:
            d = 'Fizz Buzz'
        elif number%3 == 0 or number%5 == 0:
            if number%3 == 0:
                d = 'Fizz'
            if number%5 == 0:
                d = 'Buzz'
        else:
            d = int(number)
    return d