# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:43:39 2019

Author: Philip Behrend
"""

def fibonacci(n):
    """Returns the nth fibonacci number"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0,1]
        for i in range(n-2):
            fib.append(fib[i]+fib[i+1])
        return fib[-1]

def lucas(n):
    """Returns the nth lucas number"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = [2,1]
        for i in range(n-2):
            lucas.append(lucas[i]+lucas[i+1])
        return lucas[-1]
    
def sum_series(start,n):
    """This function generalizes fibonacci formula based on different starting numbers"""
    if n == 0:
        return start
    elif n == 1:
        return 1
    else:
        lucas = [start,1]
        for i in range(n-2):
            lucas.append(lucas[i]+lucas[i+1])
        return lucas[-1]    
    
