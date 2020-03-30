def fibonacci(n):
    """
    Return nth value of fibonacci sequence
    :param n: Requested value in fibonacci sequence
    """
    previous = 1
    previous_previous = 0
    if n == 0:
        return previous_previous
    if n == 1:
        return previous
    for i in range(2,n+1):
        result = previous+previous_previous
        previous_previous = previous
        previous = result
    return result

def lucas(n):
    """
    Return nth value of lucas sequence
    :param n: Requested value in lucas sequence
    """
    previous = 1
    previous_previous = 2
    if n == 0:
        return previous_previous
    if n == 1:
        return previous
    for i in range(2,n+1):
        result = previous+previous_previous
        previous_previous = previous
        previous = result
    return result

def sum_series(n,x = 0, y = 1):
    """
    Return nth value of a sum sequence with first 2 values in sequence defined
    :param n: Requested value in sum sequence
    :param x: Sets the value of the first element of sequence
    :param y: Sets the value of the second element of sequence
    """
    previous = y
    previous_previous = x
    result = 0
    if n == 0:
        return previous_previous
    if n == 1:
        return previous
    for i in range(2,n+1):
        result = previous+previous_previous
        previous_previous = previous
        previous = result
    return result

def fibonacci2(n):
    """
    Return nth value of fibonacci sequence.  Incorporates sum_series function.
    :param n: Requested value in fibonacci sequence
    """
    return sum_series(n,0,1)

def lucas2(n):
    """
    Return nth value of lucas sequence.  Incorporates sum_series function.
    :param n: Requested value in lucas sequence
    """
    return sum_series(n,2,1)

if __name__ == "__main__":
    # run some tests
    assert fibonacci2(0) == 0
    assert fibonacci2(1) == 1
    assert fibonacci2(2) == 1
    assert fibonacci2(3) == 2
    assert fibonacci2(4) == 3
    assert fibonacci2(5) == 5
    assert fibonacci2(6) == 8
    assert fibonacci2(7) == 13

    assert lucas2(0) == 2
    assert lucas2(1) == 1
    assert lucas2(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci2(5)
    assert sum_series(7, 0, 1) == fibonacci2(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas2(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    assert fibonacci2(0) == fibonacci(0)
    assert fibonacci2(3) == fibonacci(3)
    assert fibonacci2(5) == fibonacci(5)

    assert lucas2(0) == lucas(0)
    assert lucas2(3) == lucas(3)
    assert lucas2(5) == lucas(5)

    print("tests passed")