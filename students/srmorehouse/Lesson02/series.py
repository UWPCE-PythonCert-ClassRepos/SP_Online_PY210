#!/usr/bin/env python3

"""
fibonacci

input: n : series in the fibonacci series

return: if 0, 0
        if 1, 1
        else (n-2)+(n-1)

No negative number error checking
"""


def fibonacci(n):
    if n == 0:
        retVal = 0
    elif n == 1:
        retVal = 1
    else:
        retVal = fibonacci(n - 2) + fibonacci(n - 1)
    return retVal


"""
lucas

input: n : series in the lucas series

return: if 0, 2
        if 1, 1
        else (n-2)+(n-1)

No negative number error checking
"""


def lucas(n):
    if n == 0:
        retVal = 2
    elif n == 1:
        retVal = 1
    else:
        retVal = lucas(n - 2) + lucas(n - 1)
    return retVal


"""
sum_series

inputs:
  n is the fibonacci/lucas series number
  firstVal is the optional zeroth value (default zero)
  secondVal is the optional first value (default one)

output:
  fibonacci (default)

No negative number error checking
"""

 
def sum_series(n, firstVal=0, secondVal=1):
    if n == 0:
        retVal = firstVal
    elif n == 1:
        retVal = secondVal
    else:
        retVal = sum_series(n - 2, firstVal, secondVal) + sum_series(n - 1, firstVal, secondVal)
    return retVal


if __name__ == '__main__':

    # print out values to verify
    for x in range(0, 10):
        print('fibonacci of ' + str(x) + ' is ' + str(fibonacci(x)))

    # now assert
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    for x in range(0, 10):
        print('fibonacci sum_series of ' + str(x) + ' is ' + str(sum_series(x)))

    # now assert sum_series
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(7) == 13

    for x in range(0, 10):
        print('lucas of ' + str(x) + ' is ' + str(lucas(x)))

    # now assert
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    for x in range(0, 10):
        print('lucas sum_series of ' + str(x) + ' is ' + str(sum_series(x, 2, 1)))

    # now assert sum_series
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    assert sum_series(3, 2, 1) == 4
    assert sum_series(4, 2, 1) == 7
    assert sum_series(5, 2, 1) == 11
    assert sum_series(6, 2, 1) == 18
    assert sum_series(7, 2, 1) == 29

    # run some more tests
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
