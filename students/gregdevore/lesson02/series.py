# Module for Fibonacci series and Lucas numbers
# Also includes function for general summation series (specify first two terms)

def fibonacci(n):
    """ Return the nth number in the Fibonacci series (starting from zero index)

    Parameters:

    n : integer
        Number in the Fibonacci series to compute

    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """ Return the nth Lucas number (starting from zero index)

    Parameters:

    n : integer
        Lucas number to compute

    """
    # Base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        # Recursive case
        return lucas(n-1) + lucas(n-2)

def sum_series(n, n0=0, n1=1):
    """ Return the nth term in the summation series starting with
    the terms n0 and n1. If first two terms are not specified, the
    Fibonacci series is printed by default.

    Parameters:

    n : integer
        The number in the summation series to compute

    Keyword arguments:

    n0 : The first term in the series (default 0)

    n1 : The second term in the series (default 1)

    """

    # Base cases
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        # Recursive case
        return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)

if __name__ == "__main__":
    # Run some tests

    # Fibonacci series
    # Assert first 10 terms are correct
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34

    # Lucas numbers
    # Assert first 10 terms are correct
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    assert lucas(9) == 76

    # Sum series
    # Make sure defaults are for Fibonacci series
    assert sum_series(4) == fibonacci(4)
    # Make sure entering Lucas number values generates correct term
    assert sum_series(4, 2, 1) == lucas(4)

    print("All tests passed")
