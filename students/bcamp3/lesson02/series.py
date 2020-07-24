#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth value in the fibonacci series (starting with zero index)
    
    """
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    

def lucas(n):
    """Return the nth value in the lucas numbers series (starting with zero index)
    
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    

def sum_series(n,zero_val=0,one_val=1):
    """Return fibonacci sequence with no optional parameters
    sum_series(n, 0, 1) should be equivalent to fibonacci(n)
    sum_series(n, 2, 1) should be equivalent to lucas(n)
    
    :param n: integer, The nth element of the sum series to compute, starting with zero (0)
    
    :param zero_val=0: integer, The sum series value for the first element in the series
    
    :param one_val=1: integer, The sum series value for the second element in the series
    
    """
    if n==0:
        return zero_val
    elif n==1:
        return one_val
    else:
        return sum_series(n-1,zero_val,one_val) + sum_series(n-2,zero_val,one_val)
    

def print_sum_series(n=7,zero_val=0,one_val=1):
    """print sum_series result for range(n)"""
    for i in range(n):
        print(sum_series(i,zero_val,one_val))
        

if __name__ == "__main__":
    # Run test cases
    
    # Fibonacci series
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    
    # Lucas series
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    assert lucas(9) == 76
    
    # Sum series
    # Makem sure defaults return Fibonnaci series
    assert sum_series(4) == fibonacci(4)
    # Make sure Lucas number values returns correct result
    assert sum_series(4,2,1) == lucas(4)
    
    print("tests passed")