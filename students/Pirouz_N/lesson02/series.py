"""
Purpose: Lessen 2 homework four python certificate from UW
Author: Pirouz Naghavi
Date: 06/26/2020
"""


def fibonacci(n):
    """"This function will generate the fibonacci sequence until index n and return that value.

    Args:
      n: Is the index that the fibonacci sequence will be generated until and the value of index
          n will be returned.

    Returns:
       value of index n of the fibonacci sequence will be returned.

    Raises:
        ValueError: If n is less than zero.
    """

    if n < 0:
        raise ValueError('n has to be zero or larger.')

    # Index allows the algorithm to know how much more of the sequence we need to generate
    index = 1

    # Last and current are fn-1 and fn at each index
    last = 0
    current = 1

    # Returning initial indices of the sequence that don't need to be generated
    if n == 0:
        return last
    elif n == 1:
        return current
    else:
        # Generating the sequence
        while index != n:
            # Moving fn-1 and fn to next index
            last_temp = current
            current += last
            last = last_temp
            index += 1
    return current


def lucas(n):
    """"This function will generate the lucas sequence until index n and return that value.

    Args:
      n: Is the index that the lucas sequence will be generated until and the value of index
          n will be returned.

    Returns:
       value of index n of the lucas sequence will be returned.

    Raises:
        ValueError: If n is less than zero.
    """

    if n < 0:
        raise ValueError('n has to be zero or larger.')

    # Index allows the algorithm to know how much more of the sequence we need to generate
    index = 1

    # Last and current are fn-1 and fn at each index
    last = 2
    current = 1

    # Returning initial indices of the sequence that don't need to be generated
    if n == 0:
        return last
    elif n == 1:
        return current
    else:
        # Generating the sequence
        while index != n:
            # Moving fn-1 and fn to next index
            last_temp = current
            current += last
            last = last_temp
            index += 1
    return current


def sum_series(n, n0=0, n1=1):
    """This function will generate the lucas sequence until index n and return that value.

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies

    Args:
        n: Is the index that the sum sequence will be generated until and the value of index
            n will be returned
        n0=0: value of zeroth element in the series
        n1=1: value of first element in the series

    Returns:
        Value of sum series at index n.

    Raises:
        ValueError: If n is less than zero.
    """

    if n < 0:
        raise ValueError('n has to be zero or larger.')

    # Index allows the algorithm to know how much more of the sequence we need to generate
    index = 1

    # Last and current are fn-1 and fn at each index
    last = n0
    current = n1

    # Returning initial indices of the sequence that don't need to be generated
    if n == 0:
        return last
    elif n == 1:
        return current
    else:
        # Generating the sequence
        while index != n:
            # Moving fn-1 and fn to next index
            last_temp = current
            current += last
            last = last_temp
            index += 1
    return current


if __name__ == "__main__":
    # run some tests on fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # run some tests on lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

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
