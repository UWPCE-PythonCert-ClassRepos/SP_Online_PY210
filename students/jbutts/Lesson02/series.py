#!/usr/bin/env python

'''
py210: Mod2: Series

Recursion!
'''


def fibonacci(n):
    '''
    Calculate Fibonacci sequence position of n, by calling this function reursively.

    Values for the first two positions in the sequence (0, 1) are 0, 1, so handle those separately.

    Caches prior values in a dictionary to eliminate repeatedly calculating the same position in the sequence

    :param n: find the value of nth position in the sequence
    :return:
    '''
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n <= 1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value

    return value

def lucas(n):
    '''
    Recursively compute a Lucas sequence, which is like Fibonacci, but the first two number in the sequence are 2, 1

    Caches prior values in a dictionary to eliminate repeatedly calculating the same position in the sequence

    :param n: spot in the sequence in the Nth position
    :return: return the calculation or cached value
    '''

    if n in lucas_cache:
        return lucas_cache[n]

    if n == 0:
        value = 2
    elif n == 1:
        value = 1
    else:
        value = lucas(n-1) + lucas(n-2)
    lucas_cache[n] = value

    return value


def sum_series(n, a=0, b=1):
    '''
    Make a more general function that will handle Fibonacci and Lucas with two addition, optional, args to the function

    Don't use a caching dictionary for this one, as the cache need to get deleted anytime the optional args change.

        * I need to go back and figure out how to do this later.

    :param n: calculate series to 'n'
    :param a: optional parameter for position 0, as fibonacci and lucas have different values in sequence 0 and 1
    :param b: optional parameter for position 1, as fibonacci and lucas have different values in sequence 0 and 1
    :return: the calculation or cached value
    '''


    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        value = sum_series(n-1, a, b) + sum_series(n-2, a, b)

    return value

fibonacci_cache = {}  # Use a dictionary to cache previous results so we don't repeat recursion for previous values of n
lucas_cache = {}  # Use a dictionary to cache previous results so we don't repeat recursion for previous values of n


assert fibonacci(4) == 3
assert fibonacci(7) == 13
assert fibonacci(27) == 196418
assert lucas(3) == 4
assert lucas(7) == 29
assert lucas(27) == 439204
assert sum_series(7) == 13
assert sum_series(7, 2, 1) == 29
assert sum_series(27, 2, 1) == lucas(27)

print("Tests Passed!")





