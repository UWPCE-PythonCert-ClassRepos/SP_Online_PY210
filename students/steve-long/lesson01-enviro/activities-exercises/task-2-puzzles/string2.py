# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 2: Puzzles (http://codingbat.com/python) (string2.py)
# Steve Long 2020-09-15

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/string2.py


# double_char:
# ------------

# Given a string, return a string where for every char in the original, there are two 
# chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(s):
	dcs = ""
	for c in s:
		dcs = dcs + c + c
	return dcs
	
print("\ndouble_char:\n")	
for s in ["The", "AAbb", "Hi-There", "barbara-anne", "abradabracadabra", "sheet", \
"mississippi"]:
	print("double_char(\"{}\") = \"{}\"".format(s, double_char(s)))


# count_code:
# -----------

# Return the number of times that the string "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

import re

def count_code(s):
	pattern = "co.e"
	return len(re.findall(pattern,s))
	
print("\ncount_code:\n")	
for s in ["aaacodebbb", "codexxcode", "cozexxcope", "co3ecodecobecogh", "cozecosecade", \
"fred", "codi"]:
	print("count_code(\"{}\") = {}".format(s, count_code(s)))

# count_hi:
# ---------

# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

# ASSUMPTION: Do not ignore char case.

def count_hi(s):
	return s.count("hi")
	
print("\ncount_hi:\n")	
for s in ["abc hi ho", "ABChi hi", "hihi", "Hei! Wakeramasu.", "hidyho", "hihihi", \
"<Hi>"]:
	print("count_hi(\"{}\") = \"{}\"".format(s, count_hi(s)))

# end_other:
# ----------

# Given two strings, return True if either of the strings appears at the very end of the 
# other string, ignoring upper/lower case differences (in other words, the computation 
# should not be "case sensitive"). Note: s.lower() returns the lowercase version of a 
# string.

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
	result = False
	a = a.lower()
	b = b.lower()
	lenA = len(a)
	lenB = len(b)
	if (lenB <= lenA):
		if (a[(lenA - lenB):] ==  b):
			result = True
	if (lenA <= lenB):
		if (b[(lenB - lenA):] ==  a):
			result = True
	return result
	
print("\nend_other:\n")	
for ab in [["Hiabc","abc"],["AbC","HiaBc"],["abc","abXabc"],["Jalod","DarmokAndJalod"], \
["x",""], ["K'Vort","Vorcha"], ["Hajarezadeh","Rezadeh"]]:
	a = ab[0]
	b = ab[1]
	print("end_other(\"{}\",\"{}\") = {}".format(a, b, end_other(a, b)))
	

# cat_dog:
# --------

# Return True if the string "cat" and "dog" appear the same number of times in the given 
# string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(s):
	s = s.lower()
	return (s.count("cat") == s.count("dog"))
	
print("\ncat_dog:\n")	
for s in ["catdog", "catcat", "1cat1cadodog", "dawg-Dog-and-cat", \
"doggy-doo-hop-skip-and-jump", "alligator"]:
	print("cat_dog(\"{}\") = {}".format(s, cat_dog(s)))


# xyz_there:
# ----------

# Return True if the given string contains an appearance of "xyz" where the xyz is not 
# directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

# NOTE: It should have been possible to handle this with a regex lookbehind reference.

def xyz_there(s):
	found = False
	s = s.lower()
	prevChar = ""
	for n in range(0,len(s) - 2):
		if (s[n:n+3] == "xyz"):
			if (prevChar != "."):
				found = True
				break
		prevChar = s[n:n+1]
	return found
	
print("\nxyz_there:\n")	
for s in ["abcxyz", "abc.xyz", "xyz.abc", "ABC-xYZ", "x-xy-..xyz-XYZ", "fred"]:
	print("xyz_there(\"{}\") = {}".format(s, xyz_there(s)))
	
	
	