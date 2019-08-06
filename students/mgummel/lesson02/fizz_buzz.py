#!/usr/bin/env python3

def fizz_buzz():
    """
    Print numbers in range from 1 to 100. Will print 'Fizz' if the number
    is a multiple of 3 and 'Buzz' if the number is a multiple of 5. Print 
    'FizzBuzz' in the event the number is a mutliple of both 3 and 5.
    """
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else: 
            print(number)


if __name__=='__main__':
    fizz_buzz()