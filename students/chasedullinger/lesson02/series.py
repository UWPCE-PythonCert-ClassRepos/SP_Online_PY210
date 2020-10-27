# PY210 Lesson 02 Fibonacci Series Exercise - Chase Dullinger

def fibonacci(n):
    """Given n, returns the nth value of the Fibonacci series"""
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci(n-2)+fibonacci(n-1)

    return result

def lucas(n):
    """Given n, returns the nth value of the Lucas series"""
    if n == 0:
        return 2
    if n == 1:
        return 1

    result = lucas(n-2)+lucas(n-1)

    return result

def sum_series(n, n0=0, n1=1):
    """Given n, returns the nth value of the series defined by f(n)=f(n-2)+f(n-1).
        :param n0=0: is the value of the 0th position n
        :param n1=0: is the value of the 1st position n
        default values of n0=0 and n1=1 will give the Fibonacci series
    """
    if n == 0:
        return n0
    if n == 1:
        return n1

    result = sum_series(n-2, n0, n1)+sum_series(n-1, n0, n1)

    return result

if __name__=="__main__":
    #check that fibonacci() returns known values for the fibonacci series
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #check that lucas() returns known values for the lucas series
    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
