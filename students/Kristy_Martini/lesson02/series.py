def fibonacci(n):
    """
    Function to return the nth value of the fibonacci sequence
    
    Inputs:
    n   the "nth" integer of the fibonacci sequence

    Returns:
    The fibonacci sum value at n 
    """
    i = 1
    first = 0 
    second = 1
    
    if(n == 0):
        print(first)
        return first
    
    while(i < n):
        second_copy = second
        second = second + first 
        first = second_copy
        i += 1 
    print(second)
    return second

def lucas(n):
    """
    Function to return the nth value of a lucas numbers
    
    Inputs:
    n   the "nth" integer of the lucas numbers

    Returns:
    The lucas numbers value at n 
    """
    i = 0 
    first = 2
    second = 1
    
    if(n == 0):
        print(first)
        return first 
    elif(n == 1):
        print(second)
        return second
    else:
        i = 1
        while(i < n):
            second_copy = second
            second = second + first 
            first = second_copy
            i += 1
        print(second)
        return second

def sum_series(n, first=0, second=1):
    """
    Function to return the nth value of a summation series given the 
    two starting values. The default values are 0 and 1 for the fibonacci
    sequence but the user can specify the two starting values
    
    Inputs:
    n       the "nth" integer of the sum series
    first   the first (zero index) value of the series, default is 0 for fibonacci sequence
    second  the second (first index) value of the series, default is 1 for fibonacci sequence

    Returns:
    The sum value of the sum series at "n"
    """

    if(n == 0):
        print(first)
        return first
    
    i = 1
    while(i < n):
        second_copy = second
        second = second + first 
        first = second_copy
        i += 1 
    print(second)
    return second


if __name__ == "__main__":
    #Test fibonacci sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(10) == 55

    #Test lucas numbers
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(10) == 123

    #Test sum series
    assert sum_series(0) == fibonacci(0)
    assert sum_series(10) == fibonacci(10)
    assert sum_series(3, 0, 1) == fibonacci(3)
    assert sum_series(0, 2, 1) == lucas(0)
    assert sum_series(4, 2, 1) == lucas(4)

    #Test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
