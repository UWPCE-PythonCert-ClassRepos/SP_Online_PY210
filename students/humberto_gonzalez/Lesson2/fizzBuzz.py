#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:28:56 2019

@author: humberto gonzalez
"""

def fizzBuzz(n):
    if n%5==0 and n%3==0:
        print('FizzBuzz')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    else:
        print(str(n))

for i in range(101):
    fizzBuzz(i)