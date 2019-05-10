#!/usr/bin/env python
'''
py210: Mod2: FizzBuzz
Write a program that prints numbers from 1 to 100, inclusive.
But for multiples of three, print "Fizz" instead of the number.
For for multiples of five, print "Buzz" instead of the number.
But for multiples of three and five, print "FizzBuzz" instead of the number.
'''

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))


