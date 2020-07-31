#!/usr/bin/env python3

'''
 - create series.py in the Lesson_1 folder.
 - add a function called fibonacci with input 'n' to return nth value of the Fibonacci series.
 - add a function to produce the Lucas numbers - similar to the fibonacci series but starting with 2 and 1 in place of 0 and 1
 - create a function to create any variation of the Fibonacci and Lucas series defaulting to the Fibonacci, but allowing user-defined start points.
 
 - Finally, have the program test its functions by using assertions
'''

#Define function for the Fibonacci Series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


#Define function for the Lucas Numbers.  Same as Fibonacci, but with different start points.
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))

#Define function to do what the Lucas function does, but with user-definable start values that defaults to the Fibonacci series.
def sum_series(n, n_0 = 0, n_1 = 1):
    if n == 0:
        return n_0
    elif n == 1:
        return n_1
    else:
        #retrive the prior (2) function results and add together
        return (sum_series(n-1, n_0, n_1) + sum_series(n-2, n_0, n_1))


#have program test itself as a script
if __name__ == '__main__':
    #Test the Fibonacci Series Function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    print('Fibonacci Tests Passed.')

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    print('Lucas Tests Passed.')

    #test the sum-series function.
    #check sum_series against fibonacci
    assert sum_series(0) == fibonacci(0)
    assert sum_series(1) == fibonacci(1)
    assert sum_series(2) == fibonacci(2)
    assert sum_series(3) == fibonacci(3)
    assert sum_series(4, 0, 1) == fibonacci(4)
    assert sum_series(5, 0, 1) == fibonacci(5)
    assert sum_series(6, 0, 1) == fibonacci(6)
    assert sum_series(7, 0, 1) == fibonacci(7)

    #check sum_series against lucas
    assert sum_series(0, 2, 1) == lucas(0)
    assert sum_series(1, 2, 1) == lucas(1)
    assert sum_series(2, 2, 1) == lucas(2)
    assert sum_series(3, 2, 1) == lucas(3)
    assert sum_series(4, 2, 1) == lucas(4)

    #make some new series
    assert sum_series(0,5,2) == 5   #user-specified values 2 and 1 in place of defaults
    assert sum_series(1,5,2) == 2   #user-specified values 2 and 1 in place of defaults
    assert sum_series(2,5,2) == 7   #user-specified values 2 and 1 in place of defaults
    assert sum_series(3,5,2) == 9   #user-specified values 2 and 1 in place of defaults
    assert sum_series(4,5,2) == 16   #user-specified values 2 and 1 in place of defaults

    print('sum_series Tests Passed.')
    print('\nAll TESTS PASSED.\n')
