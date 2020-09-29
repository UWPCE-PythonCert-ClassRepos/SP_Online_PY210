# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01 
# Task 2: Puzzles (http://codingbat.com/python) (list1.py)
# Steve Long 2020-09-15

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/list1.py

# first_last6:
# ------------

# Given an array of ints, return True if 6 appears as either the first or last element in 
# the array. The array will be length 1 or more.


# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
	return ((len(nums) > 0) and ((nums[0] == 6) or (nums[len(nums) - 1] == 6)))
	
print("\nfirst_last6:\n")	
for iArray in [[1,2,6], [6,1,2,3], [13,6,1,2,3], [], [6,0], [0,6], [11], [6]]:
	print("first_last6({}) = {}".format(iArray, first_last6(iArray)))


# common_end:
# -----------

# Given 2 arrays of ints, a and b, return True if they have the same first element or they 
# have the same last element. Both arrays will be length 1 or more.

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
	result = False
	if ((len(a) * len(b)) > 0):
		result = ((a[0] == b[0]) or (a[len(a) - 1] == b[len(b) - 1]))
	return result
	
print("\ncommon_end:\n")	
for iArray in [[[1,2,3],[7,3]], [[1,2,3],[7,3,2]], [[1,2,3],[1,3]], [[1],[1]], \
[[3,2,4,1],[1,4,2,3]], [[1],[0]], [[],[13]] ]:
	a = iArray[0]
	b = iArray[1]
	print("common_end({}, {}) = {}".format(a, b, common_end(a, b)))


# reverse3:
# ---------

# Given an array of ints length 3, return a new array with the elements in reverse order, 
# so {1, 2, 3} becomes {3, 2, 1}.

# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
	return [n for n in reversed(nums)]

print("\nreverse3:\n")	
for iArray in [[1, 2, 3], [5, 11, 9], [7, 0, 0], [11, 17], [19], []]:
	print("reverse3({}) = {}".format(iArray, reverse3(iArray)))
	

# middle_way:
# -----------

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their 
# middle elements.

# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
	return [a[1],b[1]]
	
print("\nmiddle_way:\n")	
for iArray in [[[1, 2, 3], [4, 5, 6]], [[7, 7, 7], [3, 8, 0]], [[5, 2, 9], [1, 4, 5]], \
[[98, 97, 96], [1, 4, 9]]]:
	a = iArray[0]
	b = iArray[1]
	print("middle_way({}, {}) = {}".format(a, b, middle_way(a, b)))


# same_first_last:
# ----------------

# Given an array of ints, return True if the array is length 1 or more, and the first 
# element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
	return ((len(nums) > 0) and ((nums[0] == nums[len(nums) - 1])))
	
print("\nsame_first_last:\n")	
for iArray in [[1, 2, 3], [1, 2, 3, 1], [1, 2, 1], [4, 2], [4, 4], [7], []]:
	print("same_first_last({}) = {}".format(iArray, same_first_last(iArray)))


# sum3:
# -----

# Given an array of ints length 3, return the sum of all the elements.

# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(nums):
	sum = 0
	for n in nums:
		sum += n
	return sum

print("\nsum3:\n")	
for iArray in [[1, 2, 3], [5, 11, 2], [7, 0, 0], [4, 2], [7], []]:
	print("sum3({}) = {}".format(iArray, sum3(iArray)))


# max_end3:
# ---------

# Given an array of ints length 3, figure out which is larger, the first or last element 
# in the array, and set all the other elements to be that value. Return the changed array.

# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
	newNums = []
	if (len(nums) > 0):
		maxEnd = max(nums[0],nums[(len(nums) - 1)])
		newNums = [maxEnd]*(len(nums))
	return newNums

print("\nmax_end3:\n")	
for iArray in [[1, 2, 3], [11, 5, 9], [2, 11, 3], [1, 4, 9], [2, 32, 14], [2, 3], [7], []]:
	print("max_end3({}) = {}".format(iArray, max_end3(iArray)))
	

# make_ends:
# ----------

# Given an array of ints, return a new array length 2 containing the first and last 
# elements from the original array. The original array will be length 1 or more.

# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
	result = []
	if (len(nums) > 0):
		result = [nums[0], nums[len(nums) - 1]]
	return result
	
print("\nmake_ends:\n")	
for iArray in [[1, 2, 3], [1, 2, 3, 4], [7, 4, 6, 2], [1, 4], [2], []]:
	print("make_ends({}) = {}".format(iArray, make_ends(iArray)))

# make_pi:
# --------

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() → [3, 1, 4]

def make_pi():
	return [3, 1, 4]

print("\nmake_pi:\n")	
print("make_pi() = {}".format(make_pi()))
	

# rotate_left3:
# -------------

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 
# 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
	rotated = []
	if (len(nums) > 0):
		rotated = nums[1:]
		rotated.append(nums[0])
	return rotated
	
print("\nrotate_left3:\n")	
for iArray in [[1, 2, 3], [5, 11, 9], [7, 0, 0], [1, 4], [2], []]:
	print("rotate_left3({}) = {}".format(iArray, rotate_left3(iArray)))


# sum2:
# -----

# Given an array of ints, return the sum of the first 2 elements in the array. If the 
# array length is less than 2, just sum up the elements that exist, returning 0 if the 
# array is length 0.

# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
	sum = 0
	for i in range(0,min(2,len(nums))):
		sum += nums[i]
	return sum
	
print("\nsum2:\n")	
for iArray in [[1, 2, 3], [1, 1], [1, 1, 1, 1], [17], [-47, 81], []]:
	print("sum2({}) = {}".format(iArray, sum2(iArray)))

# has23:
# ------

# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
	result = False
	for n in nums:
		if ((n == 2) or (n == 3)):
			result = True
	return result

print("\nhas23:\n")	
for iArray in [[2, 5], [4, 3], [4, 5], [-2, -3], [2], [17], []]:
	print("has23({}) = {}".format(iArray, has23(iArray)))

