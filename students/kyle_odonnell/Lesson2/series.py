# ------------------------------------------------------------------------ #
# Title: Fibonacci Series
# Description: Introduction to Python: Lesson 2 Exercise 2.4
# ChangeLog:
# KODonnell,10.14.2020,Created script
# KODonnell,10.17.2020,Updated comments and docstrings
# ------------------------------------------------------------------------- #

def fibonacci(n):
    """
    compute the nth Fibonacci number
    :param n: index of fibonacci sequence to calculate
    :return: nth number of Fibonacci Sequence
    """
    return sum_series(n)  # Call sum_series with default arguments

def lucas(n):
    """ compute the nth Lucas number
    :param n: index of Lucas sequence to calculate
    :return: nth number of Lucas Sequence
    """

    return sum_series(n,2,1)  # Call sum_series with 2,1 as start of sequence

def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.
    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    """

    fib = [n0,n1]
    for i in range(2,n+1):
            fib.append(fib[-1]+fib[-2])
    return fib[n]


# Confirm functions run as expected
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