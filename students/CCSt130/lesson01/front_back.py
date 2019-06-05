# -*- coding: utf-8 -*-
"""
Created on Mon May 13 2019

@author: Chuck Stevens :: CCSt130
"""

varGW = "Strategery"

def front_back(str):
    
    # Find length of the string and assign it to a variable
    index = (len(varGW)-1)
    
    print("\nWe're going to swap the first and last characters of our string.")
    
    # Display string passed to the function
    print("\nOur string is: '%s' " % (varGW))

    # Concatenate the last char with the middle chars and the first char
    varSwap = varGW[index]+varGW[1:(index-1)]+varGW[0]

    # Display result on screen
    print("\nThe result is: '%s' " % (varSwap))
    
front_back(varGW)
    
    