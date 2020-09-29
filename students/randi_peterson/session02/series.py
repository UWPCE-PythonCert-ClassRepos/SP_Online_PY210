def fibonacci(n):
    """
    Return the nth value of the fibonacci series
    """
    prev_val = 1
    two_prev_val = 0
    if n == 0:
        finalval = 0
    elif n == 1:
        finalval = 1
    else:
        for i in range(2,n+1):
            value = prev_val + two_prev_val
            two_prev_val = prev_val
            prev_val = value

            finalval = value
    return finalval

def lucas(n):
    """
    Return the nth value of the Lucas series
    """
    prev_val = 1
    two_prev_val = 2
    if n == 0:
        finalval = 2
    elif n == 1:
        finalval = 1
    else:
        for i in range(2, n + 1):
            value = prev_val + two_prev_val
            two_prev_val = prev_val
            prev_val = value
            finalval = value

    return finalval

def sum_series(n,two_prev_val = 0,prev_val = 1):
    """
    Return the nth value of the Fibonacci (default) or Lucas sequence if (n, 2, 1) inputs
    """

    if n == 0:
        finalval = two_prev_val
    elif n == 1:
        finalval = prev_val
    else:
        for i in range(2, n + 1):
            value = prev_val + two_prev_val
            two_prev_val = prev_val
            prev_val = value
            finalval = value

    return finalval

#Perform tests on all three functions
if __name__ == "__main__":
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

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
