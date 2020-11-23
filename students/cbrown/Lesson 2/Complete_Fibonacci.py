#Fibonacci Series Exercise
def fibonacci(n):
    '''
    returns the nth value of the fibonacci series
    '''
    #fibonacci sequence list
    fib_seq = [0,1]

    #fibonacci series counter
    index = 0

    if n == 0:
        return fib_seq[0]

    for i in range(n - 1):
        new_fib_num = fib_seq[index] + fib_seq[index+1]
        fib_seq.append(new_fib_num)
        index = index + 1

    return fib_seq[-1]

#Lucas Series Exercise
def lucas(n):
    '''
    returns the nth value of the fibonacci series
    '''
    #lucas sequence list
    fib_seq = [2,1]

    #lucas series counter
    index = 0

    if n == 0:
        return fib_seq[0]

    for i in range(n - 1):
        new_fib_num = fib_seq[index] + fib_seq[index+1]
        fib_seq.append(new_fib_num)
        index = index + 1

    return fib_seq[-1]

#Sum Series Exercise
def sum_series(n,x = 0,y = 1):
    '''
    returns the nth value of the fibonacci series
    '''
    #sequence list
    fib_seq = [x,y]

    #fibonacci series counter
    index = 0

    if n == 0:
        return fib_seq[0]

    for i in range(n - 1):
        new_fib_num = fib_seq[index] + fib_seq[index+1]
        fib_seq.append(new_fib_num)
        index = index + 1

    return fib_seq[-1]

if __name__ == "__main__":
    #ensure fibonacci function returns correct values
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #ensure lucas series returns correct values
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    #ensure fibonacci matches sum series
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

    print('tests passed')
