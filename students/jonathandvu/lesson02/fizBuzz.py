#!/usr/bin/env python
# PY210 Lesson 2 Grid Printer Excercise
# Jonathan Vu 08/22/19
# 
def fizBuzz():
	for i in range(1,101):
		output = ''
		if i % 3 == 0:
			output += 'Fizz'
		if i % 5 == 0:
			output += 'Buzz'
		else:
			output = i
		print(output)

fizBuzz()
