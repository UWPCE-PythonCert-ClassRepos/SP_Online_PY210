#!/usr/bin/env python3


def main():

    # fibonacci tests
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3

    # lucas tests
    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(3) == 3
    assert lucas(4) == 4
    assert lucas(5) == 7

    # sum_series tests
    assert sum_series(1) == 0
    assert sum_series(2) == 1
    assert sum_series(3) == 1
    assert sum_series(4) == 2
    assert sum_series(5) == 3
    assert sum_series(6) == 5
    assert sum_series(20) == 4181

    assert sum_series(1, 2, 1) == 2
    assert sum_series(2, 2, 1) == 1
    assert sum_series(3, 2, 1) == 3
    assert sum_series(4, 2, 1) == 4
    assert sum_series(5, 2, 1) == 7
    assert sum_series(20, 2, 1) == 9349

def fibonacci(n):
    '''
    :param n: the nth element of the fibonacci sequence e.g. n=5 is 3 [0, 1, 1, 2, 3, ... ]
    :return: the nth element of fibonacci sequence
    '''
    return sum_series(n)


def lucas(n):
    '''
    :param n: the nth element of the lucas sequence e.g. n=5 is 7 [2, 1, 3, 4, 7, ...]
    :return: the nth element of the lucas sequence
    '''
    return sum_series(n, 2, 1)


def sum_series(n, first=0, second=1):
    '''
    :param n: the nth element of a sequence
    :param first seed of recursive series
    :param second seed of recursive series
    :return: the nth element of sequence: fibonacci, lucas or otherwise specified
    '''
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)