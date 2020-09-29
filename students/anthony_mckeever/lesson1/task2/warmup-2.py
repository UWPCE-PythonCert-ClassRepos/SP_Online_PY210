"""
Programming In Python - Lesson 1 Task 2: Puzzles - Warmup-2
Code Poet: Anthony McKeever
Date: 07/19/2019
"""

# Warmup-2 > string_times
def string_times(inString, n):
    return inString * n

# Warmup-2 > front_times
def front_times(inString, n):
    if n > -1:
        front = inString[0:3]
        return front * n
    return None

# Warmup-2 > string_bits
def string_bits(inString):
    output = ""
    for i in range(0, len(inString), 2):
        output = output + inString[i]
    return output

# Warmup-2 > string_splosion
def string_splosion(inString):
    output = ""
    for i in range(len(inString)):
        output = output + inString[:i+1]
    return output

# Warmup-2 > last2
def last2(inString):
    count = 0
    if len(inString) < 2:
        return count

    end = inString[len(inString)-2:]

    for i in range(len(inString)-2):
        current = inString[i:i+2]
        if current == end:
            count+=1

    return count

# Warmup-2 > array_count9 
def array_count9(nums):
    return nums.count(9)

# Warmup-2 > array_front9
def array_front9(nums):
    for i in range(len(nums)):
        if i == 4:
            break
        elif nums[i] == 9:
            return True

    return False

# Warmup-2 > array123 
def array123(nums):
    numsLength = len(nums)
    if numsLength < 3:
        return False

    for i in range(numsLength):
        if i > numsLength - 2:
            break
        elif nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True

    return False

# Warmup-2 > string_match 
def string_match(a, b):
    count = 0
    lower = min(len(a), len(b))

    for i in range(lower - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
