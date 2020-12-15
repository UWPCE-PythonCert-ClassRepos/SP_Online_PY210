# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:41:41 2020

FizzBuzz

@author: johnh
"""

for i in range(1,101):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)