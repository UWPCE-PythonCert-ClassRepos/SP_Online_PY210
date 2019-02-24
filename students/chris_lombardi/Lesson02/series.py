#UWPCE PY210
#Lesson02, Sum Series

def fibonacci(n):
    """Compute the nth fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
    """Compute the nth value lucas number"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))

def sum_series(n, first_val = 0, second_val = 1):
    """
    Return the nth value in a series based on set first and second value

    param first_val = 0: value of the zeroth element in the series
    param second_val = 1: value of the first element in the series

    This function generalizes the fibonacci() and lucas() so that the
    function works for any first two numbers in a sum series.
    sum_series(n, 0, 1) is equivalent to fibonacci(n).
    sum_series(n, 2, 1) is equivalent to lucas(n).
    """
    if n == 0:
        return first_val
    elif n == 1:
        return second_val
    else:
        return (sum_series(n-1,first_val,second_val) +
                sum_series(n-2, first_val, second_val))

if __name__ == "__main__":
    """Test the functions for expected values."""
    print("...Testing Fibonacci...")
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(9) == 34

    print("...Testing Lucas...")
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(7) == 29

    print("...Testing Sum Series...")
    assert sum_series(9) == fibonacci(9)
    #Test to see if sum_series works as a lucas series.
    assert sum_series(9, first_val = 2, second_val = 1) == lucas(9)
    assert sum_series(25, first_val = 2, second_val = 1) == lucas(25)
    print("Tests Pass")