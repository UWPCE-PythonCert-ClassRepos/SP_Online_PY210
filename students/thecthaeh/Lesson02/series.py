#!/usr/bin/env python3
    
def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    if n == 0:
        return 0
        
    elif n == 1:
        return 1
        
    return fibonacci(n - 2) + fibonacci(n - 1)    



def lucas(n):
    """ Return the nth value in the lucas series."""
    if n == 0:
        return 2
        
    elif n == 1:
        return 1
        
    return lucas(n - 2) + lucas(n - 1)


def sum_series(n, index0 = 0, index1 = 1):
    """ Return the nth value in any sum series.
    
    n - the element to return 
    index0 - the 0th element (default to 0)
    index1 - the 1st element (default to 1)
    
    Using the default values for the optional arguments should return the fibonacci series.
    """
    if n == 0:
        return index0
       
    elif n == 1:
        return index1
        
    return sum_series(n - 2, index0, index1) + sum_series(n - 1, index0, index1)
    
if __name__ == "__main__":
    # test the fibonacci and lucas series'
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    
    assert fibonacci(6) == 8
    assert fibonacci(8) == 21
    
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    
    assert lucas(5) == 11
    assert lucas(7) == 29
    
    # test that sum_series matches fibonacci
    assert sum_series(4) == fibonacci(4)
    assert sum_series(5, 0, 1) == fibonacci(5)
    
    # test that sum_series matches lucas
    assert sum_series(4, 2, 1) == lucas(4)
    
    # test that sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19
    
    print("tests passed")