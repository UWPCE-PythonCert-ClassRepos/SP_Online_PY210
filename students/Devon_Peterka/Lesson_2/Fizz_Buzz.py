#!/usr/bin/env python3

'''Fizz Buzz class exercise.  Count from 1 to 100, replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of 3 AND 5 with "FizzBuzz" '''

for i in range (1, 100 + 1):                     #count through loop from 1 to 100
    print_value=''                               #initialize print_value string as empty
    print_value += "Fizz" if i%3 == 0 else ''    #if i is a multiple of 3, add "Fizz" to the empty print_value string, otherwise add nothing yet
    print_value += "Buzz" if i%5 == 0 else ''    #if i is a multiple of 5, add "Buzz" to whatever is in the print_value string
    if i%5 != 0 and i%3 !=0:                     #if neither condition is met, set print_value to the number i
        print_value = i
    print(print_value)                           #print whatever prin_value is
