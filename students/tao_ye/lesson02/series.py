def sum_series(n, zero=0, one=1):
    """
    compute the nth value of a summation series.

    :param n: (int) nth index of the numbers series
    :Param zero: (int) 0th value of the numbers series
    :Param one: (int) 1th value of the numbers series
    :return: (int) nth value of the numbers series
    
    """
    
    n=int(n)
    
    if (n == 0):
        return zero
    elif (n == 1):
        return one
    elif (n >= 2):
        return sum_series(n-2, zero, one) + sum_series(n-1, zero, one)
    else:
        print("Error: n should be a positive integer")

def fibonacci(n):
    """
    compute Fibonacci series

    :param n: (int) nth index of the Fibonacci series
    :return: (int) nth value of the numbers series
    
    """
    
    return(sum_series(n))

def lucas(n):
    """
    compute Lucas numbers series

    :param n: (int) nth index of the Lucas numbers series
    :return: (int) nth value of the numbers series
    
    """
    
    return(sum_series(n,2,1))
        
        
if (__name__ == "__main__"):

    # run some tests to check the results
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
