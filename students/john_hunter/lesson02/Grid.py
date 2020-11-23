# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:33:29 2020
Grid
@author: johnh
"""

block = int(input('Enter size of each block, an integer: '))
maxSize = int(input('enter the max size of the array, an integer: '))

def printGrid(block,maxSize):
    
    plusDash = "+----+----+"
    upRights = "|    |    |"
    
    for printer in range(maxSize):
        if printer % block == 0 or (printer+1) == maxSize:
            print (plusDash)
        else :
            print (upRights)

printGrid(block,maxSize)

def fizzBuzz():
    for x in range(101):
        if x==0:
            continue
        if x%15==0:
            print('FizzBuzz')
        elif x%3==0:
            print ('Fizz')
        elif x%5==0:
            print('Buzz')
        else:
            print(x)

fizzBuzz()
            