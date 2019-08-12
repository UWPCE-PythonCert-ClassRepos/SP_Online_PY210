def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1:
            if nums[i + 1] == 2:
                if nums[i + 2] == 3:
                    return True
    return False

print(array123([1,2,4,1,2,3]))
