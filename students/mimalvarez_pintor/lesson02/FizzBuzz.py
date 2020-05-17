# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:11:34 2020

@author: miriam
"""

# Fizz Buzz Problem 
for value in range(1,101):
    if value % 3 == 0 and value % 5 == 0:
        print('FizzBuzz')    
    elif value % 3 == 0:
            print('Fizz')
    elif value % 5 == 0:
            print('Buzz')
    else:
        print(value)
    