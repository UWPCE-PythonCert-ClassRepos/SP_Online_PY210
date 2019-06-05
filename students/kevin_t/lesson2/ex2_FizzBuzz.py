# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:58:15 2019

@author: Kevin
"""
#Iterate on numbers 1 to 100, inclusive
for i in range(1,101):
    #Checks if number is a multiple of 3 and 5, prints "FizzBuzz" if both
    if i%3 == 0 and i%5 == 0:
        print ('FizzBuzz')
    #Checks if number is a multiple of 3, prints "Fizz" if so
    elif i%3 == 0:
        print ('Fizz')
    #Checks if number is a multiple of 5, prints "Buzz" if so
    elif i%5 == 0:
        print ('Buzz')
    #Otherwise, prints the number itself
    else:
        print (i)        