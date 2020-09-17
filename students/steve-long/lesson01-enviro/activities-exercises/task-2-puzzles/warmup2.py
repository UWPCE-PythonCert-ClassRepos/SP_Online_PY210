# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 2: Puzzles (http://codingbat.com/python) (warmup2.py)
# Steve Long 2020-09-11

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/warmup2.py

# string_times:

# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(s, n):
	return s * n
	
print("\nstring_times:\n")	
for sn in [["Hi",2], ["Hi",3], ["Hi",1], ["Java",0], ["601",8],["OT",-1],["",12]]:
	s = sn[0]
	n = sn[1]
	print("string_times(\"{}\",{}) = \"{}\"".format(s,n,string_times(s,n)))


# string_splosion:

# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(s):
	result = ""
	for n in range(0,len(s)): 
		result = result + s[0:(n+1)]
	return result
	
print("\nstring_splosion:\n")	
for s in ["Code","abc","ab","","601","9/11"]:
	print("string_splosion(\"{}\") = \"{}\"".format(s,string_splosion(s)))

# array_front9:

# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(a):
	result = False
	for n in range(0,min(4,len(a))):
		if (a[n] == 9):
			result = True
			break
	return result

print("\narray_front9:\n")	
for a in [[1, 2, 9, 3, 4], [1, 2, 3, 4, 9], [1, 2, 3, 4, 5], [9, 1, 1], [17], []]:
	print("array_front9({}) = \"{}\"".format(a,array_front9(a)))

# front_times:

# Given a string and a non-negative int n, we'll say that the front of the string is the 
# first 3 chars, or whatever is there if the string is less than length 3. Return n copies 
# of the front.

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(s, n):
	return ((s[0:min(len(s),3)]) * abs(n))
	
print("\nfront_times:\n")	
for sn in [["Chocolate",2], ["Chocolate",3], ["Abc", 3], ["s",-7], ["yo", 5], ["", 2]]:
	s = sn[0]
	n = sn[1]
	print("front_times(\"{}\", {}) = \"{}\"".format(s,n,front_times(s,n)))

# last2:

# Given a string, return the count of the number of times that a substring length 2 
# appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 
# (we won't count the end substring).

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

# SAL: The directions for this one were a little vague.

def last2(s):
	last2Count = 0
	if (len(s) >= 2):
		last2 = s[len(s) - 2:]
		for n in range(len(s) - 2):
			subS = s[n:n + 2]
			if (subS == last2):
				last2Count += 1
	return last2Count
	
print("\nlast2:\n")	
for s in ["hixxhi", "xaxxaxaxx", "axxxaaxx", "v", "vv", "vvv", "kamho-fong-as-chen-ho"]:
	print("last2(\"{}\") = {}".format(s,last2(s)))
	


# array123:

# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the 
# array somewhere.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(a):
	result = False
	for n in range(0,(len(a) - 2)):
		if ((a[n] == 1) and (a[n+1] == 2) and (a[n+2] == 3)):
			result = True
			break
	return result
	
print("\narray123:\n")	
for a in [[1, 1, 2, 3, 1], [1, 1, 2, 4, 1], [1, 1, 2, 1, 2, 3]]:
	print("array123({}) = {}".format(a,array123(a)))

# string_bits

# Given a string, return a new string made of every other char starting with the first, so 
# "Hello" yields "Hlo".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(s):
	result = ""
	for n in range(0,len(s),2):
		result = (result + s[n])
	return result
	
print("\nstring_bits:\n")	
for a in ["Hello", "Hi", "Heeololoo", "d9r0ijnvkx -yzoyuxrw vo2vva#l0t!ignqa2", ""]:
	print("string_bits(\"{}\") = \"{}\"".format(a,string_bits(a)))


# array_count9:

# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(a):
	count9 = 0
	for n in range(0,len(a)):
		if (a[n] == 9):
			count9 += 1
	return count9

print("\narray_count9:\n")	
for a in [[1, 2, 9], [1, 9, 9], [1, 9, 9, 3, 9], [42], []]:
	print("array_count9({}) = {}".format(a,array_count9(a)))

# string_match

# Given 2 strings, a and b, return the number of the positions where they contain the same 
# length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
# substrings appear in the same place in both strings.

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

# SAL: The directions for this one should have included the requirement for the position
# of the two characters being the same in both strings described in the first sentence. 
# This requirement was inferred from the example in the second sentence.

def string_match(a,b):
	matchCount = 0
	for i in range(0,(min(len(a),len(b)) - 1)):
		if (a[i:i+2] == b[i:i+2]):
			matchCount += 1
	return matchCount
	
print("\nstring_match:\n")	
for ab in [["xxcaazz","xxbaaz"], ["abc","abc"], ["abc","axc"], \
["palendrome","palendromic"], ["a","ab"], ["","z"]]:
	a = ab[0]
	b = ab[1]
	print("string_match(\"{}\",\"{}\") = \"{}\"".format(a,b,string_match(a,b)))


	
	