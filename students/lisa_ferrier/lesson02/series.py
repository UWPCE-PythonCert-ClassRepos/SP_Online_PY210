# series.py
# Lisa Ferrier, Python 201, Lesson 02


def fibonacci(n):
    """
    Calculates the fibonacci value for an integer supplied by a user. Sequence
    begins at zero. Input value must be >=0. Function calls sum_series and
    accepts the default starting values (0,1) to initiate the sequence.
    """
    return sum_series(n)
    pass


def lucas(n):
    """
    Calculates the lucas value for an integer supplied by a user. Input value
    must be >=0. Function calls sum_series function and sets the first two
    values (2,1) to initiate the sequence.
    """
    return sum_series(n, 2, 1)
    pass


def sum_series(n, a=0, b=1):
    """
    Computes the nth value of a summation series.

    :param a=0: value of zeroth element in the series
    :param b=1: value of first element in the series
    Defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci series
    """
    if n < 0:
        print('Input must be >=0.')
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-1, a, b)+sum_series(n-2, a, b)
    pass


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
