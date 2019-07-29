def fibonacci(n):
    """
    Return the nth value in the Fibonacci sequence.

    :param n: An integer n representing the nth value
    :type n: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """
    Return the nth value in the Lucas sequence.

    :param n: An integer n representing the nth value
    :type n: int
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, first_num=0, second_num=1):
    """
    Return the nth value in the Lucas sequence.

    :param n: An integer n representing the nth value
    :type n: int
    """

    if n == 0:
        return first_num
    elif n == 1:
        return second_num
    else:
        return sum_series(n - 2, first_num, second_num) + sum_series(n - 1, first_num, second_num)

if __name__=='__main__':
    test = sum_series(12)
    print(test)
    test1 = fibonacci(12)
    print(test1)

    test2 = sum_series(7, first_num=2, second_num=1)
    print(test2)
