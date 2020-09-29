#
# Author: Brian Minsk

def fibonacci (n):
    """Return the nth value (starting with 1) of a Fibonacci series. A Fibonacci series is computed by 
    fib(n) = fib(n-2) + fib(n-1)
    where fib(1) is 0 and fib(2) is 1

    Keyword arguments:
    n -- how far to go in the series to find the value to return, for example if n is 7 it would be the 7th number in the sequence
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas (n):
    """Return the nth value (starting with 1) of a Lucas Numbers sequence. A Lucas Numbers sequence is computed by 
    fib(n) = fib(n-2) + fib(n-1)
    where fib(1) is 2 and fib(2) is 1

    Keyword arguments:
    n -- how far to go in the sequence to find the value to return, for example if n is 7 it would be the 7th number in the sequence
    """
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2) 

def sum_series (n, n1 = 0, n2 = 1):
    """Return the nth value (starting with 1) of a sequence computed by the following
    fib(n) = fib(n-2) + fib(n-1)
    where fib(1) is first and fib(2) is second

    Keyword arguments:
    n -- how far to go in the sequence to find the value to return, for example if n is 7 it would be the 7th number in the sequence
    n1 -- first number in the sequence (default is 0, which is the first number in a Fibonacci sequence)
    n2 -- second number in the sequence (default is 1, which is the first number in a Fibonacci sequence)
    """
    if n == 1:
        return n1
    if n == 2:
        return n2
    return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2) 

if __name__ == "__main__":
    # run some tests
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13

    assert lucas(1) == 2
    assert lucas(2) == 1

    assert lucas(5) == 7

    #test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)
    
    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(1, 3, 2) == 3
    assert sum_series(2, 3, 2) == 2
    assert sum_series(3, 3, 2) == 5
    assert sum_series(4, 3, 2) == 7
    assert sum_series(5, 3, 2) == 12
    assert sum_series(6, 3, 2) == 19

    print("tests passed")
