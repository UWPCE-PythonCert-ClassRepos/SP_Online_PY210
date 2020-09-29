#Isabella Kemp
#Jan-6-20
#Fibonacci Series

'''def fibonacci(n):   #First attempt at this logic
    fibSeries = [0,1,1]
    if n==0:
        return 0
    if n == 1 or n == 2:
        return 1
    for x in range (3,n+1):
        calc = fibSeries[x-2] + fibSeries[x-1]
        fibSeries.append(calc)
    print (fibSeries[:]) #prints the entire fib series
    return fibSeries[-1] # returns the last value in the series
print (fibonacci(5))'''

#Fibonacci Series computed. Series starts with 0 and 1, the following integer is the
#summation of the previous two.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#Lucas Numbers. Series starts with 2 at 0 index followed by 1.
def lucas(n):
    #lucasSeries = [2,1]
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

#sum series will return fibonacci sequence if no optional parameters are called
#b and c are optional parameters. If 2 and 1 are called for optional parameters
#lucas sequence is called. Other optional parameters gives a new series.
def sum_series(n,b=0,c=1):
    if n == 0:
        return b
    if n == 1:
        return c
    return sum_series(n-1, b, c) + sum_series(n-2, b, c)

#Tests
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

    print("tests passed")





