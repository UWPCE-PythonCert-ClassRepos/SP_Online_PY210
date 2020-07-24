def fibonacci(n):
    num = [0,1]
    if n == 0:
        return num[0]
    elif n == 1:
        return num[1]
    else:
        for i in range(n-1):
            fib = num[0] + num[1]
            num.append(fib)
            num.pop(0)
        try:
            return num[1]
        except:
            return 'error'
#fibonacci(0)

def lucas(n):
    num = [2,1]
    if n == 0:
        return num[0]
    elif n == 1:
        return num[1]
    else:
        for i in range(n-1):
            fib = num[0] + num[1]
            num.append(fib)
            num.pop(0)
        return num[1]
        
#lucas(6)

def sum_series(n, m=0, z=1):
    num = [m, z]
    if n == 0:
        return num[0]
    elif n == 1:
        return num[1]
    else:
        for i in range(n-1):
            fib = num[0] + num[1]
            num.append(fib)
            num.pop(0)
        return num[1]
        
#sum_series(4,0,1)


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
