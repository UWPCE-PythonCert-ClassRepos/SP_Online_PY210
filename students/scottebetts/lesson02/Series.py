
def fibonacci(n):
    """returns nth Fibonacci number"""
    a = 0
    b = 1
    if (n == 0) :
        return a
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
    return b

def lucas(n):
    """returns nth Lucas number"""
    a = 2
    b = 1
    if (n == 0) :
        return a
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
    return b

def sum_series(n, a = 0, b = 1):
    """returns nth series number"""
    if (n == 0) :
        return a
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
    return b

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

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
