#Computing the Fibonacci and Lucas series

#Part 1: Fibonacci series (commented out the function because of later
#assignment to generalize the function via sum_series)
#def fibonacci(n):
#    """compute the nth value in the fibonacci series"""
#    fib_series = [0, 1]
#    i = 2
#    while i <= n:
#        fib_series.append(fib_series[i-1] + fib_series[i-2])
#        i = i + 1
#    return fib_series[n]

#Part 2: Lucas series (commented out the function because of later
#assignment to generalize the function via sum_series)
#def lucas(n):
#    """compute the nth value in the Lucas series"""
#    lucas_series = [2, 1]
#    i = 2
#    while i <= n:
#        lucas_series.append(lucas_series[i-1] + lucas_series[i-2])
#        i = i + 1
#    print(lucas_series[n])



#Part 3: Generalizing
def sum_series(n, x = 0, y = 1):
    """Compute the nth value of a given series.
    Default is the Fibonacci series
    sum_series(n, 2, 1) will compute the nth value of the Lucas series
    Other numbers for x and y will compute nth value of another series.
    """
    gen_series = [x, y]
    i = 2
    while i <= n:
        gen_series.append(gen_series[i-1] + gen_series[i-2])
        i = i + 1
    return gen_series[n]

#Part 4: Integrating generalized sum_series into Fibonacci and Lucas series functions
def fibonacci(n):
    """returns nth value of Fibonacci series using sum_series function"""
    return sum_series(n)

def lucas(n):
    """returns nth value of Lucas series using sum_series function"""
    return sum_series(n, 2, 1)

#Part 5: add assert statements
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
