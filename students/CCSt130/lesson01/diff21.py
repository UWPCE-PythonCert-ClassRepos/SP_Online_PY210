# -*- coding: utf-8 -*-
"""
Created on Tue May 14 2019

@author: Chuck Stevens :: CCSt130
"""

"""
Puzzle:
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff_21(19) → 2
diff_21(10) → 11
diff_21(21) → 0

"""
# Global constant
global_const_int = 21

import random

def diff_21(n):
           
    # Generate pseudo-random int
    my_int = random.randint(-50,50)
    print("\n\n>>> The PRNG returned: '%d'. <<<" % (my_int))
    print("\nThe value of our constant is: '%d'." % (global_const_int))
    
    # Determine abs of the difference between PRNG and constant.
    diff_int = abs(my_int - global_const_int)
    # diff_int = ((abs(my_int)) - (global_const_int)) # incorrect
    print("\nThe ABS of the difference between our constant and PRNG is: '%d'." % (diff_int))
    
    # Is abs of difference greater than the constant?
    if(diff_int > global_const_int):
        print("\n'%d' is Greater Than '%d', so we will double it." % (diff_int, global_const_int))
        diff_int += diff_int
        print("\nThe value of our difference has been doubled to: '%d'." % (diff_int))
    # Value of abs of difference is equal to constant.
    elif(diff_int == global_const_int):
        print("\n'%d' is Equal to '%d', so we will return '%d'." % (diff_int, global_const_int, diff_int))
        print("\nThe value of our difference, '%d' was not changed." % (diff_int))            
    # Value of abs of difference is less than the constant.
    elif(diff_int < global_const_int):
        print("\n'%d' is Less Than '%d', so we will return '%d'." % (diff_int, global_const_int, diff_int))
        print("\nThe value of our difference, '%d' was not changed." % (diff_int))          
    else:
        print("\nAn error occurred. Please rerun.")      
        
    return diff_int

diff_21(global_const_int)


 