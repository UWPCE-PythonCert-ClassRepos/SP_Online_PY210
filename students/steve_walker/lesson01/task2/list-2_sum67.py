# List-2 > sum67

# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.

def sum67(nums):
  sum = 0
  switch = 0
  for i in nums:
    if i==6:
      switch = 1
    elif i==7 and switch==1:
      switch = 0
    elif switch == 0:
      sum = sum + i
  return(sum)
