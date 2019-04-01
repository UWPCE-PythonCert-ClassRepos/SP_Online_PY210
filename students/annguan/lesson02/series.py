#Lesson 2 Fibonacci Series Exercise
#fibonacci(n)
#lucas(n)
#sum_series(n,a,b)


###Functions###

def fibonacci(n):
    """
    compute nth Fibonacci Series value, starting with zero index
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """compute nth Lucas Numbers"""
    if n == 0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(n,a=0,b=1):
    """compute nth value for either Fibonacci Series or Lucas series based on
    the the two optional values.
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-2, a, b) + sum_series(n-1, a, b)

###Tests###

# Test function: fibonacci(n)
assert fibonacci(0) == 0,
assert fibonacci(1) == 1,
assert fibonacci(7) == 13;
assert fibonacci(12) == 144;

# Test function: lucas(n)
assert lucas(0) == 2,
assert lucas(1) == 1,
assert lucas(7) == 29,
assert lucas(12) == 322,

# Test sum_series (n,a=0,b=1)
assert sum_series (0) == 0,
assert sum_series (1) == 1,
assert sum_series (7) == 13,
assert sum_series (12) == 144,
assert.sum_series (11,2,1) == 199,
assert.sum_series (13,7,1) == 1241,