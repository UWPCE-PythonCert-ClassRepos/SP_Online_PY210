"""
Programming In Python - Lesson 1 Task 2: Puzzles - List-2
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# List-2 > count_evens 
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

# List-2 > big_diff 
def big_diff(nums):
    lower = min(nums)
    upper = max(nums)
    return upper - lower

# List-2 > centered_average 
def centered_average(nums):
    total = 0
    upper = max(nums)
    lower = min(nums)

    for i in nums:
        upper = max(upper, i)
        lower = min(lower, i)
        total += i

    return (total - upper - lower) / (len(nums) -2)

# List-2 > sum13 
def sum13(nums):
    total = 0

    if len(nums) == 0:
        return total

    last13 = False
    for i in range(len(nums)):
        current = nums[i]

        if not last13:
            if current != 13:
                total += current
            else:
                last13 = True
        else:
            last13 = False

    return total

# List-2 > sum67 
def sum67(nums):
    ignoring = False
    total = 0

    for i in nums:
        if i == 6:
            ignoring = True

        if not ignoring:
            total += i

        if i == 7:
            ignoring = False

    return total

# List-2 > has22 
def has22(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
