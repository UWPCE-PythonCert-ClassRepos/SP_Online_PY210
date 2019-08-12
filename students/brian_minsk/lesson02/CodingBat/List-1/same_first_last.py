def same_first_last(nums):
    if len(nums) > 0 and nums[0] == nums[len(nums) - 1]:
        return True
    return False

print(same_first_last([1, 1, 3, 1]))
print(same_first_last([0, 1, 3, 1]))
print(same_first_last([5]))