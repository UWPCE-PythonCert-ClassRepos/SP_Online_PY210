"""
fizzBuzz.py
by David Baylor
uses python 3

loops through numbers 1 to 100 and for multipuls of 3 it prints fizz, for multipuls of 5 it prints buzz and for multipuls of 3 and
5 it prints FizzBuzz.
"""

def detFactor(n):
    """determin if the number is a factor of 3, 5 or both"""
    if n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return n

for i in range (1,101):
    print(detFactor(i))

