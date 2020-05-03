# ---------------------------------------------------------------------------- #
# Title: break_me.py
# Description: Four error sample Python functions, each function
#              when called will have an exception:
#              NameError, TypeError, SyntaxError, AttributeError
# ---------------------------------------------------------------------------- #


# SyntaxError: invalid syntax
# The "+" should be a comma (a, b)
def add_numbers(a + b):
    sum = a + b
    return sum

# NameError
# The variable is incorrect on line 12 should be 'name'
def your_name():
    name = input ("Enter your name: ")
    print ("your name is " + yourname)


# TypeError
# Adding a string ('5') to an integer
def add_numbers():
    sum = '5' + 10


# AttributeError
# can't append an integer
def int_append(10):
    int.append(5)


