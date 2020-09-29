#!/usr/bin/env python3
import sys
##############################################################
#
# 20200603    djm Duane McCollum,
#
#  https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/fizz_buzz.html
#
#  Write a program that prints the numbers from 1 to 100 inclusive.
#  But for multiples of three print “Fizz” instead of the number.
#  For the multiples of five print “Buzz” instead of the number.
#  For numbers which are multiples of both three and five print “FizzBuzz” instead.

##############################################################

def fizzBuzz():
    n= 101
    for i in range (n):
        if i != 0:
            if (i % 3 == 0) and (i % 5 == 0):
                print('FizzBuzz')
            elif (i % 3 == 0) and (i % 5 != 0):
                print('Fizz')
            elif  (i % 3 != 0) and (i % 5 == 0):
                print('Buzz')
            else: print(str(i))
        else:
            None

fizzBuzz()