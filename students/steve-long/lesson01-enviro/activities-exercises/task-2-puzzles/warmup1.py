# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 2: Puzzles (http://codingbat.com/python) (warmup1.py)
# Steve Long 2020-09-10

# /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/warmup1.py


# sleep_in
# --------

# The parameter weekday is True if it is a weekday, and the parameter vacation is True if  
# we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True  
# if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
	return (vacation or (not weekday))	

print("\nsleep_in:\n")
print("sleep_in({},{}) = {}".format(False,False,sleep_in(False,False)))
print("sleep_in({},{}) = {}".format(True,False,sleep_in(True,False)))
print("sleep_in({},{}) = {}".format(False,True,sleep_in(False,True)))


# diff21:
# -------

# Given an int n, return the absolute difference between n and 21, except return double 
# the absolute difference if n is over 21.

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
	result = abs(21 - n)
	if (n > 21):
		result = result * 2
	return result

print("\ndiff21:\n")	
print("diff21({}) = {}".format(19,diff21(19)))
print("diff21({}) = {}".format(10,diff21(10)))
print("diff21({}) = {}".format(21,diff21(21)))
print("diff21({}) = {}".format(37,diff21(37)))	


# near_hundred:
# -------------

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes 
# the absolute value of a number.

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
	return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
	
print("\nnear_hundred:\n")	
print("near_hundred({}) = {}".format(93,near_hundred(93)))
print("near_hundred({}) = {}".format(90,near_hundred(90)))
print("near_hundred({}) = {}".format(89,near_hundred(89)))
print("near_hundred({}) = {}".format(190,near_hundred(190)))
print("near_hundred({}) = {}".format(210,near_hundred(210)))
print("near_hundred({}) = {}".format(211,near_hundred(211)))


# missing_char:
# -------------

# Given a non-empty string and an int n, return a new string where the char at index n has 
# been removed. The value of n will be a valid index of a char in the original string  
# (i.e. n will be in the range 0..len(str)-1 inclusive).

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(s, n):
	return (s[:n] + s[n+1:])
	
print("\nmissing_char:\n")	
for sAndN in [["kitten", 1], ["kitten", 0], ["kitten", 4], ["kitten", 5], ["k",0]]:
	s = sAndN[0]
	n = sAndN[1]
	print("missing_char(\"{}\",{}) = \"{}\"".format(s,n,missing_char(s,n)))


# monkey_trouble:
# ---------------

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is 
# smiling. We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile,b_smile):
	return (a_smile == b_smile)

print("\nmonkey_trouble:\n")	
for ab_smile in [[True, True], [True, False], [False, False], [False, True]]:
	a_smile = ab_smile[0]
	b_smile = ab_smile[1]
	print("monkey_trouble({},{}) = {}".format(a_smile,b_smile, \
	monkey_trouble(a_smile,b_smile)))

	
# parrot_trouble:
# ---------------

# We have a loud talking parrot. The "hour" parameter is the current hour time in the 
# range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or 
# after 20. Return True if we are in trouble.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False	

def parrot_trouble(talking, hour):
	return (talking and ((hour < 7) or (hour > 20)))
	
print("\nparrot_trouble:\n")	
for talkingHour in [[True, 6], [True, 7], [False, 8], [False, 7], [True, 20], \
[True, 21], [False, 21], [False, 6]]:
	talking = talkingHour[0]
	hour = talkingHour[1]
	print("parrot_trouble({},{}) = {}".format(talking, hour, \
	parrot_trouble(talking,hour)))		


# pos_neg:
# --------

# Given 2 int values, return True if one is negative and one is positive. Except if the 
# parameter "negative" is True, then return True only if both are negative.

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True
	
def pos_neg(a, b, negative):
	result = False
	if (negative):
		result = ((a < 0) and (b < 0))
	else:
		result = (((a < 0) and (b >= 0)) or ((a >= 0) and (b < 0)))
	return  result
	
print("\npos_neg:\n")	
for abn in [[-1,-1,True], [-1,-1,False], [-1,0,True], [-1,0,False], [-1,1,True], \
[-1,1,False], [0,-1,True], [0,-1,False], [0,0,True], [0,0,False], [0,1,True], \
[0,1,False], [1,-1,True], [1,-1,False], [1,0,True], [1,0,False], [1,1,True], [1,1,False]]:
	a = abn[0]
	b = abn[1]
	negative = abn[2]
	print("pos_neg({}, {}, {}) = {}".format(a, b, negative, \
	pos_neg(a, b, negative)))	
	
# front_back:	
# -----------

# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# ASSUMPTION: String is pass-by-reference. Return a NEW string.

def front_back(s):
	ns = s.encode().decode()
	result = ns
	if (len(ns) > 1):
		result = (ns[(len(ns) - 1):] + ns[1:(len(ns) - 1)] + ns[0:1])
	return result
	
print("\nfront_back:\n")	
for s in ["code","a","ab","","gold-pressed-latinum"]:
	print("front_back(\"{}\") = \"{}\"".format(s,front_back(s)))
	
	
# sum_double:
# -----------

# Given two int values, return their sum. Unless the two values are the same, then return 
# double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
	result = a + b
	if (a == b):
		result = 2 * result
	return result
	
print("\nsum_double:\n")	
for ab in [[1,2],[3,2],[2,2],[0,0],[-7,-8],[47,-47]]:
	a = ab[0]
	b = ab[1]
	print("sum_double({},{}) = {}".format(a,b,sum_double(a,b)))
	
	
# makes10:
# --------

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
	return ((a == 10) or (b == 10) or ((a + b) == 10))
	
print("\nmakes10:\n")	
for ab in [[9,10],[9,9],[1,9],[3,7],[17,-7],[4,5]]:
	a = ab[0]
	b = ab[1]
	print("makes10({},{}) = {}".format(a,b,makes10(a,b)))
	
	
# not_string:
# -----------

# Given a string, return a new string where "not " has been added to the front. However, 
# if the string already begins with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(s):
	result = s
	if (s[0:3] != "not"):
		result = ("not " + s)
	return result
	
print("\nnot_string:\n")	
for s in ["candy","x","not bad","nottingham","the name of a flavor","head",""]:
	print("not_string(\"{}\") = \"{}\"".format(s,not_string(s)))


# front3:
# -------

# Given a string, we'll say that the front is the first 3 chars of the string. If the 
# string length is less than 3, the front is whatever is there. Return a new string which  
# is 3 copies of the front.

# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

def front3(s):
	front = s[:min(3,len(s))]
	return (front * 3)
	
print("\nfront3:\n")	
for s in ["Java","Chocolate","601","OT","tactical","Jettison",""]:
	print("front3(\"{}\") = \"{}\"".format(s,front3(s)))

	
	