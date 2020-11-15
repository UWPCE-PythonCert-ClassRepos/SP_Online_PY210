#!/usr/bin/env python3
# Craig Simmons
# Python 210
# fizzbuzz.py - Lesson02 - FizzBuzz Exercise
# Created 11/13/2020 - csimmons
# Modified 11/14/2020 - csimmmons

def fizz_buzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

fizz_buzz()

