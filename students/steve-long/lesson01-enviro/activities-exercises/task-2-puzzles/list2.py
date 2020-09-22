# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01
# Task 2: Puzzles (http://codingbat.com/python) (list2.py)
# Steve Long 2020-09-15

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/list2.py


# count_evens:
# ------------

# Return the number of even ints in the given array. Note: the % "mod" operator computes 
# the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
	eCount = 0
	for n in nums:
		if ((n % 2) == 0):
			eCount += 1
	return eCount
	
print("\ncount_evens:\n")	
for iArray in [[2, 1, 2, 3, 4], [2, 2, 0], [1, 3, 5], [17], [24], []]:
	print("count_evens({}) = {}".format(iArray, count_evens(iArray)))

# sum13:
# ------

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the 
# number 13 is very unlucky, so it does not count and numbers that come immediately after 
# a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
	sum = 0
	prevWas13 = False
	for n in nums:
		if (n == 13):
			prevWas13 = True
		else:
			if (not prevWas13):
				sum += n
			prevWas13 = False
	return sum
	
print("\nsum13:\n")	
for iArray in [[1, 2, 2, 1], [1, 1], [1, 2, 2, 1, 13], [17], [7, 13, 12, 11, 13], []]:
	print("sum13({}) = {}".format(iArray, sum13(iArray)))
				

# big_diff:
# ---------

# Given an array length 1 or more of ints, return the difference between the largest and 
# smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions 
# return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
	diff = 0
	if (len(nums) > 0):
		largest = nums[0]
		smallest = nums[0]
		for n in nums[1:]:
			largest = max(largest,n)
			smallest = min(smallest,n)
		diff = (largest - smallest)
	return diff

print("\nbig_diff:\n")	
for iArray in [[10, 3, 5, 6], [7, 2, 10, 9], [2, 10, 7, 2], [17, 83], [54], []]:
	print("big_diff({}) = {}".format(iArray, big_diff(iArray)))
	
# Alternate solution:

def big_diff_alt(nums):
	diff = 0
	if (len(nums) > 0):
		working = nums.copy()
		working.sort()
		diff = working[len(working) - 1] - working[0]
	return diff
	

# sum67:
# ------

# Return the sum of the numbers in the array, except ignore sections of numbers starting 
# with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
# Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
	sum = 0
	section6 = False
	for n in nums:
		if (n == 6):
			section6 = True
		elif (n == 7):
			if (not section6):
				sum += n
			section6 = False
		else:
			if (not section6):
				sum += n
	return sum
	
print("\nsum67:\n")	
for iArray in [[1, 2, 2], [1, 2, 2, 6, 99, 99, 7], [1, 1, 6, 7, 2], [7, 6, 5, 4, 7, 3], \
[6, 7], [6], [7], [8], []]:
	print("sum67({}) = {}".format(iArray, sum67(iArray)))


# centered_average:
# -----------------

# Return the "centered" average of an array of ints, which we'll say is the mean average 
# of the values, except ignoring the largest and smallest values in the array. If there 
# are multiple copies of the smallest value, ignore just one copy, and likewise for the 
# largest value. Use int division to produce the final average. You may assume that the 
# array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# ASSUMPTIONS: (1) Result should be an int; (2) OK to raise error for invalid list length.

# FAVORITE

def centered_average(nums):
	if (len(nums) > 2):
		try: 
			working = nums.copy()
			working.sort()
			working = working[1:(len(working) - 1)]
			workingCount = len(working)
			return int(sum(working)/workingCount)
		except:
			pass
	else:
		raise ValueError("Argument must be an array of 3 or more integers")

print("\ncentered_average:\n")
print("NOTE: Test case for <3 element array omitted on purpose.")	
for iArray in [[1, 2, 3, 4, 100], [1, 1, 5, 5, 10, 8, 7], [-10, -4, -2, -4, -2, 0], [9, 1, 4], ["a", 2, 3]]:
	print("centered_average({}) = {}".format(iArray, centered_average(iArray)))	

# has22:
# ------

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
	result = False
	for i in range(0,(len(nums) - 1)):
		j = i + 1
		if (nums[i] == 2):
			if (nums[i + 1] == 2):
				result = True
				break
	return result

print("\nhas22:\n")	
for iArray in [[1, 2, 2], [1, 2, 1, 2], [2, 1, 2], [4, 11, 36], [19, 37], [2], []]:
	print("has22({}) = {}".format(iArray, has22(iArray)))
	