
def fibonacci(n): 
    '''
    fibonacci function to return
    the nth value from the given 
    element position
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n): 
    '''
    lucas function to return
    the nth value from the given 
    element position
    '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, n0=0, n1=1):
    # rule out negative numbers
    if n < 0:
        return "Invalid"
    # created a non fibonacci or lucas function
    def non_lucas(num):
        if num == 0:
            return n0
        elif num == 1:
            return n1
        else:
            return non_lucas(num - 1) + non_lucas(num - 2)
    # if statments to recognize the type of sequence requested
    if n0 == 0 and n1 ==1:
        return fibonacci(n) 
    elif n0 == 2 and n1 == 1:
        return lucas(n)
    else:
        return non_lucas(n)

# test cases to verify all functions are operating as expected
if __name__ == "__main__":
    # individual function tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
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
