def fibonacci(n):
    """Return nth integer in the Fibonacci series starting from index 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Return nth integer in the Lucas series starting from index 0."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first_value = 0, second_value = 1):
    """
    Return nth integer in a custom series starting from index 0 and parameters for the first and second series values.

    Arguments:
        
        first_value = 0; value at index n=0 of series
        second_value = 1; value at index n=1 of series
    
    This function provides a generalized version of the Fibonacci and Lucas integer series by allowing the user to
    input the first two numbers of the series.

    The default values of the first and second values of the series are 0 and 1, respectively, which are the first
    two values of the Fibonacci series.
    """
    if n == 0:
        return first_value
    elif n == 1:
        return second_value
    else:
        return sum_series(n - 1, first_value, second_value) + sum_series(n - 2, first_value, second_value)

if __name__ == "__main__":
    # run tests on fibonacci and lucas functions
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

    # run tests on sum_series function for arbirtary value inputs
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")