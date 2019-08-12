def first_last6(nums):
    if nums[0] == 6:
        return True
    if nums[len(nums) - 1] == 6:
        return True
    return False

print(first_last6([1, 2, 3, 4, 5, 6]))
print(first_last6([6, 2, 3, 4, 5, 6]))
print(first_last6([1, 2, 3, 4, 5, 6, 7]))
