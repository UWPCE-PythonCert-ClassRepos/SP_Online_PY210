# ---------------------------------------------------------------------------- #
# Title: Lesson 1
# Description: Python Pushups
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,12-28-2020, Task 2 - Puzzles - CodingBat Warmup-2
# ---------------------------------------------------------------------------- #

def string_times(my_str, n):
    return my_str * n

def front_times(my_str, n):
    if len(my_str) < 3:
        return my_str * n
    else:
        return my_str[:3] * n

def string_bits(my_str):
    result = ""
    for i in range(0, len(my_str), 2):
        result += my_str[i]
    return result

def string_splosion(my_str):
    result = ""
    for i in range(len(my_str)):
        result += my_str[:i+1]
    return result

def last2(my_str):
    count = 0
    for i in range(len(my_str) - 2):
        if my_str[i:i+2] == my_str[-2:]:
            count += 1
    return count

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

def array_front(nums):
    for i in range(min(len(nums), 4)):
        if nums[i] == 9:
            return True
    return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count