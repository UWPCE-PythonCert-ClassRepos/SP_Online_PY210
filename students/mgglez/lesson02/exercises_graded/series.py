#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Exercise 2.2 - Fibonacci and Lucas Series
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-02-2020, Created Fibonacci & Lucas Function
# ---------------------------------------------------------------------------- #

def fibonacci(n):
    """
    Compute the nth Fibonacci number

    :param n: (int) nth element from Fibonacci Series (starting with zero index)
    :return: (int) Value from the nth element from Fibonacci Series
    """
    return sum_series(n)


def lucas(n):
    """
    Compute the nth Lucas number

    :param n: (int) nth element from Lucas Series (starting with zero index)
    :return: (int) Value from the nth element from Lucas Series
    """
    return sum_series(n, 2, 1)


def sum_series(n, zero_index=0, one_index=1):
    """
    Compute the nth value of a summation series.

    :param zero_index=0: value of zeroth element in the series
    :param one_index=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate another series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci series
    """
    if n < 0:
        print("Incorrect element index provided. It must be greater than or equal to zero")
    elif n == 0:
        return zero_index
    elif n == 1:
        return one_index
    else:
        return sum_series(n - 1, zero_index, one_index) + sum_series(n - 2, zero_index, one_index)


if __name__ == '__main__':
    n = int(input("\nWhich value from the Fibonacci series do you want to obtain? n = "))
    print("nth Fibonacci number is: ", fibonacci(n))
    fibonacci_series = [fibonacci(i) for i in range(n + 1)]
    print(f"Fibonacci series up to the {n} value: {fibonacci_series}")

    n = int(input("\nWhich value from the Lucas series do you want to obtain? n = "))
    print("nth Lucas number is: ", lucas(n))
    lucas_series = [lucas(i) for i in range(n + 1)]
    print(f"Lucas series up to the {n} value: {lucas_series}")

    print("\nRunning some tests ...")
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

    print("\ntests passed")


