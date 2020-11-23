# Warmup-1 Excercise 1 - "Sleep-in"

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# Warmup-1 Excercise 2 - "MonkeyTrouble"

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

# Warmup-1 Excercise 3 - "Sum Double"

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

# Warmup-1 Excercise 4 - "Diff21"

def diff21(n):
  if n > 21:
    return (n - 21) * 2
  else:
    return 21 - n

# Warmup-1 Excercise 5 - "Parrot_trouble"

def parrot_trouble(talking, hour):
  if talking and hour < 7:
    return True
  if talking and hour > 20:
    return True
  return False

# Warmup-1 Excercise 6 - "Makes 10"

def makes10(a, b):
  sum = a + b
  if (a == 10 or b == 10 or sum == 10):
    return True
  return False

# Warmup-1 Excercise 7 - "near_hundred"

def near_hundred(n):
  if abs(100 - n) <= 10:
    return True
  if abs(200 -n) <=10:
    return True
  return False

# Warmup-1 Excercise 8 - "pos_neg"

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# Warmup-1 Excercise 9 - "not_string"

def not_string(str):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  return 'not ' + str

# Warmup-1 Excercise 10 - "missing_char"

def missing_char(str, n):
  first_part = str[:n]
  second_part = str[n+1:]
  return first_part + second_part

# Warmup-1 Excercise 11 - "front_back"

def front_back(str):
  if len(str) <= 1:
    return str
  x = str[0]
  y = str[1:-1]
  z = str[-1]
  return z + y + x

# Warmup-1 Excercise 11 - "front3"

  def front3(str):
  if len(str) <= 3:
    return str * 3
  else:
    front = str[:3]
    return front * 3


# Warmup-2 Excercise 1 - "string_times"

def string_times(str, n):
  if n < 0:
    return False
  return str * n
  # alt solution:
  def string_times(str, n):
  result = ''
  for i in range(n): 
  return result

# Warmup-2 Excercise 2 - "front_times"

def front_times(str, n):
  target = 3
  if target > len(str):
    return str * n
  return str[:3] * n
# alt solution:
def front_times(str, n):
  target = 3
  if target > len(str):
    target = len(str)
  front = str[:target]
  result_str = ''
  for x in range(n):
    result_str += front
  return result_str

# Warmup-2 Excercise 3 - "string_bits"
# N.B. - Since the exercises all use loops, will only code w/ loops going forward
def string_bits(str):
  result_str = ''
  for bit in range(len(str)):
    if bit % 2 == 0:
      result_str += str[bit]
  return result_str

# Warmup-2 Excercise 4 - "string_splosion"
# N.B. - Since the exercises all use loops, will only code w/ loops going forward
def string_splosion(str):
  result_str = ''
  for letter in range(len(str)):
    result_str += str[:letter+1]
  return result_str

# Warmup-2 Excercise 5 - "last2"

  def last2(str):
  if len(str) <= 2:
    return 0
  last2 = str[-2:]
  count = 0
  for i in range(len(str)-2):
    substring = str[i:i+2]
    if substring == last2:
      count = count + 1
  return count

# Warmup-2 Excercise 6 - "array_count9"

  def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1
  return count


# Warmup-2 Excercise 7 - "array_front9"

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

# Warmup-2 Excercise 8 - "array123"

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

# Warmup-2 Excercise 9 - "string_match"

def string_match(a, b):
  smaller_str = min(len(a), len(b))
  count = 0
  for i in range(smaller_str-1):
    substring_a = a[i:i+2]
    substring_b = b[i:i+2]
    if substring_a == substring_b:
      count = count+1
  return count