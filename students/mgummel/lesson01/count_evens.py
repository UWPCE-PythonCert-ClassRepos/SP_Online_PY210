def count_evens(nums):
  count_variable = 0
  for element in nums:
    if element % 2 == 0:
      count_variable += 1
  return count_variable
