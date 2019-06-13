#warmup-1 front3
def front3(str):
    return (str[:3] * 3)
front3('Java')

#warmup-2 string_times
def string_times(str, n):
  return (str * n)
string_times('Hi', 2)

#string-1 make_abba
def make_abba(a, b):
  return (a + b + b + a)
make_abba('Hi','Bye')

#List-1 same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False
same_first_last([1, 2, 3])

#Logic-1 near_ten
def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True
  else:
    return False
near_ten(12)

#Logic-2 make_bricks
def make_bricks(small, big, goal):
  if (small + big*5) >= goal and goal % 5 <= small:
    return True
  else:
    return False

#String-2 count_hi
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count = count + 1
  return count

#List-2 count_evens
def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count = count + 1
  return count
