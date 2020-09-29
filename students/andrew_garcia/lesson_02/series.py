'''
Andrew Garcia
Fibonacci Sequence
6/9/19
'''

def fibonacci(n):
    """ Computes the 'n'th value in the fibonacci sequence, starting with 0 index """

    number = [0, 1]  # numbers to add together

    if n == 0:
        return(number[0])
    elif n == 1:
        return(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        return(number[1])


def lucas(n):
    """ Computes the 'n'th value in the lucas sequence, starting with 0 index """

    number = [2, 1]  # numbers to add together

    if n == 0:
        return(number[0])
    elif n == 1:
        return(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        return(number[1])


def sum_series(n, zeroth=0, first=1):
    """
    Computes the 'n'th value in a given series

        :param zeroth=0: Creates the first value to use in a series
        :param first=1: Creates the second value to use in a series

    If the two parameters are left blank, or are filled in 0 and 1, it will start the fibonacci sequence
    If the two parameters are filled in 2 and 1, it will start the lucas sequence
    If the two parameters are filled in with two random numbers, it will create its own sequence
    """
    number = [zeroth, first]  # numbers to add together

    if n == 0:
        return(number[0])
    elif n == 1:
        return(number[1])
    else:
        for item in range(n - 1):  # subtracts 1 to account for 0 index
            fib = number[0] + number[1]
            number.append(fib)
            number.pop(0)
        return(number[1])


if __name__ == "__main__":
    # Tests if Fibonacci is working
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(9) == 34
    print('Fibonacci Working')


    # Tests if lucas is working
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(5) == 11
    assert lucas(9) == 76
    print('Lucas Working')

    # Tests random sequences
    assert sum_series(0) == 0
    assert sum_series(1, 0, 1) == 1
    assert sum_series(0, 2, 1) == 2
    assert sum_series(4, 2, 3) == 13
    assert sum_series(1, 5, 7) == 7
    print('Series Working')

