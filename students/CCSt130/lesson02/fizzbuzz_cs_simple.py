# -*- coding: utf-8 -*-
"""
This code determines whether a number 1 to 100 is divisible by x or y and if 
it is divisible by both. It will print 1 of 2 strings if TRUE and a third string
if n is divisible by both x and y.
"""

"""
Lesson02 :: FizzBuzz Exercise
@author: Chuck Stevens :: CCSt130
Created on Thu May 23 10:46:13 2019
"""

def fizzy():
    """ Evaluates a range and determines if n is divisible by x and or y. """
    
    # divisors
    div1 = 4
    div2 = 5
    
    # strings to print when remainder == 0
    str1 = "Fizz"
    str2 = "Buzz"
    
    for num in range(1,101): # range evaluated: 1-100

        if(num % div1 == 0 and num % div2 == 0):
            print("%d: %s%s!" % (num, str1, str2)) 
        elif(num % div1 == 0):
            print("%d: %s!" % (num, str1))
        elif(num % div2 == 0):
            print("%d: %s!" % (num, str2))
        else:
            print("%d: ----" % (num))

fizzy()
    