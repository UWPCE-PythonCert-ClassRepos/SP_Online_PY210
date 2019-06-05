#!/usr/bin/env python3
"""
This code will calculate either the Fibonacci Sequence or the Lucas Sequence
based the user's selection, to F_n.
"""

"""
Lesson02 :: Fibonacci Series Exercise
Part 3
Please note: 
Added test function
@author: Chuck Stevens :: CCSt130
Created on Tue May 21 17:57:34 2019
"""

import random 

def fibonacci(n):
    """ Compute the nth Fibonacci number. """
           
    print()
    print("Evaluating 'n' == ", end = "")
    print(n)
    
    # Fibonacci seed values
    n0 = 0
    n1 = 1
    
    # return n or p after evaluating within if statement
    if(n == 0):
        # print()
        print("Seed value entered: ", end ='')
        print("[%d]" % n0)
        return(n0)

    elif(n == 1):
        print("Seed value entered: ", end ='')
        print("[%d, %d]" % (n0, n1))
        return(n1)

    else:
        print()
        print("*** Fibonacci series will be calculated where the nth value is: ", end ='')
        print(str(n) + " ***")
        n_fib = sum_series(n, n0, n1)
        return(n_fib)

def lucas(n):
    """ Compute the nth Lucas number. """

    print()
    print("Evaluating 'n' == ", end = "")
    print(n)
    
    # Lucas seed values
    n0 = 2
    n1 = 1
    
    if(n == 0):
        print("Seed value entered: ", end ='')
        print(n0)
        return(n0)

    elif(n == 1):
        print("Seed value entered: ", end ='')
        print(n1)
        return(n1)
        
    else:
        print()
        print("*** Lucas series will be calculated where the nth value is: ", end ='')
        print(str(n) + " ***")
        n_lucas = sum_series(n, n0, n1)
        return(n_lucas)

def sum_series(n, n0=0, n1=1):
    
    """ Compute the nth value of a summation series. """
    
    # Identify the series
    
    if(n0 == 0):
        print()
        print(">>> Calculating Fibonacci Series! <<<")
                
    elif(n0 == 2):
        print()
        print(">>> Calculating Lucas Series! <<<")
        
    else:
        print()
        print("### Unnamed series will be calculated where the nth value is: ", end = "")
        print(str(n) + " ###")       

        # Added if statement for the odd test case
        if(n == 0):
            print()
            print("Seed value entered.")
            print()
            return(n0)
        elif(n == 1):
            print()
            print("Seed value entered.")
            print()
            return(n1)
        else:
            print()
            print(">>> Calculating Unnamed Series! <<<")
                  
    seed_values = [n0, n1]
    print()
    print("Seed_values:")
    print(seed_values)

    # Initializing list so the series may be printed
    sequence_list = seed_values[:]
    print()
    print("Sequence_list:")
    print(sequence_list)
    
    i = 0 # counter for while loop
        
    while(i <= (n - 2)): # n is offset by two as the seed values are index 0, 1

        swap_sequence = n0 # first element in list to temp name    

        n0 = n1 # value of second element becomes the first

        n1 = swap_sequence + n1  # sum index 0, 1 to get subsequent value
        # n1 += swap_sequence # alternative expression
        
        sequence_list.append(n1) # append to list starting at sequence[2]
        
        i+=1 # increment while loop

    print()
    print("Sequence (list) is:")
    print (sequence_list)
    
    return(n1)    
    
def test_series():
    
    print()
    print("*** Running tests! ***")
    
    # Use PRNG for n value
    r = random.randint(3, 12)
    
    # Test Fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Test Lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # Testing with random n value
    # This could be looped for even more fun!
    assert sum_series(r) == fibonacci(r)
    
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

    print()
    print("*** Tests passed! ***")

if __name__ == "__main__":
    
    def main():
        
        # Calling test function
        test_series() 
        
main()    
