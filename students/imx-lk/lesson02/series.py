#!/usr/bin/env python3

"""
a template for the series assignment
"""


def fibonacci(n):
    '''Takes in a number n, returns the nth value of the fibonacci series'''
    return (sum_series(n))


def lucas(n):
   '''Takes in a number n , and returns the nth value and the optional arguments of 2 and 1 of the Lucas series'''
   return (sum_series(n,2,1))


def sum_series(n, n_zero=0, n_one=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n). Make sure you use this as your return
    values for the functions above

    sum_series(n, 3, 2) should generate antoehr series with no specific names

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    ******* EQUATION : fib(n) = fib(n-2) + fib(n-1) ******
    """

    if (n == 0):
        return n_zero
    elif (n == 1):
        return n_one
    elif (n >= 2):
        return sum_series(n-2, n_zero, n_one) + sum_series(n-1, n_zero, n_one)




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

