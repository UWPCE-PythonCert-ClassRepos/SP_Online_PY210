"""
fizz_buzz.py
Zachary Meves
Python 210
Lesson 02

Fizz Buzz
"""


def fizzbuzz(n):
    """Prints numbers from 1 - n, inclusive. For multiples
    of 3, prints 'Fizz'. For multiples of 5, prints 'Buzz'.
    For multiples of both, prints 'FizzBuzz'.

    Parameters
    ----------
    n : int
        Number to count up to"""

    for i in range(1, n + 1):
        _print_num = True
        if i % 3 == 0:
            _print_num = False
            print('Fizz', end='')
        if i % 5 == 0:
            _print_num = False
            print('Buzz', end='')
        if _print_num:
            print(i, end='')
        print('')


if __name__ == "__main__":
    """Main program. Count to 100"""
    fizzbuzz(100)