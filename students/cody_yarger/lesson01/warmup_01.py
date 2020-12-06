#==============================================================================
# 12/04/2020
# Dev: Cody Yarger
# Python Pushups Exercise

#Given an array of ints, return the number of 9's in the array.
#
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    count = 0 # Initialize counter
    for i in nums: # Iterate over nums list
        if i == 9:
            count += 1 # Add 1 to count when i = 9.
    return count
