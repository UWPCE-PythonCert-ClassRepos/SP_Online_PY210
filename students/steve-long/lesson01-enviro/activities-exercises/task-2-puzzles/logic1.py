# Python210 | Fall 2020
# ----------------------------------------------------------------------------------------
# Lesson01 
# Task 2: Puzzles (http://codingbat.com/python) (logic1.py)
# Steve Long 2020-09-12

# python /Users/steve/Documents/Project/python/uw_class/python210/lessons/lesson01-enviro/logic1.py


# cigar_party:
# ------------

# When squirrels get together for a party, they like to have cigars. A squirrel party is 
# successful when the number of cigars is between 40 and 60, inclusive. Unless it is the 
# weekend, in which case there is no upper bound on the number of cigars. Return True if 
# the party with the given values is successful, or False otherwise.

# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
	return ((cigars >= 40) and (is_weekend or ((not is_weekend) and (cigars <= 60))))

print("\ncigar_party:\n")	
for args in [[30,False],[50,False],[70,True]]:
	cigars = args[0]
	is_weekend = args[1]
	print("cigar_party({},{}) = {}".format(cigars,is_weekend,cigar_party(cigars,is_weekend)))

# caught_speeding:
# ----------------

# You are driving a little too fast, and a police officer stops you. Write code to compute 
# the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed 
# is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 
# 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, 
# your speed can be 5 higher in all cases.

# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, isBirthday):
	fineIndex = 0
	addSpeed = 0
	if (isBirthday):
		addSpeed = 5
	if (speed <= (60 + addSpeed)):
		fineIndex = 0
	elif ((speed >= 61) and (speed <= (80 + addSpeed))):
		fineIndex = 1
	else:
		fineIndex = 2
	return fineIndex
	
print("\ncaught_speeding:\n")	
for args in [[60,False],[65,False],[65,True],[83,True],[83,False]]:
	speed = args[0]
	isBirthday = args[1]
	print("caught_speeding({},{}) = {}".format(speed,isBirthday,caught_speeding(speed,
	isBirthday)))

# love6:
# ------

# The number 6 is a truly great number. Given two int values, a and b, return True if 
# either one is 6. Or if their sum or difference is 6. Note: the function abs(num) 
# computes the absolute value of a number.

# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True

def love6(a, b):
	return (((a == 6) or (b == 6)) or (abs(a - b) == 6) or (abs(a + b) == 6))
	
print("\nlove6:\n")	
for args in [[6,4],[4,5],[1,5],[-1,-5],[1,-7],[-8,-2],[8,2]]:
	a = args[0]
	b = args[1]
	print("love6({},{}) = {}".format(a,b,love6(a,b)))

# date_fashion:
# -------------

# You and your date are trying to get a table at a restaurant. The parameter "you" is the 
# stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your 
# date's clothes. The result getting the table is encoded as an int value with 0=no, 
# 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). 
# With the exception that if either of you has style of 2 or less, then the result is 0 
# (no). Otherwise the result is 1 (maybe).

# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
	result = 0
	if ((you <= 2) or (date <= 2)):
		result = 0
	elif ((you >= 8) or (date >= 8)):
		result = 2
	else:
		result = 1
	return result
	
print("\ndate_fashion:\n")	
for args in [[5,10],[5,2],[5,5],[7,6],[8,7],[8,2],[2,8],[3,8]]:
	a = args[0]
	b = args[1]
	print("date_fashion({},{}) = {}".format(a,b,date_fashion(a,b)))


# sorta_sum:
# ----------

# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, 
# are forbidden, so in that case just return 20.

# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
	c = a + b
	if ((c >= 10) and (c <= 19)):
		c = 20
	return c
	
print("\nsorta_sum:\n")	
for args in [[3,4],[9,4],[10,11],[0,19],[0,20],[0,10],[0,9],[23,-8]]:
	a = args[0]
	b = args[1]
	print("sorta_sum({},{}) = {}".format(a,b,sorta_sum(a,b)))


# in1to10:
# --------

# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode 
# is True, in which case return True if the number is less or equal to 1, or greater or 
# equal to 10.

# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True

def in1to10(n, outside_mode):
	result = False
	if (outside_mode):
		result = ((n <= 1) or (n >= 10))
	else:
		result = ((n >= 1) and (n <= 10))
	return result

print("\nin1to10:\n")	
for args in [[5,False],[11,False],[11,True],[1,False],[1,True],[10,False],[10,True], \
[0,False],[0,True],[5,True]]:
	n = args[0]
	outside_mode = args[1]
	print("in1to10({},{}) = {}".format(n,outside_mode,in1to10(n,outside_mode)))
	

# squirrel_play:
# --------------

# The squirrels in Palo Alto spend most of the day playing. In particular, they play if 
# the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper 
# limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return  
# True if the squirrels play and False otherwise.

# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temperature, is_summer):
	play = False
	if (temperature >= 60):
		if (is_summer):
			play = (temperature <= 100)
		else:
			play = (temperature <= 90)
	return play
	
print("\nsquirrel_play:\n")	
for args in [[70,False],[95,False],[95,True],[60,False],[60,True],[59,False],[59,True], \
[100,False],[100,True],[90,False],[90,True],[101,False],[101,True],[89,False],[89,True]]:
	temperature = args[0]
	is_summer = args[1]
	print("squirrel_play({},{}) = {}".format(temperature, is_summer, squirrel_play(temperature, is_summer)))



# alarm_clock:
# ------------

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean 
# indicating if we are on vacation, return a string of the form "7:00" indicating when the 
# alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it 
# should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" 
# and weekends it should be "off".

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
	result = ""
	if (vacation):
		if ((day >= 1) and (day <= 5)):
			result = "10:00"
		else:
			result = "off"
	else:
		if ((day >= 1) and (day <= 5)):
			result = "7:00"
		else:
			result = "10:00"
	return result

print("\nalarm_clock:\n")	
for args in [[1,False],[5,False],[0,False],[1,True],[5,True],[0,True],[6,False],[6,True]]:
	day = args[0]
	vacation = args[1]
	print("alarm_clock({},{}) = \"{}\"".format(day, vacation, alarm_clock(day, vacation)))
	
# near_ten:
# ---------

# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: 
# Introduction to Mod

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
	r = (num % 10)
	return ((r <= 2) or (r >= 8))
	
print("\nnear_ten:\n")	
for num in [12, 17, 19, 10, 20, 25, 98, 102, 404, 0, 11]:
	print("near_ten({}) = {}".format(num, near_ten(num)))
	
	
