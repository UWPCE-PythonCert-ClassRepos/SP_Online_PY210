#/usr/bin/env python3
import sys

def monkey_trouble(a_smile, b_smile):
	if not (a_smile ^ b_smile):
		return "Looks like we have a trouble monkey..."
	else:
		return "Looks like we're okay"

def input_generator():
	# a generator here to yield user input for a_smile, b_smile
	monkey_a = input("Is monkey 1 smiling? Enter True or False ")
	yield monkey_a.upper()
	#yield monkey_a
	#yield input("Is monkey 1 smiling? Enter Y or N\n").upper()
	monkey_b = input("Is monkey 2 smiling? Enter True or False ")
	yield monkey_b.upper()
	#yield input("Is monkey 2 smiling? Enter Y or N\n").upper()


def to_bool(x):
	if x == "TRUE":
		return True
	elif x == "FALSE":
		return False
	else:
		print("Let's try that again")
		main()

def main():
	smiling = input_generator()
	monkey_a = to_bool(next(smiling))
	monkey_b = to_bool(next(smiling))
	trouble = monkey_trouble(monkey_a, monkey_b)
	print(trouble)

if __name__ == "__main__":
	main()