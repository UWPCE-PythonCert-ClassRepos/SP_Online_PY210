def array_count9(nums):
  nCount = 0
  for i in range(len(nums)):
      if nums[i] == 9:
          nCount = nCount + 1
  return nCount

print(array_count9([9, 1, 2, 3, 4, 9, 8, 9]))
