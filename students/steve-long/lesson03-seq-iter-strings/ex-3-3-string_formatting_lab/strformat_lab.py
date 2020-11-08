#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson03
# String Formatting (strformat_lab.py)
# Steve Long 2020-09-28 | v0
#
# Requirements:
# =============
#
# [2-1] Task One:
# ---------------
#
#   Write a format string that will take the following four element tuple:
#
#       (2, 123.4567, 10000, 12345.67)
#
#   and produce:
#
#       'file_002 : 123.46, 1.00e+04, 1.23e+04'
#
#   Let's look at each of the four tuple elements in turn:
#
#   1.  The first element is used to generate a filename that can help with
#       file sorting. The idea behind the "file_002" is that if you have a
#       bunch of files that you want to name with numbers that can be sorted,
#       you need to "pad" the numbers with zeros to get the right sort order.
#       You need to find a string formatting operator that will "pad" the
#       number with zeros for you.
#
#   2.  The second element is a floating point number. You should display it
#       with 2 decimal places shown.
#
#   3.  The third value is an integer, but could be any number. You should
#       display it in scientific notation, with 2 decimal places shown.
#
#   4.  The fourth value is a float with a lot of digits – display it in
#       scientific notation with 3 significant figures.
#
# [2-2] Task Two:
# ---------------
#
#   Using your results from Task One, repeat the exercise, but this time using
#   an alternate type of format string (hint: think about alternative ways to
#   use .format() (keywords anyone?), and also consider f-strings if you’ve not
#   used them already).
#
# [2-3] Task Three:
# -----------------
#
#   Dynamically Building up format strings
#
#   Rewrite:
#
#       "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#
#   ...to take an arbitrary number of values. Hint: You can pass in a tuple of
#   values to a function with a* thus...
#
#       In [52]: t = (1,2,3)
#       In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t) Out[53]: 'the
#       3 numbers are: 1, 2, 3'
#
#   The idea here is that you may have a tuple of three numbers, but might also
#   have 4 or 5 or 2 or any number ... so you can dynamically build up the
#   format string to accommodate the length of the tuple. The string object has
#   the format() method, so you can call it with a string that is bound to a
#   name, not just a string literal. For example:
#
#       In [16]: form_string = "{:d}, {:d}" In [17]: nums = (34, 56)
#       In [18]: fstring.format(*nums) Out[18]: '34, 56'
#
#   Put your code in a function that will return the final string like so:
#
#       In [20]: formatter((2,3,5))
#       Out[20]: 'the 3 numbers are: 2, 3, 5'
#       In [21]: formatter((2,3,5,7,9))
#       Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'
#
#   It will look like:
#
#       def formatter(in_tuple): do_something_here_to_make_a_format_string
#           return form_string.format(*in_tuple)
#
# [2-4] Task Four:
# ----------------
#
#   Given a 5 element tuple...
#
#       (4, 30, 2017, 2, 27)
#
#   ...use string formatting to print...
#
#       '02 27 2017 04 30'
#
#   Hint: use index numbers to specify positions.
#
# [2-5] Task Five:
# ----------------
#
#   f-strings are new to Python (version 3.6), but are very powerful and
#   efficient. This means they are worth understanding and using. And this is
#   made easier than it might be because they use the same, familiar format!ng
#   language that is conven"onally used in Python (in .format()).
#
#   So in this exercise we are going to specifically use f-strings. Here’s the
#   simplest example, to show how you can use available variables in an
#   f-string:
#
#       In [2]: name = 'Andy'
#       In [3]: f'Your name is {name}'
#       Out[3]: 'Your name is Andy'
#
#   In addition to referencing variables in the local scope, f-strings can
#   evaluate simple expressions in line like so:
#
#       In [5]: f"Your name is {name.upper()}" Out[5]: 'Your name is ANDY'
#       In [6]: name = "andy"
#       In [7]: f"Your name is {name.upper()}" Out[7]: 'Your name is ANDY'
#
#   or
#
#       In [8]: a = 5 In [9]: b = 10
#       In [10]: f"The sum is: {a+b}"
#       Out[10]: 'The sum is: 15'
#
#   Here’s a [the] task for you: Given the following four element list...
#
#       ['oranges', 1.3, 'lemons', 1.1]
#
#   Write an f-string that will display...
#
#       The weight of an orange is 1.3 and the weight of a lemon is 1.1
#
#   Now see if you can change the f-string so that it displays the names of the
#   fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
#
# [2-6] Task Six:
# ---------------
#
#   Often it’s convenient to display data in columns. String formatting helps
#   to make this straightforward.
#
#   Suppose you’d like to display something like...
#
#       "First $99.01 Second $88.09"
#
#   One way to do that is...
#
#       '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')
#
#   In this simple example everything aligns nicely. But that will not be the
#   case when the numbers to the left of the decimal place vary. Then you will
#   need to use alignment specifiers. Do some research on this using the links
#   below. Then...
#
#       [A] Write some Python code to print a table of several rows, each with
#           a name, an age and a cost. Make sure some of the costs are in the
#           hundreds and thousands to test your alignment specifiers.
#
#       [B] And for an extra task, given a tuple with 10 consecutive numbers,
#           can you work how to quickly print the tuple in columns that are 5
#           chara[c]ters wide? It can be done on one short line!
#
# Implementation:
# ===============
#
#   [2-1]   multiformatting1
# 	[2-2]   multiformatting2
#   [2-3]   formatter
#   [2-4]   print_five_element_tuple
#   [2-5A]  fruit_weight_message1
#   [2-5B]  fruit_weight_message2
#   [2-6A]  print_yoyodyne_employee_report
#   [2-6B]  print_number_tuple_five_chars_wide
#
#   Checked with flake8.
#
# Verification:
# =============
#
#   [2-1]   assertion
# 	[2-2]   assertion
#   [2-3]   assertion
#   [2-4]   assertion
#   [2-5A]  assertion
#   [2-5B]  assertion
#   [2-6A]  print to stdio
#   [2-6B]  print to stdio
#
# Script:
# =======
#
#   ./strformat_lab.py
#
#   Runs assertions 2-1 thru 2-5B, prints result for 2-6A and 2-6B.
#
# Issues:
# =======
#
# History:
# ========
# 000/2020-09-28/sal/Created.
# =============================================================================

import random

# [2-1] Task One: multiformatting1
# -----------------------------------------------------------------------------
# Assumption: Element 0 shall be an integer n satisfying 0 <= n < 1000.
# Assumption: Not intended as a general solution for a tuple of the form
#             (in float, int, float).
# Assumption: Rounding issues associated with floating point and scientific
#             notation formatting (if they exist) can be ignored.


def multiformatting1():
    """
    multiformatting1()
    -----------------
    Transform the tuple (2, 123.4567, 10000, 12345.67) into a
    comma-and-space string mapping of the values of the form
    'file_002 : 123.46, 1.00e+04, 1.23e+04'.

    Entry: N/A
    Exit:  Return specified string value.
    """
    n = (2, 123.4567, 10000, 12345.67)
    s = "file_{:03d} : {:.2f}, {:.2e}, {:3.2e}".format(n[0], n[1], n[2], n[3])
    return s


assert(multiformatting1() == "file_002 : 123.46, 1.00e+04, 1.23e+04")

print("\nTask One: Pass\n")

# [2-2] Task Two: multiformatting2
# -----------------------------------------------------------------------------
# Assumptions: Same as [2-1].


def multiformatting2():
    """
    multiformatting2()
    ------------------
    Transform the tuple (2, 123.4567, 10000, 12345.67) into a
    comma-and-space string mapping of the values of the form
    'file_002 : 123.46, 1.00e+04, 1.23e+04'. Implemented using f-string
    formatting.

    Entry: N/A
    Exit:  Return specified string value.
    """
    n = (2, 123.4567, 10000, 12345.67)
    s = f"file_{n[0]:03d} : {n[1]:.2f}, {n[2]:.2e}, {n[3]:3.2e}"
    return s


assert(multiformatting2() == "file_002 : 123.46, 1.00e+04, 1.23e+04")

print("\nTask Two: Pass\n")

# [2-3] Task Three: formatter
# -----------------------------------------------------------------------------
# Assumptions: Need to account for zero arguments.
# Assumptions: Correct English is important


def formatter(*in_tuple):
    int_count = len(in_tuple)
    out = "There are 0 numbers"
    if (int_count > 0):
        pv = (" is" if (int_count == 1) else "s are")
        out = f"The {int_count} number{pv}: {in_tuple[0]:d}"
        for n in in_tuple[1:]:
            out = out + f", {n:d}"
    return out


assert(formatter() == "There are 0 numbers")
assert(formatter(0) == "The 1 number is: 0")
assert(formatter(0, 1) == "The 2 numbers are: 0, 1")
assert(formatter(0, 1, 2) == "The 3 numbers are: 0, 1, 2")

print("\nTask Three: Pass\n")

# [2-4] Task Four: print_five_element_tuple
# -----------------------------------------------------------------------------
# Assumption: The solution should be accomplished strictly with formatting.
# Assumption: A string function should be used to satisfy an assert test.
# Assumption: A print function should call the string function to satisfy the
#             print requirement.


def five_ints_to_csv(t):
    """
    five_ints_to_csv(<t>)
    ---------------------
    Convert a five-element tuple consisting entirely of integers into a
    comma-and-space delimited string, each at least 2-chars wide, with
    the tuple elements (by index) in this order: 3, 4, 2, 0, 1. This is
    accomplished strictly with string formatting.

    Entry: <t> ::= A five-integer tuple.
    Exit:  A string
    """
    return f"{t[3]:02d}, {t[4]:02d}, {t[2]:02d}, {t[0]:02d}, {t[1]:02d}"


def print_five_element_tuple(t):
    """
    print_five_element_tuple
    ------------------------
    Print the result of calling function five_ints_to_csv.

    Entry: <t> ::= A five-integer tuple.
    Exit:  The result of five_ints_to_csv(<t>) to standard output.
    """
    print(five_ints_to_csv(t))


assert(five_ints_to_csv((4, 30, 2017, 2, 27)) == "02, 27, 2017, 04, 30")

print("\nTask Four: Pass\n")

# [2-5A] Task Five, Part A: fruit_weight_message1
# -----------------------------------------------------------------------------


def fruit_weight_message1(four_fw):
    """
    fruit_weight_message1(<four_fw>)
    --------------------------------
    Print a four-element list of the form

    [<plural-fruit-name-1>, <weight-1>, <plural-fruit-name-2>,
     <weight-2>]

    as a string of the form

    'The weight of <plural-fruit-name-1> is <weight-1> and the weight
     of <plural-fruit-name-2> is <weight-2>'

    Entry: A list of the form [str, int, str, int]
    Exit:  Returns a string as described above.
    """
    s = f"The weight of {four_fw[0]} is {four_fw[1]:.1f} and" \
        + f" the weight of {four_fw[2]} is {four_fw[3]:.1f}"
    return s


def verify_fruit_weight_message1():
    """
    Collect temporary variables for assertion check and run assertion.
    """
    value_in = ['oranges', 1.3, 'lemons', 1.1]
    actual = fruit_weight_message1(value_in)
    expected = "The weight of oranges is 1.3 and the weight of lemons is 1.1"
    assert(actual == expected)
    return True


verify_fruit_weight_message1()

print("\nTask Five-A: Pass\n")

# [2-5B] Task Five, Part B: fruit_weight_message2
# -----------------------------------------------------------------------------


def fruit_weight_message2(four_fw):
    """
    fruit_weight_message2(<four_fw>)
    --------------------------------
    Print a four-element list of the form

    [<plural-fruit-name-1>, <weight-1>, <plural-fruit-name-2>,
     <weight-2>]

    as a string of the form

    'The weight of <PLURAL-FRUIT-NAME-1> is <+20%-weight-1> and the
     weight of <PLURAL-FRUIT-NAME-2> is <+20%-weight-2>'

    where PLURAL-FRUIT-NAME is capitalized plural-fruit-name and
    +20%-weight is weight increased by 20%.

    Entry: A list of the form [str, int, str, int]
    Exit:  Returns a string as described above.
    """
    s = (f"The weight of {four_fw[0].upper()} is {1.2*four_fw[1]:.1f} and "
         + f"the weight of {four_fw[2].upper()} is {1.2*four_fw[3]:.1f}")
    return s


def verify_fruit_weight_message2():
    """
    Collect temporary variables for assertion check and run assertion.
    """
    value_in = ['oranges', 1.3, 'lemons', 1.1]
    actual = fruit_weight_message2(value_in)
    expected = "The weight of ORANGES is 1.6 and the weight of LEMONS is 1.3"
    assert(actual == expected)
    return True


verify_fruit_weight_message2()

print("\nTask Five-B: Pass\n")

# [2-6A] Task Six: print_yoyodyne_employee_report
# -----------------------------------------------------------------------------

# Part One (Write some Python code to print a table of several rows...)
# ---------------------------------------------------------------------
# Assumption: The form of the source data for name, age, and cost is at the
#             discretion of the developer.
# Assumption: A degree of creativity is allowed.
# Assumption: Age should be a positive value greater than 0 from single to
#             triple digits, cost should be a positive value with 2 decimal
#             places.

# _employee_names
# ---------------
# These are the names of employees from Yoyodyne Propulsion Systems (aliens
# with a limited imagination for creating names from "The Adventures of
# Buckaroo Banzai Across the 8th Dimension", a really silly movie from back in
# 1984). I just wanted a long list of names.

_employee_names = (
    ("John Barnett"),
    ("John Bigboote"),
    ("John Camp"),
    ("John Careful Walker"),
    ("John Chief Crier"),
    ("John Cooper"),
    ("John Coyote"),
    ("John Edwards"),
    ("John Emdall"),
    ("John Fish"),
    ("John Fledgling"),
    ("John Gant"),
    ("John Gomez"),
    ("John Grim"),
    ("John Guardian"),
    ("John Icicle Boy"),
    ("John Jones"),
    ("John Joseph"),
    ("John Kim Chi"),
    ("John Lee"),
    ("John Littlejohn"),
    ("John Many Jars"),
    ("John Milton"),
    ("John Mud Head"),
    ("John Nephew"),
    ("John Nolan"),
    ("John O'Connor"),
    ("John Omar"),
    ("John Parker"),
    ("John Parrot"),
    ("John Rajeesh"),
    ("John Ready to Fly"),
    ("John Repeat Dance"),
    ("John Roberts"),
    ("John Scott"),
    ("John Smallberries"),
    ("John Starbird"),
    ("John Take Cover"),
    ("John Thorny Stick"),
    ("John Two Horns"),
    ("John Valuk"),
    ("John Whorfin"),
    ("John Wood"),
    ("John Wright"),
    ("John Ya Ya"))

# Constants used for generating random age and cost values for
# this exercise.

_EMPLOYEE_MIN_AGE_YEARS = 5
_EMPLOYEE_MAX_AGE_YEARS = 100
_EMPLOYEE_MIN_COST_DOLLARS = 0
_EMPLOYEE_MAX_COST_DOLLARS = 100000


def random_age():
    """
    random_age()
    ------------
    Generate a random age in years with the range

    _EMPLOYEE_MIN_AGE <= age <= _EMPLOYEE_MAX_AGE

    Entry: -
    Exit:  Returns an int value.
    """
    return random.randint(_EMPLOYEE_MIN_AGE_YEARS, _EMPLOYEE_MAX_AGE_YEARS)


def random_cost():
    """
    random_cost()
    -------------
    Generate a random cost (d.dd) value within the range

    _EMPLOYEE_MIN_COST <= cost <= _EMPLOYEE_MAX_COST

    Entry: -
    Exit:  Returns a 2-place decimal value.
    """
    cost = random.randint(_EMPLOYEE_MIN_COST_DOLLARS,
                          _EMPLOYEE_MAX_COST_DOLLARS)\
        + random.randint(0, 100)/100.00
    return cost


def collate_yoyodyne_employee_data(names):
    """
    collate_yoyodyne_employee_data(<names>)
    ----------------------------------------
    Collate name, age, and cost information for the
    employees of Yoyodyne Production Systems. Age and
    cost are randomly generated integer and floating
    point values.

    Entry: <names> ::= A sequence of employee names.
    Exit:  Returns a tuple of the form

           (<int:name_column_width>, <int:age_column_width>,
            <int:cost_column_width>, (<employee_data>,...))

           where <employee_data> is of the form

           (<string:name>, <int:age>, <float:cost>)

           and column_width values are the maximum char
           widths for each data element in all instances
           of <employee_data>.
    """
    name_age_cost_list = []
    name_width = 0
    age = 0
    max_age = 100
    cost = 0
    max_cost = 10000
    for name in names:
        #
        # Aggregate name, age, and cost and track
        # the maximum age, cost, and name string width.
        #
        age = random_age()
        cost = random_cost()
        name_age_cost_list.append(tuple([name, age, cost]))
        name_width = max(len(name), name_width)
        max_age = max(age, max_age)
        max_cost = max(cost, max_cost)
    #
    # Calculated age and cost string width (done outside the
    # iteration loop to avoid recurring calls to len() function.)
    #
    age_width = len("{}".format(max_age))
    cost_width = len("{}".format(max_cost))
    return (name_width, age_width, cost_width, tuple(name_age_cost_list))


def print_yoyodyne_employee_report():
    """
    print_yoyodyne_employee_report()
    --------------------------------
    Print YoyoDyne Propulsion Systems employee report.

    Entry: _employee_names is a tuple of employee names.
    Exit:  Report printed to standard output.
    """
    #
    # Retrieve employee data. See function collate_yoyodyne_employee_data
    # for a description.
    #
    employee_data = collate_yoyodyne_employee_data(_employee_names)
    #
    # Print title
    #
    print("\nYoyodyne Propulsion Systems Employee Report:\n")
    #
    # Print column headers.
    #
    heading = ("Name", "Age", "$Cost")
    name_width = max(employee_data[0], len(heading[0]))
    age_width = max(employee_data[1], len(heading[1]))
    cost_width = max(employee_data[2], len(heading[2]))
    name_fmt = "{" + "{0}: <{1}s".format(0, name_width) + "}"
    age_fmt = "{" + "{0}: <{1}s".format(1, age_width) + "}"
    cost_fmt = "{" + "{0}: <{1}s".format(2, cost_width) + "}"
    fmt = "{}  {}  {}".format(name_fmt, age_fmt, cost_fmt)
    print(fmt.format(heading[0], heading[1], heading[2]))
    fmt = "{}  {}  {}".format((name_width * "-"),
                              (age_width * "-"),
                              (cost_width * "-"))
    print(fmt)
    #
    # Print name, age, and cost for each employee.
    #
    age_fmt = "{" + "{0}: >{1}d".format(1, age_width) + "}"
    cost_fmt = "{" + "{0}: >{1}.2f".format(2, cost_width) + "}"
    fmt = "{}  {}  {}".format(name_fmt, age_fmt, cost_fmt)
    for name_age_cost in employee_data[3]:
        print(fmt.format(name_age_cost[0], name_age_cost[1], name_age_cost[2]))
    print("\nEOF\n")


print_yoyodyne_employee_report()

print("\nTask Six-A: Pass\n")

# [2-6B] Task Six, Part B: print_number_tuple_five_chars_wide
# "10 consecutive numbers..."
# ----------------------------------------------------------------------------
# Assumption: All numbers are type int.
# Assumption: Since the column is 5 chars wide, every value must be greater
#             than -10000 and less than 100000.
# Assumption: The term consecutive is irrelevant other than the numbers will
#             be printed in the order they occur in the input tuple.
# Assumption: Only output is printing result on a single line to stdio.


def print_number_tuple_five_chars_wide(num_tuple):
    """
    print_number_tuple_five_chars_wide(<num_tuple>)
    -----------------------------------------------
    Print a tuple of numbers, each 5 chars wide, right-justified with
    spaces.

    Entry: <num_tuple> ::= Tuple of int values noninclusively between
                           -10000 and 10000.
    Exit:  Each value of <num_tuple> printed 5 chars wide on a single
           line.
    """
    print((len(num_tuple) * ("{:5d}  ")).format(*num_tuple)[:-2])


# Print tuple of 10 numbers.
print("\nPrinting 10 integers, each 5 characters wide, right-justified:\n")
print_number_tuple_five_chars_wide((11, 5, 4, 2063, 3978, 0, -601,
                                    187, 31, 13))

# Print empty tuple (* prefix  is like the @ in a Lisp macro, so test how well
# it works).
print("\nPrinting 0 integers, each 5 characters wide, right-justified:\n")
print_number_tuple_five_chars_wide(())

print("\nTask Six-B: Pass\n")
