def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return nums[0] + nums[1]

print(sum2([4,5,6,7]))
print(sum2([5]))
print(sum2([]))