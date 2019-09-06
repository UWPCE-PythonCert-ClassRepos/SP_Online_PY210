#!/usr/bin/python3
'''
Author: Alex Sotelo
Exercise 2.2
Python 3 required
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html
'''

def print_plusminus(y, x):
    for i in range(y):
        print('+','- ' * x, end ='')

def print_plusminuses(y, x):
    print_plusminus(y, x)
    print('+')

def print_pipe(y, x):
    for i in range(y):
        print('|', '  ' * x, end ='')

def print_pipes(y, x):
    for i in range(x):
        print_pipe(y, x)
        print('|')

def print_grid(y, x):
    for i in range(y):
        print_plusminuses(y, x)
        print_pipes(y, x)
    print_plusminuses(y, x)

print_grid(2, 4)