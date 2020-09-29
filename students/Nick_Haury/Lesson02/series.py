'''
module containing functions which return the nth value of different
summation sequences, where each number is the sum of the two preceding
numbers in the series; probably the most well known being the Fibonacci
sequence (0, 1, 1, 2, 3, 5, 8, 13, etc.).  A general function sum_series
can be called with parameters for the first and second number in the
series.  
'''

def fibonacci(n):
    '''
    returns nth number of sum_series with starting series values of 0, 1
    better known as the fibonacci sequence
    '''    
    return sum_series(n)

def lucas(n):
    '''
    returns nth number of sum_series with starting series values of 2, 1
    better known as the lucas sequence
    '''
    return sum_series(n, 2, 1)

def sum_series(n, num0 = 0, num1 = 1):
    '''
    Returns the "nth" number in an arithmatic series where each number is
    the sum of the two preceding numbers in the series. The parameters
    num0 and num1 being the first and second number in the sequence.  If no
    optional parameters are given, the first and second numbers default to
    0 and 1, which is identical to the fibonacci sequence.
    '''
    if n == 0:
        return num0
    if n == 1:
        return num1
    else:
        return sum_series(n - 2, num0, num1) + sum_series(n - 1, num0, num1)

if __name__ == "__main__":
    # test first few numbers in fib sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5

    # test first few numbers in lucas sequence
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11

    # test that sum_series matches fibonacci
    assert sum_series(10) == fibonacci(10)
    assert sum_series(8, 0, 1) == fibonacci(8)

    # test that sum_series matches lucas
    assert sum_series(4, 2, 1) == lucas(4)

    # test if sum_series works for different inital values than fib or lucas
    assert sum_series(0, 1, 2) == 1
    assert sum_series(3, 2, 1) == 4
    assert sum_series(2, 4, 6) == 10

    print("tests passed")
