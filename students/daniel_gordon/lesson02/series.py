def fibonacci(n):
    """Calculates the nth value of the fibonacci sequence"""
    return sum_series(n)

def lucas(n):
    """Calculates the nth lucas number"""
    return sum_series(n, 2, 1)
 
def sum_series(n, n0 = 0, n1 = 1):
    """
    Calculates the nth value of an arbitrary summation series
    :param n0: zeroth element of the series
    :param n1: first element of the series
    """
    if n == 0:
        return n0
    if n == 1:
        return n1
    return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)
 
if __name__ == "__main__":
    #test fibonacci sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    
    #test lucas sequence
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(10) == 123
    
    #test generalized sequence matches fib and lucas
    assert sum_series(0) == fibonacci(0)
    assert sum_series(5) == fibonacci(5)
    assert sum_series(10) == fibonacci(10)
    assert sum_series(1,2,1) == lucas(1)
    assert sum_series(6,2,1) == lucas(6)
    assert sum_series(12,2,1) == lucas(12)
    
    #test a generalized sequence
    assert sum_series(0,4,2) == 4
    assert sum_series(1,4,2) == 2
    assert sum_series(2,4,2) == 6
    assert sum_series(3,4,2) == 8
    assert sum_series(4,4,2) == 14
    assert sum_series(5,4,2) == 22
    assert sum_series(6,4,2) == 36
    
    print("test successfull")
    