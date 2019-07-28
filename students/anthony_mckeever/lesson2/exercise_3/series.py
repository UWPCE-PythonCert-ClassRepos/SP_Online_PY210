"""
Programming In Python - Lesson 2 Exercise 3: Fibonacci Series Exercise
Code Poet: Anthony McKeever
Start Date: 07/24/2019
End Date: 07/24/2019
"""

def fibonacci(n):
    """
    Return the Fibonacci number at the nth place.

    :param n:   The number of the place in the Fibonacci series to get.  For example, n = 7 will return 13 
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """
    Return the Lucas number at the nth place

    :param n:   The number of the place in the Lucas series to get.  For example, n = 7 will return 29
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, atZero = 0, atOne = 1):
    """
    Return the Fibonacci or Lucas number at the nth place in the series depending on inputs.
    By default this method will return the Fibonacci number at n.  If you wish to return the
    Lucas number you need to set the atZero to 2.  See params below for more details.

    :param n:       The place in the series to return.
    :param atZero:  What to return when n is 0.  (Default = 0: This is the Fibonacci setting)
                    To use Lucas number, pass 2 to this parameter (atZero=2)
    :param atOne:   What to return when n is 1.  (Default = 1: This is the Fibonacci AND Lucas setting)
                    For other series, refer to that series' default One place value.
    """
    if n == 0:
        return atZero
    elif n == 1:
        return atOne
    return sum_series(n - 1, atZero, atOne) + sum_series(n - 2, atZero, atOne)

if __name__ == "__main__":
    print("Validate Fibonnaci series from the fibonacci(n) function")
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    print("Validate Lucas series from the lucas(n) function")
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    print("Validate that sum_series(n) in Fibonacci mode matches fibonacci(n)")
    for i in range(8):
        assert sum_series(i) == fibonacci(i)
        assert sum_series(i, 0, 1) == fibonacci(i)

    print("Validate that sum_series(n) in Lucas mode matches lucas(n)")
    for i in range(8):
        assert sum_series(i, 2) == lucas(i)
        assert sum_series(i, 2, 1) == lucas(i)

    print("Validate arbitrary values in sum_series")
    test_expectations = [3, 2, 5, 7, 12, 19]
    for i in range(len(test_expectations)):
        assert sum_series(i, 3, 2) == test_expectations[i]

    print("Tests passed!")
