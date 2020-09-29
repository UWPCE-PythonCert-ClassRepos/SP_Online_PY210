# Title: Fibonacci Series
# Dev: Roslyn Melookaran
# Date: 9/8/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/8/20, created script)
# --------------------------------------------------------------

def fibonacci(n):
    """ Compute the nth value of a Fibonacci series
        :param: n (integer): value
        :return: nth value
        """
    if n<=1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """ Compute the nth value of a Lucas series
        :param: n (integer): value
        :return: nth value
        """
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n,n0=0,n1=1): # Setting the initial values so that if user does not define n0 and n1, it will default to fibonacci
    """
     compute the nth value of a summation series.

     :param n0=0: value of zeroth element in the series
     :param n1=1: value of first element in the series

     This function generalizes the fibonacci() and the lucas(),
     so that this function works for any first two numbers for a sum series.
     Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
     And sum_series(n, 2, 1) should be equivalent to lucas(n).

     sum_series(n, 3, 2) should generate another series with no specific name

     The defaults are set to 0, 1, so if you don't pass in any values, you'll
     get the fibonacci series
     """
    if n0==2 and n1==1: #Lucas Function
        if n == 0:
            return 2
        if n == 1:
            return 1
        else:
            return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)
    elif n0==0 and n1==1: # Fibonacci Function
        if n <= 1:
            return n
        else:
            return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)
    else:
        if n == 0:
            return n0
        if n == 1:
            return n1
        else:
            return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)

# The following code tests the functions above to make sure the nth values are correct.
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

