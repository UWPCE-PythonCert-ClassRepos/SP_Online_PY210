"""Both the fibonacci series and the lucas numbers are based on an identical formula:
fib(n) = fib(n-2) + fib(n-1)
This formula creates a class of series that are all related – each with a different two starting numbers."""

def fibonacci(n):
    """The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two"""
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

def lucas(n):
    #The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1    if n==0:
    if n==0:
        return 2
    elif n ==1:
        return 1
    else:
        return lucas(n-2)+lucas(n-1)

#Function to use Other values for the optional parameters and will produce other series
def other_Series(n,n0,n1):
    if n == 0:
        return n0
    elif n==1:
        return n1
    else:
        for i in range (n-1):
            n2 = n0 + n1
            n0 = n1
            n1 = n2
            i +=1
        return n2
     
#sum_series is a function to  that can compute all of these related series.
def sum_series(n,n0=0,n1=1):

    if n0 == 0 and n1 == 1:
        return fibonacci(n)
    elif n0 == 2 and n1 == 1:
        return lucas(n)
    else:
        return other_Series(n,n0,n1)



# block of code that use series of assert statements that demonstrate the three functions work properly.
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