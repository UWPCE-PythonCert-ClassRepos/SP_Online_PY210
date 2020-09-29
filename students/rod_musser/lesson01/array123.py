def array123(nums):
    if (len(nums) >= 3):
        for i in range(len(nums) - 2):
            if (nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3):
                return True
    return False
