#!/usr/bin/env python3
# ========================================================================================
# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson02
# Fizz Buzz Exercise (fizzBuzz.py)
# Steve Long 2020-09-19 | v0
#
# Requirements:
# -------------
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print "Fizz" instead of the number.
# For the multiples of five print "Buzz" instead of the number.
# For numbers which are multiples of both three and five print "FizzBuzz" instead.
#
# Implementation:
# ---------------
#	fizzBuzz([<start>[,<end>]])
#
# Script Usage:
# -------------
# 	python fizzBuzz.py [<start> [<end>]]
#		<start> ::= Starting number (see function fizzBuzz for details.)
#		<end>   ::= Ending number (see function fizzBuzz for details.)
#
# History:
# --------
# 000/2020-09-20/sal/Created.
# ========================================================================================

import sys
	
def fizzBuzz(start = 1, end = 100):
	"""
	fizzBuzz([<start>[,<end>]])
	--------------------------------------------------------------------------------------
	For non-negative int values from <start> to <end>, print the following:
	* "Fizz" for multiples of 3
	* "Buzz" for multiples of 5
	* "FizzBuzz" for multiples of 3 and 5
	* The number for all other values
	
	Entry: <start> ::= Starting int value (default is 1).
	       <end>   ::= Ending int value (default is 100).
	Exit:  Returns True.
	"""
	for n in range(start, (end + 1)):
		s = ("FizzBuzz" if (((n % 3) == 0) and ((n % 5) == 0)) else \
		("Fizz" if ((n % 3) == 0) else \
		("Buzz" if ((n % 5) == 0) else n)))
		print(s)
	return True

# Command-line interface for demonstrating function fizzBuzz.

if __name__ == "__main__":
	args = sys.argv
	argCount = (len(args) - 1)
	if (argCount == 2):
		#
		# Execute validated 2-argument scenario.
		# 
		if (args[1].isnumeric() and args[2].isnumeric()):
			fizzBuzz(int(args[1]), int(args[2]))
		else: 
			if (not args[1].isnumeric()):
				print("fizzBuzz (ERROR): Invalid start argument ({})".format(args[1]))
			if (not args[2].isnumeric()):
				print("fizzBuzz (ERROR): Invalid end argument ({})".format(args[2]))
	elif (argCount == 1):
		#
		# Execute validated 1-argument scenario.
		# 
		if (args[1].isnumeric()):
			fizzBuzz(int(args[1]))
		else: 
			print("fizzBuzz (ERROR): Invalid start argument ({})".format(args[1]))
	else:
		#
		# Execute validated 0-argument scenario.
		# 
		fizzBuzz()
		
