# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01 
# Task 2: Puzzles (http://codingbat.com/python) (logic2.py)
# Steve Long 2020-09-15

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/logic2.py

# make_bricks:
# ------------

# We want to make a row of bricks that is goal inches long. We have a number of small 
# bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to 
# make the goal by choosing from the given bricks. This is a little harder than it looks 
# and can be done without any loops. See also: Introduction to MakeBricks

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
	result = False
	if ((goal > ((big * 5) + small)) or ((goal % 5) > small)):
		# Total number of bricks insufficient or nsufficient number of small bricks for 
		# single big brick.
		result = False
	else:
		# Some other combination will work.
		result = True
	return result

print("\nmake_bricks:\n")	
for args in [[3,1,8],[3,1,9],[3,2,10],[5,5,5],[1,4,21],[12,1,4],[36,3,51],[0,1,2],[1,1,7]]:
	small = args[0]
	big = args[1]
	goal = args[2]
	print("make_bricks({},{},{}) = {}".format(small,big,goal,make_bricks(small,big,goal)))	

# no_teen_sum:
# ------------

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- 
# in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not 
# count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value 
# and returns that value fixed for the teen rule. In this way, you avoid repeating the 
# teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent 
# level as the main no_teen_sum().

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
	if (((n >= 13) and (n <= 14)) or ((n >= 17) and (n <= 19))):
		n = 0
	return n
	
def no_teen_sum(a, b, c):
	return (fix_teen(a) + fix_teen(b) + fix_teen(c))
	
print("\nno_teen_sum:\n")	
for args in [[1,2,3],[2,13,1],[2,1,14],[1,14,2],[1,15,2],[1,16,2],[1,17,2],[1,19,2],[1,20,2]]:
	a = args[0]
	b = args[1]
	c = args[2]
	print("no_teen_sum({},{},{}) = {}".format(a,b,c,no_teen_sum(a,b,c)))

# make_chocolate:
# ---------------

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and 
# big bars (5 kilos each). Return the number of small bars to use, assuming we always use 
# big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
	smallCount = 0
	while (big >= 0):
		if ((big * 5) <= goal):
			break
		else:
			big -= big
	smallCount = (goal - (big * 5))
	if (smallCount > small):
		smallCount = -1
	return smallCount
	
print("\nmake_chocolate:\n")	
for args in [[4,1,9],[4,1,10],[4,1,7],[5,5,5],[1,4,21],[12,1,4],[36,3,51],[0,1,2],[1,1,7]]:
	small = args[0]
	big = args[1]
	goal = args[2]
	print("make_chocolate({},{},{}) = {}".format(small,big,goal,make_chocolate(small,big,goal)))


# lone_sum:
# ------------

# Given 3 int values, a b c, return their sum. However, if one of the values is the same 
# as another of the values, it does not count towards the sum.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
	sum = 0
	if ((a != b) and (a != c)):
		sum += a
	if ((b != a) and (b != c)):
		sum += b
	if ((c != a) and (c != b)):
		sum += c
	return sum
			
print("\nlone_sum:\n")	
for args in [[1,2,3],[3,2,3],[3,3,3],[2,2,3],[1,2,2]]:
	a = args[0]
	b = args[1]
	c = args[2]
	print("lone_sum({},{},{}) = {}".format(a,b,c,lone_sum(a,b,c)))


# round_sum:
# ----------

# For this problem, we'll round an int value up to the next multiple of 10 if its 
# rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the 
# previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, 
# write a separate helper "def round10(num):" and call it 3 times. Write the helper 
# entirely below and at the same indent level as round_sum().

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round10(num):
	r = (num % 10)
	if (r < 5):
		num = num - r
	else:
		num = (num + 10 - r)
	return num

def round_sum(a, b, c):
	return (round10(a) + round10(b) + round10(c))
	
print("\nround_sum:\n")	
for args in [[16,17,18],[12,13,14],[6,4,4],[17,35,51],[111,82,67]]:
	a = args[0]
	b = args[1]
	c = args[2]
	print("round_sum({},{},{}) = {}".format(a,b,c,round_sum(a,b,c)))



# lucky_sum:
# ----------

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it 
# does not count towards the sum and values to its right do not count. So for example, if 
# b is 13, then both b and c do not count.

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
	sum = 0
	n = [a,b,c]
	for i in range(0,3):
		if (n[i] == 13):
			break
		else:
			sum += n[i]
	return sum

print("\nlucky_sum:\n")	
for args in [[1,2,3],[1,2,13],[1,13,3],[13,5,11],[11,33,67]]:
	a = args[0]
	b = args[1]
	c = args[2]
	print("lucky_sum({},{},{}) = {}".format(a,b,c,lucky_sum(a,b,c)))


# close_far:
# ----------

# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at 
# most 1), while the other is "far", differing from both other values by 2 or more. Note: 
# abs(num) computes the absolute value of a number.

# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
	result = (((abs(a - b) < 2) and ((abs(a - c) > 1) and (abs(b - c) > 1))) \
	or ((abs(a - c) < 2) and ((abs(a - b) > 1) and (abs(b - c) > 1))))
	return result
	
print("\nclose_far:\n")	
for args in [[1,2,10],[1,2,3],[4,1,3],[9,8,7],[9,8,6],[9,7,6],[9,6,8],[9,6,7],[6,7,9]]:
	a = args[0]
	b = args[1]
	c = args[2]
	print("close_far({},{},{}) = {}".format(a,b,c,close_far(a,b,c)))
	
	
	
	
	
	
