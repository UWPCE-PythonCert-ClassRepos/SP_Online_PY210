def fibonacci(n):
    """Calculates the nth value of the fibonacci sequence"""
    return sum_series(n)

def lucas(n):
    """Calculates the nth lucas number"""
    return sum_series(n, 2, 1)
 
def sum_series(n, n0 = 0, n1 = 1):
    """
    Calculates the nth value of an arbitrary summation series
    :param n0: zeroth element of the series
    :param n1: first element of the series
    """
    if n == 0:
        return n0
    if n == 1:
        return n1
    return sum_series(n-2, n0, n1) + sum_series(n-1, n0, n1)
 