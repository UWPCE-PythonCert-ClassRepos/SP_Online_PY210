#!/usr/bin/env python

'''
py210: Mod2: Series

Recursion!
'''


def fibonacci(number):
    '''
    Calculate Fibonacci sequence position of n, by calling this function reursively.

    Values for the first two positions in the sequence (0, 1) are 0, 1, so handle those separately.

    Caches prior values in a dictionary to eliminate repeatedly calculating the same position
    in the sequence

    :param number: find the value of nth position in the sequence
    :return:
    '''
    if number in FIBONACCI_CACHE:
        return FIBONACCI_CACHE[number]

    if number <= 1:
        value = number
    else:
        value = fibonacci(number - 1) + fibonacci(number - 2)
    FIBONACCI_CACHE[number] = value

    return value

def lucas(number):
    '''
    Recursively compute a Lucas sequence, which is like Fibonacci, but the first two number in
    the sequence are 2, 1

    Caches prior values in a dictionary to eliminate repeatedly calculating the same position
    in the sequence

    :param number: spot in the sequence in the Nth position
    :return: return the calculation or cached value
    '''

    if number in LUCAS_CACHE:
        return LUCAS_CACHE[number]

    if number == 0:
        value = 2
    elif number == 1:
        value = 1
    else:
        value = lucas(number - 1) + lucas(number - 2)
    LUCAS_CACHE[number] = value

    return value


def sum_series(number, position_zero=0, position_one=1):
    '''
    Make a more general function that will handle Fibonacci and Lucas with two addition, optional,
    args to the function

    Don't use a caching dictionary for this one, as the cache need to get deleted anytime the
    optional args change.

        * I need to go back and figure out how to do this later.

    :param number: calculate series to 'n'
    :param position_zero: optional parameter for position 0, as fibonacci and lucas have
    different values in sequence 0 and 1
    :param position_one: optional parameter for position 1, as fibonacci and lucas have
    different values in sequence 0 and 1
    :return: the calculation or cached value
    '''


    if number == 0:
        return position_zero
    elif number == 1:
        return position_one
    else:
        value = sum_series(number - 1, position_zero, position_one) + \
                sum_series(number - 2, position_zero, position_one)

    return value


FIBONACCI_CACHE = {}    # Use a dictionary to cache previous results so we don't repeat
                        # recursion for previous values of n
LUCAS_CACHE = {}        # Use a dictionary to cache previous results so we don't repeat recursion
                        # for previous values of n


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
