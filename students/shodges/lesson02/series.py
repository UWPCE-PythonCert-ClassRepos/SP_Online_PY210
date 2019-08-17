#!/usr/bin/env python3

def fibonacci(n):
    """Returns the nth element of the fibonacci sequence.  Note that n is 0-based."""
    return sum_series(n)

def lucas(n):
    """Returns the nth element (0-based) of the lucas numbers."""
    return sum_series(n, 2, 1)

def sum_series(n, a = 0, b = 1):
    """Returns the nth element (note: n is 0-based) of the fibonacci series.

    Specifying a and b will override the default start points of the series.
    """
    if n == 0: return a
    elif n == 1: return b
    else:
        for i in range(2,n+1):
            tempsum = a + b
            a = b
            b = tempsum
        return tempsum

if __name__ == "__main__":
    # Since fibonacci() and lucas() are just calling back to sum_series(), let's validate that they're calling the correct start points
    assert fibonacci(7) == sum_series(7, 0, 1)
    assert lucas(12) == sum_series(12, 2, 1)

    # Validate the first few elements of the Fibonacci sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Validate the first few elements of the Lucas numbers
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # Validate the first few elements of a series with arbitrary start points
    assert sum_series(0, 3, 8) == 3
    assert sum_series(1, 3, 8) == 8
    assert sum_series(2, 3, 8) == 11
    assert sum_series(3, 3, 8) == 19
    assert sum_series(4, 3, 8) == 30
    assert sum_series(5, 3, 8) == 49
    assert sum_series(6, 3, 8) == 79
    assert sum_series(7, 3, 8) == 128

    print("Test cases passed!")
