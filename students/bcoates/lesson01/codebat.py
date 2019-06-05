# Warmup-1

def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False

def diff21(n):
    if n < 21:
        return abs(n - 21)
    else:
        return abs(n - 21) * 2

def parrot_trouble(talking, hour):
    if talking == True:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False

def makes10(a, b):
    if a == 10 or b == 10 or (a + b) == 10:
        return True
    else:
        return False

def near_hundred(n):
      if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
    if negative == False:
        if a < 0 and b > 0:
            return True
        elif a > 0 and b < 0:
            return True
        else:
            return False
    else:
        if a < 0 and b < 0:
            return True
        else:
            return False

def not_string(str):
    if str[:3] == "not":
        return str
    else:
        return "not " + str

def missing_char(str, n):
    return str[:n] + str[n + 1:]

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]

def front3(str):
    front = 3
    if len(str) < front:
        front = len(str)
        new_str = str[:front]
    return new_str + new_str + new_str

# Warmup-2

def string_times(str, n):
    new_str = ""
    for i in range(0,n):
        new_str = new_str + str
    return new_str

def front_times(str, n):
    front = 3
    if len(str) < 3:
        front = len(str)
    new_str = ""
    for i in range(0,n):
        new_str = new_str + str[:front]
    return new_str

def string_bits(str):
    new_str = ""
    for i in range(0, len(str), 2):
        new_str = new_str + str[i]
    return new_str

def string_splosion(str):
    new_str = ""
    for i in range(len(str)):
        new_str = new_str + str[:i+1]
    return new_str

def last2(str):
    if len(str) < 2:
        return 0

    last_2 = str[-2:]

    count = 0
    for i in range(len(str) - 2):
        substring = str[i:i+2]
        if substring == last_2:
            count += 1
    
    return count

def array_count9(nums):
    count = 0
    for item in nums:
        if item == 9:
        count += 1
    return count

def array_front9(nums):
    elements = len(nums)
    if elements > 4:
        elements = 4

    result = False
    for i in range(elements):
        if nums[i] == 9:
        result = True

    return result

def array123(nums):
    result = False
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            result = True

    return result

def string_match(a, b):
    count = 0
    for i in range(len(a) - 1):
        sub1 = a[i:i + 2]
        sub2 = b[i:i + 2]
    if sub1 == sub2:
        count += 1

    return count