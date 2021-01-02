# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat List-2
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-01-2021, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def count_evens(nums):
    count = 0
    for num in nums:
        if num%2 == 0:
            count += 1
    return count

def big_diff(nums):
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest

def sum13(nums):
    sum = 0
    for number in nums:
        if number == 13:
            break
        sum += number
    return sum

def sum67(nums):
    sum = 0
    found = False
    for number in nums:
        if number == 6:
            found = True
        if not found:
            sum += number
        if number == 7:
            found = False
    return sum

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2:
            if nums[i+1] == 2:
                return True
    return False




