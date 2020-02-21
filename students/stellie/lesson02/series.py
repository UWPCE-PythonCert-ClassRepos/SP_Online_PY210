# Fibonacci Series
def fibonacci(n):
    """
    Returns the nth value in the Fibonacci series (starting with zero index).
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Lucas Numbers
def lucas(n):
    """
    Returns the nth value in the Lucas Numbers series (starting with
    zero index).
    """
    if n == 0:
        return 2
    elif n == 1:
        return n
    else:
        return lucas(n - 2) + lucas(n - 1)


# Sum Series
def sum_series(n, x=0, y=1):
    """
    Calling this function with no optional parameters will produce numbers
    from the Fibonacci series (because 0 and 1 are the defaults). Calling
    it with the optional arguments 2 and 1 will produce values from the Lucas
    Numbers.
    """
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 2, x, y) + sum_series(n - 1, x, y)


# Tests
if __name__ == "__main__":
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

    print("tests passed")
