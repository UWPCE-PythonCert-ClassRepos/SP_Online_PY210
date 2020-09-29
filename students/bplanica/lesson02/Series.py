# ------------------------------ #
# Series Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/3/2019, Created and tested script
# ------------------------------ #

# ----- DATA ----- #
# ---------------- #
i = 0  # counter
series = []  # list to house series


# ----- PROCESSING ----- #
# ---------------------- #

def fibonacci(n):
    """returns the nth value in the fibonacci series (starting with zero index)"""

    return sum_series(n, 0, 1)


def lucas(n):
    """returns the nth value in the lucas numbers series (starting with zero index)"""

    return sum_series(n, 2, 1)


def sum_series(n, n0 = 0, n1 = 1):
    """returns the nth value in a numbers series (starting with zero index)
            starting numbers are optional arguments"""

    i = 2  # Starting at index 2
    series = [n0, n1]  # Define indexes 0 and 1, if applicable
    while i <= n:  # Go until the nth value
        sub_n = series[(i-2)] + series[(i-1)]  # Sum the previous two values
        series.append(sub_n)  # Append to the list
        i += 1
    return series[n]  # Return the nth value


# ----- PRESENTATION ----- #
# ------------------------ #

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

    print("tests passed!")
