def fibonacci(n):
    """Return the nth value in the fibonacci series starting with zero index.
       :param n: The Nth value to return from the series.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """Return the Nth value of the Lucas Series
    :param n: The Nth value to return from the series.
    """
    if n ==0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return lucas(n-2) + lucas(n-1)


def sum_series(n,n0=0,n1=1):
    """Return the Nth value of a number series.
    :param n: The Nth value to return from the series.
    :param y: The first number in the series.
    :param z: The second number in the series.

    The defaults are set to 0, 1, to
    get the fibonacci series
    """
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2,n0,n1) + sum_series(n-1,n0,n1)





if __name__ == "__main__":
    #run some tests
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(8) == 47
    assert lucas(3) == 4
    assert lucas(5) == 11

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert sum_series(5) == fibonacci(5)
    assert sum_series(7,0,1) == fibonacci(7)


    assert sum_series(5,2,1) == lucas(5)
    assert sum_series(8,2,1) == 47

    # test if sum_series works for arbitrary initial values
    assert sum_series(0,3,2) == 3
    assert sum_series(0, 3, 2) == 3
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19



