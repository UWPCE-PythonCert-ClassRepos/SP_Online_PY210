#--------------------------
#Title: Number sequences
#Description: Determine value of nth position in sequence
#Original Dev: Lee Deitesfeld
#Change Log:
#20190331LAD Created functions
#20190402LAD Modified logic in for-loops
#--------------------------

def fibonacci(n):
    '''Determines the nth value of the Fibonacci sequence.'''
    #initial values of the sequence
    a,b = 0,1
    fib_list = []
    #appends value to list as determined by Fibonacci calculation
    for value in range(0, n+1):
        a, b = b, a+b
        fib_list.append(a)
    #print(fib_list)
    #presets value with index zero, else calculates value
    if n == 0:
        return 0
    return fib_list[n-1]


def lucas(n):
    '''Determines the nth value of the Lucas Numbers sequence.'''
    #initial values of the sequence
    a,b = 2,1
    lucas_list = []
    #appends value to list as determined by Fibonacci calculation
    for value in range(0, n+1):
        a, b = b, a+b
        lucas_list.append(a)
    #print(lucas_list)
    #presets value with index zero, else calculates value
    if n == 0:
        return 2
    return lucas_list[n-1]


def sum_series(n, a=0, b=1):
    '''Determines the nth value of a user-provided sequence.'''
    series_list = []
    #appends values to the sequence following the same sequence as other fcns
    for value in range(0, n+1):
        a, b = b, a+b
        series_list.append(a)
    #print(series_list)
    #presets value with index zero, else calculates value
    if n == 0:
        return a
    return series_list[n-1]

#assertion tests to verify calculations
if __name__ == "__main__":
    # run some tests against fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    # run some tests against lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    # test if sum_series matched fibonacci
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
