
def fibonacci(n):
    """ compute the nth Fibonacci number  start with 0 and 1"""
    if n == 0 or n==1:
        return n

    else:
        return fibonacci(n - 2) + fibonacci(n - 1)



def lucas(n):
    """ compute the nth Lucas number start with 2 and 1 """
    if n == 0:
        return 2
    if n== 1:
        return n
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, x=0, y=1):
    """
    compute the nth value of a summation series.
     when :
     x=0: value of zeroth element in the series
     y=1: value of first element in the series
     fibonacci serise is called
     when:
     x=2: value of zeroth element in the series
     y=1: value of first element in the series
     lucas serise is called

    """

    if n == 0:
        return x
    if n == 1:
        return y
    else:
        return sum_series(n - 2, x, y) + sum_series(n - 1, x, y)


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
