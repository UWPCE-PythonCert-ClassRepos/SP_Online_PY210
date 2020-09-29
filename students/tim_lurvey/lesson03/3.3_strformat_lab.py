#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

import sys


def task_1(seq: tuple=()):
    """Task One

    Write a format string that will take the following four element tuple:

        ( 2, 123.4567, 10000, 12345.67)

        and produce:

        'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    f_val = "file_{file:03} : {dec:>8.2f}, {count:1.2e}, {time:1.2e}".format(
        file    =seq[0],
        dec     =seq[1],
        count   =seq[2],
        time    =seq[3])
    #
    print(f_val)
    return f_val


def task_2(seq: tuple = ()):
    """Task Two

    Using your results from Task One, repeat the exercise, but this time
    using an alternate type of format string (hint: think about alternative
    ways to use .format() (keywords anyone?), and also consider f-strings
    if you’ve not used them already).

    Task One

    Write a format string that will take the following four element tuple:

        ( 2, 123.4567, 10000, 12345.67)

        and produce:

        'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    file, dec, count, time = seq
    #
    f_val = f'file_{file:03} : {dec:>8.2f}, {count:1.2e}, {time:1.2e}'
    #
    print(f_val)
    return f_val


def task_3(seq: tuple = ()):
    """Dynamically Building up format strings
    rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take
    multiple values
    """
    n = len(seq)
    base_string = "the {n} numbers are: ".format(n=n)
    dynamic_string = "{:d}, " * n
    #
    full_string = base_string + dynamic_string[:-2].format(*seq)
    #
    print(full_string)
    return full_string


def task_4(seq: tuple = ()):
    """
    Given a 5 element tuple:
    ( 4, 30, 2017, 2, 27)

    use string formating to print:
    '02 27 2017 04 30'"""
    try:
        assert len(seq) == 5
    except AssertionError:
        raise ValueError("Lenght of 'seq' must be 5")
    stringx = "{0:02} {1:02} {2:02} {3:02} {4:02}".format(seq[-2], seq[-1], seq[2], seq[0], seq[1])
    print(stringx)
    return stringx


def task_5(seq: list = []):
    """
    Given the following four element list:
    ['oranges', 1.3, 'lemons', 1.1]

    Write an f-string that will display:
    "The weight of an orange is 1.3 and the weight of a lemon is 1.1"

    Now see if you can change the f-string so that it displays the
    names of the fruit in upper case, and the weight 20% higher
    (that is 1.2 times higher)."""
    #
    fruit1, weight1, fruit2, weight2 = seq
    #
    master_string = f"The weight of an {fruit1[:-1]} is {weight1} and " \
                    f"the weight of a {fruit2[:-1]} is {weight2}"
    #
    mod_string = f"The weight of an {fruit1[:-1].upper()} is {weight1 * 1.2} and " \
                 f"the weight of a {fruit2[:-1].upper()} is {weight2 * 1.2}"
    #
    print(master_string)
    print(mod_string)
    return master_string


def task_6(data: dict = {}):
    """Write some Python code to print a table of several rows, each
    with a name, an age and a cost. Make sure some of the costs are
    in the hundreds and thousands to test your alignment specifiers."""
    #
    master_string = "\n"
    #
    for key, value in data.items():
        name, age, price = value
        fprice = "$ " + "{:>8.2f}".format(price).strip()
        master_string += "{0:>3}: {1:>20} {2:>7.2f} yrs @ {3:>10}\n".format(key, name, age, fprice)
    #
    return master_string[:-1]


def task_6a(seq: tuple = ()):
    """And for an extra task, given a tuple with 10 consecutive numbers, can
    you work how to quickly print the tuple in columns that are 5 characters
    wide? It can be done on one short line!"""
    try:
        assert len(seq) == 10
    except AssertionError:
        raise ValueError("Lenght of 'seq' must be 10!")
    return ((("{:>5}" * 5) + "\n") * 2)[:-1].format(*seq)


def main(args):
    #
    assert task_1(seq=(2, 123.4567, 10000, 12345.67)) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    #
    assert task_2(seq=(2, 123.4567, 10000, 12345.67)) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    #
    assert task_3(seq=(1, 2, 3, 4, 5, 6)) == "the 6 numbers are: 1, 2, 3, 4, 5, 6"
    #
    assert task_4(seq=(4, 30, 2017, 2, 27)) == "02 27 2017 04 30"
    #
    assert task_5(seq=['oranges', 1.3, 'lemons', 1.1]) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    #
    d = {1: ("Cheddar",            1,    2.99),
         2: ("Cheddar",            10,   15.99),
         3: ("Cheddar",            100,  1009.99),
         4: ("Boerenkase",         0.05, 9.99),
         5: ("Brick",              0.75, 5.99),
         6: ("Gruyere",            1.5,  5.99),
         7: ("Pecorino Reggiano",  3,    92.99),
         }
    print(task_6(data=d))
    #
    print(task_6a(seq=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
    return True


if __name__ == '__main__':
    assert main(sys.argv[1:])
