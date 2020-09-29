"""Lesson 02 | Fibonacci Series Exercise"""
# The Fibonacci Series is a numeric series starting with the integers 0 and 1.
# In this series, the next integer is determined by summing the previous two.
#
# This gives us: 0, 1, 1, 2, 3, 5, 8, 13, ...
# We will write a function that computes this series – then generalize it.

# fib(n) = fib(n-2) + fib(n-1)

def fibonacci(n):
    """ compute the nth Fibonacci number """
    # pass
    return sum_series(n,0,1)

def lucas(n):
    """ compute the nth Lucas number """
    # pass
    return sum_series(n,2,1)

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
    # pass
    series = [n0, n1]
    for x in range(2,n+1):
        series.append(series[x-2] + series[x-1])
    return series[n]

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

    assert sum_series(5) == fibonacci(5)
    assert sum_series(5,0,1) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
