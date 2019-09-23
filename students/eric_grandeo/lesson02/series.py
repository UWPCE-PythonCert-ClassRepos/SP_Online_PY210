#fibonacci sequence
def fibonacci(n):
    '''
    Return the nth value in the Fibonacci sequence

    :param n: The number position of the value in the Fibonacci sequence (starting with zero index)
    '''

    fib = [0, 1]

    for i in range(2,n+1):
        new_num = fib[i-2] + fib[i-1]
        fib.append(new_num)

    return fib[n]

#print(fibonacci(5))

#lucas numbers
def lucas(n):
    '''
    Return the nth value in the lucas sequence

    :param n: The number position of the value in the lucas sequence (starting with zero index)
    '''

    luc = [2, 1]

    for i in range(2,n+1):
        new_num = luc[i-2] + luc[i-1]
        luc.append(new_num)

    return luc[n]

#print(lucas(7))

#sum series
def sum_series(x, y=0, z=1):
    '''
    Return the nth value in the series from 2 starting numbers

    :param x: The number position of the value in the lucas sequence
              (starting with zero index)
    :param y=0: The zero position number of the series, default value is 0
    :param z=0: The one posiion number of the series, the default value is 1

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(x, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(x, 2, 1) should be equivalent to lucas(n).

    sum_series(x, 3, 2) should generate another series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci series
    '''
    series = [y, z]

    for i in range(2,x+1):
        new_num = series[i-2] + series[i-1]
        series.append(new_num)

    return series[x]

#print(sum_series(7,2,1))


if __name__ == "__main__":
    #test the fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # test the lucas function
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

