def fibonacci(n):
    """
    Return nth value in the fibonacci series
    https://en.wikipedia.org/wiki/Fibonacci_number

    :param n: Define nth value in the fibonacci series
    :return: Return nth value in the fibonacci series
    """
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Return nth value in the lucas series
    https://en.wikipedia.org/wiki/Lucas_number

    :param n: Define nth value in the lucas series
    :return: Return nth value in the lucas series
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def print_series(series, n):
    """
    Return all the numbers in lucas series from first to nth number.
    Verifies that the n is positive value.

    :param series: Define which series, Fibonacci or Lucas

    :param n: Define nth value in the lucas series and is used to define how many times the
             lucas(n) function should be called.

    :return: Print the all the numbers in lucas series from first to nth number.
    """
    if n<0:
        print ("You entered {}, That is not valid range, please select a positive number ".format(n))
    elif series == 'Fibonacci' or series == 'Lucas':
        print()
        print (series,'sequence:', end=' ')
        for i in range(0,n+1):
            if series == 'Fibonacci':
                print(fibonacci(i), end=' ')
            elif series == 'Lucas':
                print(lucas(i),end=' ')
    else:
        print(series, 'is not valid option, Valid options:\'Fibonacci\' or \'Lucas\' ')



def other_series(n, first, second):
    """

    :param n: Define nth value in the series

    :param first: First of the two optional parameters have default values of 0
                  and will determine the first values for the series to be produced.

    :param second: Second of the two optional parameters have default values of 1
                   and will determine the second values for the series to be produced.

    :return: Print all the numbers in the series from first to nth number.
    """
    if n==0:
        return first
    elif n==1:
        return second
    else:
        return other_series(n-1, first, second) + other_series(n-2, first , second)


def sum_series(n, first = 0, second = 1):
    """

    :param n: Define nth value in the fibonacci or lucas series
              sum_series(n, first = 0, second = 1) will print all the numbers in the fibonacci series from first to nth number.
              sum_series(n, first = 2, second = 1) will print all the numbers in the Lucas series from first to nth number.

    :param first: First of the two optional parameters have default values of 0
                  and will determine the first values for the series to be produced.

    :param second: Second of the two optional parameters have default values of 1
                   and will determine the second values for the series to be produced.

    :return: Print all the numbers in the fibonacci,Lucas or other series from first to nth number.
    """
    if n<0:
        print ("You entered {}, That is not valid range, please select a positive number ".format(n))
    elif first == 0 and second == 1:
        return fibonacci(n)
    elif first == 2 and second == 1:
        return lucas(n)
    else:
        return other_series(n, first, second)

def testing():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")

if __name__ == "__main__":
    # print (fibonacci(5))
    # print (sum_series(5))
    testign()

