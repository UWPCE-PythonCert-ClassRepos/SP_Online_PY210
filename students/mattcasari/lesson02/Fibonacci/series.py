#!/usr/bin/env python3

def sum_series(n, n0=0, n1=1):
    if n < 0:
        pass
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)

def fibonacci(n):
    return sum_series(n)   


def lucas(n):
    return sum_series(n,2,1)


if __name__ == "__main__":

     # run some tests
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(6) == 8)
    assert(fibonacci(7) == 13)

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19