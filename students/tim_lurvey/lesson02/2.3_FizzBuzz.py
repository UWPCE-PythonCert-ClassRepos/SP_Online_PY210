#!/usr/bin/env python
__author__ = 'Tim Lurvey'


def fizzbuzz(i, debug=False):
    """fizzbuzz(n) -> 1 2 Fizz 4 Buzz Fizz 7 8 ... 14 FizzBuzz 16 ...
    :param i:       integer to test
    :param debug:   boolean to enable debug printing
    :return:        'Fizz' if i is divisible by 3
    :return:        'Buzz' if i is divisible by 5
    :return:        'FizzBuzz' if both"""
    fizz = ''
    buzz = ''
    db = ''
    if debug:
        db += '{0:<4}'.format(i)
    if not i % 3:
        fizz = 'Fizz'
    if not i % 5:
        buzz = 'Buzz'
    if fizz or buzz:
        return (db + fizz + buzz)
    else:
        return (i)


def main():
    for x in range(1, 101):
        print(fizzbuzz(x))
        # print(fizzbuzz(x,True))


if __name__ == '__main__':
    main()
