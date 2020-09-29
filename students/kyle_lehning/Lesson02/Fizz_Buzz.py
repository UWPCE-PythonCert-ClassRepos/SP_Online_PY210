#!/usr/bin/env python3

def Fizz_Buzz():
    """Print the range 1 to 100 with Fizz if divisible by 3, Buzz if divisible by 5, and FizzBuzz if divisible by both"""
    for number in range(1, 101):
        output_string = ""
        if number%3 ==0: output_string = 'Fizz'
        if number%5 ==0: output_string += 'Buzz'
        if output_string == "":
            print(number)
        else:
            print(output_string)
if __name__ == '__main__':
    Fizz_Buzz()