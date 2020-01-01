#!/usr/bin/env python3


def main():
    """Test that all functions return the correct values."""
    # fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # sum_series function
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19


def fibonacci(n):
    """Return the Nth value in the fibonacci series."""
    return sum_series(n)


def lucas(n):
    """Return the Nth value in the lucas numbers series."""
    return sum_series(n, first=2, second=1)


def sum_series(n, first=0, second=1):
    """
    Recursively calculates the Nth value in a sum series given the first two
    values in the series. Defaults to the Fibonacci series.

    :param n: The Nth element of the series
    :param first: The first element of the series, defaults to 0
    :param second: The second element of the series, defaults to 1
    :return: The Nth element of the series
    """
    if n < 0:
        print("ERROR: Cannot use negative numbers.")
        exit(1)
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-2, first, second) + sum_series(n-1, first, second)


if __name__ == "__main__":
    main()
