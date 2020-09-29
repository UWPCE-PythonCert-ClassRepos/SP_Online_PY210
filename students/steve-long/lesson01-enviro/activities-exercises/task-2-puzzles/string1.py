# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 2: Puzzles (http://codingbat.com/python) (string1.py)
# Steve Long 2020-09-12

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/string1.py


# hello_name:
# -----------

# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
	return "Hello {}!".format(name)
	
print("\nhello_name:\n")	
for name in ["Bob", "Alice", "X", "le Monde", "John Snow", "Daenerys Stormborn of the \
House Targaryen, First of Her Name, the Unburnt, Queen of the Andals and the First Men, \
Khaleesi of the Great Grass Sea, Breaker of Chains, and Mother of Dragons"]:
	print("hello_name(\"{}\") = \"{}\"".format(name, hello_name(name)))	


# make_out_word:
# --------------

# Given an "out" string length 4, such as "<<>>", and a word, return a new string where 
# the word is in the middle of the out string, e.g. "<<word>>".

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(os4, w):
	return (os4[0:2] + w + os4[2:])
	
print("\nmake_out_word:\n")	
for os4w in [["<<>>","Yay"],["<<>>","WooHoo"],["[[]]","word"],["(())","$"],["$..$","Clojure"]]:
	os4 = os4w[0]
	w = os4w[1]
	print("make_out_word(\"{}\",\"{}\") = \"{}\"".format(os4, w, make_out_word(os4, w)))


# first_half:
# -----------

# Given a string of even length, return the first half. So the string "WooHoo" yields 
# "Woo".

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(s):
	return s[0:int(len(s)/2)]

print("\nfirst_half:\n")	
for s in ["WooHoo", "HelloThere", "abcdef", "Nee!", "Free advice is seldom cheap", "?", \
""]:
	print("first_half(\"{}\") = \"{}\"".format(s, first_half(s)))
	

# non_start:
# ----------

# Given 2 strings, return their concatenation, except omit the first char of each. The 
# strings will be at least length 1.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
	return "{}{}".format(a[1:],b[1:])
	
print("\nnon_start:\n")	
for ab in [["Hello","There"],["java","code"],["shot1","java"],["Shat","Rabbah"], \
["Gurney","Hallick"],]:
	a = ab[0]
	b = ab[1]
	print("non_start(\"{}\",\"{}\") = \"{}\"".format(a, b, non_start(a, b)))
	

# make_abba:
# ----------

# Given two strings, a and b, return the result of putting them together in the order 
# abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
	return "{}{}{}{}".format(a,b,b,a)

print("\nmake_abba:\n")	
for ab in [["Hi","Bye"],["Yo","Alice"],["What","Up"],["Yo","Adrienne"],["Jean","Gene"],]:
	a = ab[0]
	b = ab[1]
	print("make_abba(\"{}\",\"{}\") = \"{}\"".format(a, b, make_abba(a, b)))


# extra_end:
# ----------

# Given a string, return a new string made of 3 copies of the last 2 chars of the original 
# string. The string length will be at least 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(s):
	return s[len(s) - 2:] * 3
	
print("\nextra_end:\n")	
for s in ["Hello","ab","Hi","Shizzle","Nyet"]:
	print("extra_end(\"{}\") = \"{}\"".format(s, extra_end(s)))	


# without_end:
# ------------

# Given a string, return a version without the first and last char, so "Hello" yields 
# "ell". The string length will be at least 2.

# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(s):
	return s[1:(len(s) - 1)]

print("\nwithout_end:\n")	
for s in ["Hello", "java", "coding", "declare", "$5", "yes", "biscuit"]:
	print("without_end(\"{}\") = \"{}\"".format(s, without_end(s)))
	
	
# left2:
# ------

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to 
# the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(s):
	return (s[2:] + s[0:2])
	
print("\nleft2:\n")	
for s in ["Hello", "java", "Hi", "declare", "$5", "yes", "non sequitur"]:
	print("left2(\"{}\") = \"{}\"".format(s, left2(s)))


# make_tags:
# ----------

# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In 
# this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag 
# and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
	return "<{}>{}</{}>".format(tag,word,tag)
	
print("\nmake_tags:\n")	
for tagAndWord in [["i","Yay"],["i","Hello"],["cite","Yay"]]:
	tag = tagAndWord[0]
	word = tagAndWord[1]
	print("make_tags(\"{}\",\"{}\") = \"{}\"".format(tag, word, make_tags(tag, word)))

# first_two:
# ----------

# Given a string, return the string made of its first two chars, so the String "Hello" 
# yields "He". If the string is shorter than length 2, return whatever there is, so "X" 
# yields "X", and the empty string "" yields the empty string "".

# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'

def first_two(s):
	return s[:min(len(s),2)]

print("\nfirst_two:\n")	
for s in ["Hello", "abcdefg", "ab", "#", ""]:
	print("first_two(\"{}\") = \"{}\"".format(s, first_two(s)))

# combo_string:
# -------------

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter 
# string on the outside and the longer string on the inside. The strings will not be the 
# same length, but they may be empty (length 0).

# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
	if (len(a) > len(b)):
		o = b
		i = a
	else:
		o = a
		i = b
	return "{}{}{}".format(o,i,o)
	
print("\ncombo_string:\n")	
for ab in [["Hello","hi"],["hi","Hello"],["aaa","b"],["redundancy","department"],\
["Meh",""]]:
	a = ab[0]
	b = ab[1]
	print("combo_string(\"{}\",\"{}\") = \"{}\"".format(a, b, combo_string(a, b)))

