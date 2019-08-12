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

#import sys
import random

# global constant, idk if this is bad form
# constInt = 21

def diff21(n=21): # Our constant
           
    # Generate pseudo-random int
    myInt = random.randint(-50,50)
    print("\n\n>>> The PRNG returned: '%d'. <<<" % (myInt))
    print("\nThe value of our constant is: '%d'." % (n))
    
    # Determine abs of the difference between PRNG and constant.
    diffInt = abs(myInt - n)
    # diffInt = ((abs(myInt)) - (constInt)) # incorrect
    print("\nThe ABS of the difference between our constant and PRNG is: '%d'." % (diffInt))
    
    # Is abs of difference greater than the constant?
    if(diffInt > n):
        print("\n'%d' is Greater Than '%d', so we will double it." % (diffInt, n))
        diffInt += diffInt
        print("\nThe value of our difference has been doubled to: '%d'." % (diffInt))
    # Value of abs of difference is equal to constant.
    elif(diffInt == n):
        print("\n'%d' is Equal to '%d', so we will return '%d'." % (diffInt, n, diffInt))
        print("\nThe value of our difference, '%d' was not changed." % (diffInt))            
    # Value of abs of difference is less than the constant.
    elif(diffInt < n):
        print("\n'%d' is Less Than '%d', so we will return '%d'." % (diffInt, n, diffInt))
        print("\nThe value of our difference, '%d' was not changed." % (diffInt))          
    else:
        print("\nAn error occurred. Please rerun.")      
        
    return diffInt

# diff21(constInt)  

if __name__ == "__main__":

    def main():

        # This does not work correctly (Value returned). Revisit and revise.
        myCount = 0
        while(myCount < 50):
            # The C# way
            # for(i=0; i<=50; i++):
            # Call function which calculates the abs(difference)
            # Store return value
            retInt = '' # hack which doesn't fix it
            retInt = diff21()
            # diff21()
            if(retInt != ''): # hack because I don't know why this line prints before function call
                # hack doesn't work
                print("\n!!! Value returned is: '%d' !!!" % (retInt))
            myCount += 1

        print("\n>>>> Count of PRNG evaluated is: '%d' <<<<" % (myCount))

main()    

     

 