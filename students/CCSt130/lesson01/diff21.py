# -*- coding: utf-8 -*-
"""
Created on Tue May 14 2019

@author: Chuck Stevens :: CCSt130
"""

"""
Puzzle:
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

"""
# Global constant, idk if this is good form.
constInt = 21

#import sys
import random

def diff21(n):
    # Our constant
    # constInt = 21
           
    # Generate pseudo-random int
    myInt = random.randint(-50,50)
    print("\n\n>>> The PRNG returned: '%d'. <<<" % (myInt))
    print("\nThe value of our constant is: '%d'." % (constInt))
    
    # Determine abs of the difference between PRNG and constant.
    diffInt = abs(myInt - constInt)
    # diffInt = ((abs(myInt)) - (constInt)) # incorrect
    print("\nThe ABS of the difference between our constant and PRNG is: '%d'." % (diffInt))
    
    # Is abs of difference greater than the constant?
    if(diffInt > constInt):
        print("\n'%d' is Greater Than '%d', so we will double it." % (diffInt, constInt))
        diffInt += diffInt
        print("\nThe value of our difference has been doubled to: '%d'." % (diffInt))
    # Value of abs of difference is equal to constant.
    elif(diffInt == constInt):
        print("\n'%d' is Equal to '%d', so we will return '%d'." % (diffInt, constInt, diffInt))
        print("\nThe value of our difference, '%d' was not changed." % (diffInt))            
    # Value of abs of difference is less than the constant.
    elif(diffInt < constInt):
        print("\n'%d' is Less Than '%d', so we will return '%d'." % (diffInt, constInt, diffInt))
        print("\nThe value of our difference, '%d' was not changed." % (diffInt))          
    else:
        print("\nAn error occurred. Please rerun.")      
        
    return diffInt

diff21(constInt)


 