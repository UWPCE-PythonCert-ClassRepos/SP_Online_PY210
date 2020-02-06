"""
Fibonacci Series:
f(1) = 0
f(2) = 1
F(n)= F(n-1) + F(n-2)

Lucas Number Series:
f(1) = 2
f(2) = 1
F(n)= F(n-1) + F(n-2)

"""


def fibonacci(n):
    """
    Action to return the nth value in the fibonacci series
    :param n: the index number of the series for the value you would like to return. Starts with zero index
    :return: Returns the value of the nth index of the fibonacci series
    """
    if n <= 0:
        print("not a valid number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Action to return the nth value in the Lucas Number series
    :param n: the index number of the series for the value you would like to return. Starts with zero index
    :return: Returns the value of the nth index of the Lucas Number series
    """
    if n <= 0:
        print("not a valid number")
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, x=None, y=None):
    if x and y == None:
        fibonacci(n)

    elif x == 2 and y == 1:
        lucas(n)






def print_resuls(n):
    x = lucas(n)
    print(x)



print_resuls(0)