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
# 
langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[0])
except IndexError:
    more_joke = more_fun(langs[1])
else:
   print("index error") 
finally:
    last_fun()
