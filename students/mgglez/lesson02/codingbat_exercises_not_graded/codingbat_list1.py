# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat List-1
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-01-2021, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    return [3,1,4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def rotate_left3(nums):
    first = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    nums[-1] = first
    return nums

def reverse3(nums):
    return nums[::-1]

def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = max_value
    return nums

def sum2(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 2:
            break
        sum += nums[i]
    return sum

def middle_way(a, b):
    new_array = []
    new_array.append(a[len(a)//2])
    new_array.append(b[len(b)//2])
    return new_array

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    for i in range(len(nums)):
        if nums[i] == 2 or nums[i] ==  3:
            return True
    return False

