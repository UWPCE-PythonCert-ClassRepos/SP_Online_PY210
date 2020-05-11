def array_front9(nums):
    firstfour = 4
    if len(nums) < 4:
        firstfour = len(nums)
    for i in range(firstfour):
        if nums[i] == 9:
            return True
    return False