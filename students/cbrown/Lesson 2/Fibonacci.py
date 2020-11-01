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

fibonacci(7)
