#-------------------------------------------#
#Tittle: series, PYTHON210
#Desc: Fibonacci function, Lucas function, and general sumation function.
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Oct-26>, created file
#-------------------------------------------#

def fibonacci(n):
    """Compute the nth Fibonacci number.

    Args:
        n (integer): Position in fibonacci series

    Returns:
        (integer): Value held at position n in the fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """Compute the nth Lucas number.

    Args:
        n (integer): Position in lucas series

    Returns:
        (integer): Value held at position n in the lucas series
    """
    #Lucas series position 0 is 2.
    if n == 0:
        return 2
    #Lucas series position 1 is 1.
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n, position_0 = 0, position_1 = 1):
    """Compute the nth value of a summation series.
    
    Computes the nth value of a summation series with defined values for
    position 0 and 1. The default values mimic the fibonacci series.

    Args:
        n (integer): Position in the series
        position_0 (integer): Default value at position 0
        position_1 (integer): Default value at position 1
    Returns:
        (integer): Value held at position n in the series
    """
    #Define series position 0.
    if n == 0:
        return position_0
    #Define series position 1.
    elif n == 1:
        return position_1
    else:
        #position_0 and position_1 are specified in the sum_series call so 
        #that defaults are not inserted when the function recalls itself.
        return sum_series(n-2, position_0, position_1) + sum_series(n-1, position_0, position_1)

if __name__ == "__main__":
    #Validate elements 0-7 of fibonacci().
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #Validate lucas()
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    #Test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    #Test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    #Test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")