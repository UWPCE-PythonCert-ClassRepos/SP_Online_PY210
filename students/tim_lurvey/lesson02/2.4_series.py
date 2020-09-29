#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

import sys


def sum_series(n, primer=(0, 1)):
    """This function returns the nth values in an lucas sequence where n is sum of the two previous terms.
    :param n:       nth value to be returned from the sequence
    :type n:        int
    :param primer:  the first 2 integers of the sequence to be returned. (optional), default=(0,1)
    :type primer:   sequence

    :returns:       the nth position in the sequence
    :rtype:         int"""
    #
    # test variable
    #
    try:
        assert (isinstance(n, int))
        assert (n >= 0)
    except AssertionError:
        raise TypeError("n type must be a positive integer") from None
    #
    try:
        assert (all([isinstance(x, int) for x in primer]))
    except AssertionError:
        raise TypeError("primer must be a sequence of integers") from None
    #
    # working function
    #
    if n < 2:
        return primer[n]
    else:
        return sum_series(n=(n - 2), primer=primer) + sum_series(n=(n - 1), primer=primer)


def fibonacci(n):
    """fibonacci(n) -> return the nth value in a fibonacci sequence"""
    return sum_series(n=n, primer=(0, 1))


def lucas(n):
    """lucas(n) -> return the nth value in a lucas sequence"""
    return sum_series(n=n, primer=(2, 1))


def tests():
    nFibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    for i in range(len(nFibonacci)):
        assert (fibonacci(i) == nFibonacci[i])
    print("Fibonacci test passed")
    #
    nLucas = [2, 1, 3, 4, 7, 11, 18, 29]
    for i in range(len(nLucas)):
        assert (lucas(i) == nLucas[i])
    print("Lucas test passed")
    #
    primerCustom = (4, 3)
    nCustom = [4, 3, 7, 10, 17, 27, 44]
    for i in range(len(nCustom)):
        assert (sum_series(i, primer=primerCustom) == nCustom[i])
    print("Custom (4,3) test passed")
    #
    # sum_series(3, primer="a")       #fail
    # sum_series(3, primer=("a"))     #fail
    # sum_series(-12)                 #fail
    # sum_series("a")                 #fail
    return True


def main(args):
    tests()


if __name__ == '__main__':
    main(sys.argv[1:])
