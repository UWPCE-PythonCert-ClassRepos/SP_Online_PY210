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
    # spam triggers Nameerror since s is not defined
    joke = fun(first_try[0])
except NameError:
    # calling fun again with cheese yields expected results
    joke = fun(first_try[1])

# Here is a try/except block. Add an else that prints not_joke
try:
    # fun runs and assisngs value to not_joke
    not_joke = fun(first_try[2])
except SyntaxError:
    print('Run Away!')
else:
    # printing the returned value after 
    # running fun with third element in first_try
    print(not_joke)
# 
langs = ['java', 'c', 'python']

try:
    # java triggers the IndexError
    # since test is only 3 elements long
    more_joke = more_fun(langs[0])
except IndexError:
    # after indexerror more_fun runs with c
    more_joke = more_fun(langs[1])
else:
   print("index error") 
finally:
    # then finally running the last function
    last_fun()
