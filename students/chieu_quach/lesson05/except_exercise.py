# Author      : Chieu Quach
# Assignment  : Lesson 5
# Exercise    : Except_exercise


#!/usr/bin/python

import traceback
import sys

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""


from except_test import fun, more_fun, last_fun



# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

first_fun = ['java', 'c']

# Catch nameerror in function fun
try:
    joke = fun(first_try[0])
except NameError:
    pass

# print spam, spam, spam
try:
    joke = fun(first_try[1])
except KeyError:
    print ("KeyError")
     
    
    # Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)
    
try:
    more_joke = more_fun(first_fun[1])
except NameError:
    pass
else:
    pass

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])
except IndexError:
    pass
else:
    try:
        more_joke = more_fun(langs[2])
    except IndexError:
        pass


try:
    more_joke = more_fun(langs[1])
except TypeError:
    print ("typeError")
except NameError:
    print ("NameError ")
except ValueError:
    print ("ValueError")
else:
    pass


try:
    last_fun()
except NameError:
    print ("NameError")
finally:
    pass


