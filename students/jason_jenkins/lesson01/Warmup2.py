# Lesson 1: Warmup Puzzles

def string_times(str, n):
    result = ""

    for x in range(n):
        result += str

    return result

def front_times(str, n):
    result = ""

    for x in range(n):
        result += str[0:3]

    return result

def string_bits(str):
    result = ""

    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]

    return result

def string_splosion(str):
    result = ""

    for x in range(len(str)):
        result += str[0:x+1]

    return result

def last2(str):
    last = str[len(str)-2:len(str)]
    result = 0

    for x in range(len(str) - 2):
        if(str[x:x+2] == last):
            result += 1

    return result

def array_count9(nums):
    result = 0

    for x in nums:
        if(x == 9):
            result += 1

    return result

def array_front9(nums):
    x = 0

    for num in nums:
        x += 1
        if(x <= 4 and num == 9):
            return True

    return False

def array123(nums):
    first = -1
    second = -1

    for num in nums:
        if(first == 1 and second == 2 and num == 3):
            return True
        elif(first == 1 and second == -1 and num == 2):
            second = 2
        elif(num == 1):
            first =1
            second = -1
        else:
            first = -1
            second = -1

    return False

def string_match(a, b):
    result = 0

    for x in range(min(len(a),len(b)) - 1):
        if (a[x:x+2] == b[x:x+2]):
                result += 1

    return result





