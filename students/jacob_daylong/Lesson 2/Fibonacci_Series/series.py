# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:11:54 2020

@author: jaked

series.py
"""

def sum_series(n, n0=0, n1=1):
    """
    Sums a series of numbers regardless of start point.
    Check built in for fibonacci, default with only 1 argument, Lucas requires arguments.
    """

    if n==0:
        return n0
    elif n==1:
        return n1
    else:
        return sum_series(n-1, n0, n1)+sum_series(n-2, n0, n1)
    pass

def fibonacci(n):
     """
     Returns nth fibonacci number.
     Calls sumseries with default starting values: 0, 1
     Original logic of fibonacci is retained on block coment below
     """

    #original logic for fibonacci
     '''
     if n==0:
         return 0
     elif n==1:
         return 1
     else:
         return fibonacci(n-1)+fibonacci(n-2)
     '''

     return sum_series(n)
     pass

def lucas(n):
    """
    Returns lucas numbers.
    Calls sumseries with starting values: 2, 1
    Original logic of fibonacci is retained on block coment below
    """

    #original logic for lucas
    '''
    if n==0:
         return 2
     elif n==1:
         return 1
     else:
         return lucas(n-1)+lucas(n-2)
    '''

    return sum_series(n, n0=2, n1=1)
    pass

"""
Test block
"""

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