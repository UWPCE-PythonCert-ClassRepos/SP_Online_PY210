#/usr/bin/env python3
# Fizzbuzz solution

def FizzBuzz():
	for num in range(100):
		num += 1
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz", num)
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(num)


def main():
	FizzBuzz()

if __name__ == "__main__":
	main()