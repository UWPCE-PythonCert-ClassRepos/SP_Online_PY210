#### Series Functions ####

def fibonacci(n):
    """Function computes the nth value in the Fibonacci 
    series"""

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Function that computes the nth value in the Lucas Number
    series"""

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n_0 = 0, n_1 = 1):
    """This computes the nth value in a series with the nth
    value = f(n-1) + f(n-1)."""

    """The parameters n_0 and n_1 are set by default for a 
    Fibonacci series.  You can specify them for a Lucas
    series or any other series."""

    if n == 0:
        return n_0
    elif n == 1:
        return n_1
    else:
        return sum_series(n-1, n_0, n_1) + sum_series(n-2, n_0, n_1)


# Run tests on functions to see if they work

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

    print("tests passed")
