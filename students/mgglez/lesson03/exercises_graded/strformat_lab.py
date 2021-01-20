#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson 3
# Description: Exercise 3.3 - String Formatting Lab (Graded Exercise)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-10-2021, Created String Formatting Lab Functions
# ------------------------------------------------------------------------------ #

def task_one():
    """
    Implement all the instructions from String Formatting Lab Task 1
    """
    # Formatting with format() and positional arguments
    s = "file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67)
    print(s)

def task_two():
    """
    Implement all the instructions from String Formatting Lab Task 2
    """
    # Formatting with format() and keywords arguments
    s = "file_{fnum:0>3d}: {float1:.2f}, {big_int:.2e}, {big_float:.2e}".format(fnum=2, float1=123.4567, big_int=10000, big_float=12345.67)
    print(s)
    # Formatting using fstrings
    number1 = 2
    number2 = 123.4567
    number3 = 10000
    number4 = 12345.67
    s = f"file_{number1:0>3d}: {number2:.2f}, {number3:.2e}, {number4:.2e}"
    print(s)

def task_three_formatter(t):
    """
    Implement all the instructions from String Formatting Lab Task 3
    :param t: (tuple) Original tuple with random number of items
    """
    length = len(t)
    s = ("the {} numbers are: " + ", ".join(['{:d}'] * length)).format(length, *t)
    print(s)
    return s

def task_four(t):
    """
    Implement all the instructions from String Formatting Lab Task 4
    """
    # Receive a 5 element tuple, switch last 2 elements with first two elements
    # and format it
    t2 = t[-2:] + t[(len(t)//2): (len(t)//2 + 1)] + t[:2]
    s = " ".join(['{:02d}']*len(t2))
    print(s.format(*t2))

def task_five():
    """
    Implement all the instructions from String Formatting Lab Task 5
    """
    l = ['oranges', 1.3, 'lemons', 1.1]
    s1 = f"The weight of an {l[0]} is {l[1]} and the weight of a {l[2]} is {l[3]}"
    print(s1)
    s2 = f"The weight of an {l[0].upper()} is {l[1]} and the weight of a {l[2]} is {l[3]*1.2}"
    print(s2)

def task_six():
    """
    Implement all the instructions from String Formatting Lab Task 6
    """
    # Write some Python code to print a table of several rows, each with a name, an age and a cost.
    # Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
    table = [
        ('John Silver', 27, 123453.2345),
        ('Mary Stark', 35, 54375.2323),
        ('Andrew Black', 87, 1234000.234),
        ('Joshua Smith', 102, 154000.233)
    ]
    print("{:20s}|{:>10s}|{:>21s}".format('Name', 'Age', 'Cost'))
    for person in table:
        print("{:<20s} {:>10d} ${:>20.2f}".format(person[0], person[1], person[2]))

    # And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly
    # print the tuple in columns that are 5 charaters wide? It can be done on one short line!
    tuple_10_consecutive_nums = tuple(range(10))
    print((' '.join(['{:5d}']*10)).format(*tuple_10_consecutive_nums))

if __name__ == '__main__':

    task_one()
    task_two()
    t = (2,3,5,7,9)
    task_three_formatter(t)
    t = (4, 30, 2017, 2, 27)
    task_four(t)