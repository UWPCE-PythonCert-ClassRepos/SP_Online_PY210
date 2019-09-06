def array123(nums):
  for i in range(len(nums)-2):
    if ((nums[i] == 1) & (nums[i+1] == 2) & (nums[i+2] == 3)):
      return True
  return False

def count_hi(str):
    return(str.count('hi'))

str_doub("Hi There")

str = 'Hi There hi hi '
