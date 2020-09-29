def fibonacci(n):
    """compute the nth number in the fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 2
        a = 0
        b = 1
        while i <= n:
            x = a + b
            a = b
            b = x
            i += 1
        return x
def lucas(n):
    """compute the nth number in the lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        i = 2
        a = 2
        b = 1
        while i <= n:
            x = a + b
            a = b
            b = x
            i += 1
        return x

def sum_series(n,a=0,b=1):
    """compute the nth number in the fibonacci series for a=0 and b=1
    or the lucas series for a=2 b=1"""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        i = 2
        while i <= n:
            x = a + b
            a = b
            b = x
            i += 1
        return x

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
