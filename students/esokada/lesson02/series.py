def fibonacci(n):
    """Return the nth number of the Fibonacci series."""
    if n is 0:
        return 0
    if n is 1:
        return 1
    if n is 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return the nth number of the Lucas Numbers."""
    if n is 0:
        return 2
    if n is 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, firstval=0, secondval=1):
    """Return the nth number of a series starting with the values firstval and secondval."""
    if n is 0:
        return firstval
    if n is 1:
        return secondval
    else:
        return sum_series(n-1, firstval, secondval) + sum_series(n-2, firstval, secondval)


# block of tests using assert (from series_template.py)

if __name__ == "__main__":
    # test fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # test lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # make sure that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # make sure that sum_series matches lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test sum_series with other values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")