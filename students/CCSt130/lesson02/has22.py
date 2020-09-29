# -*- coding: utf-8 -*-
"""
This code generates a 1000 element tuple then compares
element[n] with element[n+1] to see if there is a match between
those elements and a constant. 
"""

"""
Lesson02 :: Has22
CodingBat Exercise 
@author: Chuck Stevens :: CCSt130
Created on Sun Jun 30 21:11:21 2019
"""

import random

def gen_tuple():
    """ Generates ints using PRNG and creates 1000 element tuple. """
    # Holds ints from PRNG
    my_tuple = []
    # Counter for while loop
    ctr0 = 0
    # Holds pseudo-random int
    add_int = None
    
    # Generate 1000 pseudo-random ints
    while (ctr0 <= 999):
        
        add_int = (random.randint(1,12))
        # Test
        # print(add_int)
        # print()
        
        # Append ints to tuple
        my_tuple.append(add_int)
     
        # Increment while loop counter
        ctr0+=1
        
    # Test
    print()
    print(my_tuple)
    print()

    # Send that tuple back to main
    return(my_tuple)
    
def has22(a_tuple):
    """ Compares element[n] to element[n+1] and outputs match to screen. """
    # Counters to iterate through the loop
    ctr1 = 0
    ctr2 = 1
    # Value that will be searched for in tuple
    search_val = 2
    
    # Search via loop as long as ctr1 index is less than length of tuple
    while(ctr1 < len(a_tuple)):
        # Does the element in the tuple match the search value?
        if(a_tuple[ctr1] == search_val):
            print()
            print("*** Search value '{}' found in tuple. ".format(search_val), end = "")
            print("Element location is a_tuple[{}] ***".format(ctr1))
            # Is the search value found in the subsequent element also?
            if(a_tuple[ctr1] == a_tuple[ctr2]):
                print()
                print(">>> TRUE! Hooray, search value match found! ", end = "")
                print("Element locations are: ", end = "")
                print("a_tuple[{}], a_tuple[{}]".format(ctr1,ctr2))
                # One could add this match to another list
                print()
            # No match between elements
            else:
                print()
                print("Bummer! ", end = "")
                print("No search value match between: ", end = "")
                print("a_tuple[{}], a_tuple[{}]".format(ctr1,ctr2))
                print()
        else:
            pass
        # Let's increment
        ctr1+=1
        ctr2+=1
        
if __name__ == "__main__":

    def main():      
        # Call function to generate ints
        my_ints = gen_tuple()
        # Evaluate elements in tuple
        has22(my_ints)

main()
