def fibonacci(n):
    """
    Return the nth value in the Fibonacci sequence.

    :param n: An integer n representing the nth value
    :type n: int
    """
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """
    Return the nth value in the Lucas sequence.

    :param n: An integer n representing the nth value
    :type n: int

    This function generalizes the Lucas series, which is a slight modification
    to the Fibonacci sequence where the first two values of the Lucas series are
    2 and 1 respectively.
    """
    if n == 0:
        return 2
    elif n == 1:
        return n
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, first_num=0, second_num=1):
    """
    Return the nth value in a summation series.

    :param n: An integer n representing the nth value to compute in a series
    :type n: int
    :param first_num: first value in the series
    :type first_num: int
    :param second_num: second value in the series
    :type second_num: int

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """

    if n == 0:
        return first_num
    elif n == 1:
        return second_num
    else:
        return sum_series(n - 2, first_num, second_num) + sum_series(n - 1, first_num, second_num)

if __name__=='__main__':
    #Test the Fibonacci series
    #0, 1, 1, 2, 3, 5, 8, 13, 21
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21

    #Test the Lucas Series
    #2, 1, 3, 4, 7, 11, 18, 29,
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(6) == 18
    assert lucas(7) == 29

    # test that sum_series matches fibonacci
    assert sum_series(12) == fibonacci(12)
    assert sum_series(23, 0, 1) == fibonacci(23)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(19, 2, 1) == lucas(19)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 5, 1) == 5
    assert sum_series(1, 7, 6) == 6
    assert sum_series(2, 4, 2) == 6
    assert sum_series(3, 9, 2) == 13
    assert sum_series(4, 2, 4) == 16
    assert sum_series(5, 3, 2) == 19

    print("All tests have passed")
