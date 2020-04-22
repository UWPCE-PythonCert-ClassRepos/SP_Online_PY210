# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:36:54 2020

@author: miriam
"""

# Fibonacci Series Exercise
def fibonacci(n):
    """Computes the nth value in the fibonacci series starting with zero index."""
    if n==0:
        return 0
    elif n==1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    pass 

# Lucas Numbers
def lucas(n):
    """Computes the nth value in the lucas number series starting with zero index."""
    if n==0:
        return 2
    elif n==1:
        return 1
    else: 
        return lucas(n-1) + lucas(n-2)
    
    pass

# Generalizing
def sum_series(n,n0=0, n1=1):
    """
    Computes the nth value in a series starting with zero index, 
    with one required parameter and two optional parameters.
    """
    if n==0:
        return n0
    elif n==1:
        return n1
    else: 
        return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)
    
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
