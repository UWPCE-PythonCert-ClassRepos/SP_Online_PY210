#!/usr/bin/env python3

def fibonacci(n):
    """ compute the nth Fibonacci number """
    my_fibonacci = sum_series(n, n0=0, n1=1)
    return my_fibonacci

def lucas(n):
    """ compute the nth Lucas number """
    my_lucas = sum_series(n, n0=2, n1=1)
    return my_lucas

def sum_series(n, n0=0, n1=1):
    n2 = 0
    array = [n0, n1]
    for i in range(n): 
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        array.append(n2)
    if n == 0:
        return array[0]
    else:
        return array[n]
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
