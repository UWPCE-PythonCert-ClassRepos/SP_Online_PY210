# ------------------------- #
# Breeanna Planica
# Cosingbat.com exercises for Lesson 1 - Python 210
# Warmup-1 and Warmup-2 exercises
#
# https://codingbat.com/python
# ------------------------- #

# Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False

# Warmup-1 > sum_double
def sum_double(a, b):
  sum = a + b
  if a ==b:
    sum = sum * 2
  return sum

def sum_double(a, b):
  if a == b:
    sum = (2*(a+b))
    return sum
  else:
    sum = a+b
    return sum

# Warmup-1 > diff21
def diff21(n):
  if n >= 21:
    return (n - 21) * 2
  elif n < 21:
    return 21 - n

# Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False

# Warmup-1 > makes10
def makes10(a, b):
  if (a + b) == 10 or a == 10 or b == 10:
    return True
  else:
    return False

# Warmup-1 > near_hundred
def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False

# Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  if negative and (a < 0 and b < 0):
    return True
  elif not negative and ((a < 0 and b >= 0) or (a >= 0 and b < 0)):
    return True
  else:
    return False

# Warmup-1 > not_string
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    str = "not " + str
    return str

# Warmup-1 > missing_char
def missing_char(str, n):
  first = str[:n]
  second = str[n + 1:]
  return first + second

# Warmup-1 > front_back
def front_back(str):
  if len(str) == 1:
    return str
  else:
    length = len(str)
    first = str[:1]
    middle = str[1: length - 1]
    last = str[length - 1:]
    return last + middle + first

# Warmup-1 > front3
def front3(str):
  if len(str) < 3:
    return str + str + str
  else:
    str = str[:3]
    return str + str + str

# Warmup-2 > string_times
def string_times(str, n):
  str = (str * n)
  return str   

# Warmup-2 > front_times
def front_times(str, n):
  if len(str) < 3:
    str = (str * n)
    return str
  else:
    str = (str[:3] * n)
    return str

# Warmup-2 > string_bits
def string_bits(str):
  value = ""
  for i in range(len(str)):
    if i % 2 == 0:
      value = value + str[i]
  return value

# Warmup-2 > string_splosion
def string_splosion(str):
  value = ""
  	for i in range(len(str)):
      value = value + str[:i+1]
  return value

# Warmup-2 > last2
def last2(str):
  value = str[len(str)-2:]
  j = 0
  for i in range(len(str)-2):
    match = str[i:i+2]
    if match == value:
      j = j + 1
  return j

# Warmup-2 > array_count9
def array_count9(nums):
  j = 0
  for i in nums:
    if i == 9:
      j = j + 1
  return j

# Warmup-2 > array_front9
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

# Warmup-2 > array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and (nums[i + 1] == 2) and (nums[i + 2] == 3):
      return True
  return False

# Warmup-2 > string_match
def string_match(a, b):
  j = 0
  shorter = min(len(a), len(b))
  for i in range(shorter - 1):
    a_sub = a[i:i + 2]
    b_sub = b[i:i + 2]
    if a_sub == b_sub:
      j = j + 1
  return j
