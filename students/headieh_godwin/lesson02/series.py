""" compute the nth Fibonacci number """
def fibonacci(n):
    #checks to make sure n is non-negative
    if n<0:
        print('Input must be non-negative')
    #first(0 indexed) fibonacci value is 0
    elif n==0:
        return 0
    #second fibonacci value is 1(n=1 per second value of 0 index)
    elif n==1:
        return 1
    #find all other fibonacci values after defining first 2 using given formula
    else:
        return fibonacci(n-2)+fibonacci(n-1)

""" compute the nth Lucas number """   
def lucas(n):
    #checks to make sure n is non-negative
    if n<0:
        print('Input must be non-negative')
    #first(0 indexed) lucas value is 0
    elif n==0:
        return 2
    #second lucas value is 1(n=1 per second value of 0 index)
    elif n==1:
        return 1
    #find all other fibonacci values after defining first 2 using given formula
    else:
        return lucas(n-2)+lucas(n-1)

""" compute the nth Series number, given n0, n1, and formula """
def sum_series(n, n0=0,n1=1):
    #checks to make sure n is non-negative
    if n<0:
        print('Input must be non-negative')
    #first(0 indexed) value is n0
    elif n==0:
        return n0
    #second value is n1
    elif n==1:
        return n1
    #find all other series values after defining first 2 using given formula"""
    else:
        return sum_series(n-2,n0,n1)+sum_series(n-1,n0,n1)
    
""" compute the nth Lucas number using sum_series"""    
def new_lucas(n):
    l = sum_series(n=n,n0=2,n1=1)
    return l
    
""" compute the nth Fibonacci number using sum_series""" 
def new_fibonacci(n):
    f = sum_series(n=n,n0=0,n1=1)
    return f

""" Testing to make sure calculations are correct""" 
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
    
    # test that new_lucas matches lucas
    assert new_lucas(5) == lucas(5)
    assert new_lucas(7) == lucas(7)
    
    # test that new_fibonacci matches fibonacci
    assert new_fibonacci(5) == fibonacci(5)
    assert new_fibonacci(7) == fibonacci(7)

    print("tests passed")