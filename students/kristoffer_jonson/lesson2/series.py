def fibonacci(n):
    """
    Return nth value of fibonacci sequence
    :param n: Requested value in fibonacci sequence
    """
    previous = 1
    previous_previous = 0
    for i in range(2,n):
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
    for i in range(2,n):
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
    for i in range(2,n):
        result = previous+previous_previous
        previous_previous = previous
        previous = result
    return result

def fibonacci2(n):
    """
    Return nth value of fibonacci sequence
    :param n: Requested value in fibonacci sequence
    """
    return sum_series(n,0,1)

def lucas2(n):
    """
    Return nth value of lucas sequence
    :param n: Requested value in lucas sequence
    """
    return sum_series(n,2,1)