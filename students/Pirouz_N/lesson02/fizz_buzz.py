"""
Purpose: Lessen 2 homework three python certificate from UW
Author: Pirouz Naghavi
Date: 06/26/2020
"""


def fizz_buzz():
    """Prints 1 to 100 inclusive with different values for multiples of 3 and multiples of 5.

    Prints 1 to 100 inclusive, but multiples of three instead of the number Fizz is printed, and for multiples of
    5 Buzz is printed instead. For numbers that are multiples of both 5 and 3 FizzBuzz is printed instead.
    """

    for i in range(1, 101):
        # Multiples of 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        # Multiples of 3
        elif i % 3 == 0:
            print('Fizz')
        # Multiples of 5
        elif i % 5 == 0:
            print('Buzz')
        # All other numbers just the number is printed
        else:
            print(i)


if __name__ == '__main__':
    # Printing a test grid
    fizz_buzz()