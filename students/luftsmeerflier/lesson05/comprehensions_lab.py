#!/user/bin/env python3

def count_evens(list):
	evens = [num for num in list if num % 2 == 0]
	return len(evens)

def main():

	assert count_evens([2,1,2,3,4]) == 3

	assert count_evens([2,2,0]) == 3

	assert count_evens([1,3,5]) == 0

	print("All tests pass")


if __name__ == "__main__":
	main()