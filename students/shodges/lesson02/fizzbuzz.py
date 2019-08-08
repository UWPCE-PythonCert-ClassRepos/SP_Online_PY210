#!/usr/bin/env python3

for i in range(1,101):
    printi = True
    if i % 3 == 0:
        printi = False
        print('Fizz', end='')
    if i % 5 == 0:
        printi = False
        print('Buzz', end='')

    if printi == True: print(i)
    else: print('')
