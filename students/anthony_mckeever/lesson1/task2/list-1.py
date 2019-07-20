"""
Programming In Python - Lesson 1 Task 2: Puzzles - List-1
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# List-1 > first_last6 
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

# List-1 > same_first_last 
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

# List-1 > make_pi
def make_pi():
    return [3, 1, 4]

# List-1 > common_end 
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

# List-1 > sum3 
def sum3(nums):
    total = 0
    for i in nums:
        total += i
    return total

# List-1 > rotate_left3
def rotate_left3(nums):
    hold = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    nums[-1] = hold
    return nums

# List-1 > reverse3 
def reverse3(nums):
    swap = nums[0]
    nums[0] = nums[-1]
    nums[-1] = swap
    return nums

# List-1 > max_end3
def max_end3(nums):
    hold = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = hold
    return nums

# List-1 > sum2 
def sum2(nums):
    total = 0
    for i in range(len(nums)):
        if i > 1:
            break
        total += nums[i]
    return total

# List-1 > middle_way 
def middle_way(a, b):
    midA = len(a) / 2
    midB = len(b) / 2
    return [a[midA], b[midB]]

# List-1 > make_ends 
def make_ends(nums):
    return [nums[0], nums[-1]]

# List-1 > has23
def has23(nums):
    return nums.count(2) > 0 or nums.count(3) > 0
