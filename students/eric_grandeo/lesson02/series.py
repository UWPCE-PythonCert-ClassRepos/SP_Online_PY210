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

print(fibonacci(8))

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

print(lucas(6))






