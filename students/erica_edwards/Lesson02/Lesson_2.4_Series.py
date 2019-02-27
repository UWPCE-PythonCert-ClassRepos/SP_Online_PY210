#!/usr/bin/env python3

def fibinacci(n):
    """ 
    The fibinacci series starts at zero and one. The series is calculated by 
    adding the first number to the second number to find the total. For example
    0 and 1 = 1. 1 and 1 = 2. 1 and 2 = 3 and so forth.
    """
    if n < 2:
        return n
    else:
        return fibinacci(n-1) + fibinacci(n-2)

def lucas(n):
    """ 
    The lucas series starts at 2 and 1 instead of zero and calculates the series based
    on the adding the first number to the second number. For example 2 and 1 = 3, 
    1 and 3 = 4, 3 and 4 = 7 and so forth.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, a = 0, b = 1,stack = 1):
    """
    The sum_series function can calculate either fibinacci and other series based on the 
    parameters entered. When a and b are set to default the fibinacci series is calculated.
    If a and b are changed it will calculate a different series. 2 and 1 will calculate 
    the lucas series. 
    """
    if n == 0:
        # stack = stack - 1
        return a
    elif n == 1:
        # stack = stack - 1
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)


if __name__ == "__main__":
    # for x in range(10):
    #     result = fibinacci(x)
    #     print(f'{x} = {result}')
    # for x in range(10):
    #     result = lucas(x)
    #     print(f'{x} = {result}')
    # for x in range(10):
    #     result = sum_series(x, 2, 1)
    #     print (f'{x} = {result}')
    
    # Test Fibinacci method to confirm method returns correct output
    assert fibinacci(0) == 0
    assert fibinacci(2) == 1
    assert fibinacci(5) == 5
    assert fibinacci(6) == 8
   
    #Test Lucas method to confirm method returns correct output
    #First two assertions confirm that the starting point is 2 and 1.
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(5) == 11
    assert lucas(7) == 29
   
    #Test sum_series method. First two confirm Fibinacci series is 
    #correctly setting to 0,1. The second two test if Lucas series
    #numbers are set to 2,1. Last two to confirm method is returning
    #correct number in series 
    assert sum_series(0) == fibinacci(0)
    assert sum_series(1) == fibinacci(1)
    assert sum_series(0, 2, 1) == lucas(0)
    assert sum_series(1, 2, 1) == lucas(1)
    assert sum_series(3) == fibinacci(3)
    assert sum_series(3, 2, 1) == lucas(3)

    print('Tests passed')