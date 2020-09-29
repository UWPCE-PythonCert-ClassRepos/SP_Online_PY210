def fibonacci(n):
	"""This function returns the nth value of the fibonacci series"""
    i = 0
    x = 0
    y = 1
    z = 0
    for i in range(n+1):
        if i == 0:
            z = x
        elif i == 1:
            z = y
        else:
            z = y + x
            x = y 
            y = z
    return z


def lucas(n):
	"""This function returns the nth value of the fibonacci series, except the integer series starts with 2 and 1 (Lucas numbers)"""
    i = 0
    x = 2
    y = 1
    z = 0
    for i in range(n+1):
        if i == 0:
            z = x
        elif i == 1:
            z = y
        else:
            z = y + x
            x = y 
            y = z
    return z


def sum_series(n, a = 0, b = 1):
	"""This function returns the nth value of a fibonacci-like series with 2 inputted numbers"""
    i = 0
    x = a
    y = b
    z = 0
    for i in range(n+1):
        if i == 0:
            z = x
        elif i == 1:
            z = y
        else:
            z = y + x
            x = y 
            y = z
    return z


if __name__ == "__main__":
    # verify that the fibonacci and lucas series functions work properly
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

    # verify that the sum series default and 0 and 1 inputs match the fibonacci results
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # verify that the sum series 2 and 1 inputs match the lucas sequence
    assert sum_series(5, 2, 1) == lucas(5)

    # verify that the sum series works for fibonacci-like series for inputs besides fibonacci and lucas
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
