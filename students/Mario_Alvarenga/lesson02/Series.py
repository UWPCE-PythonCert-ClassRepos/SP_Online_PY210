#!/usr/bin/env python3
#Mario Alvarenga
#Lesson02
#Series

def fibonacci(n):
    '''
        This function accepts a variable n, which determines which term
        of the fibonacci series the user wants to return. The function defines the
        variables n1, n2, and nthTerm, then uses a for loop to calculate a fibonacci
        series and prints the nth term based on the function parameter
    '''
    n1, n2 = 0, 1
    nthTerm = n - 1
    if (n == 0 or n == 1):
        return n
    else:
        for i in range(n):
            next_number = (n1 + n2)
            n1 = n2
            n2 = next_number
            if (i == nthTerm):
                return n1


def lucas(n):
    """ compute the nth Lucas number, similar to the fibonacci sequence but with different
     beginning numbers"""
    n1, n2 = 2, 1
    nthTerm = n - 1
    if (n == 0 or n == 1):
        return 2 - n
    else:
        for i in range(n):
            next_number = (n1 + n2)
            n1 = n2
            n2 = next_number
            if (i == nthTerm):
                return n1


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.
    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    sum_series(n, 3, 2) should generate antoehr series with no specific name
    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """
    nthTerm = n - 1
    if (n == 0):
        return n0
    elif (n == 1):
        return n1
    else:
        for i in range(n):
            next_number = (n0 + n1)
            n0 = n1
            n1 = next_number
            if (i == nthTerm):
                return n0


if __name__ == "__main__":
    #  run some tests
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