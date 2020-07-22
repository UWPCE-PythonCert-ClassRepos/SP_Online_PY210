# Lesson 1: List2

def count_evens(nums):
    evenCount = 0

    for num in nums:
        if num % 2 == 0:
            evenCount += 1

    return evenCount


def big_diff(nums):
    maxNum = max(nums)
    minNum = min(nums)

    return maxNum - minNum

def centered_average(nums):
    maxNum = max(nums)
    minNum = min(nums)

    minIgnored = False
    maxIgnored = False

    total = 0
    totalUnits = 0

    for num in nums:
        if (num == maxNum and not maxIgnored):
            maxIgnored = True
        elif (num == minNum and not minIgnored):
            minIgnored = True
        else:
            total += num
            totalUnits += 1

    return total / totalUnits


def sum13(nums):
    total = 0

    ignoreNext = False

    if(len(nums) == 0):
        return total

    for num in nums:
        if num == 13:
            ignoreNext = True
        elif ignoreNext:
            ignoreNext = False
        else:
            total += num

    return total


def sum67(nums):
    total = 0

    ignoreNext = False

    if(len(nums) == 0):
        return total

    for num in nums:
        if num == 6:
            ignoreNext = True
        elif ignoreNext and num == 7:
            ignoreNext = False
        elif not ignoreNext:
            total += num

    return total


def has22(nums):
    prevnum = 0

    for num in nums:
        if prevnum == 2 and num == 2:
            return True

        prevnum = num
    return False
