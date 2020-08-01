#!/usr/bin/env python3

#delete the triple quote before the error you wish to cause

'''#NameError
print(3*x)	#I never actually define what 'x' is.
#'''


'''#TypeError
a = "5"
b = 5
print(a+b)	#"a" is a string, "b" is an integer.  Those types can't be added together
#'''


'''#SyntaxError
print(this is my syntax error")	#I "forgot" the quote at the beginning of the print argument string
#'''

#AttributeError
x = 5
print(x.type)	#I never gave variable 'x' an attribute called "type"
#'''
