# -*- coding: utf-8 -*-
"""
fibonacci.py

@author: Grant Dowell

Excercise 2.4 - Fibonacci Series
"""

def fibonacci(n):
    """Return the nth value of the fibonacci sequence"""
    if n == 0:
        nth = 0
    elif n ==1:
        nth = 1
    else:
        nth = fibonacci(n-2) + fibonacci(n-1)
    return nth

def lucas(n):
    """Return the nth value of the lucas sequence"""
    if n == 0:
        nth = 2
    elif n == 1:
        nth = 1
    else:
        nth = lucas(n-2) + lucas(n-1)
    return nth

def sum_series(n,n0=0,n1=1):
    """
    Returns the nth value of a sequence defined by the addition of the
    previous two elements. Defaults to the fibonacci sequence, but allows the
    user to specify a different sequence.
    
    n: The index of the sequence you are requesting.
    n0=0: Optional parameter for the first value of the sequence.
    n1=1: Optional parameter for the second value of the sequence.
    """
    if n == 0:
        nth = n0
    elif n == 1:
        nth = n1
    else:
        nth = sum_series(n-2,n0,n1)+sum_series(n-1,n0,n1)
    return nth

if __name__ == '__main__':
    #### Build Assert Tests ####
    
#    for n in range(8):
#        print(fibonacci(n))
        
#    for n in range(8):
 #       print(lucas(n))
 
#     for n in range(8):
#         print(sum_series(n))
 
     for n in range(8):
         print(sum_series(n,n0=2,n1=1))