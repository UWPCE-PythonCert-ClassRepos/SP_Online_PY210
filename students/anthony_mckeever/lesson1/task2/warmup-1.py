"""
Programming In Python - Lesson 1 Task 2: Puzzles - Warmup-1
Code Poet: Anthony McKeever
Date: 07/18/2019
"""

# Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
    return not weekday or vacation

# Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
    return a_smile is b_smile

# Warmup-1 > sum_double 
def sum_double(a, b):
    total = a + b

    if a == b:
        return total * 2
    
    return total

# Warmup-1 > diff21 
def diff21(n):
    absoluteDifference = abs(21 - n)
    if n <= 21:
        return absoluteDifference
    return absoluteDifference * 2

# Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
    if hour in range(7, 21):
        return False
    return talking

# Warmup-1 > makes10 
def makes10(a, b):
    if a == 10 or b == 10:
        return True
    return a + b == 10

# Warmup-1 > near_hundred
def near_hundred(n):
    near100 = abs(100 - n) <= 10
    near200 = abs(200 - n) <= 10
    return (near100 or near200)

# Warmup-1 > pos_neg
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 or b < 0) and (a > 0 or b > 0)

# Warmup-1 > not_string
def not_string(inString):
    if inString.startswith("not"):
        return inString
    return "not {}".format(inString)

# Warmup-1 > missing_char 
def missing_char(inString, n):
    start = inString[:n]
    end = inString[n+1:]
    return start + end

# Warmup-1 > front_back
def front_back(inString):
    if len(inString) <= 1:
        return inString

    start = inString[len(inString)-1]
    end = inString[0]
    mid = inString[1:len(inString)-1]
    return start + mid + end

# Warmup-1 > front3 
def front3(inString):
    start = inString[0:3]
    return start * 3
