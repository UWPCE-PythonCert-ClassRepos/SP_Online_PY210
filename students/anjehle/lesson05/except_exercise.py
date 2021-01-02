#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']
try:
    joke = fun(first_try[0])
except NameError:
    joke = fun(first_try[1])

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    print(not_joke)
langs = ['java', 'c', 'python']

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
try:
    more_joke = more_fun(langs[1])
except NameError:
    print(NameError)
#
# If there are no exceptions, call the more_fun function with the last
# language in the list
else:
    more_joke = more_fun(langs[:-1])
# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)
finally:
    last_fun()

count_evens = \
[for num in ls if num % 2 == 0]