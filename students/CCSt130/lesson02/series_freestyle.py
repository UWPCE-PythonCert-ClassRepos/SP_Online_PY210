# -*- coding: utf-8 -*-
"""
This code will calculate either the Fibonacci Sequence or the Lucas Sequence
based the user's selection, to F_n.
"""

"""
Lesson02 :: Fibonacci Series Exercise
Part 2
Please note: 
This version replaces redundant Fibonacci and Lucas functions with one 'sum_series' function
@author: Chuck Stevens :: CCSt130
Created on Tue May 21 10:38:35 2019
"""

import sys

def sum_series(seq, fn): # input: Sequence and F_n
    
    # Generic sequence
    if(seq == 'F' or seq == 'f'):
        seed_sequence = [0, 1]  # Fibonacci seed values

    elif(seq == 'L' or seq == 'l'):
        seed_sequence = [2, 1]  # Lucas seed values

    # Better error handling needed here
    else:
        print("Sequence choice invalid.")
        print()
        sys.exit()
        
    calc_sequence = seed_sequence[:] # Used for calculating the sequence
    
    sequence_list = seed_sequence[:] # List to hold sequence after calculating

    swap_sequence = None # temp name a.k.a. swap variable 
    
    # Confirm expected values
    print()
    print("seed_sequence values:")
    print(seed_sequence)
    print()
    print("Initial value of sequence (list): ")
    print(sequence_list)
    print()
    
    i = 0 # counter for while loop
    
    while(i <= (fn-2)): # n is offset by two as the seed values are index 0, 1
        
        print("Printing calc_sequence index 0: ", end = '')
        
        print(calc_sequence[0]) # Test
       
        swap_sequence = calc_sequence[0] # first element in list to temp name
        
        calc_sequence[0] = calc_sequence[1] # value of second element becomes the first
        
        calc_sequence[1] = swap_sequence + calc_sequence[1]  # sum index 0, 1 to get subsequent value
        # calc_sequence[1] += swap_sequence # alternative expression

        sequence_list.append(calc_sequence[1]) # append to list starting at sequence[2]

        i+=1 # increment while loop
        
    # In order to print the first 2 (seed) values, the last 2 are printed outside the loop
    print("Printing calc_sequence index 0: ", end = '')
    print(calc_sequence[0]) # Test
    print("Printing calc_sequence index 0: ", end = '')
    print(calc_sequence[1]) # Test

    # Confirm expected values    
    print()
    print("Ending calc_sequence values:")
    print(calc_sequence)
    
    print()
    print("Sequence (list) is:")
    print (sequence_list)
    
    return(calc_sequence[1])

def choose_sequence(): # Take input to display either Fibonacci or Lucas

    seq_choice = input("Please enter 'F' for the Fibonacci Sequence, or 'L' for the Lucas Sequence : ")
    # Note: change input to upper to make error handling easier
    print()
    print("You entered: '%s'." % (seq_choice))
    print()

    if(seq_choice == 'F' or seq_choice == 'f'):    
        print("You've chosen to calculate the Fibonacci sequence!")
    elif(seq_choice == 'L' or seq_choice == 'l'):    
        print("You've chosen to calculate the Lucas sequence!")
    else:            
        print()
        print("Invalid Entry, please rerun.")
        # Note: Error handling needs to be more robust
        sys.exit()

    return(seq_choice)
                
def choose_Fn(): # Take input for F_n to determine end point of sequence
    
    # Determine F_n, cast to int
    n_choice = int(input("Please enter a value 'n' for the maximum results to be displayed: "))
    print()
    print("You entered: '%s'." % (n_choice))
    
    if(n_choice >= 0):    
        return(n_choice)
    else:
        print()
        print("Invalid Entry, please rerun.") 
        # Note: Error handling needs to be more robust
        sys.exit

if __name__ == "__main__":

    def main():
        # initialize functions to determine which series to run and F_n
        x = choose_sequence()
        y = choose_Fn()
        # calculate series
        z = sum_series(x, y)
        
        print()
        print("The value for the 'Nth' position in the Sequence where 'N'=='%d' is: %d" % (y, z))
        print()
        
main()        