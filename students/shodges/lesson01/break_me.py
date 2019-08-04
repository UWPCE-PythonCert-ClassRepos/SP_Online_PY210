#!/usr/bin/env python

def name_error():
	print(test)

def type_error():
	a=1
	b='2'
	print (a+b)

def syntax_error():
	print (eval('a+'))

def attribute_error():
	val='attribute error'
	print (val.doesnotexist)
