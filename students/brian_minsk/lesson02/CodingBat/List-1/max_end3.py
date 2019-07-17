def max_end3(nums):
    nMax = nums[0]
    if nums[2] > nMax:
        nMax = nums[2]
    return [nMax, nMax, nMax]

print(max_end3([1,2,3]))
print(max_end3([9,8,7]))