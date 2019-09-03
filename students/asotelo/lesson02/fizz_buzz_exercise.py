#!/usr/bin/python3
'''
Author: Alex Sotelo
Exercise 2.3
Python 3 required
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fizz_buzz.html
'''

def fizz_buzz(i):
    if i%3 == 0 and i%5 !=0:
       print('Fizz')
    elif i%5 == 0 and i%3 !=0:
       print('Buzz')
    elif i%3 == 0 and i%5 == 0:
       print('FizzBuzz')
    else:
       print(i)

def print_range(x,y):
    for i in range(x,y):
        fizz_buzz(i)

print_range(1,101)