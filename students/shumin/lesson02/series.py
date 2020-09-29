# Fibonacci returns the nth number
# where the nth number is the sum
# of the previous two number in the series
# starting with n0 = 0 and n1 = 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    
    return fibonacci(n - 2) + fibonacci(n - 1)


# Lucas does the same thing as Fibonacci 
# except that it start with n0 = 2 and 
# n1 = 1
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1

    return lucas(n - 2) + lucas(n - 1)


# Sum_series return the nth number in the series
# where by default n0 = 0 and n1 = 1
# However, n0 and n1 are parameters that can be changed
def sum_series(n, n0 = 0, n1 = 1):
    if n == 0:
        return n0
    elif n == 1:
        return n1

    return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)


# This part runs some test to test whether fibonacci, lucas, and 
# sum_series work. If it works, it prints "test passed"
if __name__ == "__main__":
    # Testing whether fibonacci works
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    # Testing whether lucas works
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    # Testing whether sum_series matches fibonacci
    # and lucas if giving the same n0 and n1
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)
    assert sum_series(5, 2, 1) == lucas(5)
    # Testing whether sum_series works if pass in random
    # arguments for the parameter
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19
    # if successfully pass the test. Prints "test passed"
    print("test passed")
