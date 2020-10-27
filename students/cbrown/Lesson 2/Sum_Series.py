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

sum_series(0,3,2)
