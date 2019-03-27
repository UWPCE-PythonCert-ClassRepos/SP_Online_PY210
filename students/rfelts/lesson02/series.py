# Russell Felts
# Assignment 2 - Fibonacci and Lucas Series
#
# Add a function called fibonacci. It should have one parameter, n and return
# the nth value in the fibonacci series (starting with zero index).
#
# Add a function called lucas, that returns the nth value in the lucas numbers series.
#
# Add a third function called sum_series with one required parameter and two
# optional parameters. The required parameter will determine which element in
# the series to print. The two optional parameters will have default values of
# 0 and 1 and will determine the first two values for the series to be
# produced. Calling this function with no optional parameters will produce
# numbers from the fibonacci series. Calling it with the optional arguments 2
# and 1 will produce values from the lucas numbers. Other values for the
# optional parameters will produce other series.
#
# Ensure that your functions have a well-formed docstring


def fibonacci(n):
    """
    Return the fibonacci number in the series of the value passed in.

    :param n (int) The desired position in the fibonacci series

    :return int - The nth value in the fibonacci series
    """

    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n


def lucas(n):
    """
    Return the lucas number in the series of the value passed in.

    Parameters:
    :param n (int) The desired position in the lucas series

    :return int - The nth value in the lucas series
    """

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, series_a=0, series_b=1):
    """
    Return the fibonacci or lucas number in the series of the value passed in.

    :param n (int) The desired position in the series
    :param series_a (int) The first number in the series
    :param series_b (int) The second number in the series

    :return int - The nth value in the series
    """

    if n == 0:
        return series_a
    elif n == 1:
        return series_b
    else:
        return (sum_series(n - 1, series_a, series_b) +
                sum_series(n - 2, series_a, series_b))


# Testing Fibonacci function by testing the starting values and another value.
assert fibonacci(0) == 0, "The return value should be 0. Test failed!"
assert fibonacci(1) == 1, "The return value should be 1. Test failed!"
assert fibonacci(7) == 13, "The return value is incorrect. Test failed!"

# Testing the lucas function by testing the starting values and another value.
assert lucas(0) == 2, "The return value should be 0. Test failed!"
assert lucas(1) == 1, "The return value should be 1. Test failed!"
assert lucas(7) == 29, "The return value is incorrect. Test failed!"

# Testing the sum_series function against the fibonacci function
assert fibonacci(5) == sum_series(5), "The values returned do not match. Test failed!"

# Testing the sum_series function against the lucas function
assert lucas(5) == sum_series(5, 2, 1), "The values returned do not match. Test failed!"

# Testing all functions against the first 10 numbers in each series.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
luc = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

for i in range(10):
    assert fibonacci(i) == fib[i], "The return value is incorrect. Test failed!"
    assert lucas(i) == luc[i], "The return value is incorrect. Test failed!"
    assert fibonacci(i) == sum_series(i), "The values returned do not match. Test failed!"
    assert lucas(i) == sum_series(i, 2, 1), "The values returned do not match. The test failed."

print("Tests finished")
