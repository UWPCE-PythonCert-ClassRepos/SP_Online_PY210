def array_front9(nums):
    result = False
    x = 0
    for i in nums:
        x += 1
        if i == 9:
            result = True
        if (x >= 4 or result):
            break
    return result
