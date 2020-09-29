def first_last6(nums):
	length = len(nums) - 1
	if ((nums[0] == 6) or (nums[length] == 6)):
		return True
	else:
		return False