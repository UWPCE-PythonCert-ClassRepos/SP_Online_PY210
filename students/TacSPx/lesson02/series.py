# ---------------------------------------------------------------------------- #
# Title: Series
# Description: Fibonacci, Lucas, and other similar series
#              A collection of Functions that calculates and
#              returns the "nth" value in their respective series
# ---------------------------------------------------------------------------- #
def fibonacci(n):
    """
    A function that computes and returns the "nth" value in the Fibonacci series: formula fib(n) = fib(n-2) + fib(n-1)
    :param n: User inputs what the position in the series they want (n)
    :return: The position in the Fibonacci series for example '0[n=0], 1[n=1], 1[n=2], 2[n=3], 3[n=4], 5[n=5],
     8[n=6], 13[n=7]........
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

# Option for printing out fibonacci series
# f = []
# a = 0
# b = 1
# if n == 1:
#     f.append(a)
# elif n <= 1:
#     print("Choice a positive number greater than '0'")
# else:
#     f.append(a)
#     f.append(b)
#     for i in range(0, n):
#         c = a + b
#         a = b
#         b = c
#         f.append(c)
#     return f

def lucas(n):
    """
    A function that computes and returns the "nth" value in the Lucas series: formula lucas(n) = lucas(n-2) + lucas(n-1)
    :param n: User inputs what the position in the series they want (n)
    :return: The position in the Lucas series for example '2[n=0], 1[n=1], 3[n=2], 4[n=3], 7[n=4], 11[n=5],
     18[n=6], 29[n=7]........
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, a=0, b=1):
    """
    A function that computes and returns the "nth" value of the the "Fibonacci",  "Lucas", or other
    similar series = x(n) = x(n-2) + x(n-1).  The "Fibonacci series" can be used without optional parameters,
    since the defaults are "0 & 1" (n,0,1).  To use the "Lucas series" you need to type the "2 & 1" optional parameters (n,2,1).
    In all cases you still have to enter the "n" or the position of the "nth" value you want to see in the series.
    :param n: User inputs how many numbers they would like to see in the Fibonacci, Lucas, or other similar series
    :return: A list of Fibonacci/ Lucas or other similar series patters.
    example for Fibonacci: series for example '0[n=0], 1[n=1], 1[n=2], 2[n=3], 3[n=4], 5[n=5],
    8[n=6], 13[n=7]........
    example for Lucas: the position in the Lucas series for example '2[n=0], 1[n=1], 3[n=2], 4[n=3], 7[n=4], 11[n=5],
    18[n=6], 29[n=7]........
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 2, a, b) + sum_series(n - 1, a, b)

# my testing
# print(fibonacci(4))
# print(lucas(4))
# print(sum_series(7))
# print(sum_series(4,2,1))
# print(sum_series(4,4,2))

if __name__ == "__main__":
    # run some tests to see if this will work for fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    # run some tests to see if this will work for lucas
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
