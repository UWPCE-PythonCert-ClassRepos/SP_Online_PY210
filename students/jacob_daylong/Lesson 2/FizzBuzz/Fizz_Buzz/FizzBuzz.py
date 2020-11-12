# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:03:05 2020

@author: jaked
"""

x = range(1, 101)

for i in x:
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)