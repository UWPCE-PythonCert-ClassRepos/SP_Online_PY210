#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth value of the fibonacii sequence"""
    if n == 0:
        series = 0
    elif n == 1:
        series = 1
    else:
        series = 1
        previous = 0
        for i in range(1,n):
           temp_previous =  series
           series = series + previous
           previous = temp_previous
    return series

def lucas(n):
    """ Return the nth Lucas number """
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
    print("tests passed")