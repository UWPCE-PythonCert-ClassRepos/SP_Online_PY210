# -*- coding: utf-8 -*-

""" Creates x tuples of length y and returns the sum of each tuple's elements. """

"""
Lesson02 :: Sum3
CodingBat Exercise 
@author: Chuck Stevens :: CCSt130
Please note: Using PRNG here to generate more tuples (more than 3 of length 3).
Mon Jul  1 23:11:07 2019
"""

"""Given an array of ints length 3, return the sum of all the elements."""

import random

def gen_tuple():
    """ Generates ints using PRNG and creates n element tuple. """
    # Holds ints from PRNG
    my_tuple = []
    # Counter for while loop
    ctr0 = 0
    # Holds pseudo-random int
    add_int = None
    # Generate n pseudo-random ints
    # Constant below determines the length of the tuple
    while (ctr0 <= 24):
        add_int = (random.randint(1,12))
        # Append ints to tuple
        my_tuple.append(add_int)
        # Increment while loop counter
        ctr0+=1
    # Test
    print()
    print(my_tuple)
    print()
    # Send that tuple back
    return(my_tuple)

def sum_it(prng_tuple):
    added_up = sum(prng_tuple)
    
    return(added_up)

if __name__ == "__main__":

    def main():
        """ Calls functions to create tuples and sum their elements, then prints them. """
        # Counter for while loop
        ctr1 = 1
        # List for all the sums
        tuple_of_sums = []

        # Constant below determines the number of tuples
        while(ctr1 <= 12):
            temp_list = []
            sum_value = None
            
            print()
            print("PRNG'd Tuple{} values are: ".format(ctr1))
            # Run function to generate tuple
            # Assign return value to a name
            temp_list = gen_tuple()
            # Run function to sum values in a tuple
            # Assign return value to a name
            sum_value = sum_it(temp_list)
            
            print("Sum of Tuple{} values is:".format(ctr1), end = " ")
            # Print sum
            print(sum_value)
            print()
            # Append all sums to this list
            tuple_of_sums.append(sum_value)
            
            ctr1+=1

        print()
        print("Here is a list of all the sums: ")
        print()
        # Print all sums
        print(tuple_of_sums)
        print()

main()

