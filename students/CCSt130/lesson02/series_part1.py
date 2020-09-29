# -*- coding: utf-8 -*-
"""
This code will calculate either the Fibonacci Sequence or the Lucas Sequence
based the user's selection, to F_n.
"""

"""
Created on Mon May 20 10:31:21 2019
Lesson02 :: Fibonacci Series Exercise
Part 1
@author: Chuck Stevens :: CCSt130
"""
import sys

def fibonacci(n):
    
    seed_sequence = [0, 1]  # Fibonacci seed values
    
    calc_sequence = seed_sequence[:] # Used for calculating the sequence
    
    sequence = seed_sequence[:] # List to hold sequence after calculating

    swap_sequence = None # temp name a.k.a. swap variable 

    # Print to confirm expected values
    print()
    print("seed_sequence values:")
    print(seed_sequence)

    print()
    print("Initial value of Sequence: ")
    print(sequence)
    print()
    
    i = 0 # counter for while loop
    
    while(i <= (n-2)): # n is offset by two as the seed values are index 0, 1
        
        print("Printing calc_sequence index 0: ", end = '')
        
        print(calc_sequence[0]) # Test
       
        swap_sequence = calc_sequence[0] # first element in list to temp name
        
        calc_sequence[0] = calc_sequence[1] # value of second element becomes the first
        
        calc_sequence[1] = swap_sequence + calc_sequence[1]  # sum index 0, 1 to get subsequent value
        # calc_sequence[1] += swap_sequence # alternative expression

        sequence.append(calc_sequence[1]) # append to list starting at sequence[2]

        i+=1 # increment loop
        
    # In order to print the first 2 (seed) values, the last 2 are printed outside the loop
    print("Printing calc_sequence index 0: ", end = '')
    print(calc_sequence[0]) # Test
    print("Printing calc_sequence index 0: ", end = '')
    print(calc_sequence[1]) # Test

    # Print to confirm values
    print()
    print("calc_sequence values:")
    print(calc_sequence)
    
    print()
    print("Sequence (list) is:")
    print (sequence)
    
    return(calc_sequence[1])
        
if __name__ == "__main__":

    def main():

        # Determine F_n, cast to int
        print()
        print("Let's Fibonacci!")
        n_choice = int(input("Please enter a value 'n' for the maximum results to be displayed: "))
        print()
        print("You entered: '%s'." % (n_choice))
    
        if(n_choice >= 0):    
            x = fibonacci(n_choice)
        else:
            print()
            print("Invalid Entry, please rerun.") 
            # Note: Error handling needs to be more robust
            sys.exit
        
        print()
        print("The value for the 'Nth' position in the Sequence where 'N'=='%d' is: %d" % (n_choice, x))
        print()
        
main()        