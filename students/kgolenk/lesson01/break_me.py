# ---------------------------------------------------------------------------- #
# Title: Lesson 01
# Description: Four simple functions with most common exceptions
# ChangeLog (Who,When,What):
# Kate Golenkova, 09/25/2020, Created script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables
a = [1,4,6,7]
b = ("Ann", "Bob", "Apple")
c = int

# Functions ------------------------------------------------------------------ #

# function with NameError exception
def name_error():
    try:
        print(data)
    except NameError as e:
        print("NameError is occured, " + str(e))
name_error()

# function with TypeError
def type_error():
    try:
        c == a + b
        print(c)
    except TypeError as e:
        print("TypeError is occured, " + str(e))

type_error()

# function with SyntaxError
def syntax_error():
    try:
        eval("two in power two")
    except SyntaxError as e:
        print("SyntaxError is occured, " + str(e))

syntax_error()

# function with AttributeError
def attr_error():
    try:
        c == 1
        print(c.lowcase)
    except AttributeError as e:
        print("AttributeError is occured" + str(e))

attr_error()