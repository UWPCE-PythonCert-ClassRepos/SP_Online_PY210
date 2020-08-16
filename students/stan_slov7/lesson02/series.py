#!/usr/bin/env python3

def fibonacci(n):
    """ compute the nth Fibonacci number """
    if n<0:
        return None
    elif 0<=n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    """ compute the nth Lucas number """
    if n<0:
        return None
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    Generalized function for computing nth value of a summation series for any 
    first two numbers in the zeroth and first index position of series with default
    params representing the Fibonacci(n) function with params n0=0, n1=1.
    
    Thus, sum_series(n, 0, 1) would be equivalent to Fibonacci(n), 
    while sum_series(n, 2, 1) would be equivalent to Lucas(n).

    sum_series(n, 3, 2) would then generate a different series starting with values
    n0=3, n1=2

    """
    if n<0:
        return None
    elif n==0:
        return n0
    elif n==1:
        return n1
    elif n==2:
        return(n0 + n1)  #gives recursive end case for general sum_series
    else:
        return(sum_series((n-1), n0, n1) + sum_series((n-2), n0, n1))  


#test print for some n values
print("Fibonacci(5): computing 5th Fibonacci number...\n")
print(fibonacci(5))
print()

print("Lucas(5): computing 5th Lucas number...\n")
print(lucas(5))
print()

print("sum_series(5): computing 5th number using sum_series(n) function "
      "with default starting params n0=0, n1=1 same as for Fibonacci(n) series...\n")
print(sum_series(5))
print()

print("sum_series(5,4,3): computing 5th number using sum_series(n) function of a "
      "general series with starting params now set to n0=4, n1=3 ...\n")
print(sum_series(5,4,3))
print()

if __name__ == "__main__":

    # Fibonacci(n) asserts
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    
    # Lucas(n) asserts
    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7
    
    # Now add some asserts verifying generalized sum_series works as expected
    # test that sum_series matches Fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matches Lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for other arbitrarily chosen starting values of n0 and n1 
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")