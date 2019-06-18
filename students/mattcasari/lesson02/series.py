#!/usr/bin/env python3
""" Lesson 2, Excercise 3

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fib_and_lucas.html

Part 1: Create a Fibonacci Sequence function
Part 2: Create a Lucas Series Function
Part 3: Create a Summation Series function and simplify the Fibonacci and Lucas Series with it

"""
def sum_series(n, n0=0, n1=1):
    """ Compute the nth value of the summation series

    This function generalizes the Fibonacci and Lucas series, allowing
    for the user to set the first two numbers in the series.  
    Args: 
        n: nth value of the summation series to computer
        n0: the value for n[0]
        n1: the value for n[1]

    Returns:
        Computed value for nth value of summation series
    """
    if n < 0:
        pass
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)

def fibonacci(n):
    """ Compute the nth Fibonacci number """
    return sum_series(n)   


def lucas(n):
    """ Compute the nth Lucas number """
    return sum_series(n,2,1)


if __name__ == "__main__":

     # Test the Fibonacci Sequence
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(6) == 8)
    assert(fibonacci(7) == 13)

    # Test the Lucas Series
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # Test the Summation Series
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19