"""
series.py

Zach Meves
Python 210
Lesson 02
"""


def sum_series(n, first=0, second=1):
    """Returns the n-th value in a sum-series defined by

        :math:`f(n) = f(n-2) + f(n - 1)`

    with arbitrary 1st and 2nd numbers.

    Parameters
    ----------
    n : int
        Number in sequence to return, 1-indexed
    first : int
        First number in sequence
    second : int
        Second number in sequence

    Returns
    -------
    int
        n-th number in the sequence"""

    if n == 0:
        raise ValueError("This function uses 1-based indexing, not 0-based.")
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n-2, first, second) + sum_series(n-1, first, second)


def fibonacci(n):
    """Returns the n-th value in the Fibonacci sequence.

    Parameters
    ----------
    n : int
        Value in sequence to return, 1-based

    Returns
    -------
    int
        The n-th value"""

    return sum_series(n, 0, 1)


def lucas(n):
    """Returns the n-th value in the Lucas sequence.

    Parameters
    ----------
    n : int
        Value in sequence to return, 1-based

    Returns
    -------
    int
        The n-th value"""

    return sum_series(n, 2, 1)


if __name__ == "__main__":
    """Test series."""

    # Test Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, ...)
    _fib_true = (0, 1, 1, 2, 3, 5, 8, 13, 21)
    # Iterate over Fibonacci sequence, testing the function
    # returns the true value
    print('Testing fibonacci')
    for i, val in enumerate(_fib_true):
        assert fibonacci(1 + i) == val

    # Test Lucas sequence (2, 1, 3, 4, 7, 11, 18, 29, ...)
    _lucas_true = (2, 1, 3, 4, 7, 11, 18, 29)
    # Iterate over Lucas sequence, testing the function
    # returns the true value
    print('Testing lucas')
    for i, val in enumerate(_lucas_true):
        assert lucas(1 + i) == val

    # Test general sum_series function
    print('Testing sum_series')
    for i, val in enumerate(_fib_true):
        assert sum_series(i + 1) == val
    for i, val in enumerate(_lucas_true):
        assert sum_series(i + 1, 2, 1) == val

    # Create other generic sequences
    for i in range(10):
        assert sum_series(i + 1, 0, 0) == 0

    _s_ = [0, 3, 3, 6, 9, 15]
    for i, val in enumerate(_s_):
        assert sum_series(i + 1, 0, 3) == val
