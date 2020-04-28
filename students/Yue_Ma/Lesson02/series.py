def fibonacci(n):
    a = 0
    b = 1
    if n <= 1:
        return n
    else:
        for i in range(0, n-1):
            c = a + b
            a = b
            b = c
        return c


def lucas(n):
    x = 2
    y = 1
    if n == 0:
        return n + 2
    elif n == 1:
        return n
    else:
        for i in range(0, n-1):
            z = x + y
            x = y
            y = z
        return z


def sum_series(n, first=0, second=1):
    if first == 2 and second == 1:
        return lucas(n)
    elif first == 0 and second == 1:
        return fibonacci(n)
    else:
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            for i in range(0, n - 1):
                result = first + second
                first = second
                second = result
            return result


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
