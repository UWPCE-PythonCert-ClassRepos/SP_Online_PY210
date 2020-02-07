#!/usr/bin/env python3

"""
Notes for the series assignment:
Fibonacci Series:
f(1) = 0
f(2) = 1
F(n)= F(n-1) + F(n-2)

Lucas Number Series:
f(1) = 2
f(2) = 1
F(n)= F(n-1) + F(n-2)

"""


def fibonacci(n):
    """
    Action to return the nth value in the fibonacci series
    :param n: the index number of the series for the value you would like to return. Starts with zero index
    :return: Returns the value of the nth index of the fibonacci series
    """
    if n < 0:
        print("not a valid number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Action to return the nth value in the Lucas Number series
    :param n: the index number of the series for the value you would like to return. Starts with zero index
    :return: Returns the value of the nth index of the Lucas Number series
    """
    if n < 0:
        print("not a valid number")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n0=None, n1=None):
    """
    Action to compute the nth value of a summation series. Default to generalize the fibonacci() function
    if optional parameters are not used or if optional parameters are set as n0=0 and n1=1. Default to generalize
    the lucas() function if the optional parameters are set as n0=2 and n1=1. Otherwise, generate series using optional
    parameters with the same formula of f(n)=f(n-1)+F(n-2)
    :param n:  The nth value of a summation series
    :param n0: The value of the zeroth element in the series
    :param n1: The value of the first element in the series
    :return: Returns the nth value of a summation series.
    """
    if (n0 == None and n1 == None) or (n0 == 0 and n1 == 1):
        return fibonacci(n)

    elif n0 == 2 and n1 == 1:
        return lucas(n)

    else:
        if n < 0:
            print("not a valid number")

        elif n == 0:
            return n0

        elif n == 1:
            return n1

        else:
            return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)


if __name__ == "__main__":
    # run some tests
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
