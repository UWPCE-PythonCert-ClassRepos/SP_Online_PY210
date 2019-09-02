# -*- coding: utf-8 -*-
"""
Created: Mon Sep  2 07:58:20 2019
Author: Philip Behrend
Title: Fizz Buzz
"""

def fizz_buzz():
    for i in range(1,101):
        if (i % 3 == 0) & (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0 :
            print("Buzz")
        else: 
            print(i)
        