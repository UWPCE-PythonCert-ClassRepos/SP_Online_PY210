# string_times

def string_times(str, n):
  new_str = ""
  for i in range(n):
    new_str += str
  return new_str

# front_times

def front_times(str, n):
  if n > -1:
    new_str = ""
    for i in range(n):
      if len(str) < 3:
        new_str += str[0:n]
      else:
        new_str += str[0:3]
    return new_str

# string_bits

def string_bits(str):
  new_str = ""
  for i in range(len(str)):
    if i % 2 == 0:
      new_str += str[i]
  return new_str

# string_splosion

def string_splosion(str):
  new_str = ""
  for i in range(len(str)):
    new_str += str[0:i+1]
  return new_str

# last2

def last2(str):
  if len(str) < 2:
    return 0
  end_str = str[len(str)-2:]
  count = 0
  for i in range(len(str)-2):
    sub_str = str[i:i+2]
    if end_str == sub_str:
      count += 1
  return count

# array_count9

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count += 1
  return count

# array_front9

def array_front9(nums):
  new_nums =  nums[0:4]
  for num in new_nums:
    if num == 9:
      return True
  return False

# array123

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

# string_match

def string_match(a, b):
  shortest = min(len(a), len(b))
  count = 0
  for i in range(shortest-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count