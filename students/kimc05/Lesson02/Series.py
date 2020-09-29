#function for fibonacci series
def fibonacci(n):
    # in case of first 2 fibonacci sequence
    if n <= 1:
        return n
    #recursion of fibonacci series executed
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
#double checking work for fibonacci
#for x in range(8, 15):
#    print(fibonacci(x))

#function for lucas series
def lucas(n):
    #in case of first 2 lucas sequence
    if n == 0:
        return 2
    elif n == 1:
        return 1
    #recursion of lucas series executed
    else:
        return (lucas(n - 1) + lucas(n - 2))

#double checking work for lucas
#for x in range(0, 13):
#   print(lucas(x))

#function to compute all related series
def sum_series(n, s0 = 0, s1 = 1):
    #in case of first 2 sequences
    if n == 0:
        return s0
    elif n == 1:
        return s1
    #recursion of series executed
    else:
        return (sum_series(n-1, s0, s1) + sum_series(n-2, s0, s1))

#double checking work for sum_series
#for x in range(0, 13):
#    print(sum_series(x, 4, 9))

if __name__ == "__main__":
    # run some tests
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(11) == 89
    assert fibonacci(12) == 144
    assert fibonacci(13) == 233
    assert fibonacci(14) == 377
    assert fibonacci(15) == 610

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # test that sum_series matches fibonacci
    assert sum_series(20) == fibonacci(20)
    assert sum_series(21, 0, 1) == fibonacci(21)

    # test if sum_series matched lucas
    assert sum_series(35, 2, 1) == lucas(35)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 4, 9) == 4
    assert sum_series(1, 4, 9) == 9
    assert sum_series(2, 4, 9) == 13
    assert sum_series(3, 4, 9) == 22
    assert sum_series(4, 4, 9) == 35
    assert sum_series(5, 4, 9) == 57

    print("tests passed")