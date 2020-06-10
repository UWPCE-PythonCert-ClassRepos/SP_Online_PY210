#!/usr/bin/env python3
import sys
##############################################################
# 20200603    djm series.py module
#
# Duane McCollum Python self-paced winter 2020
#
##############################################################

# Step 1
#
#    Create a new module series.py in the lesson02 folder in your student folder.
#        In it, add a function called fibonacci.
#        The function should have one parameter n.
#        The function should return the nth value in the fibonacci series (starting with zero index).
#    Ensure that your function has a well-formed docstring
#
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

factorial_recursive(3)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(13):
        print(str(fibonacci(i)))

#	Lucas Numbers
#
#	The Lucas Numbers are a related series of integers that start with the values 2 and 1
#	rather than 0 and 1. The resulting series looks like this:
#
#	2, 1, 3, 4, 7, 11, 18, 29, ...
#
#	In your series.py module, add a new function lucas that returns the nth value in the
#	lucas numbers series (starting with zero index).
#
#	Ensure that your function has a well-formed docstring
#
#	You should find it’s very similar to the fibonacci() function.
#
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
lucas(3)
for n in range(4):
        print(str(lucas(n)))