#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth value of the fibonacii sequence"""
    if n == 0:
        series = 0
    elif n == 1:
        series = 1
    else:
        series = 1
        previous = 0
        for i in range(1,n):
           temp_previous =  series
           series = series + previous
           previous = temp_previous
    return series

def lucas(n):
    """ Return the nth Lucas number """
    if n == 0:
        series = 2
    elif n == 1:
        series = 1
    else:
        series = 1
        previous = 2
        for i in range(1,n):
           temp_previous =  series
           series = series + previous
           previous = temp_previous
    return series
    
def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n == 0:
        series = n0
    elif n == 1:
        series = n1
    else:
        series = n1
        previous = n0
        for i in range(1,n):
           temp_previous =  series
           series = series + previous
           previous = temp_previous
    return series
    
if __name__ == "__main__":
    # run some tests
    # check fibonacci values
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    
    # check lucas values
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    
    # check if sum_series without optional params equals fibonacci
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    
    # let user know if all tests passed
    print("tests passed")