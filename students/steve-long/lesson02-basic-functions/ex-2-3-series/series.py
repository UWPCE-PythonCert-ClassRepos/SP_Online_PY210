#!/usr/bin/env python3
# ========================================================================================
# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson02
# Fibonacci Series Exercise (series.py)
# Steve Long 2020-09-20 | v1
#
# Requirements
# ------------
#
# Part 1:
#
# 	1.1-Create a module series.py in the lesson02 folder.
# 	1.2-Add a function called 'fibonacci' that implements the Fibonacci series ( 0, 1, 1,   
#     	2, 3, 5, 8, 13, ...).
# 	1.3-The function should have one parameter, n .
# 	1.4-The function should return the nth value in the Fibonacci series starting with a  
#     	zero index.
# 	1.5-Ensure that your function has a well-formed docstring.
#
# Part 2:
#
# 	2.1-Add a new function 'lucas' that returns the nth value in the lucas series (2, 1,  
#     	3, 4, 7, 11, 18, 29, ...) starting with a zero index.
# 	2.2-Ensure that your function has a well-formed docstring.
#
# Part 3:
#
# 	3.1-Add a third function called 'sum_series' that can compute both of these related 
#     	series. 
# 	3.2-It should have one required parameter and two optional parameters. The 
#     	required parameter will determine which element in the series to print. The two 
#     	optional parameters will have default values of 0 and 1 and will determine the  
#     	first two values for the series to be produced.
# 	3.3-Calling this function with no optional parameters will produce numbers from the 
#     	Fibonacci series (because 0 and 1 are the defaults).
# 	3.4-Calling it with the optional arguments 2 and 1 will produce values from the lucas 
#     	numbers. Other values for the op!onal parameters will produce other series.
# 	3.5-Re-implement your fibonacci and lucas functions to call sum-series with particular 
#     	arguments.
#
# Implementation:
# ---------------
#	*	fibonacci(<n>)
#	*	lucas(<n>)
#	*	sum_series(<n>,[<elem0>[,<elem1>]])
# 
# Script Usage:
# -------------
# python series.py <n> [<elem0> [<elem1>]]
#
# 	<n> 	::= Nth element of Fibonacci, Lucas, or general series.
#	<elem0> ::= 0th element of general series (see sum_series for description.)
#	<elem1> ::= 1st element of general series (see sum_series for description.)
#
# 	Prints result for functions fibonacci, lucas, and sum_series at element <n>.
#
# History:
# --------
# 000/2020-09-20/sal/Created.
# 001/2020-09-21/sal/Refactored functions fibonacci and lucas.
# ========================================================================================

import sys

def fibonacci(n):
	"""
	fibonacci(<n>)
	--------------------------------------------------------------------------------------
	Determine the value of the nth element of a Fibonacci series, where element[0] = 0 and
	element[1] = 1.
	
	Entry:   <n> ::= 0-based index of the element of the series.
	       
	Exit:    Returns series element value (int) at <n>.
	
	History: 000/2020-09-20/sal/Created
	         001/2020-09-21/sal/Replaced code body with call to sum_series.
	"""
	return sum_series(n, 0, 1)
	
def lucas(n):
	"""
	lucas(<n>)
	--------------------------------------------------------------------------------------
	Determine the value of the nth element of a Lucas series, where element[0] = 2 and
	element[1] = 1.
	
	Entry:   <n> ::= 0-based index of the element of the series.
	       
	Exit:    Returns series element value (int) at <n>.
	
	History: 000/2020-09-20/sal/Created
	         001/2020-09-21/sal/Replaced code body with call to sum_series.	
	"""
	return sum_series(n, 2, 1) 
	
def sum_series(n, elem0 = 0, elem1 = 1):
	"""
	sum_series(<n>,[<elem0>[,<elem1>]])
	--------------------------------------------------------------------------------------
	Determine the value of the nth element of an integer sum series where the value of 
	the value of the first two elements (at n = 0 and n = 1) are known and the sum at 
	element n is defined as sum(n) = sum(n - 1) + sum(n - 2).
	
	Entry:   <n>     ::= 0-based index of the element of the series.
	         <elem0> ::= Element value at <n> = 0. Default is 0.
	         <elem1> ::= Element value at <n> = 1. Default is 1.
	       
	Exit:    Returns series element value (int) at <n>.
	
	History: 2020-09-20/sal/Created
	"""
	r = 0
	if (n == 0):
		r = elem0
	elif (n == 1):
		r = elem1
	elif (n > 1):
		r = sum_series(n - 2,elem0,elem1) + sum_series(n - 1,elem0,elem1)
	else:
		r = 0
	return r 		

# Command-line interface for demonstrating functions fibonacci, lucas, and sum_series.
	
if __name__ == "__main__":
	msg = ""
	if ((len(sys.argv) < 2) or (len(sys.argv) > 4)):
		#
		# Fail if one, two, or three script arguments not provided.
		#
		msg = "sum_series (ERROR): Requires 1 to 3 integer arguments"
	else:
		ok = True
		args = []
		#
		# Fail if any script argument not a positive integer. Success is an array
		# containing 1 to 3 integer values (n, [elem1, [elem2]]) used to demo the
		# three functions.
		#
		for i in range(1,len(sys.argv)):
			if (sys.argv[i].isnumeric()):
				args.append(int(sys.argv[i]))
			else:
				msg = msg + "sum_series (ERROR): arg[{}] ({}) not a positive integer"\
				.format(i,sys.argv[i])
				ok = False
		if ok:
			# 
			# Determine fibonacci(n) and lucas(n) result. Determine sum_series(n), 
			# sum_series(n, elem0), or sum_series(n, elem0, elem1) based on the number
			# of arguments.
			#
			n = args[0]
			fi = fibonacci(n)
			lu = lucas(n)
			su = -1   # Seems prudent to declare this once, not three times.
			msg = "fibonacci({}) = {}\nlucas({}) = {}".format(n,fi,n,lu)
			if (len(args) > 2):
				su = sum_series(n,args[1],args[2])
				msg = "{}\nsum_series({},{},{}) = {}".format(msg,n,args[1],args[2],su)
			elif (len(args) > 1):
				su = sum_series(n,args[1])
				msg = "{}\nsum_series({},{}) = {}".format(msg,n,args[1],su)
			else:
				su = sum_series(n)
				msg = "{}\nsum_series({}) = {}".format(msg,n,su)
	print(msg)
	
