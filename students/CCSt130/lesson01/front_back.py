# -*- coding: utf-8 -*-
"""
Created on Mon May 13 2019

@author: Chuck Stevens :: CCSt130
"""

test_string = "Watermelon"

def front_back(str):
    
    # Find length of the string and assign it to a variable
    index = (len(test_string)-1)
    
    print("\nWe're going to swap the first and last characters of our string.")
    
    # Display string passed to the function
    print("\nOur string is: '%s' " % (test_string))

    # Concatenate the last char with the middle chars and the first char
    var_swap = test_string[index]+test_string[1:(index-1)]+test_string[0]

    # Display result on screen
    print("\nThe result is: '%s' " % (var_swap))
    
front_back(test_string)
    
    