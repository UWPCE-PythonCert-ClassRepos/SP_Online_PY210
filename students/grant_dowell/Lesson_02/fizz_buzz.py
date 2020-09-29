# -*- coding: utf-8 -*-
"""
fizz_buzz.py
Created on Tue Dec 24 10:50:46 2019

@author: Grant Dowell
Excercise 2.3 - Fizz Buzz
"""

for n in range(100):
    n = n+1
    print_ln = ''
    if n%3 == 0:
        print_ln = print_ln+'Fizz'
    if n%5 == 0:
        print_ln = print_ln+'Buzz'
    if print_ln == '':
        print(n)
    else:
        print(print_ln)