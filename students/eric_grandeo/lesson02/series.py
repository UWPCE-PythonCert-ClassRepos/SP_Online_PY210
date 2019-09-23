#fibonacci sequence
def fibonacci(n):
    '''
    Return the nth value in the Fibonacci sequence

    :param n: The number position of the value in the Fibonacci sequence (starting with zero index)
    '''

    fib = [0, 1]

    for i in range(2,n):
        new_num = fib[i-2] + fib[i-1]
        fib.append(new_num)

    return fib[n-1]

print(fibonacci(9))

#lucas numbers
def lucas(n):
    '''
    Return the nth value in the lucas sequence

    :param n: The number position of the value in the lucas sequence (starting with zero index)
    '''

    luc = [2, 1]

    for i in range(2,n):
        new_num = luc[i-2] + luc[i-1]
        luc.append(new_num)

    return luc[n-1]

print(lucas(7))

#sum series
def sum_series(x, y=0, z=1):
    '''
    Return the nth value in the series from 2 starting numbers

    :param x: The number position of the value in the lucas sequence
              (starting with zero index)

    :param y=0: The starting number of the series, default is 0

    :param z=0: The second number of the series, the default is 1
    '''
    series = [y, z]

    for i in range(2,x):
        new_num = series[i-2] + series[i-1]
        series.append(new_num)

    return series[x-1]

print(sum_series(7,2,1))

