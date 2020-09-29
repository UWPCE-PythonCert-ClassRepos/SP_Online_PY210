#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 3

String Formatting Exercise

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html

Task 1:
    Write a format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67)
    and produce:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
Task 2:
    Using your results from Task One, repeat the exercise, but this time using
    an alternate type of format string (hint: think about alternative ways to
    use .format() (keywords anyone?), and also consider f-strings if you’ve not 
    used them already).

Task 3:
    Rewrite:
    "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3
    to take an arbitrary number of values.

Task 4:
    Given a 5 element tuple:
    ( 4, 30, 2017, 2, 27)
    use string formating to print:
    '02 27 2017 04 30'

Task 5:
    Here’s a task for you: Given the following four element list:
    ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).

Task 6:
    Write some Python code to print a table of several rows, each with a name,
     an age and a cost. Make sure some of the costs are in the hundreds and 
     thousands to test your alignment specifiers.

    And for an extra task, given a tuple with 10 consecutive numbers, can you
     work how to quickly print the tuple in columns that are 5 charaters wide?
     It can be done on one short line! 

"""

def print_tuple(values):
    """ Join tuples into string with 5 character per column """
    print( "".join(["{:>5}"]*len(values)).format(*values) )

def print_table(values):
    """ Prints table of Name, Age and Cost """
    print( "".join(["{:>10}"]*3).format("NAME", "AGE", "COST") )

    for value in values:
        print( "".join(["{:>10}"]*len(value)).format(*value) )

def formatter(values):
    """ Creates a f-string of varying length based on number of tuples """
    sstr = ",".join([" {:d}"]*len(values))
    return f"the {len(values)} numbers are:{sstr}".format(*values)



def task1():
    print("\nTask 1:")
    a_tuple = ( 2, 123.4567, 10000, 12345.67)
    fstr = "file_{:03d} : {:.2f}, {:.2e}, {:.3e}".format(a_tuple[0],a_tuple[1],a_tuple[2],a_tuple[3])
    print(fstr)

def task2():
    print("\nTask 2:")
    a_tuple = ( 2, 123.4567, 10000, 12345.67)
    fstr = f"file_{a_tuple[0]:03d} : {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.3e}"
    print(fstr)

def task3():
    print("\nTask 3:")
    print(formatter((2,3,5)))
    print(formatter((2,3,5,7,9)))
    

def task4():
    print("\nTask 4:")
    date = ( 4, 30, 2017, 2, 27)
    print(f"'{date[3]:02d} {date[4]:02d} {date[2]:04d} {date[0]:02d} {date[1]:02d}'")

def task5():
    print("\nTask 5:")
    t_list = ['oranges', 1.3, 'lemons', 1.1]
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    fstr = f"The weight of an {t_list[0][:-1]} is {t_list[1]} and the weight of a {t_list[2][:-1]} is {t_list[3]}"
    print(fstr)
    fstr = f"The weight of an {t_list[0][:-1].upper()} is {t_list[1]*1.2} and the weight of a {t_list[2][:-1].upper()} is {t_list[3]*1.2}"
    print(fstr)

def task6():
    print("\nTask 6:")
    values = (("Matt", 39, "$1332.54"), ("Moe", 23, "$12.73"),("Beth", 37, "412.44"),("Lindsay", 41, "$12121.77"))
    print_table(values)

    print("\nVarying Length tuple 5 char wide: ")
    print_tuple((1, 2.2, 3, 4, 5, 6, 7, 8, 9, 10))



def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

if __name__ == "__main__":
    main()