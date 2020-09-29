def fibonacci(n):
    # The function return the nth value in the fibonacci series (starting with zero index).

    # declaring base values 
    # for positions 0 and 1 
    a = 0
    b = 1
      
    if (n == 0) : 
        return a 
   
    # generating number 
    for i in range(1, n) : 
        c = a + b 
        a = b 
        b = c 
      
    return b 


def lucas(n) : 
  
    # The function should return the nth value in the lucas series (starting with zero index).
    
    # declaring base values 
    # for positions 0 and 1 
    a = 2
    b = 1
      
    if (n == 0) : 
        return a 
   
    # generating number 
    for i in range(2, n + 1) : 
        c = a + b 
        a = b 
        b = c 
      
    return b 
  


def sum_series(n,a=0,b=1):
    """compute nth value for either Fibonacci Series or Lucas series based on
    the the two optional values.
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-2, a, b) + sum_series(n-1, a, b)


if __name__ == "__main__":
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


