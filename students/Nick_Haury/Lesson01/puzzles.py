# Warmup-1

def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile and b_smile or not a_smile and not b_smile
    
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    return a + b
    
def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    return 21 - n
    
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
    
def makes10(a, b):
    return a == 10 or b == 10 or (a + b == 10)
    
def near_hundred(n):
    return abs(n - 100) < 11 or abs(n-200) < 11
    
def pos_neg(a, b, negative):
    if negative:
        return  a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)
    
def not_string(str):
    if str[:3] == 'not':
        return str
    return "not " + str
    
def missing_char(str, n):
    return str[:n] + str[n + 1:]
    
def front_back(str):
    if len(str) == 0:
        return str
    elif len(str) == 1:
        return str[::-1]
    else:
        return str[-1] + str[1:-1] + str[0]
        
def front3(str):
    return 3 * str[:3]
    
# Warmup-2

def string_times(str, n):
    return str * n
    
def front_times(str, n):
    return n * str[:3]
    
def string_bits(str):
    return str[::2]
    
def string_splosion(str):
    temp_str = ""
    for index in range(len(str) + 1):
      temp_str += str[:index]
    return temp_str
    
def last2(str):
    # test for string being too short for a match
    if len(str) < 3:
        return 0
    marker = str[-2:]
    match_count = 0;
    for index in range(len(str) - 2):
        if marker == str[index:index + 2]:
            match_count += 1;
    return match_count
    
def array_count9(nums):
    return nums.count(9)
    
def array_front9(nums):
    return 9 in nums[:4]
    
def array123(nums):
    for index in range(len(nums) - 2):
        if nums[index] == 1 and nums[index + 1] == 2 and nums[index + 2] == 3:
            return True
    return False

def string_match(a, b):
    # find shortest string to iterate over
    strLen = 0
    if len(a) > len(b):
        strLen = len(b)
    else:
        strLen = len(a)

    # count the number of len 2 substring matches
    count = 0
    for i in range(strLen - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1;

    return count
    
# String-1 problems

def hello_name(name):
  return "Hello " + name + "!"
  
def make_abba(a, b):
  return a + 2 * b + a
  
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"
  
def make_out_word(out, word):
  front = out[:len(out)//2]
  back = out[len(front):]
  return front + word + back
  
def extra_end(str):
  return 3 * str[-2:]
  
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]
  
def first_half(str):
  return str[:len(str) // 2]
  
def without_end(str):
  return str[1:-1]
  
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  return b + a + b
  
def non_start(a, b):
  return a[1:] + b[1:]
  
def left2(str):
  return str[2:] + str[:2]

#List-1

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6
    
def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]
  
def make_pi():
  return [3,1,4]
  
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
  
def sum3(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum
  
def rotate_left3(nums):
  nums.append(nums.pop(0))
  return nums
  
def reverse3(nums):
  nums.reverse()
  return nums
  
def max_end3(nums):
  if nums[0] > nums[-1]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[-1], nums[-1], nums[-1]]
    
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return sum(nums[:2])
    
def middle_way(a, b):
  return [a[1], b[1]]
  
def make_ends(nums):
  return[nums[0], nums[-1]]
  
def has23(nums):
  return 2 in nums or 3 in nums
  
# Logic-1

def cigar_party(cigars, is_weekend):
    return (cigars >= 40 and cigars <= 60) or is_weekend and cigars >= 40
    
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif (you >= 8 or date >= 8):
        return 2
    else:
        return 1
        
def squirrel_play(temp, is_summer):
    if temp >= 60:
        if is_summer and temp <= 100 or temp <= 90:
            return True
        else:
            return False
    else:
        return False
        
def caught_speeding(speed, is_birthday):
    if not is_birthday:
        if speed <= 60:
            return 0
        elif speed <= 80:
            return 1
        else:
            return 2
    else:
        if speed <= 65:
            return 0
        elif speed <= 85:
            return 1
        else:
            return 2

def sorta_sum(a, b):
    if (a + b) >= 10 and (a + b) <= 19:
        return 20
    else:
        return a + b
        
def alarm_clock(day, vacation):
    weekday = [1,2,3,4,5]
    weekend = [0,6]
    if day in weekday and not vacation:
        return "7:00"
    elif (day in weekday and vacation) or (day in weekend and not vacation):
        return "10:00"
    else:
        return "off"

def in1to10(n, outside_mode):
    nums = [1,2,3,4,5,6,7,8,9,10]
    if n in nums and not outside_mode:
        return True
    elif (n <= 1 or n >= 10) and outside_mode:
        return True
    else:
        return False

#Logic-2

def make_bricks(small, big, goal):
    big_bricks_needed = 0
    
    # only check for big bricks if we have them
    if big != 0:
        big_bricks_needed = goal // 5
    
    small_bricks_needed = goal - 5 * min(big_bricks_needed, big)
    if small_bricks_needed <= small:
        return True
    else:
        return False

def lone_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for i in my_list:
        if my_list.count(i) < 2:
            sum += i
    return sum

def lucky_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for i in my_list:
        if i == 13:
            break
        sum += i
    return sum

def no_teen_sum(a, b, c):
    ages = [a, b, c]
    sum = 0
    for age in ages:
        if not fix_teen(age):
            sum += age
    return sum


def fix_teen(n):
    teen_ages = [13, 14, 17, 18, 19]
    return n in teen_ages

def round_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for num in my_list:
        sum += round10(num)
    return sum


def round10(num):
    if num % 10 >= 5:
        return (num // 10 + 1) * 10
    else:
        return (num // 10) * 10
        
def close_far(a, b, c):
    if abs(a - b) <= 1 or abs(a - c) <= 1:
        if abs(b - c) >= 2 and (abs(a - b) >= 2 or abs(a - c) >= 2):
            return True
        else:
            return False
    else:
        return False

def make_chocolate(small, big, goal):
    if goal > small + 5 * big:
        return -1
    if goal % 5 > small:
        return -1
    return goal - 5 * min (goal // 5, big)

# String-2

def double_char(str):
    new_string = ""
    for char in str:
        new_string += 2 * char
    return new_string

def count_hi(str):
    return str.count("hi")

def cat_dog(str):
    return str.count("dog") == str.count("cat")

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if (str[i:i + 2] + str[i + 3] == "coe"):
            count += 1
    return count

def end_other(a, b):
    # find shorter string
    if len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    # check if shorter string is at end of longer string
    return longer[-len(shorter):].lower() == shorter.lower()
    
    # appears that using the string functions "startswith" and "endswith" have these built in

def xyz_there(str):
    return True if (str.count("xyz") > str.count(".xyz")) else False
    
def big_diff(nums):
    return abs(sorted(nums)[0] - sorted(nums, reverse=True)[0])

def centered_average(nums):
    # note: CodingBat site must be using an older version of Python, which doesn't have the list.copy() attribute
    sorted_nums = sorted(nums[:])
    sorted_nums.remove(sorted_nums[-1])
    sorted_nums.remove(sorted_nums[0])
    sum = 0
    for num in sorted_nums:
        sum += num
    return sum // len(sorted_nums)

def sum13(nums):
    if len(nums) == 0:
        return 0
    while 13 in nums:
        if nums[-1] == 13:
            nums.pop()
        else:
            nums = nums[:nums.index(13)] + nums[nums.index(13) + 2:]
    sum = 0
    for num in nums:
        sum += num
    return sum

def sum67(nums):
    nums_copy = nums[:]
    # remove all numbers in list between 6 and 7, inclusive
    while 6 in nums_copy:
        before_six = nums_copy[:nums_copy.index(6)]
        after_six = nums_copy[len(before_six):]
        after_seven = after_six[after_six.index(7) + 1:]
        nums_copy = before_six + after_seven
    
    #now sum
    sum = 0
    for num in nums_copy:
        sum += num
    return sum

def has22(nums):
    return "22" in ''.join(str(char) for char in nums)
    