def fibonacci(n):
    #Fibonacci sequence

    #initialize variables
    fib = []
    nth = 0

    for num in range(0,n+1):
        if num == 0:
            fib.append(0)
        elif num == 1:
            fib.append(1)
        elif num > 1:
            nth = fib[-2] + fib[-1]
            fib.append(nth)
    return(fib[n])


def lucas(n):
    #Lucas Numbers
    luc = []
    nth = 0

    for num in range(0,n+1):
        if num == 0:
            luc.append(2)
        elif num == 1:
            luc.append(1)
        elif num > 1:
            nth = luc[-2] + luc[-1]
            luc.append(nth)
    return(luc[n])




def sum_series(n, a=0, b=1):
    #related number sequence series
    seq = []
    nth = 0

    for num in range(0,n+1):
        if num == 0:
            seq.append(a)
        elif num == 1:
            seq.append(b)
        elif num > 1:
            nth = seq[-2] + seq[-1]
            seq.append(nth)
    return(seq[n])


# tests
print ("fibonacci(7) = " + str(fibonacci(7)))
print ("lucas(7) = " + str(lucas(7)))

print("sum series fib 7 = " + str(sum_series(7)))
print("sum series luc 7 = " + str(sum_series(7, 2, 1)))

# asserts test block
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

    print("assert tests passed")
