#!/usr/bin/env python3
import time

def fibonacci(n=5):
    '''This function defines the recursive Fibonacci series and returns the correlating value of the parameter-passed index position'''
    '''Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, ...'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-2) + fibonacci(n-1)

def print_fibonacci_series(n=5):
    '''This function accepts a parameter n and returns the Fibonacci series up to its nth value'''
    for i in range(n):
        print(fibonacci(i))

def lucas(n):
    '''This function defines the recursive Lucas series and returns the correlating value of the parameter-passed index position'''
    '''Lucas Series: 2, 1, 3, 4, 7, 11, 18, 29, ...'''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-2) + lucas(n-1)

def print_lucas_series(n=5):
    '''This function accepts a parameter n and returns the Lucas series up to its nth value'''
    for i in range(n):
        print(lucas(i))

def sum_series(series_element_to_print, first=0, second=1):
    '''This recursive function returns the correlating value of the seris_element_to_print position. The starting two positions are passed as the second and third parameters.'''
    if series_element_to_print == 0:
        return first
    elif series_element_to_print == 1:
        return second
    elif series_element_to_print > 1:
        return sum_series(series_element_to_print - 2, first, second) + sum_series(series_element_to_print - 1, first, second)

def print_sum_series(n, first_value=0, second_value=1):
    '''This function accepts three parameters: the first determines how many values of the sequence to print. 
    The second and third define the first two starting values, upon which the series is built.
    The defaults are set to 0, 1, so if you don't pass in any values, you'll get the fibonacci series. 
    '''
    for i in range(n+1):
        return sum_series(i, first_value, second_value)


if __name__ == "__main__":
    # These assert statements test that my functions match the expected output of their known sequence
    
    # Because the class notes mentioned that the stack can get very deep with recursion, I was curious to see how long these tests take
    # So I imported the time module and set the start variable to immediately before the assert statements:
    start = time.process_time()
    
    # First, we test for Fibonacci outputs:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(17) == 1597
    assert fibonacci(29) == 514229

    # Then, we test that my lucas() function outputs match known Lucas sequence values:
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    assert lucas(10) == 123

    # Now, we test the generalized sum_series() function to see that it matches the Fibonacci sequence (with both optional and passed parameters)
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # And then we test it against the lucas() function
    assert sum_series(5, 2, 1) == lucas(5)

    # Now we'll test sum_series() against non-Fibonacci/Lucas sequences
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    # To determine how long the tests took, I want to capture the time after they finish
    elapsed_time = time.process_time() - start

    # Now we'll calculate how long the test took 
    print("Test Successful. Completed in " + str(elapsed_time) + " seconds.")