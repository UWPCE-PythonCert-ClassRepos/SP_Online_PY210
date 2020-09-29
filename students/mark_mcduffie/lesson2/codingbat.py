
#Logic2
def make_bricks(small, big, goal):
  if (goal%5)<=small and (goal-(big*5))<=small:
    return True
  else:
    return False

def lone_sum(a, b, c):
  if (a != b and b != c and a != c):
    return a + b + c
  elif(a == c and b != a):
    return b
  elif(a == b and a != c):
    return c
  elif(b == c and a != b):
    return a
  else:
    return 0

#List2
def count_evens(nums):
  count = 0
  for n in nums:
    if(n%2 == 0):
        count = count + 1
  return count

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1]) / (len(nums) - 2)

