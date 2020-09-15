# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:11:54 2020

@author: jaked

series.py
"""

def fibonacci(n):
    """returns nth fibonacci number.
    1st 2 numbers are set to 0 and 1"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

print(lucas(4))

# def sumseries(n, n0, n1):
#     if n0==0:
#         return 0
#     elif n1==1:
#         return 1
#     else:
#         return sumseries(n-1)+sumseries(n-2)

# print(sumseries(5, 3, 2))