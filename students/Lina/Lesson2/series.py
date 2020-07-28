#! python

#-------------------------------------------------------------------
# Lesson 2 - Fibonacci Series Exercise
#-------------------------------------------------------------------

def fibonacci(n):
    """ This function returns the value of nth element in the fibonacci
        series. The fibonacci series starts with numbers 0 and 1, the next
        number is the sum of the previous two numbers and so on.
        Input
          n integer, nth element in the series
        Output
          integer, value of nth element in the series
    """
    return sum_series(n, 0, 1)

def lucas(n):
    """ This function returns the value of nth element in the lucas series.
        The lucas series starts with numbers 2 and 1, the next number is
        the sum of the previous two numbers and so on.
        Input
          n integer, nth element in the series
        Output
          integer, value of nth element in the series
    """
    return sum_series(n, 2, 1)

def sum_series(n, n0 = 0, n1 = 1):
    """ This function returns the value of nth element in the series.
        The series starts with two numbers, the next number is the sum of
        the previous two numbers and so on. The second and third parameters 
        determine type of series, if 2 and 1 are passed it will return
        the nth element in the lucas series. If 0 and 1 are passed, or no
        optional parameters are passed then it will return the nth element in
        the fibonacci series. Other optional values will return other series
        Input
          param 1: n  integer, nth element in the series
          param 2: n0 integer, first number in the series (0th element)
          param 3: n1 integer, second number in the series(first element)
        Output
          integer, value of nth element in the series
    """

    if n == 0:
      return n0
    elif n == 1:
      return n1

    for i in range(n):
        return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)


if __name__ == "__main__":
    #run some tests
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
    assert lucas(2) == 3
    assert lucas(3) == 4
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
