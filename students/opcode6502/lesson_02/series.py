# series.py
# opcode6502
#
# REQ-01: Create a new module series.py in the lesson02 folder in your
# student folder. [ note: This file. ]


# REQ-02: In it, add a function called fibonacci.
# REQ-03: The function should have one parameter n.
def fibonacci(n):

    # REQ-05: Ensure that your function has a well-formed docstring.
    """ Compute and return the nth Fibonacci number """

    # Check if (n == 0) or (n == 1)
    if n < 2:
        return n
    else:
        # REQ-04: The function should return the nth value in the
        # fibonacci series (starting with zero index).
        return fibonacci(n - 2) + fibonacci(n - 1)


# REQ-06: In your series.py module, add a new function lucas that returns the
# nth value in the lucas numbers series (starting with zero index).
def lucas(n):

    # REQ-07: Ensure that your function has a well-formed docstring.
    """ Compute the return the nth Lucas number """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


# REQ-08: Add a third function called sum_series that can compute all of these
# related series.
def sum_series(n, n0=0, n1=1):

    # REQ-09: Ensure that your function has a well-formed docstring.
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
    get the fibonacci series.
    """

    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return (sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1))


# REQ-10: Add a block of code to the end of your series.py module.
# Use the block to write a series of assert statements that demonstrate that
# your three functions work properly.
if __name__ == "__main__":

    # Tests on fibonacci series for nth value
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Tests on lucas nth value
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    assert lucas(5) == 11

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
